📊 开源日报 — 2026-06-26
共发现 20 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ripienaar/free-for-dev
    ⭐ 123486 stars  |  🍴 13038 forks  |  💻 HTML  |  📅 2015-03-18
    🔗 https://github.com/ripienaar/free-for-dev
    📡 来源: trending-daily
    🏷️ awesome-list, free-for-developers
    📝 A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev

    README 摘要:
    # free-for.dev
    
    Developers and Open Source authors now have many services offering free tiers, but finding them all takes time to make informed decisions.
    
    This is a list of software (SaaS, PaaS, IaaS, etc.) and other offerings with free developer tiers.
    
    The scope of this particular list is limited to things that infrastructure developers (System Administrator, DevOps Practitioners, etc.) are likely to find useful. We love all the free services out there, but it would be good to keep it on topic. It's a grey line sometimes, so this is opinionated; please don't feel offended if I don't accept your contribution.
    
    This list results from Pull Requests, reviews, ideas, and work done by 1600+ people. You can also help by sending Pull Requests to add more services or remove ones whose offerings have changed or been retired.
    
    **NOTE**: This list is only for as-a-Service offerings, not for self-hosted software. To be eligible, a service must offer a free tier, not just a free trial. The free tier must be for at least a year if it is time-bucketed. We also consider the free tier from a security perspective, so SSO is fine, but I will not accept services that restrict TLS to paid-only tiers.
    
    # Table of Contents
    
      * Major Cloud Providers' Always-Free Limits
      * Cloud management solutions
      * Analytics, Events, and Statistics
      * APIs, Data and ML
      * Artifact Repos
      * BaaS
      * Low-code Platform
      * CDN and Protection
      * CI and CD
      * CMS
      * Code Generation
      * Code Quality
      * Code Search and Browsing
      * Crash and Exception Handling
      * Data Visualization on Maps
      * Managed Data Services
      * Design and UI
      * Dev Blogging Sites
      * DNS
      * Docker Related
      * Domain
      * Education and Career Development
      * Email
      * Feature Toggles Management Platforms
      * Font
      * Forms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  grafana/grafana
    ⭐ 74708 stars  |  🍴 14115 forks  |  💻 TypeScript  |  📅 2013-12-11
    🔗 https://github.com/grafana/grafana
    📡 来源: trending-daily
    🏷️ alerting, analytics, business-intelligence, dashboard, data-visualization, elasticsearch, go, grafana, hacktoberfest, influxdb
    📝 The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, Elasticsearch, InfluxDB, Postgres and many more. 

    README 摘要:
    The open-source platform for monitoring and observability
    
    Grafana allows you to query, visualize, alert on and understand your metrics no matter where they are stored. Create, explore, and share dashboards with your team and foster a data-driven culture:
    
    - **Visualizations:** Fast and flexible client side graphs with a multitude of options. Panel plugins offer many different ways to visualize metrics and logs.
    - **Dynamic Dashboards:** Create dynamic & reusable dashboards with template variables that appear as dropdowns at the top of the dashboard.
    - **Explore Metrics:** Explore your data through ad-hoc queries and dynamic drilldown. Split view and compare different time ranges, queries and data sources side by side.
    - **Explore Logs:** Experience the magic of switching from metrics to logs with preserved label filters. Quickly search through all your logs or streaming them live.
    - **Alerting:** Visually define alert rules for your most important metrics. Grafana will continuously evaluate and send notifications to systems like Slack, PagerDuty, VictorOps, OpsGenie.
    - **Mixed Data Sources:** Mix different data sources in the same graph! You can specify a data source on a per-query basis. This works for even custom datasources.
    
    ## Get started
    
    - Get Grafana
    - Installation guides
    
    Unsure if Grafana is for you? Watch Grafana in action on play.grafana.org!
    
    ## Documentation
    
    The Grafana documentation is available at grafana.com/docs.
    
    ## Contributing
    
    If you're interested in contributing to the Grafana project:
    
    - Start by reading the Contributing guide.
    - Learn how to set up your local environment, in our Developer guide.
    - Explore our beginner-friendly issues.
    - Look through our style guide and Storybook.
    
    > Share your contributor experience in our feedback survey to help us improve.
    
    ## Get involved
    
    - Follow @grafana on X (formerly Twitter).
    - Read and subscribe to the Grafana blog.
    - If you have a specific question, check out our discussion forums.
    - For general discussions, join us on the official Slack team.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  commaai/openpilot
    ⭐ 61611 stars  |  🍴 11035 forks  |  💻 Python  |  📅 2016-11-24
    🔗 https://github.com/commaai/openpilot
    📡 来源: trending-daily
    🏷️ advanced-driver-assistance-systems, driver-assistance-systems, robotics
    📝 openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars.

    README 摘要:
    openpilot
    
      openpilot is an operating system for robotics.
      
      Currently, it upgrades the driver assistance system in 300+ supported cars.
    
      Docs
       · 
      Roadmap
       · 
      Contribute
       · 
      Community
       · 
      Try it on a comma four
    
    Quick start: `bash 
    
      
        
        
        
      
    
    Using openpilot in a car
    ------
    
    To use openpilot in a car, you need four things:
    1. **Supported Device:** a comma four, available at comma.ai/shop/comma-four.
    2. **Software:** The setup procedure for the comma four allows users to enter a URL for custom software. Use the URL `openpilot.comma.ai` to install the release version.
    3. **Supported Car:** Ensure that you have one of the 300+ supported cars.
    4. **Car Harness:** You will also need a car harness to connect your comma four to your car.
    
    We have detailed instructions for how to install the harness and device in a car. Note that it's possible to run openpilot on other hardware, although it's not plug-and-play.
    
    ### Branches
    
    Running `master` and other branches directly is supported, but it's recommended to run one of the following prebuilt branches:
    
    | comma four branch      | comma 3X branch        | URL                                    | description                                                                         |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  mukul975/Anthropic-Cybersecurity-Skills
    ⭐ 21602 stars  |  🍴 2481 forks  |  💻 Python  |  📅 2026-02-25
    🔗 https://github.com/mukul975/Anthropic-Cybersecurity-Skills
    📡 来源: trending-weekly
    🏷️ ai-agents, claude-code, cloud-security, cybersecurity, devsecops, ethical-hacking, incident-response, infosec, llm, malware-analysis
    📝 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 29 security domains · Apache 2.0

    README 摘要:
    #  Anthropic Cybersecurity Skills
    
    ### The largest open-source cybersecurity skills library for AI agents
    
    **817 production-grade cybersecurity skills · 29 security domains · 6 framework mappings · 26+ AI platforms**
    
    Get Started · What's Inside · Frameworks · Platforms · Contributing
    
    ---
    
    > ⚠️ **Community Project** — This is an independent, community-created project. Not affiliated with Anthropic PBC. 
    
    ## Give any AI agent the security skills of a senior analyst
    
    A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**
    
    This repo contains **817 structured cybersecurity skills** spanning **29 security domains**, each following the agentskills.io open standard.  Every skill is mapped to **six industry frameworks** — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework (F3) — making this the only open-source skills library with unified cross-framework coverage.  Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.
    
    ## Six frameworks, one skill library
    
    No other open-source skills library maps every skill to all of these frameworks.  One skill, six compliance checkboxes. 
    
    | Framework | Version | Scope in this repo | What it maps |
    |---|---|---|---|
    | MITRE ATT&CK | v19.1 | 15 tactics · 286 techniques | Adversary behaviors and TTPs |
    | NIST CSF 2.0 | 2.0 | 6 functions · 22 categories | Organizational security posture |
    | MITRE ATLAS | v5.4 | 16 tactics · 84 techniques | AI/ML adversarial threats |
    | MITRE D3FEND | v1.3 | 7 categories · 267 techniques | Defensive countermeasures |
    | NIST AI RMF | 1.0 | 4 functions · 72 subcategories | AI risk management |
    | MITRE F3 (Fight Fraud Framework) | v1.1 (2026-04-09) | 8 tactics · 123 techniques · 94 fraud-relevant skills | Cyber-enabled financial fraud TTPs |
    
    **Example — a single skill maps across all six:**
    
    | Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF | F3 |
    |---|---|---|---|---|---|---|
    | `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 | — |
    | `detecting-business-email-compromise` | T1566 | DE.AE | — | — | — | F1005.006 · monetization |
    
    ### 🆕 MITRE Fight Fraud Framework (F3) — 94 fraud-relevant skills
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  JCodesMore/ai-website-cloner-template
    ⭐ 20973 stars  |  🍴 3058 forks  |  💻 TypeScript  |  📅 2026-03-13
    🔗 https://github.com/JCodesMore/ai-website-cloner-template
    📡 来源: trending-daily
    🏷️ ai, ai-agents, ai-tools, automation, boilerplate, claude, claude-code, clone, developer-tools, nextjs
    📝 Clone any website with one command using AI coding agents

    README 摘要:
    # AI Website Cloner Template
    
      
    
    A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents. 
    
    **Recommended: Claude Code with Opus 4.7 for best results** — but works with a variety of AI coding agents.
    
    Point it at a URL, run `/clone-website`, and your AI agent will inspect the site, extract design tokens and assets, write component specs, and dispatch parallel builders to reconstruct every section.
    
    ## Demo
    
    > Click the image above to watch the full demo on YouTube.
    
    ## Quick Start
    
    > **Important:** Start by making your own copy with GitHub's **Use this template** button. Do not clone this template repository directly for your website project, and do not open pull requests here with your generated website.
    
    1. **Create your own repository from this template**
    
       On the GitHub page for this project, click **Use this template**, then click **Create a new repository**.
    
       Give your new repository a name, choose whether it should be public or private, then click **Create repository**. If GitHub shows an **Include all branches** option, you can leave it off.
    
       This gives you your own separate project to work in, so your website changes stay in your account instead of coming back to the main template.
    
    2. **Open your new repository on your computer**
    
       After GitHub creates your copy, open that new repository. Click **Code** and open or clone your new repository with your preferred coding tool.
    
       If you use the terminal, the command will look like this:
    
       ```bash
       git clone https://github.com/YOUR-USERNAME/YOUR-NEW-REPOSITORY.git
       cd YOUR-NEW-REPOSITORY
       ```
    
    3. **Install dependencies**
       ```bash
       npm install

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  google-labs-code/design.md
    ⭐ 20393 stars  |  🍴 1687 forks  |  💻 TypeScript  |  📅 2026-04-10
    🔗 https://github.com/google-labs-code/design.md
    📡 来源: trending-daily
    📝 A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system.

    README 摘要:
    # DESIGN.md
    
    A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system.
    
    ## The Format
    
    A DESIGN.md file combines machine-readable design tokens (YAML front matter) with human-readable design rationale (markdown prose). Tokens give agents exact values. Prose tells them *why* those values exist and how to apply them.
    
    ```md
    ---
    name: Heritage
    colors:
      primary: "#1A1C1E"
      secondary: "#6C7278"
      tertiary: "#B8422E"
      neutral: "#F7F5F2"
    typography:
      h1:
        fontFamily: Public Sans
        fontSize: 3rem
      body-md:
        fontFamily: Public Sans
        fontSize: 1rem
      label-caps:
        fontFamily: Space Grotesk
        fontSize: 0.75rem
    rounded:
      sm: 4px
      md: 8px
    spacing:
      sm: 8px
      md: 16px
    ---
    
    ## Overview
    
    Architectural Minimalism meets Journalistic Gravitas. The UI evokes a
    premium matte finish — a high-end broadsheet or contemporary gallery.
    
    ## Colors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  DeusData/codebase-memory-mcp
    ⭐ 15108 stars  |  🍴 1111 forks  |  💻 C  |  📅 2026-02-24
    🔗 https://github.com/DeusData/codebase-memory-mcp
    📡 来源: trending-weekly
    🏷️ aider, ast, claude-code, code-analysis, code-intelligence, codex, cursor, cypher, developer-tools, gemini-cli
    📝 High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.

    README 摘要:
    # codebase-memory-mcp
    
    **The fastest and most efficient code intelligence engine for AI coding agents.** Full-indexes an average repository in milliseconds, the Linux kernel (28M LOC, 75K files) in 3 minutes. Answers structural queries in under 1ms. Ships as a single static binary for macOS, Linux, and Windows — download, run `install`, done.
    
    High-quality parsing through tree-sitter AST analysis across all 158 languages, enhanced with **Hybrid LSP** semantic type resolution for Python, TypeScript / JavaScript / JSX / TSX, PHP, C#, Go, C, C++, Java, Kotlin, and Rust — producing a persistent knowledge graph of functions, classes, call chains, HTTP routes, and cross-service links. 14 MCP tools. Zero dependencies. Plug and play across 11 coding agents.
    
    > **Research** — The design and benchmarks behind this project are described in the preprint *Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP* (arXiv:2603.27277). Evaluated across 31 real-world repositories: 83% answer quality, 10× fewer tokens, 2.1× fewer tool calls vs. file-by-file exploration.
    
    > **Security & Trust** — This tool reads your codebase and writes to your agent configuration files. That is what it is designed to do. If you prefer to audit before running, the full source is here — every release binary is signed, checksummed, and scanned by 70+ antivirus engines. All processing happens 100% locally; your code never leaves your machine. Found a security issue? We want to know — see SECURITY.md. Security is Priority #1 for us.
    
      
      
      Built-in 3D graph visualization (UI variant) — explore your knowledge graph at localhost:9749
    
    ## Why codebase-memory-mcp
    
    - **Extreme indexing speed** — Linux kernel (28M LOC, 75K files) in 3 minutes. RAM-first pipeline: LZ4 compression, in-memory SQLite, fused Aho-Corasick pattern matching. Memory released after indexing.
    - **Plug and play** — single static binary for macOS (arm64/amd64), Linux (arm64/amd64), and Windows (amd64). No Docker, no runtime dependencies, no API keys. Download → `install` → restart agent → done.
    - **158 languages** — vendored tree-sitter grammars compiled into the binary. Nothing to install, nothing that breaks.
    - **120x fewer tokens** — 5 structural queries: ~3,400 tokens vs ~412,000 via file-by-file search. One graph query replaces dozens of grep/read cycles.
    - **11 agents, one command** — `install` auto-detects Claude Code, Codex CLI, Gemini CLI, Zed, OpenCode, Antigravity, Aider, KiloCode, VS Code,

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  simplex-chat/simplex-chat
    ⭐ 11712 stars  |  🍴 669 forks  |  💻 Haskell  |  📅 2019-12-21
    🔗 https://github.com/simplex-chat/simplex-chat
    📡 来源: trending-daily
    🏷️ chat, double-ratchet, e2ee, encryption, haskell, messaging, privacy, protocol, security
    📝 SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱!

    README 摘要:
    | 30/03/2023 | EN, FR, CZ, PL |
    
    # SimpleX - the first messaging platform that has no user identifiers of any kind - 100% private by design!
    
     &nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp; 
    
    **Why we are building SimpleX Network**
    
    ## Welcome to SimpleX Chat!
    
    1. 📲 Install the app.
    2. ↔️ Connect to the team, join user groups and follow our updates.
    3. 🤝 Make a private connection with a friend.
    4. 🔤 Help translating SimpleX Chat.
    5. ⚡️ Contribute and support us with donations.
    
    Learn more about SimpleX Chat.
    
    ## Install the app
    
    &nbsp;
    
    &nbsp;
    
    &nbsp;
    
    &nbsp;
    
    - 🖲 Protects your messages and metadata - who you talk to and when.
    - 🔐 Double ratchet end-to-end encryption, with additional encryption layer.
    - 📱 Mobile apps for Android (Google Play, APK) and iOS.
    - 🚀 TestFlight preview for iOS with the new features 1-2 weeks earlier - **limited to 10,000 users**!
    - 🖥 Available as a terminal (console) app / CLI on Linux, MacOS, Windows.
    
    ## Connect to the team
    
    You can connect to the team via the app using "chat with the developers button" available when you have no conversations in the profile, "Send questions and ideas" in the app settings or via our SimpleX address. Please connect to:
    
    - to ask any questions
    - to suggest any improvements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  baidu/Unlimited-OCR
    ⭐ 10026 stars  |  🍴 766 forks  |  💻 Python  |  📅 2026-06-18
    🔗 https://github.com/baidu/Unlimited-OCR
    📡 来源: 🚀 两周800+星
    📝 Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing.

    README 摘要:
    Unlimited OCR Works
    
      
        
      
      
        
      
    
        
        
      
      
        
      
    
    Welcome the Era of One-shot Long-horizon Parsing.
    
        
    
    ## Release
    - [2026/06/24] 🤝 Thanks to AK for creating a demo for us. It is now available at Hugging Face Spaces.
    - [2026/06/23] 📄 Our paper is now available on arXiv.
    - [2026/06/23] 🤝 Thanks to the ModelScope community for their support. Our model is now available at ModelScope.
    - [2026/06/22] 🚀 We present Unlimited-OCR, aiming to push Deepseek-OCR one step further.
    
    ## Inference
    
    ### Transformers
    Inference using Huggingface transformers on NVIDIA GPUs. Requirements tested on python 3.12.3 + CUDA12.9：
    
    ```
    torch==2.10.0
    torchvision==0.25.0
    transformers==4.57.1
    Pillow==12.1.1
    matplotlib==3.10.8
    einops==0.8.2
    addict==2.4.0
    easydict==1.13

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  alchaincyf/zhangxuefeng-skill
    ⭐ 9142 stars  |  🍴 2551 forks  |  💻 None  |  📅 2026-04-05
    🔗 https://github.com/alchaincyf/zhangxuefeng-skill
    📡 来源: trending-daily
    📝 张雪峰.skill — 张雪峰的认知操作系统。高考志愿/考研/职业规划的实战思维框架。由女娲.skill生成。

    README 摘要:
    # 张雪峰.skill
    
      
      
      动画由 huashu-design skill 制作
    
    > *「社会就是一个大筛子，用学历筛孩子，用房子筛父母，用工作筛家庭。」*
    
    **张雪峰的认知操作系统。不是语录合集，是可运行的思维框架。**
    
    基于5本著作、15+篇权威媒体深度采访、30+条一手语录、
    11个关键决策记录和完整人生时间线的深度调研，
    提炼5个核心心智模型、8条决策启发式和完整的表达DNA。
    
    看效果 · 安装 · 蒸馏了什么 · 调研来源
    
    ---
    
    ## 效果示例
    
    ### 问：我孩子今年高考，560分，河南的，想学金融，你怎么看？
    
    ```
    张雪峰    ❯ 停停停，你先别急着说金融。我问你几个问题。
    
                家里是做金融的吗？爸妈在银行、证券公司、基金公司？
                有没有亲戚在这个行业里？
    
                没有？那我跟你说，金融这个行业，千万别碰。
    
                你去看看每年金融专业毕业的学生，中位数去了哪？
                不是去了高盛，不是去了中金，是去了你家门口的银行网点
                卖理财产品。560分河南考生，大概率去个双非一本学金融，
                毕业出来跟985的抢岗位，你拿什么抢？脸吗？
    
                金融是典型的「看起来光鲜，进去才知道是坑」的行业。
                你看到的是年薪百万的基金经理，你看不到的是
                90%的人在银行网点站着数钱。
    
                560分河南，我给你一个方向：计算机或者电气工程。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  stablyai/orca
    ⭐ 7777 stars  |  🍴 549 forks  |  💻 TypeScript  |  📅 2026-03-17
    🔗 https://github.com/stablyai/orca
    📡 来源: trending-weekly
    🏷️ ade, agent-ide, ai-agents, claude-code, cli, codex, cursor-agent, devtools, ghostty, ide
    📝 Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile.

    README 摘要:
    Orca
    
      
      
      
      
      
      
    
      Español · 中文 · 日本語 · 한국어
    
      The AI Orchestrator for 100x builders.
      Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.
    
    Download Orca
    
      
    
    ## Features
    
    ### Mobile Companion
    
    Monitor and steer your agents from your phone — get notified when an agent finishes and send follow-ups from anywhere.
    
    iOS App Store · TestFlight · Android APK · Docs →
    
      
    
    ### Parallel Worktrees
    
    Fan one prompt across five agents, each in its own isolated git worktree — compare the results and merge the winner.
    
    Docs →
    
      
    
    ### Terminal Splits
    
    Ghostty-class terminals with WebGL rendering, infinite splits, and scrollback that survives restarts.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  mauriceboe/TREK
    ⭐ 7206 stars  |  🍴 634 forks  |  💻 TypeScript  |  📅 2026-03-19
    🔗 https://github.com/mauriceboe/TREK
    📡 来源: trending-daily
    🏷️ budget-tracker, collaborative, open-source, opensource, packing-list, poi, real-time, routes, self-hosted, travel
    📝 A self-hosted travel/trip planner with real-time collaboration, interactive maps, PWA support, SSO, budgets, packing lists, and more.

    README 摘要:
    A self-hosted, real-time collaborative travel planner — with maps, budgets, packing lists, a journal, and AI built in.
    
    &nbsp;
    
    &nbsp;
    
    &nbsp;
    
    &nbsp;
    
    ---
    
      
      
      
      
      
      
      
      
    
    ---
    
    ## What you get
    
      
      
    
    See all features
    
    #### 🧭 Trip planning
    
    - **Drag & drop planner** — organise places into day plans with reordering and cross-day moves
    - **Interactive map** — Leaflet or Mapbox GL with 3D buildings, terrain, photo markers, clustering, route visualization
    - **Place search** — Google Places (photos, ratings, hours) or OpenStreetMap (free, no API key)
    - **Place import** — shared Google Maps / Naver Maps lists, plus GPX and KML/KMZ/GeoJSON map files
    - **Day notes** — timestamped, icon-tagged notes with drag-and-drop reordering
    - **Route optimisation** — auto-sort places and export to Google Maps
    - **Weather forecasts** — 16-day via Open-Meteo (no key) + historical climate fallback
    - **Category filter** — show only matching pins on the map

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  kunchenguid/no-mistakes
    ⭐ 3125 stars  |  🍴 186 forks  |  💻 Go  |  📅 2026-04-05
    🔗 https://github.com/kunchenguid/no-mistakes
    📡 来源: trending-daily
    📝 git push no-mistakes

    README 摘要:
    git push no-mistakes
    
      
      
      
      
    
    Kill all the slop. Raise clean PR.
    
    English · 简体中文
    
      
    
    `no-mistakes` puts a local git proxy in front of your real remote.
    Push to `no-mistakes` instead of `origin`, and it spins up a disposable worktree, runs an AI-driven validation pipeline, forwards the branch to the configured push target only after every check passes, and opens a clean PR automatically.
    
    - **Non-blocking** - the pipeline runs in an isolated worktree without disrupting your work.
    - **Agent-agnostic** - `claude`, `codex`, `rovodev`, `opencode`, `pi`, or `acp:` via `acpx`.
    - **Agent-native** - `/no-mistakes` lets your coding agent do a task and gate it, or gate existing committed work: it runs the pipeline, has the pipeline apply safe fixes, and escalates the rest to you.
    - **Human stays in charge** - auto-fix or review findings, your call.
    - **Clean PRs by default** - push, open PR, watch CI, and auto-fix failures in one shot.
    
    Full documentation: 
    
    ## How it works
    
    ```
            your branch
                │  git push no-mistakes
                ▼
       ┌──────────────────────────────────────────────┐
       │  disposable worktree — your work stays put     │
       │  review → test → docs → lint → push → PR → CI  │
       └──────────────────────────────────────────────┘
                │  every check green
                ▼
            clean PR, opened for you
    ```
    
    Each step either passes on its own or stops with a **finding** for you to act on.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#14  zhongerxin/Cowart
    ⭐ 3027 stars  |  🍴 232 forks  |  💻 JavaScript  |  📅 2026-06-18
    🔗 https://github.com/zhongerxin/Cowart
    📡 来源: 🚀 两周800+星
    📝 无描述

    README 摘要:
    # Cowart
    
    Cowart 是一个面向 Codex 的本地无限画布插件。它基于 tldraw 提供可视化画布，用于构思、标注、生成图片和根据标注图迭代图片。画布运行在本地网页服务中，数据默认保存到当前用户项目的 `canvas/` 目录，而不是保存到插件仓库里。
    
    English README: README.en.md
    
    ## 功能
    
    - 在 Codex 中打开一个本地 tldraw 无限画布。
    - 在当前项目目录中持久化画布页面和图片资源。
    - 在画布中创建 AI image holder，并让 Codex 生成图片填入选中的 holder。
    - 上传或提供 Cowart 标注截图，让 Codex 根据标注生成干净的新图并放到原图旁边。
    - 通过 Cowart MCP 工具读取选择状态、插入图片，并保存到页面本地资源目录。
    
    ## 安装
    
    ### 让 Codex 自动安装
    
    把下面这段发给 Codex：
    
    ```text
    请从 https://github.com/zhongerxin/cowart.git 安装 Cowart Codex 插件。
    请 clone 仓库到 ~/plugins/cowart，确认 .codex-plugin/plugin.json 存在，
    把插件加入 personal marketplace，先运行 codex plugin marketplace add ~，
    再运行 codex plugin add cowart@personal。
    安装后请校验插件，并告诉我是否需要开启一个新对话来加载新技能和 MCP 工具。
    ```
    
    ### 手动安装
    
    推荐把插件 clone 到 Codex personal marketplace 默认会引用的位置：
    
    ```bash
    mkdir -p ~/plugins
    git clone https://github.com/zhongerxin/cowart.git ~/plugins/cowart
    cd ~/plugins/cowart
    npm install
    npm run build
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#15  interviewstreet/hiring-agent
    ⭐ 2851 stars  |  🍴 661 forks  |  💻 Python  |  📅 2025-07-29
    🔗 https://github.com/interviewstreet/hiring-agent
    📡 来源: trending-weekly
    📝 AI agent to evaluate and score resumes.

    README 摘要:
    # Hiring Agent
    
    Resume-to-Score pipeline that extracts structured data from PDFs, enriches with GitHub signals, and outputs a fair, explainable evaluation.
    
      
        
      
      
        
      
      
        
      
    
    ---
    
    ## Contents
    
    - Overview
    - Architecture
    - Installation and Setup
      - Prerequisites
      - Quick setup with pip
      - Ollama models
    - Configuration
    - How it works
    - CLI usage
    - Directory layout
    - Provider details
    - Contributing
    - License
    
    ---
    
    ## Overview
    
    Hiring Agent parses a resume PDF to Markdown, extracts sectioned JSON using a local or hosted LLM, augments the data with GitHub profile and repository signals, then produces an objective evaluation with category scores, evidence, bonus points, and deductions. You can run fully local with Ollama or use Google Gemini.
    
    ---
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#16  xbtlin/ai-berkshire
    ⭐ 2774 stars  |  🍴 400 forks  |  💻 Python  |  📅 2026-04-07
    🔗 https://github.com/xbtlin/ai-berkshire
    📡 来源: trending-daily
    🏷️ ai, ai-agent, anthropic, berkshire-hathaway, charlie-munger, china-stock, claude, claude-code, financial-analysis, fintech
    📝 AI 时代的伯克希尔：基于 Claude Code 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。| AI-era Berkshire: a value investing research framework   built on Claude Code. 4 masters' methodologies + multi-agent adversarial analysis.

    README 摘要:
    中文 | English
    
    # AI Berkshire - AI 时代的价值投资研究框架
    
    > "Price is what you pay, value is what you get." — Warren Buffett
    >
    > 用 AI 重新定义投资研究的深度与效率。
    
    **AI Berkshire** 是一套基于 Claude Code 的投资研究 Skill 合集，将巴菲特、芒格、段永平、李录四位价值投资大师的方法论系统化、结构化，通过 AI Agent 实现专业级投资研究。
    
    一个人 + Claude = 一个投研团队。
    
    ---
    
    ## Real Track Record
    
    > 不是纸上谈兵。这套框架背后是真金白银验证的投资体系。
    
    ### 2024 全年收益：+69.29%
    
    ### 2025 年至今收益：+66.38%
    
    ### 与主要指数对比
    
    | 指标 | 2024 全年 | 2025 至今 |
    |------|----------|----------|
    | **本框架实盘** | **+69.29%** | **+66.38%** |
    | 恒生指数 | +17.67% | +27.77% |
    | 标普500 | +23.31% | +16.39% |
    | 沪深300 | +14.68% | +17.66% |
    | 纳斯达克 | +28.64% | +20.36% |
    
    **2024 年超额收益**：跑赢标普500 **46个百分点**，跑赢恒生指数 **52个百分点**
    
    **2025 年超额收益**：跑赢标普500 **50个百分点**，跑赢恒生指数 **39个百分点**
    
    **两年累计实盘收益超 146万元**，连续两年大幅跑赢全球主要指数。
    
    > *免责声明：历史收益不代表未来表现。截图来自富途证券真实账户。*
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#17  vercel/eve
    ⭐ 2636 stars  |  🍴 199 forks  |  💻 TypeScript  |  📅 2026-06-16
    🔗 https://github.com/vercel/eve
    📡 来源: 🚀 两周800+星
    🏷️ agent, framework, harness, javascript, markdown, sandbox, typescript, vercel, workflows
    📝 The Framework for Building Agents

    README 摘要:
    eve
    
    eve is a filesystem-first framework for durable AI agents. Core agent capabilities live in
    conventional locations, so projects are easier to inspect, extend, and operate.
    
    ## The filesystem is the authoring interface
    
    A typical eve agent has this structure:
    
    ```text
    my-agent/
    └── agent/
        ├── agent.ts            # Optional: model and runtime config
        ├── instructions.md     # Required: the always-on system prompt
        ├── tools/              # Optional: typed functions the model can call
        │   └── get_weather.ts
        ├── skills/             # Optional: procedures loaded on demand
        │   └── plan_a_trip.md
        ├── channels/           # Optional: message channels (HTTP, Slack, Discord)
        │   └── slack.ts
        └── schedules/          # Optional: recurring cron jobs
            └── weekly_recap.ts
    ```
    
    Read the documentation for the full project layout and guides.
    
    ## Quick start
    
    ```bash
    npx eve@latest init my-agent
    ```
    
    This creates a new `my-agent` directory, installs its dependencies, initializes Git, and starts
    the interactive terminal UI.
    
    To add eve to an existing project, pass a path:
    
    ```bash
    cd myapp
    npx eve@latest init .

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#18  Waishnav/devspace
    ⭐ 2526 stars  |  🍴 260 forks  |  💻 TypeScript  |  📅 2026-06-14
    🔗 https://github.com/Waishnav/devspace
    📡 来源: 🚀 两周800+星
    📝 Turn ChatGPT into Codex and enjoy ChatGPT usage separately :)

    README 摘要:
    DevSpace
    
    Bring a Codex-style coding workflow to ChatGPT.
    
      
      
      
    
    **Give ChatGPT a secure connection to your own machine and Turn ChatGPT into Codex**
    
    DevSpace is a self-hosted MCP server that lets ChatGPT read, edit, search, and run code in your real local projects — your files, your tools, your terminal — without uploading anything to a third party. You run it on your machine, expose it through a tunnel you control, and approve the connection with a password only you have.
    
    ## Sponsors and Special Thanks
    
      
        
          Sponsor
          About
        
      
      
        
          
            
              
            
          
          
            The ads in your terminal pay you.
            Rebates adds one optional
            sponsored footer to your coding agent and pays you cash back for every
            session in which it is shown. Turn it off at any time.
          
        
      
    
      DevSpace is open to new sponsors.
      Get in touch to become one.
    
    ## Installation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#19  tamnd/kage
    ⭐ 2487 stars  |  🍴 83 forks  |  💻 Go  |  📅 2026-06-14
    🔗 https://github.com/tamnd/kage
    📡 来源: 🚀 两周800+星
    📝 Shadow any website for offline viewing, with the JavaScript stripped out

    README 摘要:
    # kage
    
    **kage** (影, "shadow") clones a website into a folder you can browse offline, with every script stripped out. It opens each page in real headless Chrome, waits for the page to settle, snapshots the DOM a human would have seen, then deletes all the JavaScript and pulls the CSS, images, and fonts down to local paths. What lands on disk looks like the live site and runs no code.
    
    Install • Quick start • Commands • Clone • Pack • Double-click app • Native window • How it works
    
    You already know the problem. You hit "Save As" on a page you want to keep, and six months later you open it to find a blank screen, a spinner that never stops, or a copy that still tries to phone home to an analytics server that no longer exists. The page was never really yours. It was a thin client for someone else's JavaScript.
    
    kage takes the other road. It drives a real browser, lets the page finish doing whatever it does, grabs the finished result, and then rips every script out of it. No tracking, no network calls, no surprises. Just `.html` files you can open straight off disk, hand to a friend, or pack into a single file and forget about for a decade.
    
    Full docs and guides live at **kage.tamnd.com**.
    
    ## Install
    
    ```bash
    go install github.com/tamnd/kage/cmd/kage@latest
    ```
    
    Prefer a prebuilt binary? Grab an archive, a `.deb`/`.rpm`/`.apk`, or a checksum from releases. Or let a package manager handle it:
    
    ```bash
    # Homebrew (macOS)
    brew install --cask tamnd/tap/kage
    
    # Scoop (Windows)
    scoop bucket add tamnd https://github.com/tamnd/scoop-bucket
    scoop install kage
    
    # apt (Debian, Ubuntu)
    curl -fsSL https://tamnd.github.io/linux-repo/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/tamnd.gpg
    echo "deb [signed-by=/usr/share/keyrings/tamnd.gpg] https://tamnd.github.io/linux-repo/apt stable main" | sudo tee /etc/apt/sources.list.d/tamnd.list
    sudo apt update && sudo apt install kage
    
    # dnf (Fedora, RHEL)
    sudo dnf config-manager --add-repo https://tamnd.github.io/linux-repo/dnf/tamnd.repo
    sudo dnf install kage
    ```
    
    Or skip installing Chrome yourself and use the container image, which bundles Chromium:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#20  BuilderIO/agent-native
    ⭐ 2385 stars  |  🍴 227 forks  |  💻 TypeScript  |  📅 2026-03-12
    🔗 https://github.com/BuilderIO/agent-native
    📡 来源: trending-weekly
    🏷️ agents, ai, react
    📝 A framework for building agent-native applications.

    README 摘要:
    # Agent-Native
    
    ## The framework for agent-native apps
    
    Agent-Native is an open-source framework for building robust agents that act inside real apps, not just chat next to them. It gives you primitives for product-grade agentic software: shared actions, SQL-backed state, identity, tools, skills, jobs, observability, and UI surfaces that all work together. Bring your own database, hosting provider, model stack, and app code.
    
    ```ts
    // One action powers UI, agent, HTTP, MCP, A2A, and CLI.
    export default defineAction({
      schema: z.object({
        emailId: z.string(),
        body: z.string(),
      }),
      run: async ({ emailId, body }) => {
        await db.insert(replies).values({ emailId, body });
      },
    });
    ```
    
    - **Actions**: Define work once. Use it from UI, agent, API, MCP, A2A, and CLI.
    - **Agent runtime**: Chat, tools, skills, memory, jobs, observability, and handoffs ship together.
    - **Backend agnostic**: Plug in any Drizzle-supported SQL database and Nitro-compatible host.
    
    ## Templates
    
    Start with a full featured template. Each one is a complete, 100% free and open-source SaaS app: cloneable, not scaffolded, except you own the code and can customize everything.
    
    **Clips**
    
    **Agent-Native Loom + Jam**
    
    Record your screen with auto-transcripts and captured browser debug logs, share a link, and let an agent read the transcript, see timestamped frames, and fix the bug.
    
    **Plans**
    
    **Visual plan mode for coding agents**
    
    Install `/visual-plan` and `/visual-recap` so your coding agent can plan before it builds and recap changes after they land. High-level code reviews with diagrams, wireframes, annotations, and review links.
    
    **Design**
