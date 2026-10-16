📊 开源日报 — 2026-10-16
共发现 9 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ⚠️风险  LibreSpark/LibreTV
    ⚠️ 命中风险词: cookie —— 默认归排除区，需人工确认
    ⭐ 18227 stars  |  🍴 28786 forks  |  💻 TypeScript  |  📅 2025-04-06
    🔗 https://github.com/LibreSpark/LibreTV
    📡 来源: trending-daily
    🏷️ css, film, html, movie-web-app, movies-and-cinemas, nextjs, tv
    📝 一分钟搭建影视站，支持Docker等部署方式

    README 摘要:
    # LibreTV
    
    LibreTV Next.js 迁移版：免费在线视频聚合搜索与观看平台。基于 Next.js 15（App Router）+ TypeScript + Tailwind CSS，播放内核为 ArtPlayer + hls.js，支持亮暗双主题。
    
    > 🏠 **官网**：LibreTV 官网
    >
    > 🌐 **演示站**：tv.bagiinlink.eu.org（访问密码：`libretv`）
    >
    > 📖 **完整文档**：文档首页 · 架构 · 部署 · 配置 · 数据源 · 直播 / IPTV · 首页推荐 · 播放器 · 代理与安全 · FAQ
    >
    
      
    
    ## 核心特性
    
    - **聚合搜索**：多采集站服务端并行搜索
    - **跨源同名聚合**：同名影片合并为一张卡片，展开即可比较和选择各来源
    - **HLS 播放**：ArtPlayer + hls.js，广告分片过滤、自动连播、倍速、快捷键、移动端长按 3 倍速
    - **直播 / IPTV**：M3U 订阅解析，`/live` 页面按分组浏览、搜索频道并站内播放（HLS + HTTP-FLV），支持 XMLTV 节目单（EPG）与频道收藏；直播流经专用长连接代理（`/api/live/stream`）转发
    - **进度同步**：播放进度与观看历史存于本机 IndexedDB，精确到秒的续播
    - **换源测速**：跨源搜索同名资源并测速排序，一键切换保留集数位置
    - **源测试与订阅**：一键探活点播源与直播源（支持批量测活）；搜索时自动记录各源健康度，连续失败的源按阶梯时长自动停用（30 分钟 → 24 小时 → 长期），可一键恢复；订阅远程源列表（一份 LibreTV-SourceList JSON 可同时下发点播源与直播源，也可直接填 TVBOX 配置地址，自动导入其中可直接使用的接口），可导出分享
    - **首页推荐**：豆瓣（电影/剧集分类浏览）、Bangumi 新番放送表或影视榜单（豆瓣周榜 + 百度热播，经 60s API），设置中切换；均服务端直连 + 缓存，Bangumi/榜单免 key 免配置（`60S_API_BASE` 可指向自部署 60s 实例）
    - **PWA**：可安装到桌面 / 主屏幕，亮暗双主题无首屏闪烁
    
    ## 部署
    
    ### Docker（推荐）
    
    ```bash
    # 在 .env 中设置 PASSWORD
    echo "PASSWORD=your-password" > .env
    
    # 方式一：拉取发布镜像（零构建）
    docker compose pull && docker compose up -d
    
    # 方式二：源码构建
    docker compose up -d --build
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  xerj-org/xerj
    ⭐ 5902 stars  |  🍴 319 forks  |  💻 Rust  |  📅 2026-06-30
    🔗 https://github.com/xerj-org/xerj
    📡 来源: trending-daily
    🏷️ ai-search, ai-search-algorithms, ai-search-engine, ai-search-free, ai-search-module, ai-search-optimization, ai-searchengine, bm25-search, elastic-search, elasticsearch
    📝 XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data without the token waste of grep and sed. One command indexes code, docs, logs and PDFs for search, RAG, security audits and agent memory, using 40x fewer tokens than grep. Elasticsearch compatible, so existing clients just work.

    README 摘要:
    # XERJ
    
    English | 简体中文
    
    XERJ is a community-trusted local AI search that indexes any folder automatically, so your
    coding agent stops burning tokens reading files one by one and pulls the exact code it
    needs instead. Reference coding is its main use case and the clearest win: point an agent
    at a task and it downloads the open-source repos closest to it, indexes them, and reuses
    how they solved the problem before writing its own code. In a controlled study that cut a
    coding agent's output tokens by 2.7x at the same 16/16 solve rate
    (case study), and people report
    roughly 5x in everyday work
    (field reports).
    It is enough for a smaller, cheaper model to out-code a pricier one working from memory,
    while you spend less time in fix loops. Try it now with a one-prompt install:
    
    ```text
    Install XERJ (docs: https://xerj.org/llms.txt), index this project's sources, and set up
    reference coding: clone and index the open-source repos closest to what we're building,
    and search how they solved a problem before writing code.
    ```
    
    Or run it yourself:
    
    ```sh
    curl -fsSL https://xerj.org/get | sh
    xerj --insecure --data-dir ./data &
    xerj init                                        # wire XERJ into Claude Code/Cursor (MCP + skill), one command
    xerj autoindex ~/my-project
    xerj search "how do we rotate the WAL segment"   # ranked passages, file:line
    xerj def "euler_to_rotationmatrix"               # go-to-definition: file:line + signature
    xerj gain                                        # what it did for you — counted, not estimated
    ```
    
    Windows and a hand-verified install are under Install by hand.
    
    That `--insecure` flag is a trust boundary, not a formality. It turns off TLS and API-key
    auth, so every caller that can reach the port is a superuser who can read and delete every
    index, including every `/_memory` namespace. It is meant for one user on a dev machine: a
    fresh node binds `127.0.0.1` only, and a cleartext bind on any other interface refuses to

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  lightseekorg/tokenspeed
    ⭐ 2555 stars  |  🍴 342 forks  |  💻 Python  |  📅 2026-05-06
    🔗 https://github.com/lightseekorg/tokenspeed
    📡 来源: trending-daily
    🏷️ b200, b300, blackwell, deepseek, gb200, gb300, glm, gpt-oss, inkling, kimi
    📝 TokenSpeed is a speed-of-light LLM inference engine.

    README 摘要:
    TokenSpeed is a speed-of-light LLM inference engine designed for **agentic workloads**, with TensorRT-LLM-level performance and vLLM-level usability. The goal is to be the most performant inference engine for production agentic workloads.
    
    Core components:
    
    - **Scheduler**: C++ control plane and Python execution plane. Request
      lifecycle, KV cache ownership, and overlap timing are encoded as a
      finite-state machine, with safe KV resource reuse enforced by the type system at compile time.
    - **Kernels**: pluggable, layered kernel system with a portable public API and
      a centralized registry including one of the fastest **MLA**
      (Multi-head Latent Attention) implementations on Blackwell for agentic workloads.
    - **Entrypoint**: SMG-integrated AsyncLLM for low-overhead CPU-side request
      handling.
    
    ## Differentiation
    
    TokenSpeed takes a fundamentally different architectural approach from existing LLM inference engines. The **PyTorch Foundation highlighted these architectural differentiators** when welcoming TokenSpeed to the PyTorch Ecosystem Landscape:
    
    > TokenSpeed is an open source LLM inference engine and the first to separate the control plane from the execution plane. The control plane is implemented in C++ as a finite-state machine, using the type system to enforce safe resource management, including request lifecycles and KV cache state, at compile time rather than runtime. The execution plane is implemented in Python, enabling fast iteration and lowering the cognitive load for researchers and engineers. This architecture combines strong correctness guarantees in the core scheduling system with the development velocity of a high-level execution layer.
    >
    > TokenSpeed also treats kernels as a first-class, modular subsystem, separating them from the core engine through a portable public API, centralized registry and selection model, and an extensible plugin mechanism for heterogeneous accelerators.
    
    More importantly, TokenSpeed is the **Switzerland** of open-source LLM inference engines: neutral because it's backed by the non-profit LightSeek Foundation rather than a commercial company, with **serious hardware and engineering support** from vendors like NVIDIA and AMD.
    
    ## News
    
    - [2026/10] 🔥 TokenSpeed MLA 2 for NVIDIA Vera Rubin. [blog]
    - [2026/10] 🔥 685 tokens/s per user: serving Qwen3.8-Flash-Next on NVIDIA GB300 with TokenSpeed. [blog]
    - [2026/10] 🔥 Advancing Kimi K3 inference on AMD Instinct MI355X GPUs with TokenSpeed. [AMD blog]
    - [2026/09

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Kav-K/GPTDiscord
    ⭐ 1851 stars  |  🍴 288 forks  |  💻 Python  |  📅 2022-12-08
    🔗 https://github.com/Kav-K/GPTDiscord
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | AI image generation
    🏷️ artificial-intelligence, asyncio, chatbot, code-interpreter, collaborate, dalle2, digitalocean, discord, embeddings, extractive-question-answering
    📝 A robust, all-in-one GPT interface for Discord. ChatGPT-style conversations, image generation, AI-moderation, custom indexes/knowledgebase, youtube summarizer, and more!

    README 摘要:
    # GPTDiscord
    
    OpenAI chat, vision, image generation, transcription, moderation, and web search in Discord. Python **3.11–3.13** is supported.
    
    ## Current API support
    
    - `/gpt ask` and `/gpt converse` use current Chat Completions models, including vision and reasoning models. Defaults and model limits are centralized; incompatible sampling options are omitted for reasoning models.
    - `/web` uses the **Responses API with native web search** and visible source links for recent information. It needs an OpenAI key with access to the chosen model and web search, with no Google account required. Search tool calls incur additional OpenAI charges.
    - `/dalle draw` keeps the familiar command name and generates images with the current **GPT Image** API. Image bytes are sent as Discord attachments. Retired DALL·E endpoints are no longer used.
    - Transcription and moderation use current OpenAI APIs. Long conversations, per-user keys, server roles, prompt optimization, and saved conversations remain available.
    - Document indexing, Google/Wolfram chat, Pinecone memory, Replicate, and E2B code execution are optional integrations with separate dependencies.
    
    The default chat model is `gpt-6.1-sol`, the low-cost helper model is `gpt-6-luna`, and image generation defaults to `gpt-image-2.5-flare`. Availability depends on your OpenAI project. Override models using the environment settings below. Model names and prices change; consult the OpenAI model catalog and pricing.
    
    ## Run from source
    
    ```bash
    git clone https://github.com/Kav-K/GPTDiscord.git
    cd GPTDiscord
    python3.13 -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install .
    cp sample.env .env
    # Edit .env with your credentials and Discord server ID.
    python gpt3discord.py
    ```
    
    Install FFmpeg with your operating system's package manager to transcribe downloaded media. The basic bot does not require Torch, Transformers, LlamaIndex, or LangChain.
    
    The same code installs as the `gpt3discord` console command. Prompt files and conversation openers ship in the wheel; you can run the installed bot outside the source directory.
    
    ### Required configuration
    
    | Setting | Purpose |
    | --- | --- |
    | `OPENAI_API_KEY` | OpenAI project API key. `OPENAI_TOKEN` remains a supported alias. ChatGPT subscriptions do not include API billing. |
    | `DISCORD_TOKEN` | Bot token from the Discord Developer Portal. |
    | `ALLOWED_GUILDS` | Comma-separated Discord server IDs where com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ahwootech/BRUTAL
    ⭐ 1254 stars  |  🍴 63 forks  |  💻 C#  |  📅 2026-10-14
    🔗 https://github.com/ahwootech/BRUTAL
    📡 来源: 🚀 5天300+星
    📝 A free, open source C# framework for making games, or your own game engine. Direct access to native APIs and Vulkan, with the low-level libraries around them. The foundation under Kitten Space Agency and RimWorld's Waylith engine.

    README 摘要:
    # BRUTAL Framework
    
    **A free, open source C# framework for making games, or your own game engine.**
    
    BRUTAL is a framework. You can make a game directly with it, or use it as the foundation for a separate engine. We made Kitten Space Agency directly on BRUTAL. Ludeon built their Waylith engine on it to move RimWorld off Unity.
    
    At its core is a custom interop layer giving C# direct access to native APIs and libraries. Around that we've built mathematics, memory management, strings, collections, job scheduling, logging, localization, and bindings for Vulkan, GLFW, Dear ImGui, FMOD, RakNet, Jolt and Box2D. BRUTAL doesn't make the architectural decisions for you. You write your own stack. You can use whatever NuGet packages you want, including third-party ones.
    
    It's called BRUTAL for a reason. In some ways it's much harder to use than Unity, Unreal or Godot. In other ways, particularly if you're doing something unusual, it's considerably easier. You actually have to know what you want to do first.
    
    ## Why
    
    You are only as independent as your tools are.
    
    Developers have surrendered an extraordinary amount of control over their work to companies whose interests are not necessarily aligned with their own. We're not suggesting everyone should make their own game engine. We're suggesting every developer should have the option to, without having to spend four years building the foundations first.
    
    What that means in practice:
    
    - **Free, including for commercial games.** No royalties. We don't want a percentage of your game's revenue. We ask for credit.
    - **Open source.** The source is here under an MIT-based licence. If one day we stop being accountable to developers, you can fork it and go your own way.
    - **Deliberately small.** We do a few low-level things well: interop, memory, concurrency, maths, strings, and bindings to native libraries, on the latest C# and Vulkan. We avoid allocations and unnecessary overhead and use unmanaged memory and unsafe code where it makes sense.
    - **A foundation, like a kernel.** Think of the Linux kernel and something like Ubuntu. It's not an exact comparison, but it gets the idea across. We provide the foundation and you build your own systems on top.
    
    ### What BRUTAL is not
    
    BRUTAL is not trying to be a general-purpose engine. There is no editor, no scene graph and no renderer, and we're not adding them. We push back on efforts to add more, because adding everything is how the industry ended up with the kind of

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  chenglou/handwired
    ⭐ 1195 stars  |  🍴 88 forks  |  💻 TypeScript  |  📅 2026-10-15
    🔗 https://github.com/chenglou/handwired
    📡 来源: 🚀 5天300+星
    📝 Turn your regular JavaScript code into a neural net.

    README 摘要:
    # Handwired
    
    Turn your regular JavaScript code into a neural net; no training, exact, yet also fully differentiable!
    
    ## How It Works
    
    A program's made of if-else, loops, and state. Handwired transforms them into matrix multiplication + reglu over floats. For example:
    
    ```ts
    const a = 5
    const result = (a > 4) ? 10 : 12
    ```
    
    The above can be expressed as basic arithmetic:
    
    ```ts
    const a = 5
    // Math.max(0, x) is ReLU. For an integer a, above4 is 1 if a > 4, and 0 otherwise
    const above4 = Math.max(0, a - 4) - Math.max(0, a - 5)
    // Both branches compute, and above4 picks one
    const result = above4 * 10 + (1 - above4) * 12
    ```
    
    You can calculate that by hand and see that both arrive at the same result.
    
    We then collect the + and * and relu into a giant matmul, and either run it on JS or WebGPU, for fun.
    
    Because we basically only use these 2 primitives:
    - the full program stays differentiable
    - the weights don't need training since they're written manually
    - existing gpu techniques, such as fusion, sparsity, reordering, have a great time optimizing such minimal primitives
    
    This unlocks lots of funny use-cases, like:
    - unfreezing the weights and train them (what does that even do? Let's find out!)
    - attaching a specific frozen program to a generic neural net and train end-to-end (now a nanoGPT can do both Shakespeare and your particular UI?)
    - achieving GPU-level of parallelism with JS code that was written in a traditional single-threaded way (see the JSON search demo that runs in milliseconds over 100k documents)
    
    ## Play With It
    
    Try the demos live: https://chenglou.me/handwired/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  feder-cr/open_scion
    ⭐ 896 stars  |  🍴 107 forks  |  💻 Go  |  📅 2026-10-15
    🔗 https://github.com/feder-cr/open_scion
    📡 来源: 🚀 5天300+星
    🏷️ ai-agents, coding-agents, git, golang, scion, version-control
    📝 Open-source version of Scion: version control built for coding agents.

    README 摘要:
    # open_scion
    
    **Source control for the age of coding agents.**
    
    Anthropic built **Scion**, a faster version control system for coding agents,
    and described it in
    Redesigning source control:
    a server-centric system built for hundreds of agents that read, write and land
    code at the same time. Scion is internal to Anthropic and is not available to
    the public.
    
    So I built **open_scion**: an open-source version of that design that anyone can
    run, and that the community can improve and maintain together.
    
    MIT licensed. Vendor neutral: the server never calls a language model, and every
    AI feature works with any provider, or none.
    
    open_scion is an independent implementation of the publicly described design. It is not affiliated with or endorsed by Anthropic.
    
    ---
    
    ## Why
    
    Classic Git hosting was built for humans who clone a repository, work for hours
    and push once. Coding agents work differently: thousands of short-lived tasks,
    each touching a few files, each wanting to land in seconds, all on the same
    branches. Full clones, merge queues and client-side history walks become the
    bottleneck.
    
    Scion's answer is to move the work to the server: clients stay online and fetch
    only what they need, history questions are answered (and cached) by the server,
    changes land through a compare-and-swap instead of a queue, every update is an
    entry in a changeset log, and the repository state lives in a consistent
    database plus object storage so servers scale out. open_scion implements these
    ideas, with normal Git repositories underneath.
    
    ## The Scion ideas, implemented
    
    | Scion idea | In open_scion |
    |---|---|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  outcrawlai/scout
    ⭐ 845 stars  |  🍴 26 forks  |  💻 TypeScript  |  📅 2026-10-13
    🔗 https://github.com/outcrawlai/scout
    📡 来源: 🚀 5天300+星
    🏷️ ai-agent, browser-agent, browser-automation, cdp, llm, typescript, web-automation
    📝 Scout: the open-source browser agent, by Outcrawl. Mirrored automatically from Outcrawl's own repository.

    README 摘要:
    Quickstart
      &nbsp;·&nbsp;
      Examples
      &nbsp;·&nbsp;
      Models
      &nbsp;·&nbsp;
      Cloud
      &nbsp;·&nbsp;
      Docs
    
      
      
      
    
    # Tell it the task. It opens a browser and gets it done.
    
    Scout is an open-source agent that uses a real browser to finish a task for you. Describe what you need in plain words. Scout reads the page, clicks, types and scrolls until the job is done, then hands back the answer. If it cannot finish, it tells you what is missing and returns what it found.
    
    **Scout runs best on Outcrawl's cloud.** One line gives it a browser that sites treat like anyone at home, with captcha solving and a replay of every run. It also runs on your own machine.
    
      
      
      
    
    A recorded run on Outcrawl's cloud, 13 October 2026, shown at 6x speed with nothing cut.
    
    ## Start in three steps
    
    **1. Install Scout.** You need Node 22 or later. On the cloud there is no browser to install.
    
    ```sh
    npm i @outcrawl/scout
    ```
    
    **2. Add your keys.** An Outcrawl key for the browser (get one free at outcrawl.ai: 1,000 credits every month, no card needed) and a key for your model. Scout works with any AI model service that speaks the standard chat completions API, including a model running on your own computer:
    
    ```sh
    export OUTCRAWL_API_KEY=your-outcrawl-key
    export SCOUT_BASE_URL=https://your-endpoint/v1
    export SCOUT_API_KEY=your-model-key

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  Caho1/open-claude-ui
    ⭐ 819 stars  |  🍴 193 forks  |  💻 TypeScript  |  📅 2026-10-14
    🔗 https://github.com/Caho1/open-claude-ui
    📡 来源: 🚀 5天300+星
    🏷️ anthropic, audioworklet, claude, design-system, framer-motion, motion-physics, react, reverse-engineering, tailwindcss, ui-components
    📝 基于 REA 深度拆解并高保真还原 Claude 官方桌面端 UI。纯手写 30 个独立 React 组件与 8 项硬核交互物理算法，附带 3000+ 行逆向分析手册。

    README 摘要:
    # Open Claude UI (`open-claude-ui`)
    
      
    
      基于 REA 深度拆解，高保真生产级还原 Claude 设计系统 (CDS) 与工程交互物理学。
    
      简体中文 · English
    
      
      
      
      
      
      
      
    
    ---
    
    ## 📖 简介 (Introduction)
    
    `open-claude-ui` 是基于对现代桌面端 AI 客户端进行深度拆解与逆向分析构建的高保真开源 UI 组件库与动效引擎。
    
    整个逆向推导、反混淆静态分析与 ASAR 资源解构，均依托于先进的多平台逆向工程框架 **REA (Reverse Engineer Anything)** 完成——通过 REA 的静态 AST 解析、闭包代码反混淆与运行时跟踪能力，穿透生产级压缩包，精准还原了底层工程物理常数与数学模型。
    
    不同于市面上常见的盲猜或近似复刻，本项目所有组件规范、物理阻尼常数、着色器关键帧及音频管道均**严格依据真实前端架构反编译验证**提炼而成：
    * **温润的人文质感 (Editorial Warmth)**：纯正陶土橙（Clay `#d97757`）、4 层微对比表面阶梯（Surface 0-3）与视网膜高分屏发丝细边补偿（Hairline Ring）；
    * **严苛的交互物理学 (Interaction Physics)**：4 套生产级物理弹簧参数调校、4px 指针移动死区、CJK 输入法合成守卫、7 档渐隐非线性 Alpha 遮罩；
    * **高阶视听与系统架构 (Audiovisual & Architecture)**：基于原生 Web Audio API 的零延迟合成提示音、以光标为锚点的画廊跑道平移缩放、macOS 桌面毛玻璃透明融合与 Cowork 多代理协同拓扑。
    
    > ⚖️ **版权与合规声明 (DMCA & Assets Policy)**：  
    > 本开源项目**不公开分发任何专有二进制资产**（包括商业字体 `.ttf` 与录音 `.mp3`）。本项目提供原生系统级字体回退栈与 Web Audio API 纯代码合成音效，完全自包含、合规安全。详情参见 assets/README.md。
    
    ---
    
    ## 🌟 核心特性 (Key Features)
    
    ```mermaid
    graph TD
        OCUI["open-claude-ui"]
        
