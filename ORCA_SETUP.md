# Orca 接入说明

前提：你已经会用 git 和 Claude Code，本机装了 Orca。
这里只讲这个项目特有的配置。

## 这个项目在干嘛

`scout.py` 跑在 GitHub Actions 上，每天北京 9:00 抓 20 个开源项目，
结果写进 `latest.md`（仓库根目录）。你要做的是让 Orca 里的 Claude Code
读 `latest.md` + 用 `noveltime-repo-scout` skill 分析，按价值给 NovelTime 排序。

## 配置（一次性）

```bash
# 1. clone
git clone https://github.com/wenxiu216/github-scout.git

# 2. 装分析 skill（noveltime-repo-scout.skill 找 Wendy 要）
mkdir -p ~/.claude/skills
unzip noveltime-repo-scout.skill -d ~/.claude/skills/
# 确认：ls ~/.claude/skills/noveltime-repo-scout/SKILL.md
```

3. Orca → Projects → **+** → 选 clone 下来的 `github-scout`

4. Orca → 快捷命令 → 添加：
   - 标签：`分析日报`
   - 操作：**Agent 提示**　Agent：**Claude**　范围：**项目 / github-scout**
   - 提示：
     ```
     读 latest.md，按 noveltime-repo-scout skill 的方法分析里面的项目，
     挑出值得做的，按优先级排，说清每个为什么值得做、怎么用在 NovelTime。
     ```

## 日常

```bash
cd github-scout && git pull    # 拉当天日报
```
然后 Orca 里点「分析日报」。

## skill 的分析逻辑（改 skill 前先看）

`~/.claude/skills/noveltime-repo-scout/SKILL.md` 的核心约束：
默认每个项目都可能有用 → 拆能力原语 → 逐个往 NovelTime 业务面碰 →
给能达到的**最高**价值档（直接用/改造用/借鉴架构/思路启发）→
四个角度全靠不上才判「暂无连接」。
**别把它改回"先证明有用才看"的姿势——那是反的。**

## 改抓取范围

`scout.py` 里的 `SEARCH_GROUPS`（关键词分组）、`MAX_REPOS`、`MIN_STARS`、
`SEARCH_DAYS`。改完 push，Actions 自动生效。

## 手动触发抓取

GitHub → Actions → Daily GitHub Scout → Run workflow。跑完 `git pull`。
