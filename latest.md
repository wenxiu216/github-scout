📊 开源日报 — 2026-11-14
共发现 14 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  louislam/uptime-kuma
    ⭐ 93968 stars  |  🍴 8728 forks  |  💻 JavaScript  |  📅 2021-07-03
    🔗 https://github.com/louislam/uptime-kuma
    📡 来源: trending-daily
    🏷️ docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring
    📝 A fancy self-hosted monitoring tool

    README 摘要:
    # Uptime Kuma
    
    Uptime Kuma is an easy-to-use self-hosted monitoring tool.
    
        
    
    ## 🥔 Live Demo
    
    Try it!
    
    Demo Server (Location: Frankfurt - Germany): 
    
    It is a temporary live demo, all data will be deleted after 10 minutes. Sponsored by Uptime Kuma Sponsors.
    
    > [!WARNING]
    > Be careful - the top result in Google, uptimekuma.co, is not our official website, we don't control the website. I recommend following the installation guide in this GitHub repo.
    
    ## ⭐ Features
    
    - Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Websocket / Ping / DNS Record / Push / Steam Game Server / Docker Containers
    - Fancy, Reactive, Fast UI/UX
    - Notifications via Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and 90+ notification services, click here for the full list
    - 20-second intervals
    - Multi Languages
    - Multiple status pages
    - Map status pages to specific domains
    - Ping chart
    - Certificate info
    - Proxy support
    - 2FA support
    
    ## 🔧 How to Install
    
    ### 🐳 Docker Compose
    
    ```bash
    mkdir uptime-kuma
    cd uptime-kuma
    curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
    docker compose up -d

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  google/elephant-goldfish-model
    ⭐ 18737 stars  |  🍴 1399 forks  |  💻 Python  |  📅 2026-09-13
    🔗 https://github.com/google/elephant-goldfish-model
    📡 来源: trending-weekly
    🏷️ agent-skills, ai-agents, antigravity, claude-code, claude-code-plugin, claude-skills, codex, codex-plugin, coding-agents, context-engineering
    📝 Open-source plugin for designing and reviewing software with agents

    README 摘要:
    Design with an elephant. Review with a goldfish.
    
      Install &ensp;·&ensp;
      Quickstart &ensp;·&ensp;
      Documentation &ensp;·&ensp;
      Website
    
    Develop ideas with context and review documents with fresh eyes. EGM is an open-source plugin for AI assistants.
    
    **Elephant** holds your project context and drafts the specification. **Goldfish** reviewers examine the draft and referenced source material without the earlier conversation, helping expose unstated assumptions and blind spots. **You** make the architectural trade-offs and approve the specification before implementing.
    
    The built-in draft and design-review workflow targets software specifications. For other documents, choose reviewers and standards with `/egm-review-loop`. Bootstrap and drift reporting apply to software codebases.
    
    https://github.com/user-attachments/assets/93c799a2-10a3-4266-af02-eb79dd33a9a2
    
    ## Install
    
    Choose your coding agent. Install the complete plugin so its skills can read the reviewer prompts and document standards.
    
    ### ChatGPT and Codex desktop
    
    Open the published EGM plugin in the desktop app and install it. This listing is desktop-only. For Codex CLI, use the commands below.
    
    ### Antigravity CLI
    
    ```sh
    agy plugin install https://github.com/google/elephant-goldfish-model
    ```
    
    For the **Antigravity App** and **Antigravity for IDEs** (Visual Studio Code extension), run `/plugin` or see the installation instructions.
    
    ### Claude Code
    
    ```sh
    claude plugin marketplace add google/elephant-goldfish-model
    claude plugin install egm@egm
    ```
    
    ### Codex CLI
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  backnotprop/plannotator
    ⭐ 10572 stars  |  🍴 791 forks  |  💻 TypeScript  |  📅 2025-12-28
    🔗 https://github.com/backnotprop/plannotator
    📡 来源: trending-daily
    🏷️ agents, claude-code, code-review, codex, obsidian, opencode, pi-mono, plan-mode, skills
    📝 The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click. 

    README 摘要:
    Everything you need to annotate and stay in the loop with your agents
      Inbox Surface • Artifacts • Code Review
      Annotate plans, specs, markdown, HTML, and other interactive artifacts. Review diffs and PRs. Send feedback to your agent.
    
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      
        
        
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      
        
        
      &nbsp;&nbsp;
      
        
        
      
    
      Plannotator Inbox · Official site · Code Review · Visual HTML Skills · Herdr Annotate · (Legacy) Plan Mode
    
    # Plannotator
    
    **⭐️ NEW:** Plannotator Inbox is the missing review layer between you and multi-agent work. It surfaces decisions, prototypes, variations, plans, and everything you need to stay in the loop. Works with all coding agents and personal assistants.
    
    Plannotator is a local, browser-based review surface for AI coding agents: Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro, Droid, Amp, DeepSeek Harness, and Pi. Plannotator Inbox also works with personal assistants (Grok Bot, Muse, Hermes, OpenClaw).
    
    **It plugs directly into your agent** through plugins, hooks and commands. When the agent proposes a decision, plan, html, or finishes working, the app opens in your browser and you mark it up, comment, and send feedback directly to the agent for it to act on it.
    
    ### Review documents, plans, and agent messages
    
    Annotate plans, specs, messages, html, then send the feedback to your agent. 
    
    Demo: Plan review with Pi
    
    ### Code Review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  tradermonty/claude-trading-skills
    ⭐ 4314 stars  |  🍴 881 forks  |  💻 Python  |  📅 2025-10-19
    🔗 https://github.com/tradermonty/claude-trading-skills
    📡 来源: trending-daily
    📝 Claude Code skills for equity investors and traders — market analysis, technical charting, economic calendars, screeners, and trading strategy development.

    README 摘要:
    # Claude Trading Skills
    
    Claude Trading Skills started as a personal project to use AI to improve my own trading process.
    
    Claude Trading Skills is a Claude Skills-based trading workflow toolkit for time-constrained individual investors.
    
    It is designed for investors who use long-term investing, ETFs, and dividend stocks as their core, while using disciplined swing trading as a satellite strategy when market conditions are favorable.
    
    The goal is not to outsource buy/sell decisions to AI. The goal is to structure market review, risk management, trade planning, journaling, and continuous improvement. It is open source because the workflows, checklists, and review habits behind better trading decisions can improve through shared practice.
    
    This is not a signal service or a promise of profitability. It is a toolkit for traders who want to build a better decision process.
    
    The project follows a **first for self, open for others** stance: it is built first as a practical workflow the author uses, then shared openly for others who face similar constraints.
    
    📖 **Documentation site:** 
    
    **Project vision:** `PROJECT_VISION.md`
    
    日本語版READMEは`README.ja.md`をご覧ください。
    
    ## Disclaimer
    
    This repository is for educational, research, and process-improvement purposes only. It is not financial advice, investment advisory service, tax advice, legal advice, a signal service, or a broker execution platform. Trading and investing involve risk, including loss of principal. Past performance, backtests, screens, reports, and AI-generated analysis do not guarantee future results. All trading decisions, position sizing, tax/regulatory compliance, and broker usage are the user's responsibility.
    
    The project is provided under the MIT License, **AS IS, WITHOUT WARRANTY**.
    
    ## Who This Is For
    
    This repository is designed for:
    
    - Time-constrained individual investors
    - Long-term investors who also want disciplined swing-trading upside
    - Dividend and ETF investors who want structured portfolio review
    - Traders who want to manage risk before finding trade candidates
    - Investors who want to journal and improve their decision process
    
    It is not designed for fully automated trading, signal outsourcing, or short-term scalping.
    
    ## Recommended Starting Path
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  expo/exact
    ⭐ 4062 stars  |  🍴 98 forks  |  💻 Rust  |  📅 2026-11-02
    🔗 https://github.com/expo/exact
    📡 来源: 🚀 两周800+星
    🏷️ ai-agents, appkit, coding-agents, cross-platform, css, ios, linux, macos, native-apps, rust
    📝 Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

    README 摘要:
    # Exact
    
    **Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI
    agent can build it, run it, see it, and test it on every one of them.**
    
    **Building an app?** With the tools installed (Quick start, step 1),
    run `bun scripts/exact.mjs setup` once, make the app with `bun scripts/exact.mjs new `,
    and read `docs/start-here.md` (for a website,
    `docs/start-here-site.md`): that guide is the only required
    reading. The rest of this page describes Exact for people deciding whether to use it
    or working on it.
    
    > [!TIP]
    > **Try it with a coding agent.** On a Mac with Xcode, Rust, Bun, and Chrome installed,
    > give Claude Code this prompt:
    >
    > ```text
    > Clone https://github.com/expo/exact and follow its README to make a new Exact
    > app with `exact new`. Run `bun scripts/exact.mjs setup` once first. Make a todo
    > list where I can add items, check them off, delete them,
    > and see how many are left. Put the view in Contract and keep the list in `app.ts`.
    > Write an `app.test.contract`, pass it on web, macOS, and the iOS Simulator with
    > `scripts/agent.mjs`, then open the app for me on all three.
    > ```
    >
    > A fresh agent given the earlier version of this prompt on a clean clone (2026-10-04, Hermes already in the
    > machine cache, Cargo's cache warm) finished in about 57 minutes, and its tests passed
    > on all three platforms. About 25 of those minutes were the first macOS and iOS builds,
    > roughly 13 minutes each; later builds take a minute or two. On a machine that has
    > lacked Hermes, its source build came first and added time. Current setup downloads and
    > verifies the pinned host/iOS bundles once instead; ordinary builds stay offline.
    
      
        Web
        iOS
        macOS
      
      
        
        

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  shanselman/gputaskman
    ⭐ 3123 stars  |  🍴 151 forks  |  💻 Python  |  📅 2026-11-03
    🔗 https://github.com/shanselman/gputaskman
    📡 来源: 🚀 两周800+星
    📝 A GPU task manager for Windows, Linux, and WSL: per-process VRAM, GPU activity, and LLM model/KV-cache insights (Windows AMD and NVIDIA).

    README 摘要:
    # gputaskman
    
    **An `htop` for what's inside your GPU, not just how full it is.**
    
    Windows with NVIDIA/AMD telemetry and Intel WDDM activity, plus Linux and WSL support (NVIDIA
    everywhere, AMD and Intel on native Linux; see
    Linux and WSL) and macOS on Apple Silicon (see macOS). A terminal UI
    that connects per-process GPU memory and engine activity with loaded runtimes, model files, and
    LLM buffer breakdowns.
    
    Task Manager says "15 GB used." This tries to answer: *by what? Model weights? KV cache?
    Your browser? The desktop compositor? And why is so much GPU memory in system RAM?*
    
    **Scope: local GPU workloads, not cloud services.** Decision models, vision, speech, LLM inference,
    training/fine-tuning (including Unsloth), graphics, and video all belong here. Visibility varies:
    process memory and engine activity are measured; identifying individual models and their work
    requires supporting evidence. A PyTorch/CUDA DLL alone cannot identify a model or prove training,
    and a mapped file does not prove that model is resident on the GPU or being exercised.
    CPU-only, NPU-only, and cloud workloads are out of scope.
    
    > Early, experimental software. Device and process counters are measurements; classifications
    > and GGUF-derived breakdowns are estimates. This does not dump VRAM or enumerate a game's textures.
    
    ## Install from PyPI
    
    gputaskman is on PyPI. No repository clone is needed:
    
    ```powershell
    uv tool install gputaskman
    gputaskman
    ```
    
    Or, with pipx:
    
    ```powershell
    pipx install gputaskman
    gputaskman
    ```
    
    Works on Windows, Linux/WSL, and macOS with Python 3.11+ and the supported GPU/driver

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  Likely7/Veyra-NRVideo
    ⭐ 1728 stars  |  🍴 77 forks  |  💻 C++  |  📅 2026-09-09
    🔗 https://github.com/Likely7/Veyra-NRVideo
    📡 来源: trending-daily
    📝 Bring PS5 GTA6 to 120FPS with DLSS 5. An advanced Windows video player and capture enhancement tool featuring real-time preview for videos, images, and capture card sources. Combine AI-powered Super Resolution, DLSS5 image enhancement, and Frame Generation to deliver a next-generation visual experience.

    README 摘要:
    # Veyra
    
    ### Real-time GPU Video Enhancement for Windows
    
    **Super Resolution · Denoising · HDR · Frame Generation · Capture · PS5 / Xbox / PC Streaming**
    
    Turn local video, capture cards and game streaming into one real-time GPU enhancement pipeline.
    
    **79K+ cumulative Veyra portable-package downloads** (79,332 as of 2026-11-08) · **103K+ downloads across all GitHub Release assets** (103,337 including source archives, checksums and images). GitHub Releases · Counts are download events, not unique users.
    
    **⬇ Download Latest Release**
    &nbsp;&nbsp;·&nbsp;&nbsp;
    **📖 User Guide / Wiki**
    &nbsp;&nbsp;·&nbsp;&nbsp;
    **🇨🇳 简体中文**
    &nbsp;&nbsp;·&nbsp;&nbsp;
    **🐛 Report an Issue**
    
      
        
      
    
    One engine. Any source. Real-time enhancement.
    
      
    
    ⭐ Star History
    
      
    
      Open source · GPL-3.0 · Windows 11 · C++ · DirectX 12 · NVIDIA & AMD
    
    ---
    
    **2.1.2 update:** dual SR, SR-then-downsample, NVIDIA Low Latency, experimental RX 7000 NR and capture/FG/audio/volume fixes. Full update and migration.
    
    **2.1.1 historical release, 2026-10-27:** processed-picture recording with audio,90° playback rotation, per-layer NR percentage controls and export sizing, event-driven refresh/VRR/HDR queries, AMD HDR+NR handling, AA ordering, capture timestamp handling, NR shutdown, popup layout, screenshots and fullscreen fixes. All changes since2.1.0.
    
    **New-effect cost examples:** RTX5070 standard4K anti-aliasing fixtures: FXAA~0.15ms, SMAA/MLAA~0.30ms. Final single-face mesh beauty:1080p~0.93ms,4K~1.42ms. Costs vary with content/hardware; no local AMD speedup percentage was measured. Conditions and limits.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  deepseek-ai/chat-demo
    ⭐ 1174 stars  |  🍴 190 forks  |  💻 TypeScript  |  📅 2026-11-12
    🔗 https://github.com/deepseek-ai/chat-demo
    📡 来源: 🚀 5天300+星
    📝 Chat Demo

    README 摘要:
    # chat-demo
    
    English | 简体中文
    
    A static chat demo powered by the DeepSeek API. No application backend is required: the browser connects directly to the configured API service.
    
    You can try the app online or download the archive from Releases, extract it, and double-click `index.html` to use it locally without installation or a build. Enter your API key in Settings before your first chat.
    
    ## Getting started
    
    Install Node.js 22.12+ and pnpm, then run:
    
    ```sh
    git clone https://github.com/deepseek-ai/chat-demo.git
    cd chat-demo
    pnpm install
    pnpm dev
    ```
    
    Open http://localhost:8090.
    
    To build the static site:
    
    ```sh
    pnpm build
    ```
    
    The output is written to `dist/`. Deploy it to a static web server or open `dist/index.html` directly. Opening the file directly requires browser support for storage on `file://` pages and an API service that permits their cross-origin requests.
    
    ## Features
    
    - Multiple conversations with automatic titles, renaming, and deletion; edit prompts, regenerate replies, and switch between message branches.
    - Streaming replies, deep thinking, smart search, link reading, and source citations; stop generation or continue eligible replies.
    - Upload, paste, or drag and drop attachments; use voice input and read replies aloud. A live audio spectrum appears in the first row of the input area while recording on mobile.
    - Markdown, syntax highlighting, KaTeX math, and Mermaid diagrams.
    - Simplified Chinese and English, light and dark themes, mobile layouts, location settings, and chat history import and export.
    
    ## Data and storage
    
    Your API key and settings are stored in the browser's localStorage. Conversations and original attachments are stored in IndexedDB. Local data is isolated by browser profile and site origin. Sending messages, uploading attachments, and using speech features sends the relevant content to the configured API service.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  JDhruv14/line-art-animation
    ⭐ 678 stars  |  🍴 108 forks  |  💻 TypeScript  |  📅 2026-11-10
    🔗 https://github.com/JDhruv14/line-art-animation
    📡 来源: 🚀 5天300+星
    🏷️ claude-skill, line-art, svg-animation, typescript
    📝 A Claude skill and TypeScript library for animated line-art SVG components: ink figures that walk and react, scenes with a day/night cycle.

    README 摘要:
    # line-art-animation
    
    A Claude skill and a small TypeScript library for animated line-art components:
    ink-on-paper figures that walk, ride and react, in scenes that run from day to night.
    Everything is drawn live in SVG, so it stays sharp at any size and responds to the
    pointer.
    
    | Day | Night |
    |---|---|
    |  |  |
    
    ## What's in the repo
    
    | | |
    |---|---|
    | `SKILL.md`, `references/` | The skill: workflow, the rules that make the style work, and guides for style, motion, scenes, verification, matching a reference clip and rendering video. |
    | `lib/` | Four dependency-free TypeScript modules: drawing primitives (`ink.ts`), a walk/run solver (`gait.ts`), springs, pendulums and wind (`motion.ts`), and a time-of-day palette (`daynight.ts`). |
    | `examples/walker/` | One figure in about 150 lines: a man with a briefcase walks across the card; click him and he tips his hat. |
    | `examples/village/` | A full scene: a street of machiya, a tea house and a bath house by a canal, villagers on schedules, a cat, birds, a boatman, lit windows and reflections, about a dozen interactions. |
    | `scripts/` | Deterministic frame capture for video, and tools for measuring a reference clip. |
    
    ## Install the skill
    
    For Claude Code, clone it into your skills folder:
    
    ```sh
    git clone https://github.com/JDhruv14/line-art-animation ~/.claude/skills/line-art-animation
    ```
    
    or into `.claude/skills/` inside a single project. Then ask for what you want, for example:
    
    - "Make a line art animation of a bakery at dawn: a baker carrying trays, steam from the oven, a cat in the window."
    - "Turn this clip into a looping line-art component, matching its walk exactly." (attach or link the clip)
    - "Add a day-night cycle to the scene and render a 30-second 1080p video."
    
    Claude reads `SKILL.md`, copies `lib/` into your project, shows one figure for approval
    before building the rest, and checks motion frame by frame before handing it over.
    
    ## Run the examples
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  DevedevT/FFmpeg-GUI-Editor-Windows
    ⭐ 541 stars  |  🍴 0 forks  |  💻 Visual Basic .NET  |  📅 2026-11-12
    🔗 https://github.com/DevedevT/FFmpeg-GUI-Editor-Windows
    📡 来源: 🚀 5天300+星
    🏷️ converter, ffmpeg, ffmpeg-command, ffmpeg-gui, ffmpeg-libraries, ffmpeg-script, gui, gui-application, image-compression, media-converter
    📝 Lightweight portable FFmpeg GUI & lossless video trimmer for Windows (ready-to-use .exe). Supports English, Russian, Chinese, German, French & Italian.

    README 摘要:
    # FFmpeg-GUI-Editor-Windows — Ready-to-Use Free Portable Video Editor (.exe)
    
    **FFmpeg-GUI-Editor-Windows** is a lightweight, fast, and **free open-source video editor for Windows 10 and Windows 11** that works as an intuitive graphical user interface (**FFmpeg GUI**). Built specifically for users who want to **download a ready-to-use `.exe` executable** to trim, crop, compress, and convert videos without touching the command line.
    
    No installation, no Python setup, no manual `PATH` configuration, and no watermarks. Just download the release files, place them in the same folder, and start editing. Licensed under **GPL v3**.
    
    ---
    
    ### 📥 Direct Download & Important Setup Instructions (`.exe` + `libvlc.dll`)
    The release package consists of **two required files**: the main executable (`.exe`) and the media engine library (**`libvlc.dll`**).
    
    1. Open the **Releases** page of this repository.
    2. Download **both files** from the latest release:
       * **`FFmpeg-GUI-Editor.exe`** (the main application)
       * **`libvlc.dll`** (required core video playback & rendering library)
    3. **Important:** Place both files inside the **same folder** on your PC or USB drive (do not separate them).
    4. Double-click the **`.exe`** file to launch the editor immediately — no installation required.
    
    > **⚠️ Note:** Both the `.exe` file and `libvlc.dll` must remain in the exact same directory for the program to start and preview videos properly.
    
    ---
    
    ### 🖼️ Interface & Quick Visual Guide
    
    ---
    
    ### 🌍 Multi-Language Interface (6 Languages Built-In)
    Switch between 6 languages directly in the interface without downloading extra language packs:
    * 🇬🇧 **English**
    * 🇷🇺 **Русский** (Russian)
    * 🇨🇳 **中文** (Chinese)
    * 🇩🇪 **Deutsch** (German)
    * 🇫🇷 **Français** (French)
    * 🇮🇹 **Italiano** (Italiano)
    
    ---
    
    ### 🎬 Core Video Editing Features
    * **Lossless Video Trimmer & Cutter:** Cut and trim video start/end points with frame-level precision without re-encoding.
    * **Smart Video Crop Tool:** Manual crop selection or automatic black-bar removal (**auto-crop**).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  AIRzZ90/study-materials-fork
    ⭐ 521 stars  |  🍴 723 forks  |  💻 TypeScript  |  📅 2026-11-12
    🔗 https://github.com/AIRzZ90/study-materials-fork
    📡 来源: 🚀 5天300+星
    📝 A cross-platform Tauri 2 interface and interaction practice project

    README 摘要:
    转载来自：HGhub 源库，请点击小星星
    
    # HGhub
    （FROK不点小星星的人=看黄果也打不出来-哈哈）
    
    **基于 Rust 与 Tauri 2 的跨平台界面与交互实践项目。**
    
    HGhub 起源于个人对 Tauri 2 和移动端开发的学习与尝试。感谢大家的关注与贡献；项目由个人利用业余时间维护，关注度的增长不会改变维护范围，也不代表服务或支持承诺。
    
    ## 维护范围与社区反馈
    
    维护者本人后续仅主动维护 **UI/UX、交互细节与用户体验**，不再主动跟进上游数据获取、解析或播放链路适配，不承诺外部接口及相关功能持续可用。
    
    **任何主题的 PR 与 Issues 均可提交。**维护者会根据时间与精力低频阅读、酌情响应，并逐项决定是否处理或合并。提交不代表一定获得回复或被采纳；接受某次社区贡献，也不代表维护者恢复该方向的主动开发或承担持续适配承诺。
    
    本说明用于交代维护者的工作范围与支持边界，不构成对其他开发者的维护要求，也不代表维护者为第三方贡献、修改版或独立项目提供持续担保。
    
    ## 非商业立场
    
    本项目采用 PolyForm Noncommercial 1.0.0，**禁止任何商业用途**，包括销售、广告变现、卡密、VIP、付费解锁，以及作为收费产品或服务的一部分使用；具体授权范围以许可证全文为准。
    
    维护者**不提供商业授权，不接受任何广告、推广、商务合作或其他合作洽谈**，也未授权任何个人或组织以维护者或本项目名义收费、招揽业务。社区技术贡献与问题反馈不属于商务合作。
    
    ## 项目说明与责任边界
    
    - 本仓库记录个人技术实践，包含界面、播放、网络请求等实现。维护者不运营内容托管服务，不参与外部音视频内容的制作、上传或经营。
    - 项目与外部站点、内容提供者及其权利方不存在官方隶属、代理或背书关系。涉及第三方内容、名称或标识时，相关权利仍归各自权利人；代码公开不代表已取得这些内容的使用或传播授权。
    - 软件按现状提供。在适用法律允许的范围内，维护者不保证其完整性、准确性、安全性、适用性或持续可用性，也不承诺修复、更新或响应期限。
    - 第三方修改、分发、宣传或经营行为不代表维护者的意见或授权；维护者无法控制独立副本及其后续行为。本项目的信息以本仓库的公开记录为准。
    - 以上说明用于澄清项目性质、维护范围与授权边界，不替代适用法律，也不排除依法应承担的责任。软件许可证仅涉及相应代码权利，不构成对第三方内容或服务的授权。
    
    ## 官方通知与权益反馈
    
    维护者尊重各方合法权益，**将积极响应来自上游、GitHub 平台、版权方及其授权代表、有关机构或公众组织的正式通知与合理关切**。此类事项不适用普通功能反馈的低频处理安排。
    
    可通过 GitHub Issues或平台正式渠道联系，说明相关主体、涉及内容、具体诉求及可核实依据。涉及个人信息或非公开材料时，可先提出联系请求，再协商适当的沟通方式。
    
    收到通知后，维护者会尽快核实、沟通并配合处理，视具体情况采取修改或移除相关内容、暂停相关功能、停止维护、归档或调整仓库可见性等措施。处理范围限于维护者能够控制的仓库和渠道，不承诺控制已独立分发的副本。
    
    ## 技术与目录

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  makepad/relax
    ⭐ 514 stars  |  🍴 27 forks  |  💻 Rust  |  📅 2026-11-11
    🔗 https://github.com/makepad/relax
    📡 来源: 🚀 5天300+星
    📝 Relax Rust JIT

    README 摘要:
    # Relax
    
    > [!WARNING]
    > **Experimental.** Relax is for development iteration: running, testing and live-editing your program while you work on it. Build anything you release with Rust itself: `cargo build --release` with rustc. So far it has been tested mostly in Makepad's own edit-run loop and only lightly on other projects, so expect rough edges elsewhere and please report them.
    
    ### Rust without the wait.
    
    **rustc builds your program, then you run it. Relax runs your program while it builds it.**
    
    Relax is a live compiler and JIT runtime for Rust, written in Rust. It runs a Cargo package straight
    from source, with no rustc, LLVM or linker in the loop: it compiles each function when it is first
    called, optimises the hot ones while the program runs, and patches your edits into the running process.
    
    ## Relax vs cargo and rustc
    
    | | cargo + rustc | **Relax** |
    | --- | --- | --- |
    | **Large 3D game, clean checkout → first frame** | ~3 min build, then start | **11 s** on an M4 MacBook, straight from source |
    | **Same game, second run → first frame** | start the built binary | **1.15 s** on an M4 MacBook, nothing recompiled |
    | **Small app → first frame** | build it first | **3.7 s** cold, **0.41 s** warm (M4 MacBook) |
    | **Change one function in a running program** | rebuild, relink, restart: state lost | **patched in**: state kept |
    | **Save a file → 92 tests re-run** | rebuild the test binary first | **2.2 s** after the save |
    | **Type and borrow check** | `cargo check`; a build checks everything first | `relax check`; a run type-checks each function before it runs and borrow-checks in the background |
    | **Speed of optimised code** | 1.00× (`--release`) | **slower: 1.12× the time on x64, 1.24× on arm64** (geomean of 21 workloads) |
    | **Needs** | rustc, LLVM, a linker | **one Rust library**: 438k lines, 0 crates.io dependencies |
    
    Code generation for x86-64 and AArch64; from a fresh clone the repository
    builds and its tests pass on Linux x86-64 and macOS arm64. Windows isn't tested.
    
    ## The tradeoffs
    
    - **Slower optimised code.** Overall the code Relax runs is slower than rustc's `--release`: 1.12× the time on x64
      and 1.24× on arm64 (geomean of 21 workloads), 1.22× and 1.25× against a native-CPU build. It is faster on only
      a few workloads: see where LLVM still wins.
    - **More memory.** The compiler, its caches and every code version it publishes share your program's
      process, and JIT code is append-only. `relax inspect  memory` shows the split, `code` th

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  rivet-dev/open-orange
    ⭐ 471 stars  |  🍴 18 forks  |  💻 TypeScript  |  📅 2026-11-12
    🔗 https://github.com/rivet-dev/open-orange
    📡 来源: 🚀 5天300+星
    🏷️ cloudflare, cloudflare-workers, durable-objects, nodejs, rivet, self-hosted, serverless, sqlite, typescript, wrangler
    📝 Run Cloudflare Workers and Durable Objects unchanged on AWS, GCP, Azure or your own servers.

    README 摘要:
    Run Cloudflare Workers anywhere: AWS, Google Cloud, Azure, or your own servers.
    
    The same developer experience, without the runtime limits, for a fraction of the bill.
    
      Docs ·
      Deploy ·
      Migrate ·
      Bindings ·
      Examples ·
      Discord
    
    ## What is OpenOrange
    
    OpenOrange runs your existing Cloudflare Workers project on AWS, Google Cloud, Azure or your own servers, with no changes to your code. It's built with four goals:
    
    - **Zero refactoring, zero-downtime migration**: your Workers and Durable Objects run as they are, and your data moves off Cloudflare while your app keeps serving.
    - **The same developer experience**: `wrangler dev` becomes `orange dev`, and everything underneath is open source and self-hostable.
    - **Simpler bills**: you pay for the machines you run on, not Cloudflare's metering or an enterprise contract. Compute is 4.8× cheaper and storage 8.7× cheaper.
    - **Built for scale**: storage is backed by S3, so scaling out is a matter of adding machines.
    
    ## Quickstart
    
    You need a Worker project with a `wrangler.jsonc`, `wrangler.json`, or `wrangler.toml` (or use `examples/hello-durable-object`), Node.js 22 or later, and pnpm. Deploying also needs Docker.
    
    ### Use a coding agent
    
    Paste this into your coding agent (Claude Code, Codex, Cursor, …) from your Worker project:
    
    ```text
    First, add the Rivet MCP (https://mcp.rivet.dev/mcp) to this agent, and ask me to approve the Rivet sign-in. Then run this project's Cloudflare Worker on Rivet with OpenOrange: ask me where it should run (on my machine, on a Rivet cluster, or on my own Rivet Engine), read https://github.com/rivet-dev/open-orange/blob/main/README.md and follow its quickstart. Do not change my app code.
    ```
    
    ### Step 1: Install
    
    Install the `orange` CLI globally, then run it in your Worker project. Your code and your Wrangler configuration do not change.
    
    ```sh
    pnpm add -g open-orange
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#14  brave-plum-co/leonardo-ai-desktop
    ⭐ 187 stars  |  🍴 0 forks  |  💻 C++  |  📅 2026-11-14
    🔗 https://github.com/brave-plum-co/leonardo-ai-desktop
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai-art-platform, ai-creative-suite, ai-generation-tools, ai-image-generator, ai-image-tools, generative-ai-art, leonardo-ai-api, leonardo-ai-api-wrapper, leonardo-ai-automation, leonardo-ai-extension
    📝 Leonardo AI 2026 desktop setup with text-to-image generation using fine-tuned models, canvas editor with inpainting and outpainting, plus real-time generation and image-to-motion for Windows 11

    README 摘要:
    # 🎨 Leonardo AI 2026: Standalone Offline Build for Windows 11
    
        
    
    ## 📦 Intro
    
    This repository distributes a standalone offline Windows x64 build intended for the Leonardo AI workflow. The package is a self-contained deployment bundle that ships the runtime, the asset pipeline, and the local render dependencies required for the generative image workflow, packaged for Windows 10 and 11. It is assembled by independent maintainers and published here as a reproducible distribution artifact.
    
    The deployment audience for this build includes air-gapped design workstations, bandwidth-constrained lab environments, and teams that require reproducible installs across many machines without touching a network. Because the bundle is offline, it removes the dependency on live model fetching during first-run initialization, which matters when workstations are provisioned in batches.
    
    This build supports most common image generation formats and bundles the diffusion runtime, the model cache loader, and a portable launcher alongside the standard installed mode. A single `Leonardo AI on Windows` deployment covers both portable and installed configurations, so the same artifact can be used across mixed fleet environments.
    
    ## 01 · ⬇️ Download
    
      
        
          
          
        
      
    
      
    
    ## 02 · ✨ Features
    
    **📦 Offline Bundle**
    
    The package includes the runtime, the model loader, and the local asset cache in a single distributable archive.
    
    **🖥️ x64 Native**
    
    Compiled against the Windows x64 target with native CPU acceleration paths for the raster and diffusion pipelines.
    
    **💼 Portable Mode**
    
    The build can run from a removable volume without writing to system directories when launched in portable mode.
    
    **🔐 SHA256 Manifest**
    
    Each release publishes a hash manifest at the artifact root so installations can be verified before first run.
