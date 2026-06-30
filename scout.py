#!/usr/bin/env python3
"""
NT Scout — 每日开源项目自动发现
抓取 GitHub Trending + 多维度关键词搜索 → 去重 → 存入 Google Doc
配合 Claude 人工分析，发现对产品有价值的开源项目
"""

import os
import json
import time
import re
import base64
from datetime import datetime, timedelta, timezone

import requests
from bs4 import BeautifulSoup


def utcnow():
    """替代已弃用的 datetime.utcnow()（Python 3.12+）"""
    return datetime.now(timezone.utc)


# ══════════════════════════════════════════════════════════════
# 配置
# ══════════════════════════════════════════════════════════════

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
APPS_SCRIPT_URL = os.environ.get("GOOGLE_APPS_SCRIPT_URL", "")

HISTORY_FILE = "history.json"
MAX_REPOS = 20
README_MAX_CHARS = 2500
SEARCH_DAYS = 7
MIN_STARS = 30

GH_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


# ══════════════════════════════════════════════════════════════
# 搜索关键词 — 按业务方向分组
# ══════════════════════════════════════════════════════════════

SEARCH_GROUPS = {
    "📖 阅读/内容平台": [
        "reading app ebook mobile",
        "web novel reader",
        "epub reader open source",
        "comic manga webtoon reader",
        "audiobook text-to-speech TTS",
        "story writing platform",
    ],
    "🤖 AI / LLM / RAG": [
        "RAG retrieval augmented generation",
        "vector database embedding",
        "LLM agent framework",
        "AI chatbot character roleplay",
        "knowledge base question answering",
        "open source ChatGPT alternative",
        "AI image generation",
        "AI comic manga generation",
        "prompt engineering tool",
    ],
    "💰 变现/支付/订阅": [
        "in-app purchase subscription mobile",
        "paywall monetization",
        "payment gateway mobile app",
        "revenue analytics SaaS",
        "stripe integration mobile",
    ],
    "📈 增长/推广/运营": [
        "mobile attribution analytics",
        "push notification engagement",
        "app store optimization ASO",
        "user acquisition mobile",
        "A/B testing mobile app",
        "deep linking mobile",
        "social sharing viral growth",
        "influencer marketing tool",
        "content recommendation engine",
    ],
    "🌍 本地化/多语言": [
        "localization i18n translation",
        "machine translation open source",
        "multilingual app framework",
        "GDPR privacy compliance",
    ],
    "🔧 开发/工具链": [
        "Flutter framework plugin",
        "Unity mobile game",
        "cross-platform mobile framework",
        "CI CD mobile deployment",
        "content moderation safety AI",
        "mobile app performance monitoring",
        "feature flag remote config",
        "backend as a service mobile",
    ],
    "🎬 互动叙事/创作": [
        "interactive fiction engine",
        "visual novel framework",
        "branching narrative game",
        "AI storytelling writing assistant",
        "spine 2D animation",
        "dialogue system game",
    ],
}

ROCKET_QUERIES = [
    {"q": "stars:>300", "days": 5, "label": "🚀 5天300+星"},
    {"q": "stars:>800", "days": 14, "label": "🚀 两周800+星"},
]

# ── 推广类特殊处理 ──
# 推广/增长工具星标涨得慢，容易被 AI/开发类大项目挤出 Top N。
# 给它单独降门槛 + 保底配额，确保每天都能看到推广向的新项目。
PROMO_GROUP = "📈 增长/推广/运营"
PROMO_MIN_STARS = 10   # 推广类只要 ≥10 星（其他类 ≥30）
PROMO_QUOTA = 5        # 每天最少保 5 个推广类名额，不管星标高低

# ── 新老结合：活跃老仓库搜索 ──
# Step 3 除了搜"最近新建"(created)，再搜一轮"老但最近活跃"(pushed)。
# 活跃轮星标门槛抬高，避免被老牌大项目刷屏。
ACTIVE_DAYS = 14         # 最近 14 天内有 push 视为活跃
ACTIVE_MIN_STARS = 150   # 活跃老仓库门槛更高（新仓库 30 / 推广 10）
ACTIVE_PROMO_MIN_STARS = 50  # 活跃推广类适当放低

# ── 风险词标记 ──
# 命中这些词的项目在日报里打 ⚠️风险 前缀，便于一眼识别、归入排除区。
# 不阻止收录（仍需人判断），只做预警标记。
RISK_KEYWORDS = [
    "exploit", "0-day", "0day", "poc", "vulnerability research",
    "trading bot", "trading agent", "trade bot", "polymarket", "copy-trader", "copy trader",
    "play-to-earn", "play to earn", "cash out", "$plum", "gasless",
    "bypass", "unfilter", "绕过", "绕开", "破解", "cookie", "薅羊毛", "白嫖",
    "交易机器人", "自动交易", "量化交易",
]


def risk_flags(repo):
    """检查项目是否命中风险词，返回命中的词列表（空=无风险信号）"""
    text = " ".join([
        str(repo.get("full_name", "")),
        str(repo.get("description") or ""),
        " ".join(repo.get("topics", []) or []),
        str(repo.get("readme_excerpt", "")),
    ]).lower()
    hits = [kw for kw in RISK_KEYWORDS if kw.lower() in text]
    return hits


# ── README 乱码/污染检测 ──
# 防止 Some-Many-Books 这类项目：README 是几十万字符的生僻字乱码/盗版书单，
# 会污染风险扫描、拖慢抓取、错配分类。四条件同时满足才判乱码，避免误杀正常长文档。
README_GARBAGE_MIN_CHARS = 50000   # 必须超长（正常 README 极少 >50KB）
README_GARBAGE_MAX_ASCII = 0.40    # ASCII 占比 <40%（正常技术文档 ASCII 很高）
README_GARBAGE_MAX_WS = 0.05       # 空白占比 <5%（正常 markdown 有大量换行结构）
README_GARBAGE_MIN_UNIQ = 0.50     # CJK 独特字符比 >50%（乱码字字不同；自然语言常用字反复）
README_GARBAGE_SENTINEL = "(README 疑似乱码/污染数据，已跳过"


def _cjk_unique_ratio(text):
    """CJK 字符里不重复字符的占比。乱码≈1（字字不同），自然语言低（常用字反复出现）。"""
    cjk = [c for c in text if "\u4e00" <= c <= "\u9fff" or "\u3400" <= c <= "\u4dbf"]
    if len(cjk) < 200:
        return 0.0
    return len(set(cjk)) / len(cjk)


def is_garbage_readme(text):
    """四条件同时满足才判乱码，返回 (是否乱码, 说明字符串)。保守，宁漏勿误杀。"""
    n = len(text)
    if n < README_GARBAGE_MIN_CHARS:
        return False, ""
    ascii_r = sum(1 for c in text if ord(c) < 128) / n
    ws_r = sum(1 for c in text if c.isspace()) / n
    uniq = _cjk_unique_ratio(text)
    is_garbage = (
        ascii_r < README_GARBAGE_MAX_ASCII
        and ws_r < README_GARBAGE_MAX_WS
        and uniq > README_GARBAGE_MIN_UNIQ
    )
    detail = f"长度{n} ASCII{ascii_r:.0%} 空白{ws_r:.0%} 独特{uniq:.0%}"
    return is_garbage, detail


# ══════════════════════════════════════════════════════════════
# 工具函数
# ══════════════════════════════════════════════════════════════

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return set(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(sorted(history), f, indent=2, ensure_ascii=False)


def gh_get(url, params=None):
    resp = requests.get(url, headers=GH_HEADERS, params=params, timeout=15)
    if resp.status_code == 403 and "rate limit" in resp.text.lower():
        reset_at = int(resp.headers.get("X-RateLimit-Reset", 0))
        wait = max(reset_at - int(time.time()), 30)
        print(f"  ⏳ GitHub API 限速，等待 {wait}s...")
        time.sleep(wait)
        resp = requests.get(url, headers=GH_HEADERS, params=params, timeout=15)
    return resp


def search_github(query_str, days=SEARCH_DAYS, min_stars=MIN_STARS, per_page=8, mode="new"):
    """搜索 GitHub 仓库。
    mode='new'    → 最近 days 天内**新建**的仓库（created:>）
    mode='active' → 任意时间创建、最近 days 天内**有更新**的活跃仓库（pushed:>）
    """
    date_from = (utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    time_filter = f"created:>{date_from}" if mode == "new" else f"pushed:>{date_from}"
    full_q = f"{query_str} {time_filter} stars:>{min_stars}"
    params = {
        "q": full_q,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
    }
    resp = gh_get("https://api.github.com/search/repositories", params)
    if resp.status_code == 200:
        return resp.json().get("items", [])
    else:
        print(f"  ⚠ 搜索失败 ({resp.status_code}): [{mode}] {query_str[:40]}")
        return []


def scrape_trending():
    all_repos = []
    for period in ["daily", "weekly"]:
        try:
            url = f"https://github.com/trending?since={period}"
            resp = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
                timeout=15,
            )
            if resp.status_code != 200:
                print(f"  ⚠ Trending 页面请求失败 ({period}): {resp.status_code}")
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            articles = soup.select("article.Box-row")
            if not articles:
                articles = soup.select("[class*='Box-row']")

            for article in articles:
                link = article.select_one("h2 a") or article.select_one("h1 a")
                if not link:
                    continue
                href = link.get("href", "").strip("/")
                if "/" not in href:
                    continue

                desc_el = article.select_one("p")
                desc = desc_el.text.strip() if desc_el else ""

                all_repos.append({
                    "full_name": href,
                    "description": desc,
                    "source": f"trending-{period}",
                })

            print(f"  ✓ Trending ({period}): 找到 {len(articles)} 个")

        except Exception as e:
            print(f"  ⚠ Trending 抓取异常 ({period}): {e}")

    seen = set()
    unique = []
    for r in all_repos:
        if r["full_name"] not in seen:
            seen.add(r["full_name"])
            unique.append(r)
    return unique


def fetch_repo_info(full_name):
    resp = gh_get(f"https://api.github.com/repos/{full_name}")
    if resp.status_code == 200:
        return resp.json()
    return None


def fetch_readme(full_name):
    resp = gh_get(f"https://api.github.com/repos/{full_name}/readme")
    if resp.status_code != 200:
        return "(README 获取失败)"
    try:
        raw = base64.b64decode(resp.json()["content"]).decode("utf-8", errors="ignore")
        raw = re.sub(r"!\[.*?\]\(.*?\)", "", raw)
        raw = re.sub(r"<img[^>]*>", "", raw)
        raw = re.sub(r"<[^>]+>", "", raw)
        raw = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        # 乱码/污染检测（在截断前，对完整内容判断）
        garbage, detail = is_garbage_readme(raw)
        if garbage:
            print(f"     🗑️ README 疑似乱码/污染，已跳过 — {detail}")
            return f"{README_GARBAGE_SENTINEL} — {detail})"
        return raw[:README_MAX_CHARS].strip()
    except Exception:
        return "(README 解析失败)"


# ══════════════════════════════════════════════════════════════
# Google Doc 写入（通过 Apps Script）
# ══════════════════════════════════════════════════════════════

def write_to_doc(text):
    """通过 Google Apps Script Web App 写入 Google Doc"""
    if not APPS_SCRIPT_URL:
        print("  ⏭ 未配置 Apps Script URL，跳过 Google Doc 写入")
        return
    try:
        resp = requests.post(
            APPS_SCRIPT_URL,
            data=text.encode("utf-8"),
            headers={"Content-Type": "text/plain; charset=utf-8"},
            timeout=30,
            allow_redirects=True,
        )
        if resp.status_code == 200:
            print("  ✓ 已写入 Google Doc")
        else:
            print(f"  ⚠ Google Doc 写入失败: {resp.status_code} {resp.text[:200]}")
    except Exception as e:
        print(f"  ⚠ Google Doc 写入异常: {e}")


def write_to_repo(text, date_str):
    """把日报存进仓库：reports/YYYY-MM-DD.md 归档 + latest.md 指向最新
    这样 Orca 里的 Claude Code 拉一下仓库就能读到最新日报，不依赖 Google Drive"""
    os.makedirs("reports", exist_ok=True)

    # 当日归档
    archive_path = f"reports/{date_str}.md"
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write(text)

    # latest.md —— 始终指向最新一期，Orca 固定读这个文件
    with open("latest.md", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"  ✓ 已写入仓库: {archive_path} + latest.md")


# ══════════════════════════════════════════════════════════════
# 报告格式化
# ══════════════════════════════════════════════════════════════

def format_report(repos, date_str):
    lines = [
        f"📊 开源日报 — {date_str}",
        f"共发现 {len(repos)} 个新项目（已自动过滤历史记录）",
        "",
    ]

    for i, repo in enumerate(repos, 1):
        fn = repo["full_name"]
        stars = repo.get("stargazers_count", "?")
        forks = repo.get("forks_count", "?")
        lang = repo.get("language", "未知")
        created = str(repo.get("created_at", ""))[:10]
        desc = repo.get("description") or "无描述"
        topics = repo.get("topics", [])
        source = repo.get("source", "search")
        readme = repo.get("readme_excerpt", "")

        lines.append(f"{'━' * 55}")
        risk = repo.get("risk_hits", [])
        if risk:
            lines.append(f"#{i}  ⚠️风险  {fn}")
            lines.append(f"    ⚠️ 命中风险词: {', '.join(risk[:6])} —— 默认归排除区，需人工确认")
        else:
            lines.append(f"#{i}  {fn}")
        lines.append(f"    ⭐ {stars} stars  |  🍴 {forks} forks  |  💻 {lang}  |  📅 {created}")
        lines.append(f"    🔗 https://github.com/{fn}")
        lines.append(f"    📡 来源: {source}")
        if topics:
            lines.append(f"    🏷️ {', '.join(topics[:10])}")
        lines.append(f"    📝 {desc}")
        lines.append(f"")
        lines.append(f"    README 摘要:")
        for readme_line in readme.split("\n")[:40]:
            lines.append(f"    {readme_line}")
        lines.append("")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════
# 主流程
# ══════════════════════════════════════════════════════════════

def main():
    print("🚀 NT Scout 启动")
    print(f"   时间: {utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    date_str = utcnow().strftime("%Y-%m-%d")

    history = load_history()
    print(f"   历史记录: {len(history)} 个已分析项目")

    candidates = {}

    # ── Step 1: GitHub Trending ──
    print("\n📈 Step 1: 抓取 GitHub Trending...")
    trending = scrape_trending()
    if not trending:
        print("  ⚠️⚠️ Trending 返回 0 个！GitHub 可能改了页面结构，scrape_trending 需检查。")
    for t in trending:
        fn = t["full_name"]
        if fn in history or fn in candidates:
            continue
        info = fetch_repo_info(fn)
        if info:
            info["source"] = t["source"]
            candidates[fn] = info
        time.sleep(0.3)

    # ── Step 2: 火箭上升项目 ──
    print("\n🚀 Step 2: 搜索火箭上升项目...")
    for rq in ROCKET_QUERIES:
        results = search_github(rq["q"], days=rq["days"], min_stars=0, per_page=10)
        for repo in results:
            fn = repo["full_name"]
            if fn not in history and fn not in candidates:
                repo["source"] = rq["label"]
                candidates[fn] = repo
        time.sleep(1)

    # ── Step 3: 分方向关键词搜索（新建 + 活跃老仓库 两路）──
    print("\n🔍 Step 3: 分方向关键词搜索（新建 + 活跃）...")
    for group_name, queries in SEARCH_GROUPS.items():
        print(f"   {group_name}")
        is_promo = group_name == PROMO_GROUP
        new_min = PROMO_MIN_STARS if is_promo else MIN_STARS
        active_min = ACTIVE_PROMO_MIN_STARS if is_promo else ACTIVE_MIN_STARS
        for q in queries:
            # ① 最近新建的仓库
            for repo in search_github(q, min_stars=new_min, mode="new"):
                fn = repo["full_name"]
                if fn not in history and fn not in candidates:
                    repo["source"] = f"{group_name} | 新建 | {q[:24]}"
                    candidates[fn] = repo
            time.sleep(2)  # 搜索 API 限速 30/分钟 → 间隔 ≥2s
            # ② 老但最近活跃的仓库
            for repo in search_github(q, days=ACTIVE_DAYS, min_stars=active_min, mode="active"):
                fn = repo["full_name"]
                if fn not in history and fn not in candidates:
                    repo["source"] = f"{group_name} | 活跃 | {q[:24]}"
                    candidates[fn] = repo
            time.sleep(2)

    print(f"\n📦 去重后候选项目: {len(candidates)} 个")

    # ── Step 4: 选取 Top N（推广类保底配额）──
    all_sorted = sorted(
        candidates.values(),
        key=lambda x: x.get("stargazers_count", 0),
        reverse=True,
    )

    # 推广类候选（按 source 前缀识别），单独按星标排序
    promo_repos = [
        r for r in all_sorted
        if str(r.get("source", "")).startswith(PROMO_GROUP)
    ]

    # 先锁定推广保底名额
    reserved = promo_repos[:PROMO_QUOTA]
    reserved_names = {r["full_name"] for r in reserved}

    # 剩余名额用全体（含未入选的推广项）按星标补满
    remaining_slots = MAX_REPOS - len(reserved)
    fillers = [
        r for r in all_sorted
        if r["full_name"] not in reserved_names
    ][:remaining_slots]

    # 合并后整体按星标重排（保底项混入正常排序，阅读体验一致）
    sorted_repos = sorted(
        reserved + fillers,
        key=lambda x: x.get("stargazers_count", 0),
        reverse=True,
    )

    promo_in_output = sum(
        1 for r in sorted_repos
        if str(r.get("source", "")).startswith(PROMO_GROUP)
    )
    print(f"   推广类保底: {len(reserved)} 个锁定 / 输出共含 {promo_in_output} 个推广项")

    if not sorted_repos:
        print("⚠ 今天没有发现新项目，跳过")
        return

    # ── Step 5: 抓取 README ──
    print(f"\n📖 Step 5: 获取 Top {len(sorted_repos)} 项目的 README...")
    for repo in sorted_repos:
        fn = repo["full_name"]
        print(f"   → {fn}")
        repo["readme_excerpt"] = fetch_readme(fn)
        if not repo.get("topics"):
            info = fetch_repo_info(fn)
            if info:
                repo["topics"] = info.get("topics", [])
        # 风险词扫描（含 README）
        repo["risk_hits"] = risk_flags(repo)
        # README 乱码也作为风险信号，归入排除复核
        if str(repo.get("readme_excerpt", "")).startswith(README_GARBAGE_SENTINEL):
            repo["risk_hits"] = ["README乱码/污染"] + repo["risk_hits"]
        if repo["risk_hits"]:
            print(f"     ⚠️ 风险信号: {', '.join(repo['risk_hits'][:5])}")
        time.sleep(0.5)

    # ── Step 6: 生成报告 & 写入 Google Doc + 仓库 ──
    print(f"\n📝 Step 6: 生成报告并写入...")
    report = format_report(sorted_repos, date_str)
    write_to_doc(report)
    write_to_repo(report, date_str)

    # ── Step 7: 更新历史记录 ──
    for repo in sorted_repos:
        history.add(repo["full_name"])
    save_history(history)

    print(f"\n✅ 完成!")
    print(f"   本次分析: {len(sorted_repos)} 个新项目")
    print(f"   历史总计: {len(history)} 个")


if __name__ == "__main__":
    main()
