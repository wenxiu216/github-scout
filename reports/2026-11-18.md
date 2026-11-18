📊 开源日报 — 2026-11-18
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ⚠️风险  huami-dev/GestaltX
    ⚠️ 命中风险词: exploit —— 默认归排除区，需人工确认
    ⭐ 8210 stars  |  🍴 2705 forks  |  💻 Swift  |  📅 2026-11-09
    🔗 https://github.com/huami-dev/GestaltX
    📡 来源: 🚀 两周800+星
    📝 An MobileGestalt editor for iOS 27.x, featuring region-code tweaks, device presets, backups.

    README 摘要:
    GestaltX
    
    English · 简体中文 · 日本語 · 한국어 · Türkçe
    
    A MobileGestalt editor for iPhone and iPad. Developed by huamidev.
    
    ## Features
    
    | Category | Presets and tools |
    | --- | --- |
    | Display | Dynamic Island capability and layout, Always-On Display, AOD Vibrancy, high-luminance AOD, AOD flipbook, HDR photo display, wallpaper parallax, Liquid Glass low-power rendering, experimental PWM and DisplayPort flags |
    | Device | Model name, boot/shutdown chime, charge limit, tap to wake, Camera Control settings, Action Button settings, Collision SOS, Audio Mix, Spatial FaceTime audio |
    | iPad | Apple Pencil settings, Stage Manager capability, iPad app compatibility |
    | Intelligence | Independent region-code options, Apple Intelligence capability flag, on-device Siri, Audio Intelligence, Personal Translator, Photos Clean Up, Handwriting Synthesis, always-listening Hey Siri, and sales-region options for activation attempts on China-mainland devices |
    | Advanced | Apple internal feature flags, the system-wide InternalBuild flag with explicit enable confirmation, internal settings bundle, Security Research Device flag |
    | Field editor | Read, search, add, edit, and remove `CacheExtra` fields; local plist import/export; String, Integer, Real, Boolean, Data, Date, Array, and Dictionary values |
    | Changes | Automatic reading and manual re-read, staged before/after review, verified writes, per-preset restore |
    | Backups | Automatic initial backup before device editing, backup before every write, original-value records; open, export, restore, and delete |
    | Logs & respring | Actual exploit-stage logs and manual NeoSpring respring |
    
    Usually, changing the region code is enough to try enabling AI; there is no need to change Sales Region. Selecting United States for Region Code sets `RegionCode` to `LL` and keeps the sales-region suffix. You can also choose China (Mainland), Hong Kong, Taiwan, Japan or the United Kingdom. Sales Region and Region Code can be applied together: the sales suffix follows Sales Region, while the code follows Region Code.
    
    *If you previously changed Sales Region, restore your device’s original sales region and apply it first.*
    
    Disabling a preset or using its Revert button restores the recorded original values and types. Keys that were originally absent are removed. If an older change has no original record, use Remove Added Fields only when you know those fields were added.
    
    Presets modify capability flags; actual effects depend on the device and OS.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  truefoundry/cognita
    ⭐ 4407 stars  |  🍴 396 forks  |  💻 Python  |  📅 2023-07-26
    🔗 https://github.com/truefoundry/cognita
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | RAG retrieval augmented 
    🏷️ agent, ai, application, data, deep-learning, fine-tuning, framework, generative-ai, llm, llm-ops
    📝 RAG (Retrieval Augmented Generation) Framework for building modular, open source applications for production by TrueFoundry 

    README 摘要:
    > [!Note]
    > This project is no longer actively maintained. We thank all contributors for their contributions.
    
    # Cognita
    
    ## Why use Cognita?
    
    Langchain/LlamaIndex provide easy to use abstractions that can be used for quick experimentation and prototyping on jupyter notebooks. But, when things move to production, there are constraints like the components should be modular, easily scalable and extendable. This is where Cognita comes in action.
    Cognita uses Langchain/Llamaindex under the hood and provides an organisation to your codebase, where each of the RAG component is modular, API driven and easily extendible. Cognita can be used easily in a local setup, at the same time, offers you a production ready environment along with no-code UI support. Cognita also supports incremental indexing by default.
    
    You can try out Cognita at: https://cognita.truefoundry.com
    
    # 🎉 What's new in Cognita
    
    - [September, 2024] Cognita now has AudioParser (https://github.com/fedirz/faster-whisper-server) and VideoParser (AudioParser + MultimodalParser).
    - [August, 2024] Cognita has now moved to using pydantic v2.
    - [July, 2024] Introducing `model gateway` a single file to manage all the models and their configurations.
    - [June, 2024] Cognita now supports it's own Metadatastore, powered by Prisma and Postgress. You can now use Cognita via UI completely without the need of `local.metadata.yaml` file. You can create collections, data sources, and index them via UI. This makes it easier to use Cognita without any code changes.
    - [June, 2024] Added one click local deployment of cognita. You can now run the entire cognita system using docker-compose. This makes it easier to test and develop locally.
    - [May, 2024] Added support for Embedding and Reranking using Infninty Server. You can now use hosted services for variatey embeddings and reranking services available on huggingface. This reduces the burden on the main cognita system and makes it more scalable.
    - [May, 2024] Cleaned up requirements for optional package installations for vector dbs, parsers, embedders, and rerankers.
    - [May, 2024] Conditional docker builds with arguments for optional package installations
    - [April, 2024] Support for multi-modal vision parser using GPT-4
    
    # Contents
    
    - Cognita
      - Why use Cognita?
    - 🎉 What's new in Cognita
    - Contents
      - Introduction
        - Advantages of using Cognita are:
        - Features:
    - :rocket: Quickstart: Running Cognita Locally
      - :whale: Using Docker compose (recommended)
      - Cogn

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  ersinkoc/phonebox
    ⭐ 2846 stars  |  🍴 400 forks  |  💻 C#  |  📅 2026-11-07
    🔗 https://github.com/ersinkoc/phonebox
    📡 来源: 🚀 两周800+星
    🏷️ android, claude-code, codex, dashboard, desk-panel, dotnet, linux, macos, old-phone, smart-stack
    📝 Turn an old Android phone into a customizable desk panel and touch control deck for Windows, Linux and macOS. 115 widgets for system stats, AI coding, media and automation. USB or paired Wi-Fi. No cloud required.

    README 摘要:
    PhoneBox
    
      English ·
      Türkçe ·
      Deutsch ·
      Français ·
      Español ·
      Italiano ·
      Português ·
      Nederlands ·
      Polski ·
      Русский ·
      Tiếng Việt ·
      中文 (简体)
    
    Turn an old Android phone into a desk panel for your computer.
    PC stats, AI coding sessions, music and touch controls over USB or Wi-Fi.
    Windows, Linux and macOS. No root, PhoneBox account or cloud service required.
    
      Try the live demo ·
      Download ·
      Quick start
    
      
      
      
      
      
    
    Example layouts with demo data.
    
    PhoneBox pairs a full-screen **Android app** with a small **desktop agent**. Build your panel in a browser-based
    visual editor: **123 widgets**, **30 templates**, multiple pages and a live preview. Connect several phones with
    their own layouts, or switch one phone between paired computers.
    
    ## What you can do
    
    | Use it for | What appears on the phone |
    |---|---|
    | **PC monitoring** | CPU, GPU, RAM, disks, network and ping; charts, GPU details and process controls |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  gylive/google-ultra
    ⭐ 2263 stars  |  🍴 831 forks  |  💻 Python  |  📅 2026-11-17
    🔗 https://github.com/gylive/google-ultra
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # google-ultra
    
    简体中文 | English
    
    Google One 的 AI Ultra 有个 12 个月免费试用的 offer，任何页面上都看不到，只存在于 Play 结算库（BillingClient）的返回值里。这个脚本把「查 offer → 拉起 Play 收银台 → 确认 0 元 → 开通」串成了一条命令。
    
    原理是借 Google One 自己的进程调 BillingClient，不需要 Xposed，不需要改 APK。
    
    ## 两个版本
    
    **简单版**：一个网页，双击 `web/index.html` 打开，登录 → 绑卡 → 点一下，完事。不用装 Python，不用 root，不用数据线。
    
    **脚本版**：`ultra0.py`，要一台 root 手机和 frida。优点是 offer 从真实客户端取，不依赖浏览器指纹。
    
    先试简单版，不行再上脚本。
    
    ## 能拿到什么
    
    拿到的是 **Ultra 5x，20TB，12 个月 $0**，到期前取消就不用付钱。开通后 Play 订阅页会写「即将扣款 2027-11-17 US$99.99/月」，这是试用结束后的价格，不是现在扣。
    
    30TB 那档（20x）也查得到 offer，但 Play 结算时会二次校验，大部分号会弹「您不符合免费试用条件」。这个脚本不会去点它。
    
    ## 需要什么
    
    一台 root 过的安卓手机，USB 连着电脑。Magisk、KernelSU、APatch 都行，模拟器也行。
    
    电脑上要 Python 3.9 以上，外加两个包：
    
    ```bash
    pip3 install frida
    ```
    
    adb 用 Android SDK 里的 platform-tools。装好后 `adb devices` 能看到手机就行。没装过的话，Mac 上 `brew install android-platform-tools`，Windows 去下 platform-tools 压缩包，解压后把目录加进 PATH。
    
    手机上要开「开发者选项 → USB 调试」，插上后在弹窗里点允许。
    
    ## 用法
    
    ### 简单版怎么用
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  erkamyaman/rust-anything
    ⭐ 2000 stars  |  🍴 144 forks  |  💻 Rust  |  📅 2026-11-16
    🔗 https://github.com/erkamyaman/rust-anything
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, claude-code, cli, code-migration, codex, ffi, golang, java, javascript, mcp
    📝 Rewrite your whole app in Rust, one piece at a time, checked against the original's recorded behavior at every step. CLIs, HTTP servers and libraries in TypeScript, Python, C, Go, Ruby and Java.

    README 摘要:
    rust-anything
    
    by erKam Yaman
    
    English · Türkçe · 简体中文 · 繁體中文 · Deutsch · Français · Русский · Українська · 日本語 · 한국어 · Azərbaycanca · Oʻzbekcha · Қазақша · Кыргызча · Türkmençe · Татарча · ئۇيغۇرچە
    
    Rewrite your whole app in Rust. Keep it working the whole way.
    
    CLIs, servers and libraries, piece by piece, checked against the original at every step.
    
    Node.js and TypeScript · Python · C · Go · Ruby · Java · PHP and C# in preview
    
      
      
      
      
      
      
      
    
    up to 20x faster · 38,251 recorded cases replayed · 0 mismatches · one command
    
      
    
    **Rewrite your whole app in Rust, one piece at a time.** rust-anything records what your
    Node.js (TypeScript/JavaScript), Python, C, Go, Ruby or Java app does today, then checks every piece of the
    Rust rewrite against that recording before it moves on, until the app is pure Rust. CLIs, HTTP
    servers and libraries; your coding agent (or you) writes the Rust. It can only catch what the
    recording covers: see What it can't catch. Only need the slow part fast?
    Port just that, one hot path at a time:
    
    | Real workload, same results as the original | Original | With rust-anything |
    | --- | ---: | ---: |
    | x18n's sidebar search, 50,000 keys (TypeScript, Node) | 10 ms per query | **0.5 ms: 20x faster** |
    | The same search in the browser (wasm, one thread) | 10 ms | **0.95 ms: 11.5x** |
    | `slugify` over 20,000 strings (Python) | 98 ms | **17x faster** |
    | `Shellwords.shellescape` from Ruby's standard library, 50,000 values | 88 ms | **11.8x faster** |
    | `Slugify` over 50,000 strings (Go) | 49 ms | **4x faster** |
    | `slugify` over 50,000 strings (Java) | 43 ms | **3x faster** |
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  sybil-solutions/inference-optimisation-skill
    ⭐ 989 stars  |  🍴 85 forks  |  💻 Python  |  📅 2026-11-16
    🔗 https://github.com/sybil-solutions/inference-optimisation-skill
    📡 来源: 🚀 5天300+星
    🏷️ agent-skill, benchmarking, claude-code, inference, llm, speculative-decoding
    📝 Agent skill for hill-climbing local LLM serving speed (decode, speculative decoding, prefill, KV, startup, TTFT) on any hardware and quantization

    README 摘要:
    # inference-optimisation
    
    An agent skill for **hill-climbing the speed of a local LLM server** on any hardware and any quantization. It covers:
    
    - single-user and concurrent decode
    - speculative decoding
    - prefill
    - KV cache size
    - startup time and time to first token
    
    It works under a memory cap, and every result has to survive a full-context stability check.
    
    It encodes how we actually got these speedups. It is not a list of flags. The workflow:
    
    1. Compute the theoretical ceiling.
    2. Change one thing at a time.
    3. Measure against interleaved controls.
    4. Log every result, including the failures.
    5. Gate on long-context retrieval.
    6. Qualify a clean, pinned build before publishing.
    
    It works with Claude Code and any agent that loads `SKILL.md`-style skills. Any model can also follow it from `PROMPT.md`.
    
    ## What we've been able to accomplish
    
    Results from the hill-climbs this skill was distilled from. Every number was measured on the hardware named; see the linked sources for methods and raw data.
    
    | Hardware | Model / quant / engine | Before → after |
    |---|---|---|
    | **Intel Arc B390 iGPU** (laptop, 64 GB unified LPDDR5X, ~115 GB/s) | Ornith-1.5-35B-A3B, EXL3 4 bpw, SGLang XPU + MTP | Decode, 1 user: 43.6 → **53 tok/s** (median)Decode, 4 users: 84.7 → **103 tok/s**Prefill 32K: 1,037 → **1,660 tok/s**Prefill 256K: 297 → **628 tok/s** (2.1×)KV cache: 264K tokens → **4 × 256K**Startup: 113 → **43 s**Registry Lab gates: decode 28.6 → **41.0**, prefill 255 → **667** |
    | **Intel Arc Pro B70** | Qwen3.8-27B, EXL3 4 bpw, vLLM + custom XPU kernels | Decode: **91.2 tok/s** at 1 user, **365** at 16 (prose, thinking on)Same card with llama.cpp Q4_K_M: 25.0Prefill 4K/32K/128K/254K: 1,654/1,434/928/650 → **2,421/2,259/1,415/911**Agent-session replay: 193 → **147 s** |
    | **Intel Arc Pro B70** | Same model, SGLang + the same kernels | Decode, 1 user: **82.6 tok/s**, vs vLLM 75.7 on the same card and day |
    | **RTX 3090** | Qwen3.8-27B EXL3 3 bpw + MTP | **96.2 tok/s** prose / **141.1** code, 1 user |
    | **RTX 3090** | Qwen3.6-35B-A3B EXL3 3 bpw + MTP | **251.7 / 357.9 tok/s**, 1 user |
    | **RTX 3090** | Flash-Next EXL3, 256K context | MTP: 45.5 → **65.6 tok/s** |
    | **4× H200 NVL** | DeepSeek-V4.1-Flash, vLLM + speculative decoding | Crashed under load → **229.1 tok/s** decode, **17,546 tok/s** prefill; all six gates pass |
    
    Sources:
    
    - local-ai-registry:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  chuanqisun/spaceship
    ⭐ 781 stars  |  🍴 77 forks  |  💻 HTML  |  📅 2026-11-16
    🔗 https://github.com/chuanqisun/spaceship
    📡 来源: 🚀 5天300+星
    📝 Steer your ideas in realtime

    README 摘要:
    # 🕹️ Spaceship IDE
    
    Steer your ideas in realtime, space pilot style!
    
    ## Demos
    
    Watch on Instagram and YouTube. You can try the simulator at https://chuanqisun.github.io/spaceship/ with the option to go live with your API keys for Cerebras and Gemini. Keys stay in your browser local storage. Do it at your own risk.
    
    ## Conjecture
    
    > In the near future, LLM and Decision Models will reach 60 FPS interactivity.
    
    When that happens, what new interaction paradigms will unlock? This project demonstrates plausible and desirable interactions for that future.
    
    1. **Focus monitor**: can we visualize what LLM is paying attention to, and use that to guide human's focus towards what's important?
    
       
    
    2. **Attention lock**: can we force LLM to pay more attention to specific phrases so as to bias its future behavior?
    
       
    
    3. **Future Vector Steering**: can we decompose the task into eigenvectors, independently tune each, and re-compose them to influence the incoming text?
    
       
    
    4. **Realtime re-generation**: when text generation is cheap and fast, can we explore alternative futures by scrubbing?
    
       
    
    ## Design process
    
    I used Claude Code for most of the implementation but stayed hands-on for the UI/UX. I iterate using interactive style swatch, a technique where I prompt AI to give me diverse options of designs, I provide feedback, and it iterates. You can see the design artifacts in the extra page.
    
    To achieve the realtime experience, I have to use agreesive speculative generation and manage cache invalidation based on user interactions. For example, when the main knob moves backward, I have to empty future texts and cancel ongoing requests. There are many considerations like this throughout the system and that took a lot of human judgement - claude didn't one shot them.
    
    ## Theory
    
    I'm currently focusing on systems that help human shape ideas in realtime. This project is a small step towards my upcoming thesis at the MIT Media Lab, where I investigate how semantic and symoblic systems can be coupled to enhance human creativity, agency, and joy of craft.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  superwyh/Game-Localization-Engineering
    ⭐ 74 stars  |  🍴 1 forks  |  💻 Python  |  📅 2026-11-14
    🔗 https://github.com/superwyh/Game-Localization-Engineering
    📡 来源: 🌍 本地化/多语言 | 新建 | localization i18n transl
    🏷️ agent-skills, codex, game-development, game-localization, i18n, l10n, localization, python, quality-assurance, translation
    📝 Engineering-focused game localization for coding agents: contextual translation, naturalness review, engine integration, QA, and detailed developer reports.

    README 摘要:
    # Game Localization Engineering
    
    **English** · 简体中文 · 繁體中文 · 日本語 · 한국어 · Français · Deutsch · Español (ES) · Português (BR) · All languages
    
    ## Install with your agent
    
    Copy this prompt into your coding agent:
    
    ```text
    Install the game-localization skill from this repository:
    https://github.com/superwyh/Game-Localization-Engineering
    
    Locate game-localization/SKILL.md and preserve the complete folder.
    Use the current agent’s supported user-level skill directory.
    Check existing local changes before updating.
    Verify Python 3.10+ and run scripts/check_package.py in the installed package.
    Report the installation path, check results, and invocation method.
    ```
    
    Game Localization Engineering is a self-contained skill for translating game projects, preserving resource integrity, reviewing updates, and producing a detailed developer handoff. The agent translates using the game’s context; bundled Python tools manage extraction, review records, structural checks, staging, integration, and recovery.
    
    ## Capabilities
    
    | Capability | What it handles |
    |---|---|
    | Context and voice | Terminology by concept; speaker, addressee and story-stage voice; UI, dialogue, subtitles, items, quests, humor and linked puzzle clues. |
    | Resource protection | Stable IDs, parameters, markup, protected literals, source revisions and metadata. Direct adapters for flat JSON maps, CSV and TSV. |
    | Incremental updates | Retain unchanged translations, mark changed source/context/guidance as stale, keep the original translation basis, and preserve removed entries for recovery. |
    | Returned reviews | Export CSV packets; match reordered rows by ID; detect competing edits, changed source fields and concurrent local changes before writing. |
    | Guarded integration | Stage outputs, inspect per-ID changes, check destination hashes, retain backups and refuse rollback over later developer edits. |
    | Coverage and LQA | Separate logical messages, physical resource slots and build-bound scene evidence; validate layout, switching, input, fonts and accessibility when applicable. |
    | Scoped compliance | Off by default. Enable triage or release review only for selected markets, platforms and mechanics, using local versioned evidence. |
    | Developer delivery | Full source/target comparison plus decisions, file changes, actual checks, unresolved issues, exclusions and a concrete verification checklist. |
    
    ## Naturalness and translation post-editing
    
    Review awkward phrasing, sou
