📊 开源日报 — 2026-10-13
共发现 11 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  open-webui/open-webui
    ⭐ 155345 stars  |  🍴 22664 forks  |  💻 Python  |  📅 2023-10-06
    🔗 https://github.com/open-webui/open-webui
    📡 来源: trending-daily
    🏷️ ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai
    📝 User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

    README 摘要:
    # Open WebUI 👋
    
    Open WebUI is **a home for AI**, a self-hosted AI platform that's **extensible**, **feature-rich**, user-friendly, and built to run **entirely offline**. With support for **Ollama** and **OpenAI-compatible APIs**, it gives you a powerful, provider-agnostic interface for both local and cloud-based models.
    
    Passionate about open-source AI? Join our team →
    
    > [!TIP]  
    > **Looking for an Enterprise Plan?** – **Speak with Our Sales Team Today!**
    
    For more information, be sure to check out our Open WebUI Documentation.
    
    ## Key Features of Open WebUI ⭐
    
    - 🚀 **Effortless Setup**: Install seamlessly via pip, uv, Docker, or Kubernetes (kubectl, kustomize, or helm), with `:ollama` and `:cuda` tagged images available for container deployments.
    
    - 🤝 **Broad Model & API Integration**: Connect any OpenAI-compatible API alongside local Ollama models. Point the API URL at **LMStudio, GroqCloud, Mistral, OpenRouter, vLLM, and more** to mix and match providers freely.
    
    - 🔐 **Granular RBAC & User Groups**: Administrators define detailed roles, groups, and permissions, giving each user exactly the access they need. Secure by default, with tailored experiences per group.
    
    - 🧩 **Plugin Support**: Extend Open WebUI with **Filters**, **Actions**, **Pipes**, **Tools**, and **Skills**. Connect external services through **MCP**, **MCPO**, and **OpenAPI tool servers**. Build custom integrations, rate limits, approval flows, data connections, and more.
    
    - 🤖 **Models & Agents**: Wrap any base model with custom instructions, tools, and knowledge to build specialized agents. Supports dynamic variables, per-user/group access control, and community preset imports via Open WebUI Community.
    
    - ⚡ **Agentic Execution with Open Terminal**: Give your agents a terminal and filesystem to carry out multi-step tasks. Let them analyze data, run scripts, fix errors, and produce files directly in chat. Scale to teams with **Terminals (Enterprise)** for per-user isolated environments, resource limits, and automatic lifecycle management.
    
    - 📝 **Notes**: A dedicated workspace for content outside conversations. Draft with a rich editor, use AI to rewrite selected text, and attach notes to any chat for full-context injection.
    
    - 📢 **Channels**: Real-time shared spaces where your team and AI models collaborate in one timeline. Tag models to draft or critique, with threads, reactions, pins, and access control.
    
    - 🧠 **Persistent Memory**: The AI remembers facts about you across conversations, ca

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  microsoft/BitNet
    ⭐ 41031 stars  |  🍴 3819 forks  |  💻 C++  |  📅 2024-08-05
    🔗 https://github.com/microsoft/BitNet
    📡 来源: trending-daily
    📝 Official inference framework for 1-bit LLMs

    README 摘要:
    # bitnet.cpp
    
    📰 News
    
    07/23/2026: 📣 We released VibeASR.cpp — a real-time multilingual ASR inference engine on CPU using BitNet I2_S quantization, achieving RTF Code] [Models] [Report] 
    
    07/20/2026: 📣 We released BitNet-embedding-0.6B and BitNet-embedding-270M on Hugging Face — the first 1-bit embedding models that deliver competitive embedding quality with significantly faster inference on CPUs.
    - **1.42x to 2.28x speedup** over F16 on BitNet-embedding-0.6B prefill (8 threads)
    - **1.32x to 1.74x speedup** over F16 on BitNet-embedding-270M prefill (8 threads)
    - Supports I2_S conversion with optimized kernels on x86 CPUs
    - Lossless inference with 2 bits per weight
    
    07/16/2026: 📣 Released BitNet Embeddings 0.6B/270M: I2_S Conversion and Inference Optimization — detailed guide for converting and running BitNet embedding models with optimized I2_S kernels.
    
    01/15/2026: 📣 Released BitNet CPU Inference Optimization — parallel kernel implementations with configurable tiling and embedding quantization support, achieving **1.15x to 2.1x** additional speedup over the original implementation.
    
    05/20/2025: 📣 Released BitNet Official GPU inference kernel — extending 1-bit inference beyond CPUs.
    
    04/14/2025: 📣 Released BitNet Official 2B Parameter Model on Hugging Face — the first official BitNet b1.58 model trained with 4T tokens.
    
    02/18/2025: 📑 Bitnet.cpp: Efficient Edge Inference for Ternary LLMs — system-level paper on bitnet.cpp's architecture and design.
    
    11/08/2024: 📑 BitNet a4.8: 4-bit Activations for 1-bit LLMs — enabling 4-bit activations for further efficiency gains.
    
    10/21/2024: 📑 1-bit AI Infra: Part 1.1, Fast and Lossless BitNet b1.58 Inference on CPUs — the technical report behind bitnet.cpp.
    
    10/17/2024: 📣 bitnet.cpp 1.0 released.
    
    03/21/2024: 📑 The-Era-of-1-bit-LLMs: Training Tips, Code, FAQ
    
    02/27/2024: 📑 The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits — the foundational paper introducing BitNet b1.58.
    
    10/17/2023: 📑 BitNet: Scaling 1-bit Transformers for Large Language Models — the original BitNet paper.
    
    ## Overview
    
    bitnet.cpp is the official inference framework for 1-bit LLMs (e.g., BitNet b1.58). It offers a suite of optimized kernels that support **fast** and **lossless** inference of 1.58-bit models on **CPU** and **GPU** (NPU support coming next).
    
    Try it out via this online demo, or build and run it on your own CPU or GPU.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  liseami/CCBaga
    ⭐ 1815 stars  |  🍴 176 forks  |  💻 Rust  |  📅 2026-10-11
    🔗 https://github.com/liseami/CCBaga
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    CCBaga
      A native macOS, Linux and Windows toolkit for a cleaner workspace and an environment you can verify.
      Claude identities · Browser fingerprints · System settings · Network Skill
      
        
        
        
        
        
      
      
        Features ·
        Installation ·
        Updates ·
        Quick start ·
        Usage guide ·
        Architecture ·
        Development ·
        Contributing
      
    
    **Intended use:** CCBaga is intended solely for people residing or traveling abroad to manage their own Claude identities. Use that violates Anthropic's official terms of service is prohibited.
    
    CCBaga brings local maintenance and environment setup into one focused desktop workflow. Inspect Claude data before removing it, rotate your companion browser's fingerprint and restart it, align system settings with a selected region, and compare real browser readings with the machine and network exit.
    
    Two applications work together: **CCBaga-A** owns native operations; **CCBaga-B** runs an isolated Fingerprint Chromium profile. Browser measurements return to the host through a local session. Changing a setting and verifying its effect are separate steps.
    
    ## Features
    
      
        Local Claude identitiesArchive the current local identity, switch to a saved identity or start with an empty workspace. Choose what stays shared and what moves with each identity.
        Fingerprint &amp; restartGenerate a fresh seed, apply the selected region's language and timezone, then restart the companion browser.
        Real environment checksCompare browser and machine readings with the actual network exit. Passing measured checks produces a green page and a large checkmark.
      
      
        Native system settingsApply timezone, preferred language and region settings. Open desktop controls for location and permissions; see platform-specific limits.
        AI-guided network setupThree simple steps, a coding-agent selector and a copyable Skill installation prompt. Give the AI your files and connection details; it handles the commands.
        Claude Code CLI toolsDetect the installation method and version. Uninstall or reinstall through native, npm/bun, Homebrew or WinGet workflows.
      
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  finic-ai/rag-stack
    ⭐ 1582 stars  |  🍴 137 forks  |  💻 TypeScript  |  📅 2023-07-12
    🔗 https://github.com/finic-ai/rag-stack
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    📝 🤖 Deploy a private ChatGPT alternative hosted within your VPC. 🔮 Connect it to your organization's knowledge base and use it as a corporate oracle. Supports open-source LLMs like Llama 2, Falcon, and GPT4All.

    README 摘要:
    > **RAGstack is a legacy project built by the team behind Finic (formerly Psychic) and is no longer maintained.** Finic now builds AI to stop fraud, abuse and financial crimes: Finic Grayson, a decision model API for real-time fraud and risk decisions, and agents for fraud investigations. See finic.ai.
    
    # 🧺 RAGstack
    
    Deploy a private ChatGPT alternative hosted within your VPC. Connect it to your organization's knowledge base and use it as a corporate oracle. Supports open-source LLMs like Llama 2, Falcon, and GPT4All.
    
        
    
        
    
      
        
    
    **Retrieval Augmented Generation (RAG)** is a technique where the capabilities of a large language model (LLM) are augmented by retrieving information from other systems and inserting them into the LLM’s context window via a prompt. This gives LLMs information beyond what was provided in their training data, which is necessary for almost every enterprise use case. Examples include data from current web pages, data from SaaS apps like Confluence or Salesforce, and data from documents like sales contracts and PDFs.
    
    RAG works better than fine-tuning the model because it’s cheaper, it’s faster, and it’s more reliable since the source of information is provided with each response.
    
    RAGstack deploys the following resources for retrieval-augmented generation:
    
    ### Open-source LLM
    
    - GPT4All: When you run locally, RAGstack will download and deploy Nomic AI's gpt4all model, which runs on consumer CPUs.
    
    - Falcon-7b: On the cloud, RAGstack deploys Technology Innovation Institute's falcon-7b model onto a GPU-enabled GKE cluster.
    
    - LLama 2: On the cloud, RAGstack can also deploy the 7B paramter version of Meta's Llama 2 model onto a GPU-enabled GKE cluster.
    
    ### Vector database
    
    - Qdrant: Qdrant is an open-source vector database written in Rust, so it's highly performant and self-hostable.
    
    ### Server + UI
    
    Simple server and UI that handles PDF upload, so that you can chat over your PDFs using Qdrant and the open-source LLM of choice.
    
    ## Run locally
    
    1. Copy `ragstack-ui/local.env` into `ragstack-ui/.env`
    2. Copy `server/example.env` into `server/.env`
    3. In `server/.env` replace `YOUR_SUPABASE_URL` with your supabase project url and `YOUR_SUPABASE_KEY` with your supabase secret API key. In `ragstack-ui/.env` replace `YOUR_SUPABASE_URL` with your supabase project url and `YOUR_SUPABASE_PUBLIC_KEY` with your supabase secret API key. You can find these values in your supabase dashboard under Settings > API

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  onehumanbeing/esp32-iphone-agent
    ⭐ 975 stars  |  🍴 121 forks  |  💻 Python  |  📅 2026-10-11
    🔗 https://github.com/onehumanbeing/esp32-iphone-agent
    📡 来源: 🚀 5天300+星
    🏷️ ai-agent, airplay, automation, computer-use, esp32, esp32-s3, iphone, llm, usb-hid
    📝 Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

    README 摘要:
    # ESP32 iPhone Agent
    
    **Let an AI model use a real iPhone — with a $7 ESP32. No Mac, no developer account, no jailbreak.**
    
    English · 简体中文
    
    Demo video and updates: X @iamhenryyuan · YouTube demo
    
    **Example 1 — draw on a canvas.** *"Open Whiteboard and draw a smiley face"*: the agent searches for the app, opens it and draws the face with continuous strokes. Every step's screenshot, with its tap or stroke drawn on top, stays on the step wall.
    
    **Example 2 — set an alarm.** *"Set an alarm for 7:00 AM that repeats every day, then save it"*: the agent opens Clock, types 0700 into the time wheel, ticks the days under Repeat several taps at a time, and saves. Left: the real iPhone with the ESP32 plugged in; right: the web UI.
    
    The agent sees the phone through AirPlay screen mirroring and touches it through a tiny ESP32-S3 board that
    plugs into the phone's USB port as a mouse and keyboard. Any OpenAI-compatible vision model can be the brain —
    a cloud API, or a model you run yourself.
    
    ## Why
    
    Most iPhone automation drives the phone through XCTest / WebDriverAgent. That needs a Mac, Xcode, a signed
    helper app and an Apple developer account (a free account's signature expires every 7 days). This project
    uses the same paths a person uses — the screen and a pointer — so the phone needs nothing installed.
    
    |                                  | ESP32 iPhone Agent        | XCTest / WebDriverAgent tools |
    |----------------------------------|---------------------------|-------------------------------|
    | Apple developer account          | **Not needed**            | Needed (to sign the runner)   |
    | Xcode                            | **Not needed**            | Needed                        |
    | Computer                         | Mac **or Linux**          | Mac                           |
    | App installed on the phone       | **None**                  | Test runner app               |
    | Jailbreak                        | Not needed                | Not needed                    |
    | Extra hardware                   | ESP32-S3 board (~$7)      | USB cable                     |
    | Works in any app, incl. games    | Yes (it only sees pixels) | Mostly (depends on the accessibility tree) |
    
    ## How it works
    
    - **Eyes — AirPlay mirroring.** The phone mirrors its screen to UxPlay running
      on your computer; a GStreamer pipeline turns the stream into JPEG frames for the agent and the web page.
    - **Hands — a USB HID bridge.** An ESP32-S3 plugged into the phone shows up as a standard USB

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  shaongitbd/doory
    ⭐ 889 stars  |  🍴 40 forks  |  💻 TypeScript  |  📅 2026-10-10
    🔗 https://github.com/shaongitbd/doory
    📡 来源: 🚀 5天300+星
    📝 Open source canva alternative

    README 摘要:
    **See it in action** &nbsp;·&nbsp;
    **Features** &nbsp;·&nbsp;
    **Templates** &nbsp;·&nbsp;
    **Doory vs Canva** &nbsp;·&nbsp;
    **Self-host** &nbsp;·&nbsp;
    **FAQ**
    
    Doory is a full design editor that runs in your browser. Make posters, social posts, stories, slides,
    invitations, resumes, thumbnails and business cards: start from a template or a blank page, edit everything,
    and export to PNG, JPG, SVG, PDF, MP4 or GIF. **Every feature is free, nobody needs an account to start, and you
    can run the whole thing on your own server.**
    
    ## 🎬 See it in action
    
      
    
    A real, unedited recording: pick a template, rename the band, recolour the dates, add a star, export.
    
    ## 💜 Why people pick Doory
    
      
        
          🆓 Free, for real
          No Pro plan, no locked templates, no watermarks, no ads. Every tool in the editor is there for everyone,
          from background removal to video export.
        
        
          ⚡ Start in one click
          Open the editor and design. Guests' work is saved in the browser; create an account only when you want
          your designs in the cloud, and they move over in one step.
        
      
      
        
          🏠 Yours to host
          One docker compose up runs the app, the API, the database and live collaboration on your own
          server. Every design and upload stays under your control.
        
        
          🛠️ A real editor

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  jhaizhou-ops/d2r-mobile
    ⭐ 880 stars  |  🍴 348 forks  |  💻 C  |  📅 2026-10-12
    🔗 https://github.com/jhaizhou-ops/d2r-mobile
    📡 来源: 🚀 5天300+星
    🏷️ compatibility-layer, diablo-2-resurrected, diablo2, game-port, ios, ipad, iphone, metal, reign-of-the-warlock
    📝 Open-source iOS compatibility layer for Diablo II: Resurrected with the Reign of the Warlock expansion. Runs your own Switch copy natively on iPhone and iPad — full touch controls, 60 fps, new endgame modes. Bring your own game files. 开源的《暗黑破坏神 II：狱火重生》术士君临 iOS 兼容层

    README 摘要:
    # D2R Mobile
    
    **An open-source iOS compatibility layer for Diablo II: Resurrected with the Reign of the Warlock expansion.** It brings the Nintendo Switch release you bought, expansion included, to iPhone and iPad in full: the original game code runs natively, every control is rebuilt for touch, the frame rate holds at 60 fps, and you are in a game one second after the main menu.
    
    This is not a tech demo that "sort of runs". It is a mobile version polished for daily play, from your first character all the way through the endgame.
    
    Platforms: iPhone / iPad (iOS 26 and later) · Game version: Switch release with Reign of the Warlock, 3.3.94012 (shown as 1.0.34.0 on the console) · English / 中文 · License: MIT · **Bring your own game files**
    
    中文: README.zh-CN.md
    
      
    
      
      
    
    | 100% | 60 fps | about 1 s | about 3.8 W |
    |:---:|:---:|:---:|:---:|
    | The original gameplay, because it is the original program | Steady, with no drops once the device warms up | From the main menu into a game | Whole-device power draw at 60 fps |
    
    ## What it is, and what it is not
    
    **It is:**
    
    - The game's own aarch64 program, **executing directly on the device**, with no emulated CPU. iPhone and Switch use the same class of processor; only the handful of instructions that cannot run unchanged under Apple's kernel are rewritten, and every other byte of the program is left exactly as shipped. Every class, every Runeword, Terror Zones, bosses, drop rules and quest flow are identical to the original.
    - The platform services the game expects — system calls, the file system, the graphics API, audio, input — provided by a small host written for Apple platforms. The graphics API is reimplemented entirely on Apple's Metal with no emulation layer in between, and the shaders are translated offline from the game's originals.
    - A port built for phones, and taken all the way: a complete touch control scheme, edge-to-edge iPhone and true full-screen iPad display, controller support, a power saver mode, save sync, English and Chinese, and a whole set of endgame modes and quality-of-life features the original never had.
    
    **It is not:**
    
    - An emulator, cloud gaming, or streaming.
    - **A source of game content. It contains none and distributes none.** There is no game program, art, text, data table or shader in this repository; all of that is generated on your own machine from your own files (see docs/GAME_FILES.md). What the repository does carry is the interface information we recorded to make the port wor

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  zhuyansen/new-term-radar
    ⭐ 727 stars  |  🍴 300 forks  |  💻 Python  |  📅 2026-10-12
    🔗 https://github.com/zhuyansen/new-term-radar
    📡 来源: 🚀 5天300+星
    🏷️ ai, aisa, github-actions, keyword-research, seo, trends
    📝 Daily radar for new AI terms: names of new models, products and repos, caught on X, Hugging Face, GitHub and sitemaps before keyword tools list them.

    README 摘要:
    # new-term-radar
    
    中文说明
    
    A daily report of the names that are starting to surge in AI: new models, products, tools and repos, caught where they are said first, before they show up in keyword tools.
    
    Built for people who make pages, posts or products around new terms: SEO for AI tool sites, newsletters, directories, anyone who wants to know about "Strata" or "Seedance" the day it appears and not two weeks later.
    
    ## Why
    
    A new name leaves a trail, in this order:
    
    1. A lab or a well-followed account says it on X; a model enters Hugging Face's trending list.
    2. One GitHub repo takes off on its own.
    3. Directories and competitors add pages for it; someone registers a domain for it and the site starts to rank.
    4. Your own site gets its first search impressions for it.
    5. Google Trends shows the curve, days or weeks later.
    
    Keyword tools read step 5. This radar reads steps 1 to 4 every day and uses step 5 only to check itself.
    
    One example it was built around: Niko1221/Strata was created on 2026-09-24 and had 7,700 stars nine days later. People were searching "niko strata" from 9/26, while no second repo carried the name and no keyword tool listed it. A single repo gaining 800 stars a day is the whole signal, and it is public.
    
    ## What it reads
    
    | Signal | What it catches | Needs | Cost |
    |---|---|---|---|
    | ① X | Names the accounts in your list used for the first time in 60 days | AIsa key | $0.003 per account per run |
    | ① Hugging Face | Models new to the trending top 50; quantised copies grouped under the base name | nothing | free |
    | ② GitHub breakout | A repo under 14 days old averaging 200+ stars a day, or +400 since yesterday; adds the search variants people use ("niko strata") | nothing (a GitHub token raises the rate limit) | free |
    | ③ Sitemaps | Words that several new URLs on a site share and its older URLs rarely carried | the sitemaps you list | free |
    | ③ New sites | Domains registered and first indexed in the last 90 days that already rank for 20+ keywords | AIsa key | about $0.13 per query, weekly |
    | ④ Search Console | Queries your site got impressions for, for the first time (fresh data) | your own Google token | free |
    | ⑤ Review | Each lead checked in Google Trends 14 days later, against its own baseline; hit rate and days ahead per signal | AIsa key | $0.0012 per search variant |
    | Keyword table | For the day's new names: the generic search terms behind them (what people do with the new thing), each sized and given a decision | AIsa key; GoA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  n1tr00-10/tiktok-web-signature
    ⭐ 711 stars  |  🍴 0 forks  |  💻 Python  |  📅 2026-10-09
    🔗 https://github.com/n1tr00-10/tiktok-web-signature
    📡 来源: 🚀 5天300+星
    🏷️ chacha, chacha20, encryption, python, reverse-engineering, signatur, tiktok, tiktok-algo, tiktok-api, tiktok-automation-script
    📝 tiktok web signature reverse engineer generates valid tiktok signatures for API requets

    README 摘要:
    tikTok Web Signature Generator
    
    Fully reverse-engineered TikTok Web API signature generator. Produces valid X-Gnarly, X-Bogus, and X-Dynosaur signatures that TikTok accepts with success responses.
    
        Confirmed working — TikTok returns status_code: 0 (success) when requests are signed with these generators.
    
        Need more than signatures? Profiles, followers, videos, comments, live chat and search through one REST API:
        Unofficial TikTok API - dev.omar-thing.site
    
    Reverse-Engineered Algorithm
    
    This project contains a complete reverse engineering of TikTok's web signature algorithm (SDK version 5.3.2, build 1.0.0.417).
    
    The algorithm was recovered through:
    
        Deobfuscation of the production webmssdk.js bundle
    
        Static analysis of the ChaCha-based cipher implementation
    
        Dynamic tracing of signature generation at runtime
    
        Byte-level reconstruction of the payload serialization format
    
        Verification against live TikTok API responses
    
    Result: Signatures generated by this library are accepted by TikTok's servers and return success responses (status_code: 0).
    Features
    
        Generate X-Dynosaur signatures with ChaCha20 encryption and FNV-1a hashing
    
        Generate X-Gnarly signatures with ChaCha20 encryption, MD5 digests and PRNG shuffle
    
        Generate X-Bogus placeholder (legacy compatibility)
    
        Support for SDK version 5.3.2 (build 1.0.0.417)
    
        Custom Base64 alphabet encoding
    
        Pure Python implementation
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  zeusinsight/FinderSearch
    ⭐ 652 stars  |  🍴 17 forks  |  💻 Swift  |  📅 2026-10-09
    🔗 https://github.com/zeusinsight/FinderSearch
    📡 来源: 🚀 5天300+星
    🏷️ appkit, file-manager, macos, search, swift
    📝 A native macOS file browser with fast fuzzy filename search, powered by fsearch.

    README 摘要:
    # FinderSearch
    
    A native Mac file browser with fast, fuzzy filename search. Browse folders,
    preview files, and manage your files in a familiar macOS interface.
    
    **Download for Apple Silicon**
    · macOS 15+
    · Usage & shortcuts
    · Release notes
    
    Still preview
    
    ## Features
    
    - **Find files quickly.** Fuzzy matching, relevance ranking, folder scope, and
      filters like `ext:pdf` and `mtime:<7d`.
    - **Browse your way.** Icon, list, column, and gallery views, Quick Look previews,
      and tabs that restore when you reopen the app.
    - **Get file work done.** Drag selection, copy and move, batch rename, ZIP tools,
      tags, sharing, Trash, and undo.
    - **Stay in control.** Transfer progress, cancellation, and clear choices when
      files conflict.
    
    Built with SwiftUI and AppKit, powered by
    fsearch. Search runs locally;
    your files aren't uploaded.
    
    ## Install
    
    1. Download the DMG and drag **FinderSearch** into **Applications**.
       When updating, quit the old app first and replace it.
    2. Eject the disk image and open FinderSearch.
    3. Enable **Full Disk Access** in **System Settings → Privacy & Security** to
       search protected folders, then quit and reopen the app.
    
    The app is not yet Developer ID-signed or notarized. If macOS blocks it, choose
    **Privacy & Security → Open Anyway**. Allow the first search index to finish building.
    
    Permissions and troubleshooting →
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  DRincs-Productions/pixi-vn
    ⭐ 151 stars  |  🍴 8 forks  |  💻 TypeScript  |  📅 2024-02-14
    🔗 https://github.com/DRincs-Productions/pixi-vn
    📡 来源: 🎬 互动叙事/创作 | 活跃 | visual novel framework
    🏷️ adventure-game-engine, cross-platform, galgame, game-engine, game-framework, ink, javascript, npm-package, nvl, pixi-js
    📝 Create visual novels with a modern 2D rendering engine and your favorite JavaScript framework.

    README 摘要:
    # Pixi’VN - PixiJS Game Engine
    
      
      
      
      
      
    
    Pixi’VN is a very versatile and powerful story-driven engine. It is based on JavaScript/TypeScript and PixiJS, and supports animated characters through Spine 2D and Live2D.
    
    Pixi’VN aims to be an innovative and fast engine, and puts a strong emphasis on AI-assisted development: an AI agent can start your game, gain all the knowledge it needs about your project through Agent Skills, and test the game by launching it in a browser — with the ability to keep driving it from the outside while it plays.
    
    You can use narrative languages that are able to take full advantage of the engine's features, as well as any custom features you add to your project. Currently supported:
    
    - _ink_
    
    ## Templates
    
    For a quick start, various project templates are available, built with React. Less experienced developers can use these templates without much knowledge of JavaScript/TypeScript.
    
    - **Visual Novel**: a classic dialogue-driven experience, with characters, backgrounds, and choices.
    - **Point & Click Adventure**: an adventure game where the player explores scenes and interacts with objects and characters.
    - **Interactive Fiction**: feels like reading a book. Unlike a visual novel, images are shown as vignettes, just as illustrations would appear on a page.
    
    To create a new project from a template, run:
    
    ```npm
    npm create pixi-vn@latest
    ```
    
    ### Distribution
    
    Pixi’VN is independent of any distribution technology, but strong emphasis is being placed on Roves, built by the same team behind Pixi’VN.
    
    | Platform    | Roves | Tauri | Electron |
    | ----------- | ----------------------------------- | ------------------------------ | --------------------------------------- |
    | Windows     | ✅                                  | ✅                             | ✅                                      |
    | macOS       | ✅                                  | ✅                             | ✅                                      |
    | Linux       | ✅                                  | ✅                             | ✅                                      |
    | Android     | ✅                                  | ✅                             | ❌                                      |
