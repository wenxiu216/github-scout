📊 开源日报 — 2026-10-12
共发现 10 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  danyuchn/asd-ste100-skill
    ⭐ 4581 stars  |  🍴 266 forks  |  💻 Python  |  📅 2026-07-20
    🔗 https://github.com/danyuchn/asd-ste100-skill
    📡 来源: trending-weekly
    📝 ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill for rewriting ambiguous agent-facing English.

    README 摘要:
    # ASD-STE100 Skill — Simplified Technical English for Agent Output
    
    A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructions cannot be misread.
    
    This skill repurposes that same discipline for a different reader: an **AI agent** parsing another agent's output, a tool description, an error message, or an inter-agent instruction, with no human in the loop to resolve ambiguity.
    
    ## Why STE, and Why for Agents
    
    STE exists because a misread instruction on an aircraft can kill people, and the intended readers were often not native English speakers with no author to call for clarification. The standard's fix: one meaning per word, active voice, simple tenses, one instruction per sentence, short sentences, no dropped words.
    
    An LLM agent parsing another agent's output is in a strikingly similar position — no back-channel, no way to ask "did you mean X or Y?" The same rules that keep a mechanic from misreading a torque spec keep a downstream agent from misreading a tool description or an inter-agent message.
    
    ## Before / After
    
    | Before | After |
    |---|---|
    | "This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review." | "The tool tries to synchronize state across the configured backends. If it finds a conflict, it reads the configured strategy. If the strategy allows automatic resolution, the tool may resolve the conflict without a user. If the tool does not resolve the conflict, it reports the conflict for manual review." |
    | "An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version." | "Your request may have failed. The cause may be a data format that does not match what the server expects. An outdated client can cause this mismatch. Check your client version." |
    
    More examples, including illustrations of the official STE rules themselves, in `examples/before-after.md`.
    
    ## What This Skill Does
    
    1. Picks a mode. **Strict** covers procedures, error messages, and tool descriptions. **STE-flavored** covers READMEs, PR descriptions, and explanatory prose. STE-flavored keeps the sentence discipli

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  wheresryan22/anatomy
    ⭐ 4095 stars  |  🍴 322 forks  |  💻 JavaScript  |  📅 2026-10-08
    🔗 https://github.com/wheresryan22/anatomy
    📡 来源: 🚀 5天300+星
    🏷️ agent-skill, open-source, svg, vizualization
    📝 An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems. Generates polished SVGs with optional WebGL shaders and 3D effects.

    README 摘要:
    Anatomy
    
    A Claude skill that explains an idea by building it as a real, working object.Also runs in OpenCode and Codex.Crafted, interactive isometric figures with many small precise parts, in SVG, WebGL and 3D.
    
      
      
      
      
      
      
    
      
      &nbsp;
      
      &nbsp;
      
    
      Quick start ·
      Gallery ·
      What it makes ·
      Install ·
      Usage ·
      Examples ·
      How it works ·
      Limits
    
      
    
    examples/raptor-engine, light theme, firing. The engine and stand are SVG; the plume is a WebGL shader in the same isometric camera.
    
    ---
    
    Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working *is* the concept. A cache key that skips work when nothing changed becomes a pin-tumbler lock that only turns when every pin matches. One GPU context serving many canvases becomes a gantry plotter whose single print head visits 16 wells.
    
    Then Claude builds that thing out of dozens of small, solid, shaded parts, puts it in a framed card with a title, a hint and a live readout, makes it move calmly under the pointer and the keyboard, and checks its own work by zooming in on every joint. Every number the figure shows comes from the same small model that moves its parts.
    
    ## Quick start
    
    ```sh
    npx skills add wheresryan22/anatomy -g -a claude-code

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  storytold/craft-launcher
    ⭐ 1378 stars  |  🍴 478 forks  |  💻 Rust  |  📅 2026-10-09
    🔗 https://github.com/storytold/craft-launcher
    📡 来源: 🚀 5天300+星
    📝 The Craft App Launcher

    README 摘要:
    ArtCraft Launcher
    
      One place to install, update and open every app in the Craft App Suite, rebuilt in pure Rust.
      PhotoCraft, LightCraft, FilmCraft, DesignCraft, VectorCraft, PdfCraft, EffectCraft, WordCraft,
      DeckCraft, GridCraft, CADCraft and SoundCraft: the right build for your computer, kept up to date.
    
      
      
      
      
    
      
    
      Download ArtCraft Launcher ·
      ArtCraft ·
      The Craft App Suite
    
    > [!NOTE]
    > **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
    > filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
    > last week. If you make things, you're one of us. **Come say hi on Discord.**
    
      What it does ·
      Features ·
      Downloads ·
      Build from source ·
      Craft App Suite ·
      Discord
    
      
    
      
      Switch between the grid and a sortable table.
    
    ## What it does
    
    The Craft apps each ship their own builds for every platform. ArtCraft Launcher saves you from
    hunting through a dozen release pages: it lists every app in the suite, shows which ones you have
    and which version, installs the right build for your operating system and processor, and tells
    you when an update is out. It is a small native app that can sit in your menu bar or system tray.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  ARahim3/DigUp
    ⭐ 1345 stars  |  🍴 93 forks  |  💻 Swift  |  📅 2026-10-08
    🔗 https://github.com/ARahim3/DigUp
    📡 来源: 🚀 5天300+星
    🏷️ embeddinggemma, embeddings, llama-cpp, local-first, macos, menubar-app, multimodal, on-device, semantic-search, swift
    📝 Search your Mac by what's in your files: photos, PDFs, recordings, videos and code. On-device, built on Google DeepMind's EmbeddingGemma 2.

    README 摘要:
    DigUp
    
    Describe it. Dig it up.
    Search the files on your Mac by what's in them, with Google DeepMind's
    EmbeddingGemma 2.
    
    Download for Mac · Apple Silicon,
    macOS 14 or later · Free and open source
    
    EmbeddingGemma 2 is the multimodal embedding model Google DeepMind released in October 2026. It puts text, images,
    audio and video into one shared space: a photo of a dog on a beach lands next to the words "a dog on the beach", and a
    recording of someone talking about sleep lands next to "where they talk about sleep". It understands more than 100
    languages, it's open (Apache 2.0), and at 740M parameters it's small enough to run comfortably on a laptop.
    
    DigUp brings that to the files on your Mac. Pick the folders to search, and it reads the pictures, PDFs, documents,
    recordings and videos in them. Then describe what you're looking for, in your own words, and it finds the match,
    whatever kind of file it is. All of it happens on your Mac.
    
    ## What you can find
    
    - "zebra in a video" opens the clip at the moment the zebra shows up
    - "where they talk about sleep" jumps to that minute of a podcast
    - "the clause about pets in the lease" shows the PDF page, with the words marked
    - "a dog on the beach" finds the photo, and "payment declined error" the screenshot
    - a search in English can find a note written in Bengali, Arabic or any of the model's 100+ languages, and the other
      way around
    - "code: retry a failed call with backoff" finds the function in your projects, if you turn on code search
    
    Exact words count too. Invoice numbers, error codes and names are matched as written, in file names, document text
    and the text inside screenshots, so a search gets both the meaning and the exact string.
    
    ## Private
    
    Nothing you index leaves your Mac. DigUp goes online only to download the model once and to check for updates once a
    day. The update check sends nothing about your files, and you can turn it off. No account, no telemetry.
    
    ## Install
    
    1. Download the DMG from Releases and drag DigUp to Applications, or use
       Homebrew: `brew install --cask arahim3/tap/digup`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ⚠️风险  anthropics/oss-scanner
    ⚠️ 命中风险词: 0-day —— 默认归排除区，需人工确认
    ⭐ 823 stars  |  🍴 413 forks  |  💻 Dockerfile  |  📅 2026-10-08
    🔗 https://github.com/anthropics/oss-scanner
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # OSS Scanner
    
    OSS Scanner is a service by Anthropic to scan critical open-source repositories for security vulnerabilities. Learn more about the service at red.anthropic.com/oss-scanner.
    
    Note, use of this tool is subject to the terms and conditions outlined in the OSS Scanner terms.
    
    ## How to sign up
    
    Enroll an open-source project by opening a pull request that adds one directory:
    
    ```
    projects/
    ```
    
    Our security scanner builds your project in an isolated VM, then analyses it with no Internet access and emails what it finds to `primary_contact` (and any CCs), each with a reproducer and a proposed patch where available. Reports are model-generated and are not reviewed by a human. Because of this we do not place a 90-day disclosure period on these findings and will not make them public. Project owners should provide `project.yaml` (to configure the scanner), a `Dockerfile` (stating how to build the project), and optionally a `threat_model.md` (providing project-specific threat modeling).
    
    ### project.yaml
    
    Start from `templates/project.yaml`:
    
    ```
    repo: https://github.com/example/project    # required: the git repository to scan; add #branch to pin one
    primary_contact: security@example.org       # required: reports and build problems go here (one address)
    auto_ccs:                                   # optional: more addresses on every mail
      - maintainer@example.org
    homepage: https://example.org               # optional
    disabled: false                             # optional: true pauses reports without removing the enrolment
    dockerfile: .oss-scanner/Dockerfile         # required unless a Dockerfile sits in this repo next to your project.yaml
    threat_model: .oss-scanner/threat_model.md  # optional; also supports placing the file in this repository
    ```
    
    `repo` and `primary_contact` are always required. `dockerfile` is required unless you keep your Dockerfile next to `project.yaml` (see below). Others are optional.
    
    The email addresses in `project.yaml` are public. Use addresses you are happy to see published, such as a security alias.
    
    To receive reports encrypted, add your armored OpenPGP public key. Reports then go to `primary_contact` only; pgp cannot be combined with `auto_ccs`:
    ```
    pgp: |
      -----BEGIN PGP PUBLIC KEY BLOCK-----
      mQINBF...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  wesbos/photo-frame-dashboard
    ⭐ 814 stars  |  🍴 68 forks  |  💻 Python  |  📅 2026-10-08
    🔗 https://github.com/wesbos/photo-frame-dashboard
    📡 来源: 🚀 5天300+星
    📝 Getting ADB, root, backups and custom apps onto locked-down Android photo frames (Skylight Calendar, BIUFRAME)

    README 摘要:
    # Taking over Android photo frames
    
    ▶️ **Watch the video: https://youtu.be/ZLycoUMltNI**
    
    If you are coming from reddit or youtube, you can purchase almost any photo frame from amazon. This is the one, I used: https://amzn.to/4zneGNM (amazon aff link)
    
    Notes and scripts from getting full control of locked-down Android displays: getting ADB,
    backing up the firmware, getting root, removing the vendor app, and running our own launcher,
    browser and kiosk app.
    
    **Which frame do you have?** Frames sold under the same name, even the same Amazon listing, can
    have different boards. Check Settings → About before you follow any guide:
    
    - Firmware string contains **`A33`** and **`PF1007L`**, home app is **AiMOR**: you have the
      Allwinner **PF1007L**. Many viewers of the video got this one. Start with
      pf1007l-start-here.md. Try ADB over USB first, then over the
      network. The SD card boot patch is the last resort.
    - Rockchip board, USB name `Synergy 10X1`, ADB prompt on screen: you have the frame from the video.
      Start with biuframe-setup-guide.md.
    - Anything else: see For agents: start here, and please
      send in what you find.
    
    |                    | Skylight Calendar 15" (150-CAL)                                | BIUFRAME 10.1" picture frame (in the video)      | PF1007L 10.1" picture frame (BIUFRAME and others)                                   |
    | ------------------ | -------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
    | SoC / Android      | Rockchip RK3566, Android 12                                    | Rockchip RK3126, Android 6.0.1                   | Allwinner A33, Android 6.0.1, AiMOR home app                                         |
    | USB name / IDs     | `rockchip D156`, `2207:0007` (MTP) → `2207:0006` (ADB)         | `Synergy 10X1`, `2207:0006` (ADB)                | `1f3a:1000` (mass storage only) → `1f3a:1002` (ADB, after the boot patch)            |
    | Cable              | Not recorded                                                   | USB-C. The first cable gave nothing, the second worked | USB-C-only units need a **USB-A to USB-C** cable. USB-C to USB-C gives no power or data.The cable in the box is likely power only. It does not carry data. Use another cable that already allows data transfer. |
    | ADB out of the box | No                                                             | Yes, accept the p

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  marclou/mailcheap
    ⭐ 790 stars  |  🍴 193 forks  |  💻 JavaScript  |  📅 2026-10-10
    🔗 https://github.com/marclou/mailcheap
    📡 来源: 🚀 5天300+星
    📝 Self-hosted newsletters on Amazon SES. About $0.10 per 1,000 emails.

    README 摘要:
    # Mailcheap
    
    Mailcheap is a self-hosted newsletter app on Amazon SES. Write an issue, send it to your list, publish it on the web. About $0.10 per 1,000 emails.
    
    > [!IMPORTANT]
    > **No support.** This is a one-time open-source release. Issues are off, and setup questions go unanswered. Fork it, deploy it, make it yours.
    
    ## Why
    
    Newsletter platforms charge for every subscriber, every month. With your own SES account you pay for the emails you send: 10,000 readers and 4 issues a month is 40,000 emails, about $4.
    
    Mailcheap is the rest of what a newsletter needs, in one small Next.js app: an editor, a list, signup forms, unsubscribe handling, bounce and complaint handling, stats and a public archive. One admin, no teams, no plans. Your list stays in your database.
    
    ## Features
    
    **Write and send**
    
    - Editor with a live email preview, slash commands, image uploads and boxes. Markdown and raw HTML work too.
    - Checks before every send: subject, preview text, unsubscribe link, size under Gmail's 100 KB clip, postal address, verified domain.
    - Test emails, scheduling, and sending in batches through QStash at the rate you set.
    - Send in steps: start with your most engaged readers, then send to more.
    
    **Grow the list**
    
    - Several newsletters in one install, each with its own from address, reply-to and postal address.
    - A signup form on each newsletter's archive, and a signup API with API keys.
    - Confirmed opt-in per newsletter, off by default. Welcome email.
    - Rate limits on signups, login, unsubscribes and the API, on by default.
    
    **Keep it healthy**
    
    - SES events (deliveries, bounces, complaints) and a suppression list shared by every newsletter.
    - A send pauses itself when bounces pass 2% or complaints pass 0.08%.
    - One-click unsubscribe (RFC 8058 `List-Unsubscribe` headers) and an unsubscribe page, with signed links.
    - List cleanup, off by default: readers who ignored several issues get one "do you still want this?" email, then stop getting issues.
    - Open and click tracking on your own domain, with link scanners filtered out.
    
    **Publish and measure**
    
    - A public archive for each newsletter: issue pages, author page, share images, sitemap. Optional custom domain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  rociiu/talorys
    ⭐ 787 stars  |  🍴 61 forks  |  💻 TypeScript  |  📅 2026-10-10
    🔗 https://github.com/rociiu/talorys
    📡 来源: 🚀 5天300+星
    🏷️ ai-agent, cloudflare, cloudflare-workers, durable-objects, personal-assistant, react, self-hosted, typescript, workers-ai
    📝 Your personal AI agent in your own Cloudflare account. Chat, memory, tasks, notes and scheduled reminders, deployed with one command: npx create-talorys@latest. Free-tier friendly, single-user, no telemetry.

    README 摘要:
    # Talorys
    
    **Your personal AI agent. Your own cloud.**
    
    Talorys is a free, open-source personal AI assistant that runs entirely inside
    **your own Cloudflare account**. It chats with you, remembers what matters,
    manages tasks, notes and projects, and runs reminders and routines on a
    schedule — without any server, database or account operated by the Talorys
    developers.
    
    One person. One Cloudflare account. One command. One personal AI agent.
    
    ```bash
    npx create-talorys@latest
    ```
    
    ---
    
    ## 1. What Talorys is
    
    - **A private assistant** — chat with streaming responses, Markdown and tool activity indicators.
    - **Memory** — durable personal facts and preferences you can view, edit and delete. Only the most relevant memories are sent to the model on each turn.
    - **Semantic recall (optional)** — finds memories by meaning as well as keyword, and lists them newest first with their saved date. Off by default; turn it on in Settings → AI or install with `--semantic`. See docs/semantic-recall.md.
    - **Memory history** — facts that change over time: when you say you sold your car, the old one is kept as a past fact instead of being treated as current, and unclear conflicts wait for your review. See docs/memory-history.md.
    - **Tasks, notes and projects** — full CRUD in the UI, and from chat ("Add a task to review my project tomorrow").
    - **Automations** — one-time and recurring reminders, daily task digests and optional AI routines, delivered to an in-app notification center. They run on Durable Object alarms, so nothing has to stay online.
    - **Single-user by design** — no signup, no accounts, no teams. The installer sets the owner password.
    - **Works without AI** — tasks, notes, memories and reminders keep working if Workers AI is unavailable or your free quota is used up.
    
    ### Screenshots
    
    | Chat with tool activity | Tasks |
    | --- | --- |
    |  |  |
    | **Memory (dark mode)** | **Automations** |
    |  |  |
    
     &nbsp; 
    
    ## 2. How it works

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  nanihadesuka/NovelDokusha
    ⭐ 362 stars  |  🍴 39 forks  |  💻 Kotlin  |  📅 2021-07-21
    🔗 https://github.com/nanihadesuka/NovelDokusha
    📡 来源: 📖 阅读/内容平台 | 活跃 | web novel reader
    🏷️ android, android-app, epub-reader, jetpack-compose, kotlin, light-novel, light-novel-reader, light-novels, novel, reader
    📝 Android web novel reader

    README 摘要:
    ## ⚠️ Project Status: No Longer Maintained
    
    This project is no longer actively maintained.
    Feel free to fork it or use it as-is, but note that no further updates, bug fixes, or support will be done.
    
    # NovelDokusha
    Android web novel reader. Reader focused on simplicity, improving reading immersion.
    Search from a large catalog of content, open your pick and just enjoy.
    
    # License
    Copyright © 2023, nani, Released under GPL-3 FOSS
    
    ## Features
      - Multiple sources from where to read novels
      - Multiple databases to search for novels
      - Local source to read local EPUBs
      - Easy backup and restore
      - Light and dark themes
      - Follows modern Material 3 guidelines
      - Reader
        - Infinite scroll
        - Custom font, font size
        - Live translation
        - Text to speech
          - Background playback
          - Adjust voice, pitch, speed
          - Save your preferred voices
    
      
    ## Screenshots
     
    |              Library               |                Finder                |
    |:----------------------------------:|:------------------------------------:|
    |        |           |
    |             Book info              |            Book chapters             |
    |      |     |
    |               Reader               |           Database search            |
    |         |  |
    |           Global search            |                                      |
    |  |                                      |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  0xcro3dile/answerui
    ⭐ 31 stars  |  🍴 0 forks  |  💻 TypeScript  |  📅 2026-10-07
    🔗 https://github.com/0xcro3dile/answerui
    📡 来源: 🤖 AI / LLM / RAG | 新建 | open source ChatGPT alte
    🏷️ generative-ui, llm, nextjs, ollama, openui, react, typescript
    📝 Open-source alternative to ChatGPT's Intelligent UI. Answers arrive as live charts, forms and calculators. Works with any OpenAI-compatible model, in the cloud or local.

    README 摘要:
    Answers you can use, not just read. Open source, any AI model.
      Ask how something works and get a live 3D scene you can steer.
    
      
      
      
    
      
    
    Watch in full quality · answers by Kimi K3, sped up 1.2×
    
    ---
    
    AnswerUI is an open-source alternative to ChatGPT's Intelligent UI. It answers with interfaces instead of
    walls of text: charts, forms, calculators, and live 3D and 2D scenes. Move a slider and the scene changes
    instantly, and the numbers it works out flow back into the text. It works with any OpenAI-compatible model,
    in the cloud or on your own machine.
    
    **How it works:** the model streams the interface in OpenUI Lang, and each scene runs as a sandboxed code
    island, two-way bound to the answer's state.
    
      
      
    
    In full quality: 2D animations · tools
    
    ## Quick start
    
    ```bash
    npx answerui-app
    ```
    
    The first run asks for your API key. Press Enter instead to use a local model with
    Ollama.
    
    Docker
    
    ```bash
    docker run -p 127.0.0.1:3000:3000 --env-file .env ghcr.io/0xcro3dile/answerui
    ```
