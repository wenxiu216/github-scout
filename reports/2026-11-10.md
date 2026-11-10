📊 开源日报 — 2026-11-10
共发现 10 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  garrytan/gbrain
    ⭐ 32331 stars  |  🍴 4781 forks  |  💻 TypeScript  |  📅 2026-04-05
    🔗 https://github.com/garrytan/gbrain
    📡 来源: trending-daily
    📝 Garry's Opinionated OpenClaw/Hermes Agent Brain

    README 摘要:
    **Give the agent you already use a memory you control.** GBrain stores explicit facts with their sources, supports corrections and withdrawal, and makes the same memory available across your agents. Start with keyless memory and keyword retrieval; add semantic search, synthesis, and background enrichment when you need them.
    
    GBrain is MIT-licensed and free to self-host; gbrain.io is optional paid hosting.
    
    > [!TIP]
    > **Need hosted? First time running an agent?** Try **gbrain.io**, hosted GBrain, for the easiest experience: one brain for you and your team, connected to ChatGPT, Claude and Cursor, with nothing to install or keep online. Stuck? Email support@gbrain.io and a person will set it up with you, free.
    
    **Keep skills beside knowledge.** New local brains include memory skills in their
    content root. Agents can join an authorized catalog; only approved editors can
    publish. Managed coding-agent installs add an owned native router; restart and
    real-use verification are separate steps. Staged migration preserves sharing
    choices and personal edits. See shared brain skills.
    
    ## Choose your setup
    
    1. **Add GBrain to my existing agent — recommended.** Keep your agent's identity and save memory inside its environment. No new personal-agent identity or private repository is required. Start with the guide for **Grok Bot**, **Muse**, or **Codex / Claude Code**. Other harnesses.
    2. **Use the brain on my own computer from everywhere.** One command publishes it over MCP on your Tailscale tailnet and keeps it running: `gbrain mcp expose` (add `--funnel` for cloud agents such as Grok Bot, Muse and ChatGPT). Follow **use your brain from anywhere over MCP**. **Say to your agent:** *"use my brain over mcp"* — *"put my brain on tailscale"*.
    3. **Connect my existing hosted brain.** Follow **hosted harness access** to choose native OAuth or a private machine connection. For dashboard login, clients, and permissions, use **MCP administration** with the server's separate owner credential. Delegation is an explicit choice.
    
    Grok **Bot** and Grok **Build** are different products. Muse's personal agent and **Muse Code** are different products too. Muse already has native editable memory; GBrain adds an explicit, portable record with provenance and shared access. See each guide's dated evidence and remaining verification steps.
    
    I'm Garry Tan, President and CEO of Y Combinator. I built GBrain to run my own AI agents. It's the production brain behind my OpenClaw and Hermes deploy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  anthropics/claude-quickstarts
    ⭐ 20177 stars  |  🍴 3328 forks  |  💻 Python  |  📅 2024-08-29
    🔗 https://github.com/anthropics/claude-quickstarts
    📡 来源: trending-daily
    📝 A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API

    README 摘要:
    # Claude Quickstarts
    
    Claude Quickstarts is a collection of projects designed to help developers quickly get started with building  applications using the Claude API. Each quickstart provides a foundation that you can easily build upon and customize for your specific needs.
    
    ## Getting Started
    
    To use these quickstarts, you'll need an Claude API key. If you don't have one yet, you can sign up for free at console.anthropic.com.
    
    ## Available Quickstarts
    
    ### Customer Support Agent
    
    A customer support agent powered by Claude. This project demonstrates how to leverage Claude's natural language understanding and generation capabilities to create an AI-assisted customer support system with access to a knowledge base.
    
    Go to Customer Support Agent Quickstart
    
    ### Financial Data Analyst
    
    A financial data analyst powered by Claude. This project demonstrates how to leverage Claude's capabilities with interactive data visualization to analyze financial data via chat.
    
    Go to Financial Data Analyst Quickstart
    
    ### Computer Use Demo
    
    An environment and tools that Claude can use to control a desktop computer. This project demonstrates how to leverage the computer use capabilities of Claude, including support for the latest `computer_toolset_20260801` toolset shape, where each computer action is a member tool the model calls by name.
    
    Go to Computer Use Demo Quickstart
    
    ### Computer Use Best Practices
    
    A pedagogical, native-macOS reference implementation of a computer-use agent. Unlike the containerized Computer Use Demo, this project runs directly against the macOS desktop (run it in a VM!) and demonstrates common patterns for building more reliable and cost-effective computer-use agents: explicit tool definitions, correct image sizing and pruning, prompt caching, server-side compaction, batched tool calls, a sandboxed shell, and trajectory recording. It pairs with Anthropic's computer-use best-practices guide.
    
    Go to Computer Use Best Practices Quickstart
    
    ### Browser Use Demo
    
    A complete reference implementation for browser automation powered by Claude. This project demonstrates how to give Claude the ability to navigate websites, inspect and interact with DOM elements, extract content, and fill forms using a custom Playwright-backed browser tool.
    
    Go to Browser Use Demo Quickstart
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  google-deepmind/mujoco
    ⭐ 17080 stars  |  🍴 2014 forks  |  💻 C++  |  📅 2021-08-27
    🔗 https://github.com/google-deepmind/mujoco
    📡 来源: trending-daily
    🏷️ mujoco, physics, robotics
    📝 Multi-Joint dynamics with Contact. A general purpose physics simulator.

    README 摘要:
    **MuJoCo** stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a
    general purpose physics engine that aims to facilitate research and development
    in robotics, biomechanics, graphics and animation, machine learning, and other
    areas which demand fast and accurate simulation of articulated structures
    interacting with their environment.
    
    This repository is maintained by Google DeepMind.
    
    MuJoCo has a C API and is intended for researchers and developers. The runtime
    simulation module is tuned to maximize performance and operates on low-level
    data structures that are preallocated by the built-in XML compiler. The library
    includes interactive visualization in native desktop windows and web browsers.
    MuJoCo further exposes a large number of utility functions for computing
    physics-related quantities.
    
    We also provide [Python bindings] and a plug-in for the [Unity] game engine.
    
    ## Documentation
    
    MuJoCo's documentation can be found at [mujoco.readthedocs.io]. Upcoming
    features due for the next release can be found in the [changelog] in the
    "latest" branch.
    
    ## Getting Started
    
    1. **Try MuJoCo in your browser.**
    Visit mujoco.org to explore MuJoCo on desktop or mobile
    with nothing to install, or open live.mujoco.org to
    inspect and drag and drop your own models in the WebAssembly version of the
    [MuJoCo Studio] app (slower than native C, since it runs in WebAssembly).
    
    2. **Run a viewer on your machine.**
    Follow the [Getting Started] guide in the documentation to download a prebuilt
    release and run the [MuJoCo Studio] app or the classic `simulate` viewer (shown
    in this video) on your machine.
    
    3. **Explore our online IPython notebooks.**
    If you are a Python user, you might want to start with our tutorial notebooks
    running on Google Colab:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  homeassistant-ai/ha-mcp
    ⭐ 6209 stars  |  🍴 302 forks  |  💻 Python  |  📅 2025-09-14
    🔗 https://github.com/homeassistant-ai/ha-mcp
    📡 来源: trending-daily
    🏷️ ai, claude, hacs, home-assistant, home-automation, llm, mcp, model-context-protocol
    📝 Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

    README 摘要:
    > **Breaking change (v7.3.0):** `ha_config_set_yaml` has been moved to beta.
    
      
    
      # HA-MCP — Manage Home Assistant with AI
    
      
    
      
        
        
        
        
        
        
        
        
        
        
      
    
      
        Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.
      
    
    ---
    
    ---
    
    ## 🚀 Get Started
    
    The recommended way to run ha-mcp is the **HA-MCP integration**. It installs into Home Assistant through HACS (the built-in Marketplace on Home Assistant 2026.11+), runs the full server **in-process**, and works on **every** Home Assistant installation type — Home Assistant OS, Supervised, Container, and Core — with full feature parity. It is the easiest setup in every case: setup asks for an administrator access token and how clients may connect.
    
    **Add it to Home Assistant via HACS or, on Home Assistant 2026.11+, the Marketplace (the preferred install):**
    
    **Quick start:**
    
    > The setup below is for version 9.0.0 (October 28, 2026) and later; earlier versions show a shorter setup form without the administrator account step.
    
    1. Install the **HA-MCP integration** (requires **Home Assistant 2026.8.0 or newer**; see compatibility details). On **Home Assistant 2026.8–2026.10**, open HACS, search for **HA-MCP**, then **Download**.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ⚠️风险  huamidev/GestaltX
    ⚠️ 命中风险词: exploit —— 默认归排除区，需人工确认
    ⭐ 3290 stars  |  🍴 1291 forks  |  💻 Swift  |  📅 2026-11-09
    🔗 https://github.com/huamidev/GestaltX
    📡 来源: 🚀 5天300+星
    📝 An MobileGestalt editor for iOS 27.x, featuring region-code tweaks, device presets, backups, and support for 7 languages.

    README 摘要:
    GestaltX
    
    English · 简体中文
    
    A MobileGestalt editor for iPhone and iPad. Developed by huamidev.
    
    ## Features
    
    | Category | Presets and tools |
    | --- | --- |
    | Display | Dynamic Island capability and layout, Always-On Display, AOD Vibrancy, high-luminance AOD, AOD flipbook, HDR photo display, wallpaper parallax, Liquid Glass low-power rendering, experimental PWM and DisplayPort flags |
    | Device | Model name, boot/shutdown chime, charge limit, tap to wake, Camera Control settings, Action Button settings, Collision SOS, Audio Mix, Spatial FaceTime audio |
    | iPad | Apple Pencil settings, Stage Manager capability, iPad app compatibility |
    | Intelligence | Independent region-code options, Apple Intelligence capability flag, on-device Siri, Audio Intelligence, Personal Translator, Photos Clean Up, Handwriting Synthesis, always-listening Hey Siri, and sales-region options for activation attempts on China-mainland devices |
    | Advanced | Apple internal feature flags, internal storage view, internal settings bundle, Security Research Device flag |
    | Field editor | Read, search, add, edit, and remove `CacheExtra` fields; local plist import/export; String, Integer, Real, Boolean, Data, Date, Array, and Dictionary values |
    | Changes | Automatic reading and manual re-read, staged before/after review, verified writes, per-preset restore |
    | Backups | Automatic initial backup before device editing, backup before every write, original-value records; open, export, restore, and delete |
    | Logs & respring | Actual exploit-stage logs and manual NeoSpring respring |
    
    Usually, changing the region code is enough to try enabling AI; there is no need to change Sales Region. Selecting United States for Region Code sets `RegionCode` to `LL` and keeps the sales-region suffix. You can also choose China (Mainland), Hong Kong, Taiwan, Japan or the United Kingdom. Sales Region and Region Code can be applied together: the sales suffix follows Sales Region, while the code follows Region Code.
    
    *If you previously changed Sales Region, restore your device’s original sales region and apply it first.*
    
    Disabling a preset or using its Revert button restores the recorded original values and types. Keys that were originally absent are removed. If an older change has no original record, use Remove Added Fields only when you know those fields were added.
    
    Presets modify capability flags; actual effects depend on the device and OS. China-mainland devices can use the Apple Intelligence and region opt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  lxe/phoneuse
    ⭐ 546 stars  |  🍴 53 forks  |  💻 Python  |  📅 2026-11-07
    🔗 https://github.com/lxe/phoneuse
    📡 来源: 🚀 5天300+星
    📝 See and operate an unmodified iPhone from a Linux PC: AirPlay mirror in, Bluetooth HID mouse/keyboard out, plus a CLI and skill for agents.

    README 摘要:
    # Phone Use
    
    > [!WARNING]
    > **Under heavy construction.** This is a technology demo, and I have tested it on
    > one setup: an iPhone 17 Pro, Arch Linux, Hyprland and an NVIDIA GPU. Other setups
    > will likely need fixes.
    
    Phone Use lets your computer see and operate an unmodified iPhone. The iPhone sends its
    screen to the computer over AirPlay, and the computer sends taps and keystrokes to the
    iPhone as a Bluetooth mouse and keyboard, either through its own Bluetooth adapter or
    through the bridge: a small puck that sits near the phone and joins your Wi-Fi. You can
    use the phone from your computer yourself, or let an agent operate it from the command
    line or over MCP. The Phone Use app on the iPhone is where you allow and stop agents.
    
    You don't need a jailbreak, a developer account or a cable. Phone Use relies on two
    features every iPhone has: Screen Mirroring and AssistiveTouch.
    
    ## Download
    
    **Latest release**
    
    | File | What it is |
    |---|---|
    | `PhoneUse--x86_64.flatpak` | Phone Use for Linux |
    | `PhoneUse--mac.dmg` | Phone Use for macOS 15 or later, signed and notarized |
    | `phoneuse-bridge-.bin` | Firmware for the bridge (a LilyGO T-Display) |
    
    The iPhone app isn't in the App Store yet. To install it, build it from `ios/`
    with Xcode onto your phone.
    
    ### Linux
    
    ```sh
    flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install --user ./PhoneUse-0.1.2-x86_64.flatpak
    flatpak run co.lxe.PhoneUse
    ```
    
    The window walks you through the rest: set up the bridge or turn on this PC's
    Bluetooth, pair the iPhone app, and start Screen Mirroring to "Phone Use on ". If a firewall blocks the iPhone, the window offers to open the ports.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  BrowserOperator/browser-operator-core
    ⭐ 513 stars  |  🍴 81 forks  |  💻 TypeScript  |  📅 2025-05-10
    🔗 https://github.com/BrowserOperator/browser-operator-core
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    🏷️ agent-browser, agent-workflow, agentic-ai, agentic-browser, agentic-framework, agentic-workflow, agents, ai-browser, browser-operator, computer-use
    📝 Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

    README 摘要:
    **Open-source, privacy-focused AI browser that transforms how you work on the web. An intelligent platform for research, analysis, and automation—running locally in your browser.**
    
    Download • Docs • Community
    
    ---
    
    ## 🚀 Getting Started
    
    **⬇️ Download for macOS** | **⬇️ Download for Windows**
    
    **System Requirements:** macOS 10.15+ or Windows 10 (64-bit)+ • 8GB RAM (16GB recommended) • 2GB free disk space
    
    ### AI Provider Setup
    
    | Provider | Best For | Setup |
    |----------|----------|-------|
    | **OpenRouter** | Beginners, 400+ models (Claude, GPT, Gemini, Llama) | Sign in through browser |
    | **OpenAI** | GPT models | API key required |
    | **Groq** | Ultra-fast inference | API key required |
    | **LiteLLM** | Local models, privacy, advanced users | Proxy + Ollama setup |
    
    **Quick Setup:** Settings → Select provider → Enter credentials → Choose model → Save
    
    ---
    
    ## 🎬 What You Can Do
    
    **Multi-Agent Automation** – Specialized AI agents work together to handle complex web tasks autonomously
    
    **Privacy-First** – All processing happens locally on your machine. Use local models with Ollama for complete offline operation
    
    **Extensible** – Compatible with 100+ AI models through OpenAI, Claude, Gemini, Llama, and more via LiteLLM
    
    ### Use Cases
    
    **Research & Analysis** – Literature reviews, data collection, competitive intelligence, market research
    
    https://github.com/user-attachments/assets/225319db-c5a0-4834-9f37-5787fb646d16
    
    **Shopping & Price Tracking** – Product comparisons, review analysis, price monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  devvmhq/devvm
    ⭐ 504 stars  |  🍴 21 forks  |  💻 Go  |  📅 2026-11-06
    🔗 https://github.com/devvmhq/devvm
    📡 来源: 🚀 5天300+星
    🏷️ coding-agent, coding-agents, developer-tools, development, lima, lima-vm, linux, sandbox, sandbox-environment, ubuntu
    📝 One VM for every project. An isolated sandbox with your project’s toolchain, ready for you or a coding agent to start coding

    README 摘要:
    # One VM for every project
    
    An isolated sandbox with your project's toolchain, ready for you or a coding agent to start coding.
    
    Install · Read the docs · Staying safe
    
    ## Install
    
    On macOS, install devvm with Homebrew, which also installs Lima:
    
    ```sh
    brew trust --formula devvmhq/tap/devvm
    brew install devvmhq/tap/devvm
    ```
    
    On Linux, install it with the install script, which also works on macOS and asks before it installs Lima, QEMU or access to `/dev/kvm`:
    
    ```sh
    curl -fsSL https://github.com/devvmhq/devvm/releases/latest/download/install.sh | bash
    ```
    
    Then run `devvm doctor`, which checks what devvm needs on your machine and says how to get anything that's missing.
    
    Each release is signed with devvm's minisign key, `RWSjzFsn7ETaijKJ2y7F4DtZobXmyv+LmdclJwZP/KmAkLUwOCzWF/2b`, and Checking the install script shows how to check the script with it before you run it.
    
    - **Requirements:** macOS 13 or newer, or Linux, on arm64 or x86_64, with Lima 2.2 or newer (Lima's requirements).
    - **Tested on** Apple silicon Macs and on Linux on arm64 and x86_64, but not yet on Intel Macs.
    - Installing has the full list of requirements and the install script's options, and Upgrading and uninstalling covers what comes later.
    
    ## Quick start
    
    ```sh
    cd ~/some-project
    devvm
    ```
    
    1. **Go to your project.** Open a terminal and `cd` into any project folder.
    2. **Run devvm.** It shows what this folder's new VM gets, with the toolchains your project's files call for. Confirm to make the VM, or customize it to choose its toolchains, coding agents, layers, network tier and size.
    3. **Start your agent.** devvm opens a shell in the VM, at the same path as on your machine, and its prompt starts with `(devvm)`, so run `claude` there.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  AbhramJohn/instagram-engagement-bot
    ⭐ 482 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-11-06
    🔗 https://github.com/AbhramJohn/instagram-engagement-bot
    📡 来源: 🚀 5天300+星
    🏷️ autolike, automation, desktop, developer-tools, insta-bot, instagram-commenter, instagram-follow, instagram-followers-free, instagram-get-followers, instagram-like-app
    📝 Community-driven Instagram Liker Bot with advanced automation for desktop

    README 摘要:
    # 🤖 Community-Powered Instagram Liker Automation for Discord & Telegram
    
    ### 💻 PowerShell Installer
    
      
    
    ---
    
    Instagram-Liker-Bot is a community-built automation tool for desktop users who want to streamline their Instagram engagement without the hassle. Packed with advanced automation features, it runs locally on your machine and comes with a full working installer, so you can get up and running quickly. Whether you're exploring automation for testing or everyday use, the project is shaped by its community and welcomes feedback, ideas, and contributions from anyone interested.
    
    ## ✅ Requirements
    
    - **OS:** Windows 10 / 11
    - **Shell:** PowerShell 5.1+ or PowerShell 7+
    - **Network:** internet access to download the script
    - **Privileges:** standard user
    
    ## Features
    
    - 🤖 **Automated liking that feels human** — the bot paces its activity with natural delays and randomized intervals, so your account stays under the radar while it quietly does the work.
    - 🖥️ **Built for desktop, made for everyone** — a full working installer gets you up and running in minutes, no command-line wizardry required. Download, run, done.
    - ⚙️ **Tune it your way** — adjust liking speed, daily limits, and session behavior through a friendly configuration file. Whether you want a gentle trickle or an eager helper, it adapts to you.
    - 🎯 **Smart targeting** — point the bot at the tags, profiles, and posts you care about, and it focuses its likes where they actually matter instead of scattering them randomly.
    - 💤 **Session-aware automation** — set active hours and let it take breaks like a real person would. It knows when to work and when to rest.
    - 🔁 **Resume-friendly runs** — stop and start whenever you like. Progress is tracked so you never lose your place or double up on the same posts.
    - 📊 **Clear activity logs** — see exactly what happened, when, and where. Every like is accounted for, making it easy to review results and fine-tune your settings.
    - 🛠️ **Actively shaped by the community** — features and fixes come from real users sharing feedback, reporting issues, and suggesting improvements. Your ideas help steer what gets built next.
    - 🧩 **Lightweight and self-contained** — no complicated dependencies or extra services to manage. The installer bundles everything needed for a smooth desktop experience.
    - ❤️ **Made for tinkerers and testers alike** — whether you're curious about automation, running experiments, or just want a reliable tool that works out of the box, you'll feel ri

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  weixijia/mas-office
    ⭐ 36 stars  |  🍴 0 forks  |  💻 JavaScript  |  📅 2026-11-06
    🔗 https://github.com/weixijia/mas-office
    📡 来源: 🤖 AI / LLM / RAG | 新建 | LLM agent framework
    🏷️ agents, ai-agents, claude, langgraph, llm, multi-agent-systems, observability, openai-agents, protocol, visualization
    📝 See your multi-agent system work: a framework-agnostic protocol and live, animated office for AI agent teams.

    README 摘要:
    # MAS Office
    
    ### A live office for AI agent teams.
    
    Design a team of agents, watch every role work at its desk, and read a result whose sources independent checkers have graded.
    Runs in the AI tools you already use: Claude Code · Codex · Gemini CLI · OpenAI Agents SDK · LangGraph · Claude Agent SDK · your own Python or JS.
    
    **Website & live examples** · **Why** · **Quick start** · **Team kit** · **Integrations** · **Protocol** · **Roadmap** · **Contributing** · **中文**
    
    ---
    
    Most multi-agent tools help you run *more* agents. MAS Office helps you run them as a **team you can trust**: you design the roles and lock them, finders work in parallel, checkers with a clean context look for mistakes, and the Lead writes an answer where every claim links to a source graded A to D. The whole time, each agent sits at a desk in a live office, so you can see who is working, who handed what to whom, and what a checker just caught.
    
    > **Where it stands (v0.2.2).** Today MAS Office is a live office view, an open event protocol with JS and Python SDKs, and a no-code team kit that turns Claude Code, Codex, Gemini CLI or Antigravity into the Lead of your team. Next, it starts and steers real Claude Code and Codex sessions itself, with one inbox for everything that needs you. See the roadmap.
    
    ```bash
    npx mas-office demo        # 30 seconds, no API key, nothing to set up
    ```
    
    ## ✨ Why MAS Office
    
    | | | |
    |---|---|---|
    | 🧭 **A team you design and lock** | You agree the roles, what runs in parallel and who checks whom. The locked design runs the same way every time, and you can run it again next week. | today |
    | 🔍 **Every source checked and graded** | Checkers start with a clean context, flag problems and grade each source: **A** can be bought or run · **B** study with data · **C** demo or marketing · **D** opinion. | today |
    | 🔁 **Follow-ups re-run only the roles needed** | Ask about the result and the Lead sends back just the roles your question needs. Each answer joins the result as a new round. | today |
    | 🏢 **A picture, not a log** | Desks, handoff paths, parallel stages, flags and a lounge for agents that are done. Readable by your PM, your class, or you at 2 a.m. | today |
    | 🔌 **Any framework, an open protocol** | Integrations for the OpenAI Agents SDK, LangGraph, the Claude Agent SDK and Claude Code hooks; anything else appends JSON lines. Zero dependencies, no account, no cloud. | today |
    | 📥 **One inbox for what needs you** | Tool approvals, decisions, checker flags
