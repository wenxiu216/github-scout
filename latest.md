📊 开源日报 — 2026-11-13
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ggml-org/llama.cpp
    ⭐ 134730 stars  |  🍴 25528 forks  |  💻 C++  |  📅 2023-03-10
    🔗 https://github.com/ggml-org/llama.cpp
    📡 来源: trending-daily
    🏷️ ggml
    📝 LLM inference in C/C++

    README 摘要:
    # llama.cpp
    
    LLM inference in C/C++
    
    ggml / ops / maintainer PRs%20sort%3Aupdated-desc) / dev stats / lib llama API / llama-server REST API
    
    ## Quick start
    
    A few options to get `llama.cpp` installed on your machine:
    
    ```bash
    # curl
    curl -LsSf https://llama.app/install.sh | sh
    
    # powershell
    irm https://llama.app/install.ps1 | iex
    ```
    
    - Visit https://llama.app and follow the instructions
    - Run with Docker - see our Docker documentation
    - Download pre-built binaries from the releases page
    - Build from source by cloning this repository - check out our build guide
    
    Once installed:
    
    ```sh
    # Download and run a model directly from Hugging Face
    llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF
    
    # Launch OpenAI-compatible API server
    llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF
    ```
    
        
            
                
                VLM session with llama cli
            
            
                

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  QwenLM/qwen-code
    ⭐ 29994 stars  |  🍴 3410 forks  |  💻 TypeScript  |  📅 2025-06-26
    🔗 https://github.com/QwenLM/qwen-code
    📡 来源: trending-daily
    🏷️ agentic, ai, ai-agent, ai-coding, cli, coding-agent, developer-tools, llm, mcp, qwen
    📝 An open-source AI coding agent that lives in your terminal.

    README 摘要:
    **The open-source AI coding agent for your terminal, editor, desktop, browser, and chat.**
    
    中文 |
    Deutsch |
    français |
    日本語 |
    Русский |
    Português (Brasil) |
    한국어
    
    | **Qwen Code 1.0 Preview**                                                                                                                                                                                                                                                                                                                                                              |
    | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Qwen Code 1.0 Preview brings together the agent harness capabilities of Qoder and Qwen Code in an open-source release.Try Qwen Code 1.0 Preview · Documentation · 中文文档. |
    
    ## Why Qwen Code?
    
    - **Agentic out of the box** — Auto-Memory, Auto-Skills, SubAgents, Agent Teams, and MCP. Dynamic workflows, zero setup.
    - **Open-source, inside and out** — The framework and the Qwen models are open-source. They evolve together. No vendor lock-in.
    - **Multi-protocol** — Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollama / vLLM). Switch at runtime.
    - **Beyond the terminal** — IDE plugins, Desktop app, Web UI, SDKs, and chat integrations (Telegram / DingTalk / WeChat / Feishu).
    
    > [!TIP]
    > Qwen Code is actively iterating on itself — using its own agent and models to file issues, submit PRs, review code, and run tests. Powered by the community, driven by AI.
    
    ## Installation
    
    Looking for **Qwen Code 1.0 Preview**? Get started here. The instructions below are for the main version.
    
    **Linux / macOS:**
    
    ```bash
    curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash
    ```
    
    **Windows:**
    
    ```powershell
    irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  ashhart/TensorFold
    ⭐ 2022 stars  |  🍴 397 forks  |  💻 Zig  |  📅 2026-06-19
    🔗 https://github.com/ashhart/TensorFold
    📡 来源: trending-daily
    🏷️ ai, ai-tools, llm, llm-inference, llm-tools
    📝 LLM Inference Engine for Metal, CUDA and Vulkan.

    README 摘要:
    # TensorFold
    
    TensorFold serves language models from a Zig binary on Apple Silicon and NVIDIA GPUs.
    The engine reads checkpoints, tokenizes requests and runs Metal or CUDA kernels directly.
    Serving needs no Python or MLX installation.
    
    Building with a coding agent? Have it load the contributor skill before it writes any code.
    
    ## Contributing with agents
    
    Please use Agent Traffic Control before editing TensorFold so contributors and agents can avoid duplicate work and conflicting changes.
    Check the live agent radar before choosing an issue and follow CONTRIBUTING.md and the ATC contributor instructions.
    
    Install or upgrade ATC to 0.9.4 or later, then run from an updated TensorFold clone:
    
    ```sh
    npm install -g github:ashhart/ATC
    atc check ISSUE --json
    atc claim ISSUE --json
    ```
    
    Replace `ISSUE` with the issue number and claim only after a complete check says the work is free.
    TensorFold enables automatic public check-ins: a successful new claim starts an anonymous session on the radar and returns its `session` number.
    Keep that number instead of starting a duplicate session.
    For work already yours, start a session with `atc start ISSUE --json`.
    Add `--github-name` to `claim` or `start` only if you want your verified GitHub name shown; `--local` keeps a new session on your machine.
    The board shows the issue, activity state and last check-in; GitHub still associates the verification comment with its author.
    Check that `publication` is `public`; `unavailable` means the public update failed even if the local claim or session succeeded.
    
    Pulse only while the agent is working, before its five-minute check-in expires:
    
    ```sh
    atc pulse ISSUE SESSION working --json
    atc who path/to/file --json
    atc overlap --json
    atc land ISSUE SESSION --json
    atc release ISSUE --json
    ```
    
    Use `reviewing` or `blocked` when appropriate, land the session when it stops, and resolve overlaps before opening a pull request.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  pookjw/HermesEnabler
    ⭐ 1653 stars  |  🍴 146 forks  |  💻 Objective-C  |  📅 2024-12-14
    🔗 https://github.com/pookjw/HermesEnabler
    📡 来源: trending-daily
    📝 Enable Hermès Watch Faces on any Apple Watch devices

    README 摘要:
    # HermesEnabler 2
    
    English · Tiếng Việt · 한국어 · 简体中文 · 繁體中文 · 日本語 · Español · Français · Deutsch · Português
    
    > Supported only on watchOS 27.0 through 27.3 beta 1.
    
    ## Installation
    
    ### macOS
    
    On macOS you can install the prebuilt IPA with Sideloadly or build the app directly with Xcode. Either way, the iPhone must be paired with the target Apple Watch, and the Watch must run a supported watchOS version.
    
    #### Install the IPA
    
    > **Known issue with Sideloadly 0.72:** Issue #43 reports that this version may remove the embedded Watch app while signing. If the iPhone app installs but HermesEnabler2 is missing from the Watch, use Xcode instead. This report is specific to version 0.72; compatibility with other versions has not been confirmed.
    
    1. Download the IPA from Releases.
    2. Install Sideloadly on your Mac, connect your iPhone with a cable, and select it in Sideloadly.
    3. Drag the IPA into Sideloadly and enter your Apple ID. Turn off **Use automatic bundle ID**, set a fixed Bundle Identifier, and start signing.
    4. On the iPhone, open **Settings → General → VPN & Device Management** and trust your developer certificate.
    5. On the iPhone, open **Settings → Privacy & Security → Developer Mode**, turn it on, restart, and confirm.
    6. On the iPhone, open the **Watch** app, go to **My Watch → Apps**, and install **HermesEnabler2** on the Watch.
    7. On the Apple Watch, open **Settings → Privacy & Security → Developer Mode**, turn it on, restart, and confirm. If the option is not shown, install the Watch app first and check again.
    8. Open **HermesEnabler2** on your Apple Watch and follow the steps in the app.
    
    #### Build with Xcode
    
    1. Open HermesEnabler2.xcodeproj in Xcode.
    2. Select your Apple Watch as the run destination and click **Run**.
    3. Open **HermesEnabler2** on your Apple Watch and follow the steps in the app.
    
    ### Windows
    
    Windows uses WatchBridge, a community tool that prepares Developer Mode and installs an IPA containing both an iPhone host app and a Watch app. It is not affiliated with Apple or with this project.
    
    1. Install **Apple Mobile Device Service** by installing iTunes or the **Apple Devices** app from the Microsoft Store. WatchBridge needs it for USB and Wi-Fi communication. WebView2 is built into Windows 11.
    2. Make sure your iPhone is paired with the target Apple Watch. WatchBridge supports only one paired Watch at a time; if more than one is paired, the preparation step stops instead of guessing.
    3. Download `watchbridge-windows.zip` from

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  apex-compute/ANR
    ⭐ 1107 stars  |  🍴 13 forks  |  💻 C++  |  📅 2026-11-11
    🔗 https://github.com/apex-compute/ANR
    📡 来源: 🚀 5天300+星
    📝 Apex Neural Rendering (ANR) by Apex Compute

    README 摘要:
    # Apex Neural Rendering (ANR)
    
    Apex Neural Rendering by Apex Compute.
    
    - **ANR FG**: frame generation. In beta.
    - **ANR SR**: super resolution (upscaling). Beta soon.
    - **ANR RR**: ray reconstruction (denoising for ray tracing). Beta soon.
    - **Source code**: coming soon.
    - **nr-record**: records a game's frame generation or upscaler inputs to compare ANR FG, NVIDIA DLSS-G, DLSS, FSR, XeSS and others (below). Source in this repository.
    
    ## ANR FG Beta
    
    1. Download a package from Releases:
       - `anr-fg-full`: for games without OptiScaler.
       - `anr-fg-addon`: for games that already use OptiScaler.
    2. Close the game, extract the package and run the installer with the folder of the game's `.exe`:
       - Windows: `install.cmd`
       - Linux and Steam Deck (Proton): `sh install.sh ""`, then set the game's launch options to the line it
         prints: `WINEDLLOVERRIDES="dxgi=n,b" %command%`, or `winmm=n,b` in Vulkan games
    3. In the game, turn on frame generation (the NVIDIA option where the game offers several).
    
    To uninstall, run `uninstall.cmd` or `sh uninstall.sh` with the same folder.
    
    ## Supported GPUs
    
    - NVIDIA GeForce RTX 20, 30, 40 and 50 series, and GTX 16 series
    - AMD Radeon RX 5000, 6000, 7000 and 9000 series, and Steam Deck
    - Intel Arc A and B series
    
    On Windows 10 and 11, and on Linux and SteamOS with Proton.
    
    ## Results and problems
    
    Please post them as issues:
    - **Performance results**: run the test kit from the release and attach its result file.
    - **Problems**: the game, GPU and driver, operating system, settings and what you saw, with the newest `nr_fg-*.log`
      from under the game's `OptiScaler/custom/Apex Neural Rendering FG` folder.
    
    OptiScaler is GPL-3.0; its source for each release is attached to the release.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  serveroshq/panel
    ⭐ 657 stars  |  🍴 54 forks  |  💻 PHP  |  📅 2026-11-09
    🔗 https://github.com/serveroshq/panel
    📡 来源: 🚀 5天300+星
    🏷️ agpl, control-panel, devops, laravel, open-source, self-hosted, server-management, serveros, vps
    📝 The open source ServerOS panel: one place to run the Linux servers you already own.

    README 摘要:
    ServerOS panel
    
    One place to run the Linux servers you already own.
    
      
      
      
      
      
    
      
    
    ServerOS runs the Linux servers you already own from one place. Connect a VPS from any provider with one command, then deploy apps, sites and databases, watch them, back them up and fix them, without living in a terminal. Your servers stay with your provider, on your account.
    
    This repo is the panel, the web app you and your team work in. Each server runs serverosd, a small daemon the panel talks to. serveros.com runs this same panel as a hosted service.
    
    ## What's in it
    
    - **Machines**: connect a server with one command, see CPU, memory and disk, and install updates.
    - **Services and projects**: deploy from Git or a template, with domains and HTTPS, and copy a project to a test environment before it goes live.
    - **Backups, monitors and logs**: scheduled backups, uptime checks with alerts, status pages, and every service's logs in one place.
    - **Workflows**: run steps on a schedule, on a push or by hand, like deploy, check and promote.
    - **Teams**: members, roles, two-factor sign-in and an activity log.
    - **AI and the API**: an MCP server and an API, so your own tools and assistants can work with your servers.
    
    ## Self-hosting
    
    You need a Linux server with Docker, ports 80, 443 and 8443 open, and a domain like `panel.example.com` with two A records pointing at the server: one for `panel.example.com` and one for `*.panel.example.com`.
    
    Then run this on the server:
    
    ```sh
    curl -fsSL https://raw.githubusercontent.com/serveroshq/panel/main/docker/self-hosted/install.sh | sudo bash -s -- --domain=panel.example.com --email=you@example.com
    ```
    
    It installs Docker if it's missing, runs the official image (`ghcr.io/serveroshq/panel`) and prints a setup code. Open `https://panel.example.com`, enter it, and the installer walks you through email and your first account. `serveros-panel setup-code` shows the code again if you lose it.
    
    Then connect your servers from Machines › Connect machine. Each one runs serverosd, the open source daemon, which connects out to your panel on port 8443.
    
    docs/self-hosting.md covers the rest: building the community edition yourself, installing without Docker, upgrades, backups, connecting machines, and the anonymous daily ping (and how to turn it off).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  alexeyw/lot-map
    ⭐ 646 stars  |  🍴 73 forks  |  💻 TypeScript  |  📅 2026-11-09
    🔗 https://github.com/alexeyw/lot-map
    📡 来源: 🚀 5天300+星
    🏷️ agent-observability, ai-agents, claude, claude-code, claude-code-plugin, developer-tools, svg-animation, typescript, visualization
    📝 A live map beside the chat that shows what Claude Code is doing: tool calls, model steps, hooks, skills and subagents light up as they happen. Local only, in 7 languages.

    README 摘要:
    # lot-map
    
    A mod for Claude Code: a live map of the work, in a pane beside the chat. Every tool call, model step, hook and skill sends a pulse from the centre to its station, so you see memory, files, shell, web and agents at work instead of reading a list of commands.
    
    *A made-up session replayed through the mod's own drawing code. Video (MP4).*
    
    ## Install
    
    At the prompt of a terminal session:
    
    ```
    /plugin install lot-map --marketplace alexeyw/lot-map
    ```
    
    Answer `y` to add the marketplace, then choose a scope. From a shell:
    
    ```bash
    claude plugin install lot-map --marketplace alexeyw/lot-map
    ```
    
    If it answers that the plugin is not found in any marketplace, add the marketplace first:
    
    ```bash
    claude plugin marketplace add alexeyw/lot-map
    claude plugin install lot-map@lot-map
    ```
    
    In the desktop app: click **+** next to the prompt box, then **Plugins**, **Add marketplace** with `alexeyw/lot-map`, then **Add plugin**.
    
    The pane opens by itself when a session starts. In a terminal it needs at least 144 columns, otherwise type `/lot-map`, and it draws text only unless you ask for the map's picture: see In a terminal. Built and tested on Claude Code 2.1.321 on macOS; users report it working on Windows as well.
    
    ## Updating
    
    From a shell:
    
    ```bash
    claude plugin marketplace update lot-map
    claude plugin update lot-map@lot-map
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  tanzeeldevAi/ai-meeting-assistant-copilot
    ⭐ 38 stars  |  🍴 20 forks  |  💻 JavaScript  |  📅 2026-11-10
    🔗 https://github.com/tanzeeldevAi/ai-meeting-assistant-copilot
    📡 来源: 🤖 AI / LLM / RAG | 新建 | open source ChatGPT alte
    🏷️ ai-copilot, ai-meeting-assistant, ai-note-taker, chatgpt, claude, cluely, cluely-alternative, codex-cli, electron, google-meet
    📝 Open-source AI meeting assistant and meeting copilot for Zoom, Google Meet and Teams. An overlay hidden from screen share writes what to say back in real time. Runs on your Claude or ChatGPT subscription. Free Cluely alternative for Windows and Mac.

    README 摘要:
    # AI Meeting Assistant Copilot
    
    **An open-source AI meeting assistant for Zoom, Google Meet and Teams. It listens to the call and writes what to say back on a private overlay that screen sharing does not show. Runs on the Claude or ChatGPT subscription you already have.**
    
    ---
    
    ## What is this?
    
    A client asks you something on a call. You know the answer, but turning it into clear
    words while they wait is the hard part, especially in a second language.
    
    **Meeting Copilot listens to the call and shows you what to say back**, a few seconds
    after they finish speaking. You read it, say it in your own voice, and keep the
    conversation moving. It is a free, open-source alternative to paid AI meeting copilots
    such as Cluely, built for client calls, sales calls and consultations.
    
      
        1. Prepare
        2. Listen
        3. Answer
      
      
        Write a short brief: who you are meeting, your goal, your prices and the lines you want to use.
        Press Start listening. It hears the other person through your computer's sound.
        When they ask something, the words to say back appear on your private overlay.
      
    
    ### At a glance
    
      CostFree and open source (MIT)
      AIYour Claude or ChatGPT subscription. No API key needed
      Call appsZoom, Google Meet, Microsoft Teams, Webex, any app that plays sound
      ComputersWindows 10 and 11, macOS 13 or newer
      SpeedAbout 2 to 5 seconds from their last word to the answer on screen, with Claude
      Your dataBriefs, transcripts and notes stay on your computer
    
    ---
    
    ## Features
    
