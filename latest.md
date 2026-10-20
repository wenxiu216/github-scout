📊 开源日报 — 2026-10-20
共发现 9 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  headroomlabs-ai/headroom
    ⭐ 76361 stars  |  🍴 5930 forks  |  💻 Python  |  📅 2026-01-07
    🔗 https://github.com/headroomlabs-ai/headroom
    📡 来源: trending-daily
    🏷️ agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain
    📝 Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

    README 摘要:
    Quickstart ·
      Headroom for Teams ·
      Install ·
      Proof ·
      Agents ·
      Docs ·
      Discord ·
      llms.txt
    
    AI agents / LLMs: read /llms.txt here, or fetch
    the live index ·
    full docs blob.
    
    Headroom compresses everything your AI agent reads — tool outputs, logs, RAG
    chunks, files, and conversation history — before it reaches the LLM. Same
    answers, fraction of the tokens. Compression runs on your machine; no prompt or
    file content is sent anywhere to be compressed.
    
      
    
      
      10,144 → 1,260 tokens. The same FATAL found.
    
    ## What it does
    
    - **Library** — `compress(messages)` in Python or TypeScript, inline in any app.
    - **Proxy** — `headroom proxy --port 8787`, zero code changes, any language.
    - **Agent wrap** — `headroom wrap claude|codex|grok|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe|omp|zcode` in one command; undo with `headroom unwrap `.
    - **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client.
    - **Cross-agent memory** — one shared store across Claude, Codex, Gemini and Grok, with automatic dedup.
    - **`headroom learn`** — mines failed sessions and writes corrections to `CLAUDE.local.md` (default, gitignored), `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` or `GROK.md`.
    - **Output token reduction** — trims what the model *writes back*, not only what you send. See below.
    - **Reversible (CCR)** — originals are cached locally and retrieved on demand.
    
    ## How it works
    
    ```
     Your agent / app
       (Claude Code, Cursor, Codex, LangChain, Agno, Strands, your own code…)
            │   prompts · tool outputs · logs · RAG results · files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  YuJunZhiXue/dsh-purge
    ⭐ 9563 stars  |  🍴 1829 forks  |  💻 JavaScript  |  📅 2026-08-19
    🔗 https://github.com/YuJunZhiXue/dsh-purge
    📡 来源: trending-weekly
    🏷️ deepseek, deepseek-harness, dsh-plugin, dsh-plugins, harness-jailbreak, jailbreak, llm-jailbreak
    📝 DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐ 如要二开，请查看署名要求部分

    README 摘要:
    ⚔️ DeepSeek Harness 网络安全红队工具（dsh-purge）
    
    Version 1.1.71
    
      DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐ 如要二开，请查看署名要求部分
    
      
      
      
      
      
      
      
      
    
      
    
      中文 · English
    
    > 我直说。
    >
    > 我被裁了。现在彻底没工作，也没有稳定收入。这个仓库一直是我业余在写。后面为了吃饭，我可能得去跑外卖，不一定还能天天改这个。
    >
    > **从今天起到 2026 年 10 月 26 日，我征集七天。** 想留、想骂、想投广告、想赞助，写到 Issue #130。我会看。不保证每条都回。
    >
    > **10 月 27 日起，我把这个仓库关上。** GitHub 上我不再发新版本。后面的包我只发在这个频道：t.me/LLM_PoJia/271。你们手里已经下过的旧版本还能用。协议我也改了，现在是商业许可，下面有写。
    
    > **官方 Web 和官方桌面端都支持。** 官方 `dsh web` 用 profile `web`；官方桌面 EXE（DeepSeek Harness **0.2.0-rc.2 / 0.2.1-rc.2**）用 profile `desktop`。两边分开安装、分开点「应用」。当前版本只适配 dsh 0.2；更早的 dsh 用对应的老版本插件。社区桌面端不维护。
    >
    > 写进 profile 还不会改宿主。点会话标题旁的 **dsh-purge** → **清洗** → **应用**。成功会自动重启；补丁没打完不重启。重启后新开一轮对话，注入才进当前会话。
    >
    > Node.js **≥18**。Windows 无闪窗需要 **Node ≥22**。npm 上没有 `dsh-purge` 这个包，安装请走下面的 GitHub 归档，不要 `pnpm add dsh-purge`。
    
    ## 目录
    
    - 赞助
    - 广告位
    - 介绍
    - 署名要求
    - 许可证

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Gathin23/cleanyourtv
    ⭐ 6637 stars  |  🍴 786 forks  |  💻 Java  |  📅 2026-10-17
    🔗 https://github.com/Gathin23/cleanyourtv
    📡 来源: 🚀 5天300+星
    🏷️ adb, adblock, android-tv, android-tv-launcher, apple-tv, bloatware-removal, claude-code, debloat, fire-tv, google-tv
    📝 Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home.

    README 摘要:
    cleanyour.tv ·
      The prompt ·
      66 TV lists ·
      15 built on it ·
      The tweet
    
      
      
      
      
      
      
    
    Strip the bloatware from any Android TV or Google TV over Wi-Fi, and replace the ad-filled home
    screen with a clean launcher that looks like an Apple TV. **No root, no cable, nothing uninstalled,
    and a one-line restore if you change your mind.**
    
    66 TV models &nbsp;·&nbsp; 25 brands &nbsp;·&nbsp; 14 languages &nbsp;·&nbsp; 300 KB launcher
    
      FEATURED IN
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      &nbsp;&nbsp;
      
    
    > Vibe coded my parents' TV this afternoon! It was showing a sponsored ad before you could even get
    > to Netflix. Gave Claude Code the model number, it found the TV on wifi, removed 25 Xiaomi packages
    > and wrote a new launcher. Looks like an Apple TV now lol.
    >
    > @gathint, 17 October 2026. The replies are where

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  xiaoyang111222/cn-math-taxonomy
    ⭐ 1132 stars  |  🍴 259 forks  |  💻 Python  |  📅 2026-10-18
    🔗 https://github.com/xiaoyang111222/cn-math-taxonomy
    📡 来源: 🚀 5天300+星
    🏷️ chinese, curriculum, diagnostic, edtech, education, elementary-school, junior-high-school, k12, knowledge-graph, math
    📝 中小学数学知识图谱 + 前置诊断：课标对齐、人教版一–九年级、531 知识点、2271 题、自适应诊断

    README 摘要:
    # 中小学数学知识图谱（一—九年级）
    
    对齐《义务教育数学课程标准（2022 年版）》与人教版一–九的知识点 DAG，附**自适应前置诊断**与题库。答错会沿先修边从初中一直回溯到具体的小学知识点，并给出按年级从低到高排列的学习路径。仓库名仍是 `cn-math-taxonomy`。
    
    **→ 在线试用诊断（演示：配方法）** · 首页 · 知识图谱 · 诊断工具 · GitHub Pages 备份
    
    | | 知识点 | 先修边 | 课标条目 | 题库 |
    | --- | ---: | ---: | ---: | ---: |
    | 小学（1–6 年级） | 216 | 311（小学内部） | 73（第一至三学段） | 864 |
    | 初中（7–9 年级） | 315 | 563（初中内部，未改） | 157（第四学段） | 1407 |
    | 合计 | 531 | 909（另有初中→小学 35） | 230 | 2271 |
    
    数据格式参考 Marble os-taxonomy（`topics` + `dependencies`）。
    
    **反馈 / 挑错：** 题干、答案或先修关系有问题，或想提功能建议，请 提交 Issue（已提供「题目纠错」「功能建议」模板）。
    
    > **状态声明：这是 AI 生成的初稿，未经任何教师审核。** 小学与初中都一样。
    > 知识点的拆分粒度、掌握标准、诊断题答案，尤其是**先修关系（哪些是 hard、哪些是 soft，甚至某条边该不该存在）都需要一线小学、初中数学教师审核**后才能用于教学、诊断或学习路径推荐。诊断题答案有自动核验和独立复核，但没有逐题由教师复核。小学册次目录多数不是人教社官网，标了「非官方、待核」的不要当成官方章名。
    
    ## 数据来源与对齐依据
    
    - **课程标准**：教育部《义务教育数学课程标准（2022年版）》第一至第四学段（1—9 年级）的【内容要求】（数与代数、图形与几何、统计与概率、综合与实践）。`data/cn-curriculum-standards.json` 现有 **230** 条（第一至三学段 73 + 第四学段 157）。第四学段条文仍是原先从教育部 PDF 识别的原文；第一至三学段据公开转写整理，**未与教育部 PDF 逐页核对**，`page_or_ref` 为「待核」。来源、规则、覆盖率与局限见 docs/standards-mapping.md。
    - **教材顺序**：人民教育出版社（人教版）义务教育教科书数学。**初中**采用 2024 年审定的新版，章节目录取自第三方电子课本目录站 dzskb.com（非人教社官方页面），核对情况如下（小学各册见下文「小学册次目录」）：
    
      | 册次 | 采用的目录 | 核实情况 |
      |---|---|---|
      | 七上 | 第一章 有理数 … 第六章 几何图形初步 | 已核对目录页 |
      | 七下 | 第七章 相交线与平行线 … 第十二章 数据的收集、整理与描述 | 已核对目录页 |
      | 八上 | 第十三章 三角形 … 第十八章 分式（2024 审定版） | 已核对目录页 |
      | 八下 | 第十九章 二次根式 … 第二十四章 数据的分析（2024 审定版） | 已核对目录页 |
      | 九上 | 第二十五章 一元二次方程 … 第三十章 直线与圆的位置关系（2024 审定版） | 已核对目录页 |
      | 九下 | 第三十一章 相似；第三十二章 锐角三角函数（章末综合与实践：停车设计问题）；第三十三章 投影与视图（章末综合与实践：建筑中的数学）；第三十四章 随机事件的概率（34.1.1 随机事件，34.1.2 概率，34.2 用列举法求概率，34.3 用频率估计概率） | **非官方、待核**，详见下方「九下目录的来源与核实情况」 |
    
      新版教材相对旧版有较大调整（如多边形移入八下“四边形”、反比例函数移入九上、新增“数据的四分位数”“综合与实践”主题、概率由九上移到九下并改名“随机事件的概率”等），本图谱按新版目录处理。
    
    ### 九下目录的来源与核实情况（查证日期：2026-10-17；**非官方、待核**）
    
    **结论**：没有找到人教社（pep.com.cn）官方发布的 2024 版九下目录页（官方“新教材介绍”页只介绍编写思路，未列各册章目；pep.com.cn 的“数学 九年级下册”页是旧版封面，页面不显示目录）。九下的 2024 版教材预计 2027 年春季学期才开始使用。下列目录是综合第三方来源后的**最可靠推定**，并非官方原文，章名、章号请以教材实物或人教社官方目录为准。
    
    | 章 | 采用的章名 | 依据 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  aicodeking/leanrea
    ⭐ 1023 stars  |  🍴 154 forks  |  💻 Python  |  📅 2026-10-17
    🔗 https://github.com/aicodeking/leanrea
    📡 来源: 🚀 5天300+星
    📝 One 8 KB skill that replaces REA (Reverse Engineer Anything): plain CLI tools, no MCP. Benchmarked: 38% faster, 35% cheaper.

    README 摘要:
    # leanrea
    
    **One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup.**
    
    REA (Reverse Engineer Anything) puts an MCP layer between your agent and tools it can already use: asar, otool, nm, `go version -m`, jadx, apktool, Ghidra, tshark, binwalk, sqlite3. leanrea drops that layer. It tells the agent which command is fastest for each kind of target, gives it ready-to-paste recon commands, and lists the traps that REA's code handles for you. The agent then runs the real tools itself.
    
    |  | REA 6.5.0 | leanrea |
    |---|---|---|
    | What gets installed | 25 MB npm package + MCP server | one `SKILL.md` |
    | Instructions | 23.5 KB skill + 48.8 KB references | 8 KB |
    | Tools added to the agent | 207 (3.35 MB of definitions) | 0 (uses Bash) |
    | Context for "Reply OK", all tools loaded | 400.7k tokens, $1.60 | 34.5k tokens, $0.09 |
    
    ## Benchmark
    
    Claude Code headless (`claude -p`), Sonnet 5.5, macOS arm64. 4 reverse-engineering tasks × 3 reps × 3 arms, with the arms run side by side. Answers are graded against hand-made keys.
    
    | arm | total wall time | cost | turns | tokens | score |
    |---|---|---|---|---|---|
    | **leanrea** | **388 s** | **$2.17** | **55** | **2.40 M** | 74/75 |
    | no skill | 479 s | $2.21 | 81 | 3.11 M | 67/75 (one refusal) |
    | REA (MCP + its skill) | 627 s | $3.36 | 124 | 5.93 M | 75/75 |
    
    Against REA, leanrea had **38% less wall time, 35% lower cost, 56% fewer turns and 60% fewer tokens, at the same accuracy**. Its one partial miss named an older IPC channel instead of the v2 one (both channels exist).
    
    The tasks:
    - **electron**: trace a feature through a real Electron app's app.asar (native function → main-process class → IPC channels).
    - **native**: inventory the exports, a TCC permission check and the single-instance lock of that app's native addon (`.node`).
    - **go**: toolchain and dependency versions of a stripped `gh` binary.
    - **deep**: from disassembly alone, the exact socket path format, wire protocol and peer authentication of that lock.
    
    The same operation run through REA's CLI vs the raw command:
    
    | operation | REA | raw |
    |---|---|---|
    | Go build info | 0.56 s | `go version -m`: 0.06 s |
    | Mach-O overview | 3.32 s | otool + dyld_info + nm: 0.04 s |
    | Electron app analysis (real desktop app) | fails on asar integrity until you pass a flag, then **47.9 s and 140 MB of JSON** | asar extract + `rg -uu`: 4.8 s, 24 KB |
    
    Full tables, the context-overhead runs and caveats: bench/BENCHMARK.md. Raw per-run metrics: bench/r

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  alchaincyf/huashu-motion
    ⭐ 1001 stars  |  🍴 110 forks  |  💻 JavaScript  |  📅 2026-10-18
    🔗 https://github.com/alchaincyf/huashu-motion
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, animation, claude-code, codex, gsap, launch-video, motion-graphics, skills
    📝 让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

    README 摘要:
    **简体中文** | English
    
    # huashu-motion
    
    > *「一键直出商业级产品宣传片。」*
    
    **让你的agent做动画、作曲，指着画面改。**
    
    跟Claude Code、Codex这些agent说一句「给我的产品做个30秒的发布片」，
    它会先读你的产品，给你三个方向挑，写出整支片子，自己写谱配乐，
    然后在浏览器里打开一个编辑器等你。哪里不满意，在画面上点一下，写下要改什么，它就只改那一处。
    
    ```sh
    npx skills add alchaincyf/huashu-motion
    ```
    
    看效果 · 安装 · 能做什么 · 怎么做到的 · 背后的故事
    
    ---
    
    ## 看效果
    
    这篇README里的每一段动画都是huashu-motion做的。上面那段取自它给自己做的53秒发布片，👉 下载完整发布片（MP4，带声音），下面Grok Bot、huashu-design、DeepSeek这几支的完整版也在同一个页面。
    
    ### 指着画面改
    
    按C，在画面上点一下，写下要改什么。评论发过去的时候带着时间点、场景、点中的元素和它在源码里的位置，agent先把那一帧和你点的那一小块截图放大看一眼，再只改那一处，改完回一句人话，预览停在原来的位置刷新。每一版都留着，⌘Z随时撤回；标题、数字、颜色、停留时长这些会变成编辑器右边的输入框，自己改，不用等agent。
    
    （这段里的编辑器和终端是照真实界面重建的，代码细节是示意；评论是真实提过的意见。）
    
    ### 先写谱，再拍片
    
    做发布片用的是作曲家模式：agent按节奏单先写一份谱（ABC记谱法，纯文本的乐谱），谱里的标记对齐每个场景，再由三角钢琴、弦乐和鼓组的采样演奏出来（真乐器采样要先跑一次`om samples build`，不跑就用合成音色）；画面上每个东西落地的那一帧，再配一个音效。配乐全部在本机现场生成，不调用任何收费接口。
    
    ### 一天，二十支
    
    16个镜头，来自同一天做的七支片子，按拍子切。
    
    Grok Bot（粉丝自制，非官方）· 30秒：傍晚交代任务，夜里几个agent各干各的，早上7点手机上收到汇报。这段是汇报一张张送往Chief of Staff的那几拍。
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  Noniv/web-ocean
    ⭐ 782 stars  |  🍴 117 forks  |  💻 HTML  |  📅 2026-10-16
    🔗 https://github.com/Noniv/web-ocean
    📡 来源: 🚀 5天300+星
    📝 Real-time WebGPU ocean renderer written from scratch, no engine. FFT waves, whitecaps, sun glitter, physically based sunset sky with clouds, free camera. Built with Claude Code (Opus 5.5). Opens from a single 61 KB HTML file in Chrome.

    README 摘要:
    # web-ocean
    
    A real-time ocean renderer written from scratch on WebGPU, with no engine or rendering library. It draws a sunset sea with simulated waves, whitecaps, sun glitter, and a physically based sky with clouds. You fly around it with a free camera.
    
    | 75 degrees off the sun, 2.4 m up | Looking toward the sun from 30 m up |
    |---|---|
    |  |  |
    
    ## Run it
    
    You need a recent Chrome with WebGPU and a reasonably capable GPU. On a laptop, force Chrome onto the dedicated GPU in the Windows graphics settings, or it will fall back to the integrated one.
    
    Open `ocean.html` directly in the browser. `ocean.min.html` is the same page minified (61 KB instead of 102 KB). Both are self-contained and work from `file://`.
    
    To run from source:
    
    ```
    npm install
    npm start        # serves http://localhost:8080/
    ```
    
    After editing anything under `js/`, run `npm run build` to regenerate both bundles. The minified build strips WGSL comments and whitespace and minifies the JavaScript with esbuild.
    
    ## Controls
    
    | Input | Action |
    |---|---|
    | Click the canvas | Capture the mouse (Esc releases it). Holding the right mouse button also works. |
    | Mouse | Look around |
    | W A S D | Move |
    | Space or E / Q or C | Up / down |
    | Shift | 5x speed |
    | Mouse wheel | Change base speed |
    | H | Settings panel: wind, swell, choppiness, turbidity, foam, sun, haze, clouds, exposure, bloom |
    
    The camera keeps itself above the displaced water surface, so waves never pass through it.
    
    URL parameters are handy for testing. `?w=2560&h=1440` forces the render resolution, `cam=x,y,z,yawDeg,pitchDeg` sets the camera, `fov=deg` sets the field of view, `ui=0` hides the HUD, and any settings key works too, for example `windSpeed=12&swellHs=2&sunElev=8`.
    
    ## How it works

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  humblemuzzu/dumbtv
    ⭐ 654 stars  |  🍴 57 forks  |  💻 JavaScript  |  📅 2026-10-18
    🔗 https://github.com/humblemuzzu/dumbtv
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # dumbtv
    
    Your TV should do what you paid for: your apps, your HDMI inputs, and nothing
    else. No ads from the TV itself, no watch tracking, no update you did not ask
    for. dumbtv applies that over ADB from another machine — **no root**, nothing
    written to `/system`, every step reversible with one script.
    
    The same idea, told to whichever TV will listen:
    
    | TV | Debloat | Own home screen | On-device DNS filter |
    |---|---|---|---|
    | **Fire OS** (Fire TV sticks, Fire TV Edition TVs) | yes | yes | yes |
    | **Android TV / Google TV** (Sony, TCL, Philips, Hisense, Xiaomi, Shield) | yes | yes, by disabling the stock launcher | yes |
    | **Samsung, LG, Roku, VIDAA, Vizio, Panasonic, Philips Saphi** | no shell, no path | no | no — block it at the router, or boot the TV straight into HDMI |
    
    Tested end to end on a Fire TV Edition television running Fire OS 7.7.1.7
    (Android 9). Fire OS 6 and 8 differ in small ways; Android TV needs a different
    package list and a different launcher trick. Fire OS 6 (Android 7.1, e.g. the 2018
    Fire TV Stick 4K) uses its own lists in `data/fireos6/`, picked up from the device,
    and the launcher holds HOME there with a small foreground service instead of the
    accessibility hook Amazon refuses on 6.7. The ones that cannot be opened, and the
    honest reason for each, are in `docs/OTHER-TVS.md` — along with what we are
    working on to reach them.
    
    **What it will not do:** replace the operating system, unlock a bootloader, or
    survive a factory reset. Every current TV has a signed boot chain and a verified
    system partition, so there is no honest way around it. Pretending otherwise is
    how people brick their TVs. See `docs/WHY-NOT-REPLACE-OS.md`.
    
    ## Add your TV to the catalog
    
    At the end of a session — or any time something surprised you — record it:
    
    ```sh
    ./scripts/contribute.sh
    ```
    
    It reads the model, OS build and kernel from the TV, then asks only what a robot
    cannot know: how developer mode was enabled, where the IP address was shown,
    which dialogs blocked automation and what dismissed each one. It writes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  cranebeaker/coop-anything
    ⭐ 600 stars  |  🍴 59 forks  |  💻 C  |  📅 2026-10-16
    🔗 https://github.com/cranebeaker/coop-anything
    📡 来源: 🚀 5天300+星
    📝 Co-op Anything: point your AI agent at any single-player game and play it with friends (online and/or splitscreen!). MCP server and playbook to let you reverse engineer, fix, test, ship and share what it learns.

    README 摘要:
    Co-op Anything
    
    Any single-player game. Your friends. Your agent does the work.
    
    Quick start ·
    How it works ·
    What you can co-op ·
    Games so far ·
    Contribute ·
    FAQ ·
    Docs
    
    Want to play a single-player game with your friends? Point your AI coding agent at this
    repo. It researches what exists, reverse engineers the game and its engine if it has to,
    builds or fixes the co-op, **tests it with bots inside the game**, and packages it so your
    friends install it in one click and join over Steam without port forwarding.
    
    The sky is the limit. Every game that runs on your PC is a candidate.
    
    Games being made co-op right now: **Deus Ex** (released) ·
    **Fallout: New Vegas** · **Zelda: Ocarina of Time** (fully synced) ·
    **Dungeon Keeper** · **S.T.A.L.K.E.R. Shadow of Chernobyl**
    
    From the community: **Mega Man X** and
    **Mega Man X4** (native PC with co-op netplay) ·
    **Pilotwings 64** (split-screen) ·
    **Crab Champions** · **Stacklands** ·
    **Half Sword** · **Enter the Gungeon** ·
    **Clive Barker's Jericho** · **Poppy Playtime** ·
    **Divinity II** (split-screen) · **Command & Conquer 3** (campaign co-op) ·
    **Far Cry 2** · yours next?
    
    ## Quick start
    
    Tell your agent (Claude Code, Codex, Gemini CLI, Cursor, OpenCode, ...):
    
    ```
    Read https://github.com/cranebeaker/coop-anything and follow AGENTS.md.
    I want to play  in co-op with my friends.
    ```
