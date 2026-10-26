📊 开源日报 — 2026-10-26
共发现 14 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  coollabsio/coolify
    ⭐ 64614 stars  |  🍴 5804 forks  |  💻 PHP  |  📅 2021-01-25
    🔗 https://github.com/coollabsio/coolify
    📡 来源: trending-daily
    🏷️ coolify, databases, deployment, docker, docker-compose, inertiajs, laravel, mariadb, mysql, nextjs
    📝 An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stack applications and 360+ one-click services on your own servers.

    README 摘要:
    # Coolify
    
    **An open-source platform to deploy applications, databases, and services on your own servers.**
    
    Open source & free forever, backed by our philosophy.
    
    !Latest Release Version
    
    Website · Documentation · Cloud · Discord · Community
    
    ## What is Coolify?
    
    Coolify is an open-source and self-hostable alternative to Heroku, Netlify, and Vercel. It helps you manage servers, applications, and databases on your own hardware. You only need an SSH connection.
    
    You can use a VPS, a bare-metal server, a Raspberry Pi, or any other server that accepts SSH connections. Coolify gives you the convenience of a cloud platform while you keep control of your infrastructure.
    
    Your configurations stay on your servers. If you stop using Coolify, your running resources continue to work and remain manageable.
    
    ## What can Coolify do?
    
    - **Deploy any application:** Build from GitHub, GitLab, Bitbucket, or Gitea with Nixpacks, Railpack, Dockerfile, Docker Compose, or a prebuilt Docker image.
    - **Run databases and services:** Deploy managed databases and more than 360 one-click services with persistent storage and generated credentials.
    - **Automate deployments:** Deploy on every Git push, create pull-request previews, call deployment webhooks, and roll back to retained application images.
    - **Manage networking:** Configure custom domains, automatic HTTPS certificates, reverse proxies, health checks, and container networks.
    - **Operate your infrastructure:** Manage multiple servers, inspect deployment and runtime logs, open container terminals, and monitor resource status.
    - **Protect your workloads:** Configure database and storage backups, scheduled tasks, environment variables, secrets, and notifications.
    - **Integrate with your workflow:** Manage resources through the dashboard, API, CLI, MCP, and team-based access controls.
    
    ## Quick start
    
    Install Coolify on a supported server with one command:
    
    ```bash
    curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
    ```
    
    Read the installation guide for requirements and detailed instructions. You can also review the installation script before you run it.
    
    ## Self-hosted or Cloud
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  AgriciDaniel/claude-seo
    ⭐ 21224 stars  |  🍴 2971 forks  |  💻 Python  |  📅 2026-02-07
    🔗 https://github.com/AgriciDaniel/claude-seo
    📡 来源: trending-daily
    🏷️ ai, ai-seo, claude-code, claude-code-skill, marketing-automation, open-source, seo
    📝 Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data.

    README 摘要:
    Claude SEO
    
      Free, open-source SEO audits inside Claude Code.
      Rank higher in Google and get cited by AI search.
    
      Install ·
      Demo ·
      Results ·
      Team ·
      Commands ·
      Pricing ·
      FAQ
    
      
      
      
      
      
      
      
    
      
    
    **Claude SEO is a free SEO plugin for Claude Code.** Give it any website and it runs a full SEO audit in 10 to 15 minutes, then hands you a clear action plan, sorted by what matters most.
    
    It checks everything a good SEO consultant would:
    
    - **Technical SEO.** Crawlability, indexing, sitemaps, robots.txt, redirects, page speed and Core Web Vitals.
    - **Content quality.** E-E-A-T (experience, expertise, authority and trust), thin pages and topic coverage.
    - **Structured data.** Finds, validates and writes Schema.org markup for rich results.
    - **AI search (GEO).** How likely Google AI Overviews, AI Mode, ChatGPT, Perplexity and Gemini are to cite your pages.
    - **Local and e-commerce SEO.** Google Business Profile, reviews, map pack, product pages and international sites.
    
    Claude SEO is built from 26 sub-skills and 19 specialist agents, and up to 17 agents work on your site at the same time. Every recommendation explains why it matters and how you will know it worked.
    
    ## See it in action
    
    Type `/seo` in Claude Code to see every command:
    
    Run a full audit and watch the agents fan out across the site:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  seedds/nxnative
    ⭐ 4565 stars  |  🍴 799 forks  |  💻 Objective-C  |  📅 2026-10-13
    🔗 https://github.com/seedds/nxnative
    📡 来源: 🚀 两周800+星
    📝 Switch games running natively on iPhone, iPad and Mac: an NSP folder becomes an unsigned IPA (NSO rewriter, Horizon HLE host, NVN→Metal)

    README 摘要:
    # nxnative
    
    Play your own Nintendo Switch games natively on iPhone and iPad. Bring your game (its NSP files) and your `prod.keys`; one script turns them into an IPA that you sideload.
    
    It is not an emulator: the game's own code runs directly on the Apple chip, with Switch graphics rebuilt on Metal. Nothing from any game is in this repository, and the project is not affiliated with Nintendo or any game publisher.
    
    ## Acknowledgements
    
    This project is built on other people's work:
    
    - **d2r-mobile** (MIT) developed this native-execution approach, for Diablo II: Resurrected. nxnative started as a copy of its generic parts: the NSO rewriter, the host that stands in for Horizon, the NVN-on-Metal layer and the iOS app shell. Fixes go both ways.
    - **Ryujinx** (MIT): its shader translator (`Ryujinx.Graphics.Shader`, `Ryujinx.Common` and `Spv.Generator` 1.3.2, in `dm/third_party/ryujinx` with a few fixes listed in its README) turns the games' Maxwell shaders into SPIR-V. Its emulation of the kernel and system services is also a reference when the host's behaviour is in doubt.
    - **Atmosphère**: its kernel, mesosphère, is the reference for Horizon's synchronization semantics (address arbiter, condition variables).
    - **yuzu**: Maxwell instruction encodings for the shader reference tool, and a cross-check for kernel behaviour.
    - **LibHac**: reads NSPs and layers updates over the base game in `dm/tools/nx_extract`. **hactool** did the first extractions.
    - **SPIRV-Cross**: SPIR-V to Metal Shading Language. **glslang** compiles the GLSL of OpenGL games to SPIR-V for it.
    - **deko3d** (zlib): its texture layout size algorithm is ported in `dm/gfx/nvn/nvn_tex.c`.
    - **libvpx** (VP9 movies), **stb_vorbis** (movie sound), the **Vulkan headers** and **NVIDIA FLIP** ship in `dm/third_party` with their licenses (list).
    - **Capstone**, **lz4**, **fontTools** and **XcodeGen** are used by the build.
    
    ## Games
    
    Games tested on Mac or iPhone. See the per-game notes for tested platforms, progress and known issues:
    
    Needs iOS / iPadOS 26 or later on an iPhone 15 Pro or newer (A17 Pro chip or later) or an iPad with an M1 chip or later: the games' textures are BC-compressed, and older iPhones can't read that format. Other games aren't supported yet. For them the script writes a survey and still tries its best to pack an IPA, guessing the game's settings; such an IPA may not start.
    
    Under each game: the IPA's size, and "60 fps with 1.2.0" where the game runs at 60 fps (30 on the Switch) with

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  JetBrains/thinkrail
    ⭐ 2021 stars  |  🍴 112 forks  |  💻 TypeScript  |  📅 2026-07-08
    🔗 https://github.com/JetBrains/thinkrail
    📡 来源: trending-daily
    🏷️ agent, agent-skills, agentic-ai, agentic-workflow, ai-coding, ai-tools, pi-agent, pi-agent-extension, spec-driven, spec-driven-coding
    📝 Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need

    README 摘要:
    # ThinkRail
    
    ThinkRail is the agentic IDE that gets better every time you use it — learning your project through
    living specs today, and building its own capabilities tomorrow.
    
    We built a rich interface around the `pi`
    coding agent, isolated work into separate workspaces, and gave the agent durable project knowledge
    through living specs and reusable skills. Next, we're adding full extension support, so ThinkRail can
    create the tools it needs based on how you actually work.
    
    **Website:** thinkrail.ai · **Blog:** thinkrail.ai/blog
    
    ⭐ If you find ThinkRail useful, give it a star — it helps others discover it.
    
      
      
    
    *A `pi` session and the change it made, scoped to an isolated git-worktree workspace.*
    
    ## What you get
    
    - **Isolated workspaces.** Open any git repo as a project and cut workspaces from it as `git worktree`s,
      each with its own branch and working directory. Agents work in parallel without touching your
      checkout; merge the good branch, delete the rest. You can also attach existing worktrees or explicitly
      work in the project folder itself. Finished and dormant workspaces settle onto a per-project shelf on
      their own — when their pull request merges or closes, or after a quiet week — and come back the moment
      you work in them. The topbar shows where the active branch stands against `origin` and its pull request,
      with the next step one click away: publish, push, or open a PR described from the plan, the commits,
      your PR template, or an agent-written draft. Once a GitHub PR is open it shows the CI checks and review
      decision, and lets you mark it ready, hand failing checks or a diverged branch to the agent, merge it
      with the repository's last-used method, reopen it, or delete the remote branch.
    - **A real IDE around the agent.** A splittable workbench of Monaco editor tabs, a Files tree with live git
      change marks and a Changed view, terminals, and documents — all scoped to the active workspace. Leave
      anchored review comments on files and diffs and send them to a chat as structured context, or open the
      worktree in your installed IDE.
    - **Chats that stream like the engine thinks.** Several concurrent `pi` sessions per workspace, each with
      its own model and live token and cost readout. Steer a running turn or queue a follow-up, delegate to
      subagents, and work a shared plan the agent updates and you edit — each completed step can be committed
      and reviewed on its own.
    - **Specs as ground truth.** A connected graph of `SPEC.md` f

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  rddmwmddr/android-ad-cleaner
    ⭐ 1097 stars  |  🍴 88 forks  |  💻 Python  |  📅 2026-10-24
    🔗 https://github.com/rddmwmddr/android-ad-cleaner
    📡 来源: 🚀 5天300+星
    🏷️ adb, ai-agent, android, coloros, debloat, hyperos, magicos, originos
    📝 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

    README 摘要:
    # 手机去广告
    
    关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。
    
    介绍页：**https://rddmwmddr.github.io/android-ad-cleaner/**
    
    ## 下载桌面客户端
    
    插上手机，点几下按钮。不需要 Python，也不需要 AI 工具。
    
    > **v0.2.3 · 2026-10-25**：处理读屏服务 `already registered` 冲突：退出前释放本次服务，同机任务互斥，短暂冲突只重试一次；持续占用时给出恢复步骤并跳过后续读屏任务。收尾不再误报全部完成。保留通知扫描、完整诊断及此前修复。旧版不会自动更新，请重新下载，已有备份会保留。详见 更新记录。
    
    > **最新源码补充（尚未进入 0.2.3 安装包）**：新增一加 Ace 2 Pro / ColorOS 14 的实测与有限适配，修复独立通知设置页识别、混合付款通知排除和应用启动后退出到上一应用的保护。范围与未完成项见 一加旧系统实测。
    
    > **2026-10-26 源码更新（未发布安装包）**：读屏失败时提示排查 GKD、自动记账等自动化 / 无障碍功能；找机位功能通知加入保护，旧清单也不能再次误关。排查和误关恢复见专项说明。
    
    此前版本已处理 Windows 本地页面超时、荣耀截图越界、通知渠道误操作风险、vivo 快应用与备份问题。各 Issue 的处理范围和待验证项见 社区问题处理记录。仅支持通过 adb 连接的安卓设备，暂不支持使用 HDC 的原生鸿蒙。
    
    | 电脑 | 下载 | 说明 |
    |---|---|---|
    | Mac · Apple 芯片（M1 及以后） | AndroidAdCleaner-0.2.3-mac-arm64.dmg | 已签名、通过苹果公证，双击就能打开 |
    | Mac · Intel 芯片 | AndroidAdCleaner-0.2.3-mac-intel.dmg | 同上 |
    | Windows 10 / 11 · 安装版 | AndroidAdCleaner-0.2.3-windows-setup.exe | 弹「Windows 已保护你的电脑」时点「更多信息」→「仍要运行」 |
    | Windows 10 / 11 · 免安装 | AndroidAdCleaner-0.2.3-windows-portable.zip | 解压后双击 `AndroidAdCleaner.exe` |
    
    不知道 Mac 是哪种芯片：左上角苹果图标 → 关于本机，「芯片」写 Apple M 开头的选 Apple 芯片。所有版本：Releases。用法：docs/08-桌面客户端.md。
    
    | | |
    |---|---|
    | **1 连接手机**：插线即认出手机，内置开启 USB 调试的图文教程 | **2 检测**：型号、系统版本、机型脚本、快应用、广告组件 |
    | **3 选择要关的**：营销通知按渠道勾选，服务类默认不勾 | **4 执行**：进度条和实时日志 |
    | **5 完成**：每一步的结果，最后提醒关闭开发者模式 | **反馈**：自动附诊断信息，一键提交 GitHub Issue |
    
    ---
    
    - 不 root，不解锁，不刷机，系统更新不受影响。
    - 只拨系统和 App 自带的开关。挂起广告包这一步要机主点头，一条命令可以还原。
    - 搜索、负一屏卡片、应用商店的安装和更新、天气预警、快递提醒，这些功能保留。
    
    改之前：OPPO 软件商店首页。轮播图、必备、必玩、福利标签，全是推广位。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  ⚠️风险  assetnote/php2shell-scanner
    ⚠️ 命中风险词: cookie —— 默认归排除区，需人工确认
    ⭐ 908 stars  |  🍴 133 forks  |  💻 Python  |  📅 2026-10-22
    🔗 https://github.com/assetnote/php2shell-scanner
    📡 来源: 🚀 5天300+星
    📝 High fidelity scanner for php2shell (CVE-2026-109618 and CVE-2026-109619)

    README 摘要:
    # php2shell-scanner
    
    A command-line tool for detecting CVE-2026-109618 and CVE-2026-109619 in PHP applications.
    
    ## How It Works
    
    The scanner sends a minimal multipart control request followed by up to three crafted multipart probes. The probes use PHP array keys nested 62 levels deep and increase from 1 MiB to 20 MiB, matching the detection logic used by Assetnote's internal scanner.
    
    A target is reported vulnerable when the probe produces a PHP memory-exhaustion error, a differential empty HTTP 500, a PHP-FPM worker failure, or an advertised PHP version known to be unpatched. Initial 5xx responses, common request-rejection statuses, and nonempty HTTP 500 responses without the PHP fatal-error signature are not treated as crash signals.
    
    The scanner tests `/index.php` by default. A path supplied in the URL is preserved, and `--path` or `--path-file` can test custom paths. phpMyAdmin targets are automatically retested at `/show_config_errors.php`. Redirects are not followed unless `--follow-redirects` is set.
    
    ### SAPI Modes
    
    The default `--sapi auto` mode applies both mod_php and PHP-FPM verdict rules, matching the combined behavior of Assetnote's postmodules. Use `--sapi mod_php` or `--sapi fpm` to restrict detection to a known SAPI.
    
    ### Network Impact
    
    Each tested path may receive a 42-byte control request and three probes totalling about 29 MiB. Probing stops as soon as the verdict is settled, and duplicate input URLs are scanned once.
    
    ## Requirements
    
    - Python 3.9+
    - h11
    - tqdm
    
    ## Installation
    
    ```
    pip install -r requirements.txt
    ```
    
    ### Docker
    
    Build the image:
    
    ```
    docker build -t php2shell-scanner .
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  designfuchen/word-atlas
    ⭐ 900 stars  |  🍴 231 forks  |  💻 TypeScript  |  📅 2026-10-25
    🔗 https://github.com/designfuchen/word-atlas
    📡 来源: 🚀 5天300+星
    🏷️ chinese, dataset, english-learning, flashcards, fsrs, ielts, language-learning, pwa, react, spaced-repetition
    📝 词光 · 一词一画，点亮雅思 — 7,298 IELTS words, each with an original illustration, UK/US audio, 14,596 example sentences and FSRS review. Free, open source, no login. Dataset CC BY 4.0.

    README 摘要:
    # 词光 · Word Atlas
    
    **一词一画，点亮雅思。**
    
    7,298 个雅思核心词，每个词一幅原创插画、两条原创例句、英美发音和一套刚刚好的复习节奏。
    免费，开源，无需注册，打开网页就能背。
    
    **打开词光 →** &nbsp;·&nbsp; ▶ 看宣传片 &nbsp;·&nbsp; 下载词库 &nbsp;·&nbsp; **在 X 关注更新 →** &nbsp;·&nbsp; English
    
          
    
    每本单词书都从 abandon 开始，也停在 abandon。▶ 点击画面看 48 秒完整宣传片（有声音）
    
    ---
    
    ## 为什么做词光
    
    背单词最难的不是“看过”，而是“想得起来”。
    
    纸质单词书把 7,000 个词排成一张清单，大多数人翻到第一页就停下了。词光换了个做法：给每个词一幅画，让你先**看见**它；用主动回忆让你**想起**它；再用 FSRS 算法在你快要忘记的时候让你和它**重逢**。你学会的每一个词，都会在自己的词汇星图上点亮一颗星。
    
    这是一个个人项目。所有释义、例句、插画和录音都是为这个项目新做的，制作成本由作者自己承担，然后全部开源，任何人都可以免费使用、修改和再分发。
    
    ## 一眼看懂
    
    | 数量 | 内容 |
    |---:|---|
    | **7,298** | 雅思核心词条，CEFR A1–C2 分级，19 个雅思高频话题 |
    | **7,298** | 幅原创插画，统一的复古图鉴画风，画的就是例句里的场景 |
    | **14,596** | 条原创例句：一条日常短句帮你记住，一条雅思语境长句帮你会用 |
    | **22,905** | 段录音：英音、美音单词发音，以及例句朗读 |
    | **0** | 账号、广告、追踪。进度只保存在你自己的设备上 |
    
    ## 看一看，听一听
    
    7,298 幅插画、22,905 段录音、24 段界面声音，都是为词光专门做的。下面是一小部分。
    
    ### 🖼 每个词一幅画
    
    画面讲的就是例句里的那件事，同一种复古图鉴画风贯穿全部 7,298 个词。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  morganlinton/BeautifulRust
    ⭐ 855 stars  |  🍴 40 forks  |  💻 Python  |  📅 2026-10-23
    🔗 https://github.com/morganlinton/BeautifulRust
    📡 来源: 🚀 5天300+星
    🏷️ claude-code, claude-plugin, claude-skills, coding-agent, rust, style-guide
    📝 A Claude Code plugin that teaches Claude to write idiomatic, robust Rust

    README 摘要:
    # Beautiful Rust
    
    Three standard Agent Skills and a lints config that teach coding
    agents to write, review, port, and enforce idiomatic Rust:
    
    - **`rust-best-practices`** loads whenever an agent writes or changes Rust, and steers it
      toward idiomatic, robust, maintainable code.
    - **`rust-review`** reviews existing Rust code, a file, a crate, or a diff, and writes a
      prioritized report where every finding cites the rule it breaks and shows the fix.
    - **`rust-port`** ports C, C++, Python, Go, or JavaScript to idiomatic Rust with the same
      behavior, porting the original tests first so you can prove the two match.
    - **`lints/`** is a drop-in clippy configuration that enforces the machine-checkable rules
      in CI.
    
    They work with Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI, and any other
    agent that reads the Agent Skills format. Every code example in the skills compiles on
    stable Rust, and every lint in the config was checked against current clippy.
    
    The guidance is distilled from five sources, with a condensed digest of each bundled in
    the skill so the agent can consult the original reasoning when it needs to:
    
    - Google Rust Style Guide
    - Rust API Guidelines (official rust-lang checklist)
    - Effective Rust by David Drysdale
    - Rust Design Patterns (idioms, patterns, anti-patterns)
    - Microsoft Pragmatic Rust Guidelines
    
    Where the sources disagree, the skill picks a side and says why.
    
    ## What it changes
    
    Asked for a small semver-parsing library, an agent without the skill produced working
    code with public fields, no `# Errors` docs, and `unwrap()` in its doc examples. With the
    skill, the same agent kept the fields private, documented failure modes, and wrote doc
    examples users can copy safely. Condensed from those two runs:
    
    ```rust
    // Without the skill
    /// A semantic version. The fields are public for convenience.
    pub struct Version {

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  mizorewww/gdirect
    ⭐ 619 stars  |  🍴 37 forks  |  💻 Rust  |  📅 2026-10-25
    🔗 https://github.com/mizorewww/gdirect
    📡 来源: 🚀 5天300+星
    📝 Rust Google Drive direct downloader using pinned libaria2

    README 摘要:
    # gdirect
    
    中文 · Changelog
    
    gdirect browses, downloads, uploads and mounts your Google Drive from the terminal. It finds Google IPs that are reachable from your network and sends Drive traffic straight to them, with multi-connection, resumable downloads.
    
    ## How it works
    
    | Traffic | Route |
    | --- | --- |
    | Drive API, downloads, uploads (`browse`, `ls`, `download`, `upload`) | A scanned Google IP. The hostname and certificate check stay the same. If connections carrying the real SNI are reset, gdirect automatically retries under a forged identity (`g.cn` as TLS name, the real host in the Host header) — same idea as Sheas-Cealer — and remembers what worked per IP |
    | Sign-in, account verification and token refresh (`accounts.google.com`, `oauth2.googleapis.com`, `www.googleapis.com`) | Your normal system network (DNS, proxy) |
    | `mount` (rclone) | Your normal system network |
    
    The first transfer command checks a known relay and sweeps Google's own front ends, and keeps the ones that work for 24 hours. The relay, 183.56.143.147, is not Google: it forwards connections to Google, which makes it fast and stable in mainland China, so it is tried first. It cannot read your traffic (TLS runs end to end and is verified against Google's roots), but its operator sees your IP address and, unless the forged identity is used, which Google host you connect to. To avoid it, pass `--google-only` (or set `GDIRECT_GOOGLE_ONLY=1`); only Google's own front ends are then used. Those come from the address space Google publishes as its own (goog.json minus cloud.json, embedded and refreshed weekly). Most Google IPs are blocked in mainland China, but some front ends are not: the sweep tries a TCP connection first, fully verifies only what answers (TLS, the Drive API and a test download), and stops once it has 8. Each candidate is probed with the real SNI first, then with the forged identity. If an endpoint (the relay included) stops answering, requests and downloads move to the next verified one. `login` and `mount` do not scan. Certificates are verified against Google's own GTS roots (embedded in the binary), never against a system CA bundle — a compromised third-party CA cannot impersonate Google for gdirect.
    
    Network requirements:
    
    - Sign-in needs browser access to `accounts.google.com` and application access to `oauth2.googleapis.com` and `www.googleapis.com`. Token refresh needs `oauth2.googleapis.com`. If Google is blocked, keep a proxy available for these requests, including

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  DenisSergeevitch/ex-ussr-kinship-research
    ⭐ 566 stars  |  🍴 53 forks  |  💻 Python  |  📅 2026-10-25
    🔗 https://github.com/DenisSergeevitch/ex-ussr-kinship-research
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, archives, claude-code, codex, family-history, familysearch, genealogy, ussr
    📝 Evidence-first genealogy skill for AI agents (Codex, Claude Code): church books, civil, military, deportation and repression records across the former USSR. Replies in your language.

    README 摘要:
    # ex-USSR Kinship Research
    
    **An evidence-first genealogy skill for AI agents (Codex, Claude Code and other Agent Skills runtimes).** It turns an agent into a careful family-history researcher for the former USSR, the Soviet Union and the Russian Empire. The agent reads church books and civil records, military, deportation and repression files, and unindexed archive scans. It keeps every find traceable, separates records from interpretation and says plainly what is proven and what is not.
    
    Coverage includes all 15 former Soviet republics: Russia, Ukraine, Belarus, Moldova, Estonia, Latvia, Lithuania, Georgia, Armenia, Azerbaijan, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan. Archives are chosen by the event's historical jurisdiction and current record custodian; a regional example does not replace local research.
    
    The skill's instructions are written in Russian, but **the agent talks to you in your language**: English, Ukrainian, Russian, Polish, German and so on. It quotes sources in their original spelling with a translation, and builds search queries in the languages of the records.
    
    ---
    
    ## What it does
    
    - **Case intake and scope.** One research question, known facts, who may be alive, what is off-limits.
    - **Reproducible registers.** Persons, artifacts, claims, relationships and a full search log (CSV), plus a final report template.
    - **Historical jurisdiction model.** It resolves every event to the state, province, district, parish or civil registry *as of the event date*, not today's map.
    - **Name-variant matrices.** Pre-reform Russian, Ukrainian, Polish, Romanian, German and Yiddish forms, patronymics, maiden names and transliterations.
    - **Source strategy.** Originals first, then official catalogs, indexes, published document collections, and only then trees and forums as leads.
    - **Evidence protocol.** Claims get explainable statuses, not percentages: `hypothesis`, `single-source`, `corroborated`, `strongly-corroborated`, `contradicted`, `unresolved`. Copies and mirrors of one record share an `independence_group`, so they never count as independent proof.
    - **Identity resolution.** Namesakes stay separate `person_id`s until distinguishing evidence appears: house number, parents, godparents, exact birth date or military unit.
    - **Audit script.** It checks referential integrity and flags weak corroboration before you write conclusions. An independence group counts only when a cited artifact belongs to it, so corroboration cannot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  enesozturk/dimensional-drawing
    ⭐ 563 stars  |  🍴 31 forks  |  💻 HTML  |  📅 2026-10-23
    🔗 https://github.com/enesozturk/dimensional-drawing
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    dimensional-drawing ✏️📐
    
      Give it a UI component, get back a one-page technical drawing of it.
      Paddings, gaps, corner radii, layers and viewport placement, measured and labeled like Apple's dimensional drawings.
    
      Install ·
      Use it ·
      Make it move ·
      Examples
    
    ---
    
    Apple publishes dimensional drawings for every device so accessory makers can build cases that fit. They are calm, dense and beautiful: one sheet, a few views, tiny detail circles, numbers everywhere.
    
    This repo teaches your agent to draw **your components** the same way. A card or a dialog becomes a spec sheet you could hand to anyone and they would rebuild its *architecture*: paddings, gaps, radii, layers, how it sits in the viewport. Copy and content are left out on purpose, so the drawing stays true when the text changes.
    
    ## What's inside 🎁
    
    ```
    skills/
    ├── dimensional-drawing/          the drawing skill
    │   ├── SKILL.md
    │   └── examples/                 card + dialog sheets (single HTML files)
    └── dimensional-drawing-motion/   turns a sheet into a ~10 s film
        ├── SKILL.md
        ├── templates/                reference scene + stylesheet
        └── adapters/
            ├── claude-motion.md      Claude's Motion artifact (primary)
            └── headless/             Playwright + ffmpeg, no Claude needed
    ```
    
    ### The house rules
    
    | | |
    |---|---|
    | ⚫️ **Monochrome** | grays only; things are told apart by line weight, dashes and hatches |
    | 🧱 **Architecture, not content** | `TITLE SLOT · FLEX`, `ACTION · HUG`, `CONTENT SLOT · FILL` |
    | 🔤 **Variables, not numbers** | `S1`, `R2`, `H1 = 2·S1 + H3`, `R2 = R1 − B − S6` |
    | 🏷️ **Unbranded** | neutral names like `UI-CARD-001` |
    | 🙅 **Never invent values** | unknowns stay `[TBD]` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  ⚠️风险  mateogon/pdf-narrator
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 214 stars  |  🍴 37 forks  |  💻 Python  |  📅 2024-12-15
    🔗 https://github.com/mateogon/pdf-narrator
    📡 来源: 📖 阅读/内容平台 | 活跃 | audiobook text-to-speech
    🏷️ audiobook, audiobook-generator, epub, immersive-reading, kokoro-tts, low-resource, pdf, pdf-audiobook, pdf-extraction, pdf-to-audiobook
    📝 Convert your PDFs and EPUBs into audiobooks effortlessly. Features intelligent text extraction, customizable text-to-speech settings, and efficient processing for low-resource systems.

    README 摘要:
    # PDF Narrator
    
    PDF Narrator turns PDF, EPUB, TXT and HTML books into audiobooks. It uses Kokoro-82M, a speech model that runs on your computer. Your books do not go to the internet.
    
    > For a reader that shows the text while the audio plays, see Cadence.
    
    ## Contents
    
    1. Features
    2. Requirements
    3. Install
    4. Make an audiobook
    5. Where your files are
    6. Command line
    7. Optional setups
    8. Troubleshooting
    9. Development
    10. License
    
    ## Features
    
    - **Desktop app.** A library of your books and a four-step flow: check the text, pick a voice, create the audio, export.
    - **Local speech.** Kokoro runs on the CPU, on an Apple GPU (MPS) or on an NVIDIA GPU (CUDA). The app selects the fastest one.
    - **Fast.** On an Apple M-series GPU, the app creates audio about 10 to 13 times faster than real time.
    - **Clean text.** The app skips covers, copyright pages, contents and Project Gutenberg license text. You can edit any chapter before you create audio.
    - **54 voices in 9 languages.** You hear each voice read a paragraph from your own book. Each voice shows its quality grade from Kokoro.
    - **Audiobook export.** M4B with chapters, title, author and cover, or one MP3 file for each chapter.
    - **Safe to stop.** You can pause, stop and continue. Finished chapters stay finished. If you edit a chapter, the app creates only that chapter again.
    
    ## Requirements
    
    | Item | Requirement |
    |---|---|
    | Operating system | macOS, Windows 10/11 or Linux |
    | Tools | uv and Git |
    | Disk space | About 2 GB for Python packages, plus about 350 MB for the speech model |
    | Internet | Only for the first install and the first use of each voice |
    | M4B export (optional) | FFmpeg |
    | Scanned PDFs (optional) | Tesseract and Poppler. See Scanned PDFs |
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  ngo275/app-agent
    ⭐ 191 stars  |  🍴 31 forks  |  💻 TypeScript  |  📅 2024-12-17
    🔗 https://github.com/ngo275/app-agent
    📡 来源: 📈 增长/推广/运营 | 活跃 | app store optimization A
    🏷️ agent, app-agent, app-store, app-store-connect, appagent, appstore, appstoreconnect, aso, google-play-console
    📝 AppAgent is an AI-first tool that handles your app release and App Store Optimization (ASO). An OSS alternative to App Radar, Sensor Tower, AppTweak, AppFollow, other ASO tools, built for developers who should focus on what really matters; build products.

    README 摘要:
    # AppAgent
    
    AppAgent is an open-source tool for app store optimization (ASO), multilingual
    metadata, and App Store Connect release workflows. It is intended to run in your
    own local environment, using your own database and API accounts.
    
    **The hosted offering is being discontinued. Use the local setup below instead
    of signing up for a hosted AppAgent account.** The OSS project remains available
    under AGPL-3.0-or-later. This change in direction is not a claim that old hosting,
    credentials, or stored data have already been removed.
    
    ## What it does
    
    - Research keywords and competitors, and generate localized store metadata.
    - Generate descriptions and release notes with OpenAI.
    - Import App Store Connect apps and metadata, prepare changes locally, and
      explicitly push updates or submit a version for review.
    
    App Store Connect is the primary release workflow. Google Play support is
    partial; do not assume feature parity. This is not an offline application:
    AI generation, store searches, and store updates call external services. Review
    changes before pushing or submitting them to an app store.
    
    ## Requirements
    
    - Node.js **24.22.1 or a newer 24.x release** (`.nvmrc` and `package.json`).
    - Yarn **1.22.22**, through Corepack or your own installation.
    - PostgreSQL and an empty database for a new installation.
    - An OpenAI API key for AI features, with access to the models used by the code
      (including `gpt-4.1`, `gpt-4o`, and `o3-mini`). API charges are yours.
    - Upstash Redis REST URL/token for keyword and store-search caching. These
      features currently use Upstash directly; a plain local Redis TCP URL is not a
      drop-in replacement.
    - Your App Store Connect API key for importing or modifying your apps. Enter
      these credentials in the app's team settings, not in this repository.
    
    Stripe, Vercel, Resend, Google OAuth, and analytics accounts are **not required
    for the recommended local development setup**. Authentication is still enabled.
    
    ## Local setup

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#14  chmouel/liseur
    ⭐ 158 stars  |  🍴 8 forks  |  💻 Kotlin  |  📅 2026-07-28
    🔗 https://github.com/chmouel/liseur
    📡 来源: 📖 阅读/内容平台 | 活跃 | epub reader open source
    🏷️ ai-assisted, android, calibre-web, ebook-reader, epub, epub-reader, f-droid, foss, jetpack-compose, kobo-sync
    📝 Open-source EPUB reader and remote library client for Android, with a Kindle-inspired reading experience

    README 摘要:
    # Liseur
    
      
        
      
      
      
        
      
    
      
        
        
      
    
    An open-source ebook reader for Android, and a client for calibre-web, Komga, BookOrbit, liseur-sync and any OPDS catalog: EPUBs on your phone or in sync with book server.
    
      
        
        
        
      
      
        The shelf, sorted by what you are currently reading.
        Distraction-free page with notes and bookmarks.
        Read aloud with device voices or your own speech server.
      
      
        
        
        
        
      
      
        Reading order, progress, and which volumes are missing.
        Character profiles grounded in earlier passages.
        See which characters appear together across chapters.
      
    
    More screenshots here
