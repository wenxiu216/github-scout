📊 开源日报 — 2026-11-04
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  floci-io/floci
    ⭐ 29059 stars  |  🍴 3230 forks  |  💻 Java  |  📅 2026-02-18
    🔗 https://github.com/floci-io/floci
    📡 来源: trending-daily
    🏷️ aws, aws-emulation, devops, docker, ec2, ecs, localstack, s3, sqs, testcontainers
    📝 Light, fluffy, and always free - The AWS Local Emulator alternative

    README 摘要:
    Any Cloud. Locally.
      Light, fluffy, and always free
      No account. No auth token. No feature gates. Just docker compose up.
    
      
      
      
      
      
      
    
      Quick Start ·
      Features ·
      Services ·
      SDKs ·
      Testcontainers ·
      Migration ·
      Docs
    
    ---
    
    ## What is Floci?
    
    Floci is a free, open-source local AWS emulator for development, testing, and CI.
    
    It gives you AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid feature gates. Point your AWS SDK, CLI, Terraform, CDK, OpenTofu, or test suite at `http://localhost:4566` and keep your existing workflows.
    
    Already using LocalStack? Floci is a drop-in replacement: swap the image and keep going. See Migrating from LocalStack.
    
    Floci is the AWS member of the Floci emulator family, named after floccus, the cloud formation that looks like popcorn.
    
    | Emulator | Cloud | Port |
    |---|---|:---:|
    | **floci** | **AWS** | **4566** |
    | floci-az | Azure | 4577 |
    | floci-gcp | GCP | 4588 |
    | floci-oci | OCI | 4599 |
    
    ## Quick Start
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  ⚠️风险  Usagi-org/ai-goofish-monitor
    ⚠️ 命中风险词: cookie —— 默认归排除区，需人工确认
    ⭐ 16815 stars  |  🍴 2879 forks  |  💻 Python  |  📅 2025-07-16
    🔗 https://github.com/Usagi-org/ai-goofish-monitor
    📡 来源: trending-daily
    🏷️ ai, ai-assistant, ai-tools, automation, gemini, goofish, open-source, openai, playwright, tool
    📝 基于 Playwright 和AI实现的闲鱼多任务实时/定时监控与智能分析系统，配备了功能完善的后台管理UI。帮助用户从闲鱼海量商品中，找到心仪产品。

    README 摘要:
    # 闲鱼智能监控系统
    
    [中文] ｜ English
    
    基于 Playwright 和 AI 的闲鱼多任务实时监控，提供完整的 Web 管理界面。
    
    ## 核心特性
    
    - **Web 可视化管理**: 任务管理、账号管理、AI 标准编辑、运行日志、结果浏览
    - **AI 驱动**: 自然语言创建任务，多模态模型深度分析商品
    - **多任务并发**: 独立配置关键词、价格、筛选条件和 AI Prompt
    - **高级筛选**: 包邮、新发布时间范围、省/市/区三级区域筛选
    - **即时通知**: 支持 ntfy.sh、企业微信、Bark、Telegram、Webhook等多渠道
    - **定时调度**: 支持 Cron 配置周期性任务
    - **账号与代理轮换**: 多账号管理、任务绑定账号、代理池轮换与失败重试
    - **Docker 部署**: 一键容器化部署
    
    ## 截图
    
    ## 🐳 Docker 部署（推荐）
    
    ```bash
    git clone https://github.com/Usagi-org/ai-goofish-monitor && cd ai-goofish-monitor
    cp .env.example .env
    vim .env # 填写相关配置项
    docker compose up -d
    docker compose logs -f app
    docker compose down
    ```
    
    如果镜像无法访问或下载速度慢，可尝试使用加速：
    ```bash
    
    docker pull ghcr.nju.edu.cn/usagi-org/ai-goofish:latest
    docker tag ghcr.nju.edu.cn/usagi-org/ai-goofish:latest ghcr.io/usagi-org/ai-goofish:latest
    docker compose up -d
    
    ```
    
    - 默认 Web UI 地址：`http://127.0.0.1:8000`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  spotify/portal-ai-plugins
    ⭐ 3100 stars  |  🍴 242 forks  |  💻 TypeScript  |  📅 2026-07-23
    🔗 https://github.com/spotify/portal-ai-plugins
    📡 来源: trending-daily
    📝 无描述

    README 摘要:
    # Spotify Portal AI Plugins
    
    Bring Spotify Portal into Claude Code, Codex, Cursor, and pi.
    
    This plugin provides focused workflows for the
    Portal CLI: set up
    authentication, search your software catalog, build service briefings, run
    diagnostics, and invoke Portal actions.
    
    ## Highlights
    
    - Set up the Portal CLI for your current coding-agent environment.
    - Run read-only diagnostics to verify plugin, CLI, authentication, and action readiness.
    - Search the software catalog and technical documentation using natural language queries.
    - Generate concise service briefings with available ownership, health, incident, and documentation details.
    - Discover and safely invoke Portal actions with built-in help, dry-run, and confirmation safeguards.
    - Create, run, check, and troubleshoot Fleetshift shifts, open PRs from completed runs, and stop a run on request.
    
    The marketplace also ships **shunt** (Claude Code only for now): a plugin that routes I/O-heavy agent work — bulk file reads and boilerplate generation — to AiKA modes running cheaper worker models, via the Portal CLI actions registry. See `plugins/shunt/README.md`.
    
    ## Installation
    
    ### Claude Code
    
    ```bash
    claude plugin marketplace add spotify/portal-ai-plugins
    claude plugin install portal@portal
    claude plugin install shunt@portal   # optional: token-saving AiKA delegation
    ```
    
    Start a new session and run:
    
    ```text
    /portal:setup
    ```
    
    ### Codex
    
    ```bash
    codex plugin marketplace add spotify/portal-ai-plugins

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  KKKKhazix/agent-autoloop
    ⭐ 1372 stars  |  🍴 275 forks  |  💻 TypeScript  |  📅 2026-11-03
    🔗 https://github.com/KKKKhazix/agent-autoloop
    📡 来源: 🚀 5天300+星
    🏷️ ai-agents, automation, claude-code, cli, codex, event-driven, mcp, nodejs, self-hosted, typescript
    📝 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

    README 摘要:
    # Agent Autoloop
    
    **让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。**
    
    **中文** | English
    
    上手 · 场景模板 · 插件 · 内核 · 文档
    
    ## 它解决什么问题？
    
    平时我们用 Claude Code、Codex 这类命令行 Agent，大多是“人守着终端用”：你输一句话，盯着它跑，等它问你下一步；一旦关掉窗口或者人走开，事情就断了。
    
    **Agent Autoloop** 是一个极轻量的自动化中台。它把任务调度做成一个零外部依赖的**内核**，把事件来源、Agent、通知通道，甚至代码上线流水线全部拆成可随时插拔的**插件**。
    
    - **一台电脑、一条命令就能跑。** 装在你的 Mac 或 Linux 上，不用买云服务器，也不用开放公网端口。
    - **一行配置接新 Agent。** 不需要 SDK，也不需要改 Agent 源码，能接收提示词并打印最后一条回复的命令行工具都能接。
    - **没有后台界面。** 需要你拍板时把卡片推到飞书、钉钉、企微、Slack、Discord 或桌面通知；想看全局进展，敲一行命令。
    
    ## 上手
    
    支持 macOS 和 Linux。运行前需要装好 Node 24、Git、curl，以及任意一个你已经登录好的命令行 Agent，不需要 GitHub 账号。也可以直接把安装说明丢给你的 Agent，让它替你装好。
    
    ```bash
    curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh
    ```
    
    装好后用你本机的 Agent 真实走一遍“提问 → 退出等回复 → 拍板 → 接着干完”：
    
    ```bash
    agent-autoloop try
    ```
    
    下面是在终端里的真实输出：
    
    ```text
    事件发出去了，Agent 开始干活……
    
    Agent 结束了这一轮，问了你一个问题。它现在不占进程、不花 Token。
    
    【等你决定】#1 试跑：选一个颜色

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  wquguru/cicada
    ⭐ 792 stars  |  🍴 168 forks  |  💻 Swift  |  📅 2026-11-01
    🔗 https://github.com/wquguru/cicada
    📡 来源: 🚀 5天300+星
    🏷️ live-captions, macos, meeting-notes, menubar-app, simultaneous-interpretation, speech-recognition, subtitles, swift, swiftui, translation
    📝 知了 Cicada · 任意会议与直播的实时字幕、同声传译、AI 会议纪要（macOS）。Live subtitles, interpreting and meeting notes for any call or stream on your Mac.

    README 摘要:
    知了 · Cicada
    
      任何会议、任何直播，没有语言障碍。
      听得懂，说得出，记得住。Mac 上的实时纪要、双语文字记录、字幕与同声传译。
    
      
      &nbsp;
      
    
      
      
      
      
    
    简体中文 · English
    
    无论是用 Zoom、飞书、腾讯会议开会，还是听 X Spaces 和 YouTube 直播，知了都能实时给出双语字幕、边听边写结构化纪要。遇到需要发言的时候，按住键盘右边的 `⌥` 键开口，对方就能在会里直接听到翻译好的语音。这一切都靠直接读取 Mac 系统声音并在本机识别来完成，声音不出电脑，不用往会里塞机器人，对方更是完全无感。
    
      
    
    ## 主要功能
    
    ### 实时纪要与双语文字记录
    
    开会时纪要窗口边听边整理总结、议题要点、结论、待办、鱼骨图和人名术语表，点一下结论或待办就能跳回双语文字记录里的原话。纪要会统一文中人名和术语的写法并记下听错的变体，按 `⌘F` 搜索时能连同识别错的写法一起搜出来。
    
    ### 实时字幕与语言识别
    
    对方开口几秒钟就能在本地自动认出语言并翻成你的系统语言，按 `⌃⌥S` 可以在纪要窗口、字幕条和不显示之间切换。字幕条只在有人说话时出现，鼠标划过时自动变透明，不会挡住底下的按钮。
    
    ### 同声传译
    
    按住键盘右边的 `⌥` 键说话，对方在会议软件里就能直接听到翻译后的语音，打开同声传译时知了会自动把系统麦克风切到一键安装的虚拟驱动 BlackHole 2ch。填了 Ling API key 后可以用自然人声或用 8 到 30 秒录音克隆你自己的声音，不填也能用 Mac 自带语音。
    
      
    
    ### 会议记录
    
    每场会议的双语文字记录、纪要和原始录音都保存在本机，打开实验性的说话人识别后还能区分对方不同的说话人并在有 Ling key 时填上名字。会议软件挂断或 10 分钟没人说话时会自动结束并截掉空白，会后随时可以补生成纪要，或导出成 Markdown、Word 和 SRT 字幕。目前记录里的你只包含按住说话键说的话，会上直接开口的部分见路线图。
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  AssassinCreator/steam-stash-value-report-card
    ⭐ 714 stars  |  🍴 57 forks  |  💻 Python  |  📅 2026-11-02
    🔗 https://github.com/AssassinCreator/steam-stash-value-report-card
    📡 来源: 🚀 5天300+星
    🏷️ cli, inventory, price-check, python, report-card, steam, steam-market, valuation
    📝 Value your Steam stash in the terminal and print it as a share card: per game, per market, what sold and what sits. One Windows portable build, no account.

    README 摘要:
    ```text
    $ stashcard
      paste a profile  ->  pick a card  ->  get a PNG worth posting
    ```
    
    **Stashcard** values a Steam account and its inventories (CS2, Dota 2, TF2, Rust, Steam community items
    or any custom app) from your terminal, prices them on Steam and on the big cash marketplaces, and prints
    the result as a shareable card: a report card, a game card, an inventory picture, a thermal receipt, a
    marketplace comparison, or a then-vs-now / A-vs-B diff.
    
    Every number carries its venue and window. `LOWEST` is the floor listing right now. `AVG` is the mean
    of real sales over a window you pick. Steam money is wallet funds; everything else is cash, and the two
    are never mixed silently. When a source has nothing, Stashcard falls back and says so on the row, in
    the totals and in the card footer. Nothing unpriced is ever counted as zero.
    
    Free and open source. No accounts, no paid APIs, no telemetry.
    
      
    
    > [!TIP]
    > **Run Stashcard on your home PC. Windows is the recommended setup.** Steam rate-limits datacenter,
    > VPS and cloud IPs heavily, so live scans from a server are unreliable. On a server only the demo and
    > cached data work reliably. See Where to run it.
    
    ---
    
    ## Download
    
    | System | File | |
    |---|---|---|
    | Windows 10 and 11 | `steam-stash-value-report-card.zip` | One zip. No installer, no admin rights |
    
    Unpack the whole folder and start `Main.exe`. No installer, no admin rights.
    
    `Main.exe` is code-signed, so Windows starts it without a warning. Keep
    `Stashcard` next to it: they ship together.
    
    ## Gallery
    
    Real cards from the bundled demo (a fictional profile with real item names, icons and a dated price

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  govijr/terminal-mac
    ⭐ 648 stars  |  🍴 49 forks  |  💻 Swift  |  📅 2026-11-03
    🔗 https://github.com/govijr/terminal-mac
    📡 来源: 🚀 5天300+星
    🏷️ cli, gui, macos, shell, swift, terminal, tui
    📝 Entire MacOS running in your terminal.

    README 摘要:
    # terminal-mac
    
    A separate macOS desktop for computer-use agents, viewed and controlled from a terminal.
    
    **iOS simulators and iPhones:** see the sibling project terminal-phone.
    
    `terminal-mac` is an early release candidate for Apple silicon. Apple Virtualization runs a real macOS guest. A bundled helper **inside that guest** captures its screen and posts input events. A terminal viewer streams that screen using Kitty or iTerm2 graphics. Agent commands use the same helper without moving the physical Mac's pointer or changing its clipboard.
    
    The guest is a separate Mac: it has its own apps, files, accounts and permissions. It does not inherit your running host apps or signed-in sessions. The VM still consumes host CPU, memory and storage.
    
    ## Requirements
    
    - Apple silicon Mac, macOS 14 or later.
    - No development tools are needed for a prebuilt release. Maintainers need Xcode 16 or later / Swift 6 to build.
    - Internet on first run to download macOS directly from Apple, or an existing compatible `.ipsw`.
    - Space for the cached restore image and a growing VM disk (64 GiB logical size by default).
    - Ghostty, Kitty or iTerm2 for the inline viewer. Other terminals can use the native VM window and agent CLI. tmux passthrough and automatic terminal splits are not implemented.
    
    ## Install and run
    
    ```sh
    curl -fsSL https://github.com/govijr/terminal-mac/releases/latest/download/get.sh | bash
    ```
    
    The installer downloads the latest release and verifies its SHA-256 before installing. You can also extract a release ZIP and run `bash install.sh` from it.
    
    The installer places one launcher in `~/.local/bin` and the bundled runtime under `~/.local/lib/terminal-mac`. Add `~/.local/bin` to your PATH to use simply `terminal-mac`. It needs no administrator rights and does not edit your shell configuration. `bash install.sh --prefix /absolute/path` selects another location.
    
    Running `terminal-mac` in an interactive terminal starts the guided flow. `terminal-mac up` does the same explicitly. It automatically downloads/caches a compatible Apple restore image, installs a virtual Mac, boots it and checks the guest helper. Later runs reuse the existing VM and reconnect. Unsupported terminals get the native desktop window.
    
    **Current status:** early release candidate. Releases are self-signed (no Apple notarization), which the curl installer doesn't need. Live guest acceptance on a clean Mac is still pending.
    
    ## Use with agents
    
    terminal-mac gives agents computer use in a separate v

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  vstorm-co/agenticos
    ⭐ 208 stars  |  🍴 36 forks  |  💻 Python  |  📅 2026-07-31
    🔗 https://github.com/vstorm-co/agenticos
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    🏷️ agentic-ai, agentic-os, agents, ai-agents, ai-assistant, ai-governance, ai-teammates, browser-automation, fastapi, llm
    📝 Open-source, self-hosted AI agent platform for your company's AI teammates. Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, 4,700+ MCP servers, budgets, approvals and an audit trail. An alternative to ChatGPT Enterprise and Grok Bot. Apache-2.0, built on Pydantic AI.

    README 摘要:
    Open-source, self-hosted AI agent platform for your company's AI teammates.
      Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, MCP, budgets, approvals and an audit trail.
      Apache-2.0 &middot; built on Pydantic AI
    
      🏆 Built by Vstorm — a recipient of the 2026 Open Agentic AI Innovation Award.Recognized by the Agentic AI Foundation for adopting AGENTS.md and integrating MCP in its open-source framework.Read the AAIF announcement &middot; The work behind the award
    
      See it &middot;
      Highlights &middot;
      What is it? &middot;
      Quick start &middot;
      Server, desktop &amp; mobile &middot;
      Integrations &middot;
      Product tour &middot;
      Find your path &middot;
      What ships &middot;
      FAQ &middot;
      Website &middot;
      Introduction deck &middot;
      Documentation
    
      
      
      
      
    
      English &middot;
      Polski &middot;
      Deutsch &middot;
      Español
    
    *Prepared conversation with fictional sales data in the real Visuals renderer. No live CRM or new model-generation run is represented.*
    
    AgenticOS gives every team AI teammates: agents that work with files, run code, browse the web and use your company's tools and knowledge. Your colleagues and your agents work in the same live chat, and any agent can hand code to Claude Code or Codex, on the ChatGPT or Claude subscription you already pay for. It is open source (Apache-2.0) and self-hosted, a layer you run on your own infrastructure. Build and publish agents in the browser, share them with colleagues, and manage their access, cost and results in one place.
    
    **New here?** Click through the 17-slide introduction: the problem, the idea, the product on real screens, its controls and limits, and how to start. For every screen in detail, open the 47-slide product tour. Arrow keys step through either deck; `O` lists every slide.
    
    ## New in the latest releases
    
    - **Your local Claude Code or Codex, inside desktop chat.** Choose a coding agent per conversation, work in an approved local folder, resume its session and apply corrections while it works. Sign in through the coding agent's own terminal flow.
    - **Your skills and project instructions.** Opt a desktop conversation into local skills and `AGENTS.md` / `CLAUDE.md`, read from your computer. Each new chat starts with this sharing off.
