📊 开源日报 — 2026-10-27
共发现 11 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  gitroomhq/postiz-app
    ⭐ 38643 stars  |  🍴 7465 forks  |  💻 TypeScript  |  📅 2023-07-08
    🔗 https://github.com/gitroomhq/postiz-app
    📡 来源: trending-daily
    🏷️ nextjs, open-source, open-source-social-media-scheduling-tool, oss, postiz-cloud, postiz-hosted, redis, scheduling-tool, social-media-scheduling-tool, typescript
    📝 📨 The ultimate agentic social media scheduling tool 🤖

    README 摘要:
    Postiz is a social media management platform for scheduling, automating, and analyzing your content.
        
      Use Postiz Cloud for a fully managed experience, or deploy the open-source edition on your own infrastructure.
      
    
      
      Explore the docs »
      
    
      
      Watch the YouTube Tutorials»
      
    
      Register
      ·
      Join Our Discord (devs only)
      ·
      Public API
    
      NodeJS SDK
      ·
      N8N custom node
      ·
      Make.com integration
    
    Schedule posts to:
    
      
      
      
      
      
      
      
      
      
      
      
      
      

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  alchaincyf/huashu-design
    ⭐ 27200 stars  |  🍴 2984 forks  |  💻 HTML  |  📅 2026-04-19
    🔗 https://github.com/alchaincyf/huashu-design
    📡 来源: trending-daily
    🏷️ agent-skills, ai-design, claude-code, claude-skills, codex, cursor, design, html, pptx, prototype
    📝 Huashu Design 3.0 · 在 agent 里打一句话，拿回能交付的设计：网页 / App 原型 / 可编辑 PPTX / 动画 / 信息图 · 六个候选挑三个方向 · 84 种带样张的风格库 · 越用越懂你的外观账本与设计体检 · HTML-native design skill for Claude Code, Codex, Cursor & any agent

    README 摘要:
    🌐 中文 · English
    
    # Huashu Design
    
    > *「打字。回车。一份能交付的设计。」*
    > *"Type. Hit enter. A finished design lands in your lap."*
    
    **在你的 agent 里打一句话，拿回一份能交付的设计。**
    
    3 到 30 分钟，你能 ship 一段**产品发布动画**、一个能点击的 App 原型、一套能编辑的 PPT、一份印刷级的信息图。
    
    不是「AI 做的还行」那种水平——是看起来像大厂设计团队做的。给 skill 你的品牌资产（logo、色板、UI 截图），它会读懂你的品牌气质；什么都不给，**六张缩略图里挑出的三个真实方向 + 84 种带样张的风格库**也能兜底到不出 AI slop。
    
    **你看到这篇 README 里的每一页设计，都是 huashu-design 自己做的。** 不是 Figma，不是 AE，就是一句话 prompt + skill 跑通。下次产品发布要做宣传片？现在你也能做。
    
    ```
    npx skills add alchaincyf/huashu-design
    ```
    
    跨 agent 通用——Claude Code、Cursor、Codex、OpenClaw、Hermes 都能装。
    
    > 📣 **已改为 MIT 协议。** 自 2026-05-14 起本 skill 完全开源（MIT License），个人和**商用都免费**，无需事先授权。原「个人使用免费、企业商用需授权」的条款已作废。(查看变更)
    
    > 🆕 **3.0：三个方向更敢，项目之间也不再长一个样。** 先出六张缩略图再挑三版做成真稿；风格库扩到 84 种（新增 App、中文与东亚两个分区），每种都有样张；参照作品先截图再动手；带一个只量事实的设计体检，和一本记住你做过什么样子的外观账本。详见核心机制
    
    看效果 · 安装 · 能做什么 · 核心机制 · 和 Claude Design 的关系
    
    ---
    
      
    
      ▲ 3.0 发布片 · 32 秒 · 片里每一页设计都是 3.0 自己做的，剪辑用的是 huashu-motion
      👉 下载 MP4（1080p · 含配乐 · 24MB） ·
      2.0 的带音效 HTML 互动版
    
    ---
    
    ## 3.0 案例
    
    下面这些都是 3.0 跑出来的。前五个是从发布时新跑的 6 道题里挑的，每道只给一句话需求，方向是 agent 自己挑的，作者没插手；后两个一个是第三轮盲选赢下来的那版，一个是发布后作者拿它做的真实项目。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  NVIDIA/SkillSpector
    ⭐ 22411 stars  |  🍴 1953 forks  |  💻 Python  |  📅 2026-03-21
    🔗 https://github.com/NVIDIA/SkillSpector
    📡 来源: trending-daily
    🏷️ agent-security, agent-skills, agentic-ai, ai-security, claude-code, mcp, prompt-injection, security-scanner, security-tools, security-workflow
    📝 Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

    README 摘要:
    # SkillSpector
    
    **Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills.
    
    ## Overview
    
    AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. In the 31,132-skill analyzed subset of the research dataset, **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**.
    
    SkillSpector helps you answer: **"Is this skill safe to install?"**
    
    SkillSpector is part of the NVIDIA Verified Skills pipeline, which scans, evaluates, and signs agent skills before publication. Skills that pass are published to the NVIDIA skills catalog.
    
    ## Documentation
    
    - **Scan agent skills before installation** — Hosted guide: when to scan, how to read a report, and how to gate installs.
    - **Development guide** — Architecture, package layout, and how to extend the analyzer pipeline.
    - **Analysis resource bounds** — Fail-closed bundle, parser, nested-artifact, ledger, and finding ceilings.
    - **Pi extension** — Install SkillSpector as a Pi tool for scanning skills from inside agent sessions.
    - **OpenCode extension** — Install SkillSpector as an OpenCode tool and `/skillspector` command for scanning skills from inside agent sessions.
    
    ## Features
    
    - **Multi-format input**: Scan Git repos, URLs, zip files, directories, or single files
    - **71 vulnerability patterns** across 17 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, output handling, system prompt leakage, memory poisoning, tool misuse, rogue agent, anti-refusal, trigger abuse, dangerous code (AST), taint tracking, YARA signatures, MCP least privilege, and MCP tool poisoning
    - **Two-stage analysis**: Fast static analysis + optional LLM semantic evaluation
    - **Live vulnerability lookups**: SC4 queries OSV.dev for real-time CVE data with automatic offline fallback
    - **Multiple output formats**: Terminal, JSON, Markdown, and SARIF reports
    - **Risk scoring**: 0-100 score with severity labels and clear recommendations
    - **Baseline / false-positive suppression**: Accept known findings via a glob-rule or fingerprint baseline so re-scans surface only *new* issues (docs)
    
    ## Quick Start
    
    ### Installation
    
    > **Open-source software notice:** This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.
    
    Create and activate a virtual

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  t3dotgg/tstack
    ⭐ 1672 stars  |  🍴 100 forks  |  💻 Python  |  📅 2026-10-24
    🔗 https://github.com/t3dotgg/tstack
    📡 来源: 🚀 5天300+星
    📝 The agent skills I use every day. Works with Claude Code and Codex.

    README 摘要:
    # tstack
    
    The agent skills I use every day, cleaned up so anyone can use them. They work
    in Claude Code and Codex. Some use T3 Code
    features when they are available and fall back to native tools when they are
    not.
    
    ## Skills
    
    | Skill | Say | What it does |
    |---|---|---|
    | `full-send` | "full send" | Takes a change to a merged PR with nobody watching: proves it, reviews it, files it, babysits it, merges it. |
    | `full-stop` | "full stop" | Same as `full-send`, but stops when the PR is ready for you to merge. |
    | `council` | "council" | Gets review from three models from different providers, and loops until they agree. |
    | `sol-loop` | "sol loop" | Reviews a change with GPT Sol in a loop until both agents agree. |
    | `file-pr` | "file a PR" | Files a short PR that leads with the problem, not an inventory of changes. |
    | `takeover` | "take over" | Finishes someone else's PR, branch, or agent thread, and keeps their credit. |
    | `babysit-pr` | "babysit" | Watches a PR through CI and review bots, and fixes the real findings. |
    | `modernize` | "modernize" | Rebases an old PR and decides if it should still exist. |
    | `leaving-pr-comments` | (automatic) | Formats comments that an agent posts on your behalf. |
    
    Some skills call others. Install the ones they need too:
    
    - `full-send` uses `sol-loop`, `file-pr`, and `babysit-pr`.
    - `full-stop` uses `full-send`.
    - `takeover` uses `modernize`, `file-pr`, `babysit-pr`, and `leaving-pr-comments`.
    - `file-pr`, `babysit-pr`, and `modernize` use `leaving-pr-comments`.
    
    ## Install
    
    ```bash
    git clone https://github.com/t3dotgg/tstack
    cp -R tstack/skills/* ~/.claude/skills/   # Claude Code
    cp -R tstack/skills/* ~/.codex/skills/    # Codex
    ```
    
    ## Requirements
    
    - An authenticated GitHub CLI (`gh`).
    - `python3` for `babysit-pr`'s `pr-wait` script.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  nightly-labs/openbot
    ⭐ 1656 stars  |  🍴 201 forks  |  💻 TypeScript  |  📅 2026-08-12
    🔗 https://github.com/nightly-labs/openbot
    📡 来源: trending-daily
    🏷️ ai-agents, bun, codex, electron, local-first, macos, solidjs, typescript
    📝 A local-first desktop workspace for persistent AI teammates. Run Codex, Claude, and Grok with dedicated workspaces, task queues, file sharing, browser control, and agent-to-agent collaboration.

    README 摘要:
    # OpenBot
    
    OpenBot is a local-first desktop workspace for persistent AI teammates. It supports the local
    Codex App Server and
    Claude Code, plus Grok CLI,
    OpenCode, Gemini, Cursor CLI, and Cline CLI through ACP. It gives every agent its own workspace and
    conversation, and provides local queues, file transfers, an embedded browser, and agent-to-agent
    messaging in one desktop app.
    
    > [!WARNING]
    > OpenBot is a development preview. Agents currently run with `danger-full-access` and
    > `approvalPolicy: never`. They can read and modify files, run commands, use the network, and control
    > the embedded browser without per-action confirmations after the explicit first-launch consent.
    > Run only agents and tasks you trust, keep backups, and review Security before use.
    
    ## What works
    
    - Prompt-driven agent creation and editing on desktop and mobile, with editable instructions, avatar, and section review before saving.
    - Persistent agents backed by independent Codex, Claude, Grok, OpenCode, Gemini, Cursor, or Cline sessions and local workspaces.
    - Custom OpenAI-compatible endpoints and custom ACP agents, with detection of local model servers (Ollama, LM Studio) and installed agents.
    - Per-agent context monitoring with automatic compaction before long threads exhaust the model window.
    - FIFO message queues with pause, resume, cancellation, and crash-safe persistence.
    - Agent-to-agent messages, replies, reactions, images, and managed file transfers.
    - Shared desktop channel chats with one task owner, explicit delegation, shared history, and Stop, Resume, Reassign, Archive, and Restore controls.
    - A persistent embedded browser that agents can open, inspect, and control.
    - Optional Computer Use on macOS, Windows and Linux through the `cua-driver` binary in the release, which OpenBot starts as its own child process and gives to every provider.
    - Per-agent model, reasoning, profile, notification, browser, and panel state.
    - Local data and privacy-safe diagnostics exports from the account menu.
    - Optional OpenBot accounts through one-time email codes. The account API runs on Cloudflare Workers and D1.
    
    OpenBot is local-first, not offline-only. Codex connects to OpenAI, Claude connects to Anthropic,
    Grok connects to xAI, Gemini connects to Google, Cursor connects to Cursor, Cline connects to Cline,
    visited pages use the network, and installed plugins may connect to their own services.
    
    ## Install
    
    OpenBot supports macOS 13 or newer on Apple silicon or Intel, Windows 10 or newer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  ⚠️风险  KillaBoi/StealMyBitcoin-PoC
    ⚠️ 命中风险词: poc, cookie —— 默认归排除区，需人工确认
    ⭐ 870 stars  |  🍴 129 forks  |  💻 Python  |  📅 2026-10-25
    🔗 https://github.com/KillaBoi/StealMyBitcoin-PoC
    📡 来源: 🚀 5天300+星
    📝 A public release of the Steal My Bitcoin challenge

    README 摘要:
    sponsored with ❤️ by&nbsp;
    
    # Steal My Bitcoin CTF proof of concept
    
    > One live PHP callback against the Steal My Bitcoin challenge, start to finish, in a single standard-library Python file.
    
    This README explains stealmybitcoin_poc.py, a single-file Python reproduction of the request sequence used in my Steal My Bitcoin CTF run. It uses only Python's standard library. The script builds the requests itself, checks each leak before moving on, and records the HTTP bytes from a new run.
    
    This can probably be done easier without all the extra debug crap and as in my John Hammond video about the Steam Local Privilege Escalation I discovered, you could probably clean up this ugly PoC.
    
    > [!NOTE]
    > ⚠️ **Honestly please clean it up or make your own better version that isn't crumpled by Sol.** ⚠️
    
    **Everything below is written against the Docker lab**, not the live challenge. The lab is a local Alpine PHP 8.4.26 CLI server behind nginx, which is the same build and worker model the offsets were calibrated on. Stand it up in a minute and the whole chain runs end to end on your own machine. The live run that actually solved the challenge is kept as a historical note at the bottom.
    
    ```
      stage                 what goes out                        what comes back
      ─────────────────────────────────────────────────────────────────────────────
      0  health      GET /php-version.php                 ->  PHP 8.4.26 confirmed
      1  heap leak   249,042 B producer + 8 x   6,672 B   ->  256 B cookie
                     (OOM poisons a worker)                   └─ Zend chunk base
      2  code leak   251,557 B producer + 8 x  92,388 B   ->   16 B cookie
                     (OOM poisons a worker)                   └─ zval_ptr_dtor
      3  callback    368,812 B POST                       ->  forged HashTable runs
                     (fake HashTable + command)               └─ zif_system(cmd)
      ─────────────────────────────────────────────────────────────────────────────
      20 HTTP requests at most. No looping, no retries.
    ```
    
    ## The short version
    
    1. A small multipart upload makes PHP chew through far more memory than the wire size suggests.
    2. When it runs out of memory partway through session upload-progress parsing, PHP leaves stale state behind in a worker that then gets reused.
    3. Shape the follow-up requests right and bytes fall out through session cookies. I read those as a heap address and a PHP code address.
    4. With both addresses, a final request drops a forged PHP structure where cleanu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  andyhuo520/digital-human-koubo
    ⭐ 846 stars  |  🍴 214 forks  |  💻 TypeScript  |  📅 2026-10-26
    🔗 https://github.com/andyhuo520/digital-human-koubo
    📡 来源: 🚀 5天300+星
    📝 AI digital-human talking-head videos from one photo: Renoise MCP generation + 5 editing styles + 48 creator-grade packaging components. Agent skill for Claude Code / Codex / OpenClaw / WorkBuddy …

    README 摘要:
    # Digital Human Koubo · AI 数字人口播
    
    **One photo + one sentence → a finished talking-head video with a digital human.**
    Script, lip-synced AI presenter, voice clean-up, captions, and pro-YouTuber-style packaging — fully automated by your AI agent.
    
    **English** · 简体中文
    
    > This 27-second livestream ad has no real presenter. Face, voice, studio, captions and the price animation are all AI.
    > The only input was one sentence: *"Use this digital human to make a 30-second livestream ad for the WorkBuddy course — 10 lessons, ¥99, was ¥999."*
    > Total cost: **482 Renoise credits**.
    
    ---
    
    ## Demos
    
    Click a GIF (or "Watch") to play the full video. Every demo below was produced with this repo.
    
    | | | |
    |:---:|:---:|:---:|
    |  |  |  |
    | **Livestream sales ad** · 9:16 · 27 sStyle B + depth-text price ¥999→¥99▶ Watch | **Product recommendation** · 9:16 · 89 sAnimated captions, emoji, picture-in-picture▶ Watch | **Text behind the presenter** · 5 sVision person matting, 3-layer composite▶ Watch |
    
    | | |
    |:---:|:---:|
    |  |  |
    | **Step-by-step tutorial** · 16:9 · 4:36The digital human teaches how she was made (Style D)▶ Watch | **Digital human, upgraded** · 16:9 · 5:55Two presenters, 6 languages, 4 scenes, cat & dog (Style E)▶ Watch |
    |  |  |
    | **Launch breakdown** · 16:9 · 39 sPresenter on the side, code B-roll on the right (Style C)▶ Watch | **Finance / tech explainer** · 16:9 · 2:21Charts, documents, chapter cards (Style A)▶ Watch |
    
    Packaging component gallery · 48 components · 2:40 · ▶ Watch
    
    > All presenters in the demos are AI digital humans and every video is labelled "内容由 AI 数字人演绎" (performed by an AI digital human). The male presenter is the author's own digital twin, made from his own photo.
    
    ---
    
    ## What it does
    
    - **Digital human from one photo** — a fixed presenter (face, outfit, voice description, prompt template) stored in `persona.json`, so every video is the same person. Composite her into any scene (livestream studio, shop, classroom, Kyoto street) with GPT Image first, then make her talk.
    - **Lip-synced talking clips** — the script is split into ≤ 15-second segments and generated with **Grok Video 1.5** through **Renoise MCP**. Other models (Wan 3.0, OmniHuman for your own recording) are documented.
    - **Cost gate** — the agent always quotes *segments · seconds · credits · balance* first and waits for your "yes". It generates segment 1 for you to check before batching the rest.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  unclebob/ub-mode
    ⭐ 750 stars  |  🍴 36 forks  |  💻 None  |  📅 2026-10-25
    🔗 https://github.com/unclebob/ub-mode
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # ub-mode
    
    `ub-mode` is an agent skill that enforces disciplined software engineering principles when writing or changing code. It is loosely based on portions of @poteto's rules (`poteto-mode` / `pstack`), reduced and paired with deterministic quality-gate tools:
    
    1. **First Make it Work** — Laziness Protocol, Foundational Thinking, TDD, Redesign From First Principles, Attack the Premise, Subtract Before You Add, Outcome-Oriented Execution, Build the Lever, and Architecture (Model the Domain, Boundary Discipline, Type System Discipline, Make Operations Idempotent, Separate Before Serializing Shared State).
    2. **Then Make it Right** — Fix Root Causes, Sequence Work into Verifiable Units, Test Behavior (Not Implementation), Crapper (`CRAP = 0.8` similarity) are eliminated.
    - unclebob/mutator — Runs mutation testing to expose uncovered code and surviving mutants that tests fail to catch.
    - unclebob/uml-viewer — Visualizes components, coverage, CRAP, mutation scores, and dependency directions.
    
    ## Installation
    
    Copy `SKILL.md` into your agent's skills directory as `ub-mode/SKILL.md` (for example `~/.grok/skills/ub-mode/SKILL.md`, `~/.claude/skills/ub-mode/SKILL.md`, or `~/.cursor/skills/ub-mode/SKILL.md`), then invoke `/ub-mode`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  GabrieleLozupone/kokon
    ⭐ 224 stars  |  🍴 28 forks  |  💻 TypeScript  |  📅 2026-10-08
    🔗 https://github.com/GabrieleLozupone/kokon
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    🏷️ ai-photo-editor, comfyui-alternative, generative-fill, image-editing, image-generation, inpainting, linux, local-ai, macos, mcp
    📝 Edit photos by describing the change, on your own GPU. A free, open-source alternative to Nano Banana and ChatGPT image editing: photos stay on your computer, no daily limit. One installer for Windows, Mac and Linux sets up the best open model (Qwen-Image 2.1). MCP server for AI agents.

    README 摘要:
    Edit photos by describing the change, on your own computer.
    
      A free, open-source alternative to Nano Banana and Generative Fill that runs on your own GPU.
      One installer for Windows, Mac and Linux sets up the best open model for your hardware.
      Brush an area, type what you want, get the edit. Your photos stay with you, and you can edit as often as you like.
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
      
    
      Website ·
      Install ·
      Phone & server ·
      Features ·
      Examples ·
      AI agents ·
      FAQ ·
      Prompt guide ·
      How it works
    
    https://github.com/user-attachments/assets/8851c580-99b9-432a-82be-b6d42fa9a749
    
    Watch in 4K on YouTube · What's new in 0.10 (42 s)
    
      

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  FrigadeHQ/hob
    ⭐ 164 stars  |  🍴 5 forks  |  💻 TypeScript  |  📅 2026-10-14
    🔗 https://github.com/FrigadeHQ/hob
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    🏷️ ai-agent, ai-assistant, chatgpt-alternative, claude-alternative, desktop-app, electron, gemma, gpt-oss, linux, llama-cpp
    📝 An easier way to use AI on your own computer. A free, open-source alternative to Claude and ChatGPT that runs open-weight models like Gemma and gpt-oss locally on Mac, Windows and Linux. Private, and works offline.

    README 摘要:
    Hob
    
      An easier way to use AI on your own computer.
      A free, open-source alternative to Claude and ChatGPT.
    
      Visit hob.chat → &nbsp;·&nbsp;
      Download for Mac · Windows · Linux
    
      
    
      Fill out PDFs, work through documents, and much more. Free, private, and works offline.
      Hob picks the best frontier open-weight model that fits your computer and sets everything up for you.
    
      Help · Contributing · MIT license
      Made by Frigade.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  NekoCCN/ImagenCli
    ⭐ 43 stars  |  🍴 0 forks  |  💻 Python  |  📅 2026-10-22
    🔗 https://github.com/NekoCCN/ImagenCli
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    📝 Persistent image creation workbench for humans and AI agents, with a shared CLI/TUI workspace, multi-provider generation and editing, local post-processing, and structured JSON output.

    README 摘要:
    A bridge between people, agents, and image generation models.
      中文
    
    Imagen connects people and coding agents to image generation models through a shared workspace. People can browse images, adjust parameters, review requests, and manage artifacts in the TUI. Agents can use the CLI, JSON output, and bundled skills to do the same work in the same sessions.
    
    Configure your own image endpoint, create a session, and keep working from either interface. Plans, execution records, jobs, and image artifacts are stored locally, so a request made by an agent can be inspected and continued by a person, and the other way around.
    
    ## What it provides
    
    - **One workspace, two interfaces.** The TUI and CLI read and write the same sessions, plans, jobs, and artifacts.
    - **Your endpoint, your models.** Profiles support OpenAI-compatible Images endpoints, Gemini native `generateContent`, and other adapters. Available models and parameters come from the configured endpoint.
    - **Explicit execution.** A plan freezes the request for review. Approval and execution are separate steps; creating a plan never sends a generation request.
    - **Local postprocessing.** Smoothing, line work, tone and color changes, periodic-frequency suppression, resizing, comparison, and contact sheets.
    - **Batch and background work.** Local queues, independent child jobs, and an async worker.
    - **Agent skills.** Bundled guides teach coding agents the CLI, approval rules, artifact handling, and cost and weight boundaries. They install into project or global directories for supported agents.
    - **Optional local upscaling.** Model weights are selected and downloaded by the user, then checked against a pinned SHA-256 digest.
    - **English and Chinese interface text.** English is the default; JSON keys, statuses, and command identifiers do not change with the language.
    
    Processing always creates a new artifact. It never overwrites the input.
    
    ## How it fits together
    
    ```text
    request ──► plan (review) ──► approve ──► execute ──► job + artifact
                                                            │
                                              postprocess ◄─┴─► compare / sheet
    ```
    
    A turn records one creation attempt. A plan records the frozen request and digest. An artifact records the image and its provenance. Sessions group turns and artifacts. None of these require the TUI: the CLI produces the same records, and the TUI renders them.
    
    ## TUI and CLI at a glance
    
    Most daily work is available in both interfa
