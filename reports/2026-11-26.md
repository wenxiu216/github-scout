📊 开源日报 — 2026-11-26
共发现 6 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  n8n-io/nod
    ⭐ 3688 stars  |  🍴 585 forks  |  💻 TypeScript  |  📅 2026-09-25
    🔗 https://github.com/n8n-io/nod
    📡 来源: trending-weekly
    🏷️ agents, ai-agent, ai-assistant, anthropic, automation, browser-automation, computer-use, electron, llm, local-first
    📝 Open source personal agent with its own computer. It chases invoices, preps your calls and cancels trials on real websites, and asks before it acts. Runs on your machine with the model you choose. By n8n.

    README 摘要:
    It chases invoices, preps your calls and cancels trials, on real websites.
      It runs on your machine with the model you choose, and asks before it acts for you.
    
      
      
      
      
      
      
    
      macOS 14+ (Apple silicon or Intel) · Windows 11 preview · Linux x64 preview · Free and open source · ChatGPT Plus or Pro, or an AI key
    
      
      
      
      
      
      
    
      On your machine · The hard ones · Memory · Your rules · Measured · Under the hood · Next · Answers · Get Nod · Build with us
    
      
        
          
          
          
        
      
    
    It gets on with the work across Gmail, Calendar, Slack, Notion, and the web,and asks before it speaks for you.
    
    Every morning, Nod reads your threads, your calendar, and the client's latest news,then writes a one-page brief for each call.
    
    It drafts the reply you owe from your own pricing sheet,and sends it only after you say yes.
    
    It checks a page on your schedule and tells you only when something changes.
    
      
        
          

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  Belobug/VIctory-Belobug-AMD
    ⭐ 1703 stars  |  🍴 305 forks  |  💻 Rust  |  📅 2026-11-25
    🔗 https://github.com/Belobug/VIctory-Belobug-AMD
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # VIctory on an RX 7900 XTX
    
    A fork of VIctory, a compatibility layer
    that runs an Xbox Series title natively on Windows from files the user supplies.
    This one is about **speed on AMD RDNA 3**: the world at 30 frames a second on
    one PC, without giving up the picture. It is not there yet.
    
    **This repository contains no game files, code or assets.** You need your own
    copy of the game. It is not affiliated with or endorsed by the game's developer
    or publisher.
    
    ## Where it stands (2026-11-25)
    
    Tested on one machine only: Windows 11, Intel i9-12900K, 64 GB RAM, Radeon
    RX 7900 XTX, 1440p, the Series X profile.
    
    | | |
    |---|---|
    | Menus, videos, loading screens | 30 fps |
    | Prologue, indoors | 50-75 ms a frame (13-20 fps) |
    | First mission with the boat | 46-53 ms (19-22 fps) |
    | Street chase with many cars and people | 100-165 ms (6-10 fps), single frames far longer |
    | Outdoors on foot, the camp | 60-90 ms |
    | Flying | 42-57 ms |
    | Longest session so far | 41 minutes, no crash |
    | Memory | 40-46 GB of private memory: **64 GB of RAM recommended** |
    
    It started at 280 ms a frame in the same scenes two days earlier.
    
    What is known to be wrong:
    
    - Trees, plants and far buildings flicker outdoors in some places.
    - Rooms with little direct light are too dark without `-RayTracing`.
    - Textures of what just came into view appear late while the title streams.
    - The first run with a new driver or a new build stutters while the driver makes
      pipelines (`victory warm` makes them ahead).
    - Recording a frame in the world makes the title's own watchdog end it.
    
    ## How to run it
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  crhywun/g1-acq
    ⭐ 1415 stars  |  🍴 338 forks  |  💻 JavaScript  |  📅 2026-11-22
    🔗 https://github.com/crhywun/g1-acq
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # g1-acq
    
    > 💬 **AI羊毛交流群**:https://t.me/muihbb —— 交流 AI 优惠、订阅羊毛
    
    Google One（iOS）订阅入口的商品 ID 改写与采集工具，适用于 **Shadowrocket / 小火箭**。
    
    **v7.11.0 主模块为 G1 ACQ SKU 管理，新增「1 元开 Pro」预制模板，目标命名空间支持 com.google.gemini.*。** 打开本地报告页，在 **预制映射模板** 中点击 **应用模板**，即可直接合并并保存到手机本地，无需再填源、目标或另点保存。页面继续支持添加、编辑、勾选启用、逐条保存、删除映射和恢复默认；采集列表可预填源，输入框提供已采集 SKU 与模板目标候选。**点击时保存配置，下一次 `/ai?` 响应才使用新规则**，已打开或缓存的方案页需重新进入。
    
    默认模式 `discount75` 保留 20TB / 30TB 三个月 75p 和原始 iOS 2TB → `g1.2tb.ai.12months_ip_90p`；应用模板或保存手动规则后为 `custom`，即使模板目标恰好与默认相同。**75p = 75% off、实付 25%、2.5折**。当前改写运行版本为 `g1-acq-v7.11-mappings`，保留原始 SKU 采集、最近 10 次响应、重复诊断与 JSON 导出，无需另装扫描器；完整步骤见 SKU 管理、Pro 12个月优惠测试与采集。
    
    采集只读取手机实际收到的匹配响应，**不会主动查询全量 SKU**；旧 ID 再次出现时累加次数。字符串改写与 App Store 商品返回分别记录，商品名称、周期、初次与续费金额按收银台实际显示核对，权益按 Google One 账户实际状态记录。
    
    ## 主模块安装地址
    
    **G1 ACQ SKU 管理 — 四套预制模板与本地手动映射，保留默认 75p 与 2TB 目标**
    
    ```text
    https://cdn.jsdelivr.net/gh/crhywun/g1-acq@v7.11.0/g1-acq-ultra-discount.sgmodule
    ```
    
    | 项目 | 当前主入口 |
    |---|---|
    | 当前配置 `configuredMode` | 默认 `discount75`；应用模板或保存手动规则后 `custom` |
    | 响应脚本 | g1-acq-discount.js，与 g1-acq.js 实现相同 |
    | 响应运行版本 | `g1-acq-v7.11-mappings` |
    | 报告脚本 | g1-sku-report-discount.js，与 g1-sku-report.js 实现相同 |
    | 报告版本 | `v7.11.0` |
    | 默认 2TB 目标 | `g1.2tb.ai.12months_ip_90p`，无 `.acq` |
    | 本地数据 | 沿用 v7.9 的三个 schema 1 键；模板结果仍保存在 `g1.sku.mappings.v1`，无数据迁移 |
    
    首次安装时在小火箭模块管理中添加上方地址并启用。升级顺序为：**关闭旧模块 → 安装新地址 → 只开启 G1 ACQ SKU 管理一个改写入口 → 重新连接小火箭 → 重新打开 Google App 的方案页**。曾安装 **G1 ACQ Ultra 75p**、**G1 ACQ**、**G1 ACQ Ultra 一折**、**G1 ACQ Ultra 试用**、独立 **G1 SKU Scan**、**G1 Pro Annual Test** 或其它改写副本时，停用旧副本，避免重复计数或改写。
    
    安装入口与全部内部脚本固定引用 `@v7.11.0`，无需单独添加脚本。**旧固定链接需换成新地址，不会自动更新。** 当前树保留四个模块，试用模块仍缺席；历史 `v7.10.0` / `v7.9.0` / `v7.8.0` / `v7.7.0` / `v7.6.0` / `v7.5.0` / `v7.4.0` / `v7.3.0` / `v7.2.0` / `v7.1.0` / `v7.0.0` 与 `pro-annual-test-v1` / `pro-annual-test-v2` 标签保持原样，旧试用链接仍指向原内容。
    
    升级沿用 `g1.sku.scan.v1`、`g1.pro.annual.test.v1`、`g1.sku.mappings.v1`，三个键的 `schemaVersion=1` 保持不变，无自动配置迁移；v7.9 已保存的手动规则、累计 SKU、次数、最近 10 次响应和旧执行记录继续保留。当前配置与实际采集、执行记录分别显示，应用模板、保存或恢复规则不重写历史版本、模式、目标与时间。
    
    g1-acq-v7.sgmodule 保留名称 **G1 ACQ**；g1-pro-annual-test.sgmodule 保留名称 **G1 Pro Annual Test** 和仅 `/ai?` 的响应范围，二者使用同一本地映射配置。g1-sku-scan.sgmodule 更新下载 pin 并保留报告请求体配置，扫描实现仍为 `pro-annual-test-v2`，保持响应原文，没有模式或响应事件字段；报告保留其真实旧版本、空模式与缺失历史。四个报告 `http-request` 均设置 `requires-body=1,max-size=0`，供本地表单提交使用。
    
    ## 四套预制映射模板
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  avatarmanz/VIctory-7900XTX
    ⭐ 1346 stars  |  🍴 376 forks  |  💻 Rust  |  📅 2026-11-25
    🔗 https://github.com/avatarmanz/VIctory-7900XTX
    📡 来源: 🚀 5天300+星
    📝 Goal: an Xbox Series title (your own dump) at a stable 30+ fps on PC without ray tracing, then higher. Porting, not emulating: renderer patches + ahead-of-time shaders, RX 7900 XTX first. No game files.

    README 摘要:
    # VIctory on an RX 7900 XTX
    
    A fork of VIctory, a compatibility layer
    that runs an Xbox Series title natively on Windows from files the user supplies.
    
    ## The goal
    
    **A stable 30 fps or more without ray tracing, then as high a frame rate and as
    low frame times as the PC allows**, on an AMD RX 7900 XTX first and on PCs with
    32 GB (later 16 GB) of RAM.
    
    The way there is **porting, not emulating**: patching the title's renderer so it
    behaves the way a PC renderer does, rather than having the layer watch and copy
    the console's shared memory every frame. Shaders are translated ahead of time
    into a versioned store that is kept between builds. Ray tracing stays optional
    and off by default. The picture comes after the frame rate: texture pop-in and
    lighting that is too bright or too dark when walking indoors are next in line.
    
    **This repository contains no game files, code or assets.** You need your own
    copy of the game. It is not affiliated with or endorsed by the game's developer
    or publisher.
    
    ## Where it stands (2026-11-26)
    
    Tested on one machine only: Windows 11, Intel i9-12900K, 64 GB RAM, Radeon
    RX 7900 XTX, the Series X profile, ray tracing off.
    
    | | |
    |---|---|
    | City street, renderer patches 1+2 on | about 53 ms a frame (about 19 fps) |
    | Same scene before the patches | 57-75 ms (13-17 fps) |
    | Shaders the title uses that translate | all of them (25,790 of 25,985; the rest are unused geometry shaders) |
    | Memory | about 35 GB of private memory: **64 GB of RAM recommended** for now |
    
    It started at 280 ms a frame in the same scenes three days earlier.
    
    ### Renderer patches (off by default while they are tested)
    
    | Switch | What it does |
    |---|---|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  Avaneesh-Inamdar/Stream-Tube-Desktop
    ⭐ 1324 stars  |  🍴 114 forks  |  💻 Rust  |  📅 2026-11-22
    🔗 https://github.com/Avaneesh-Inamdar/Stream-Tube-Desktop
    📡 来源: 🚀 5天300+星
    🏷️ dearrow, desktop-app, gpui, mpv, rust, sponsorblock, windows, youtube, youtube-client
    📝 Native YouTube client for Windows in Rust, with SponsorBlock, DeArrow and Return YouTube Dislike built in

    README 摘要:
    Stream Tube
    
      A native YouTube client for Windows and Linux, written in Rust.
      No browser, no ads, no tracking. SponsorBlock, DeArrow and Return YouTube Dislike built in.
    
      
      
      
      
      
    
      
    
    ## Why
    
    I wanted YouTube on my desktop without keeping a browser tab open, and without the
    ads, autoplaying junk and sponsor reads. The existing options were either Electron
    apps that eat a gigabyte of RAM or web frontends that break every other week.
    Stream Tube is a single native app: the UI is drawn on the GPU with
    GPUI, and video
    goes through libmpv, so it starts fast and scrolls smoothly even with big feeds.
    
    ## What it does
    
    **No ads, anywhere**
    - No pre-roll, mid-roll or overlay ads: the app plays the video stream directly, so YouTube's ads are never loaded
    - No promoted videos, banners or sponsored cards in Home, search or Shorts
    - Sponsor reads inside videos are skipped too, with SponsorBlock (below)
    - Nothing to install or keep updated: it isn't an ad blocker that YouTube can break, ads simply aren't part of how the app plays video
    
    **Watching**
    - Home, Shorts, Subscriptions, Explore categories, channels (including their courses and shows), playlists and search, with search suggestions and your recent searches
    - A personal Home without an account: "For you" recommends videos related to what you've watched and searched in the app, mixed with new uploads from your subscriptions. Signed in, Home is your own YouTube Home feed
    - A *Recently uploaded* chip on Home, like youtube.com's: videos from your Home feed and subscriptions uploaded in the last two weeks, newest first
    - Hover a video title in a grid or list to read the full title
    - Ctrl+click a link or middle-click a video to open it in a background tab. A video's menu also has *Open in new tab*. Switch with Ctrl+Tab, Ctrl+1…9 or a click. Ctrl+T opens a new tab. Ctrl+W or a middle click on the tab closes it.
    - Videos made for kids (YouTube Kids) play and download like any other video
    - Old video annotations are back: notes, speech bubbles and clickable links from YouTube's annotation archive, drawn over the video where they used to be (turn them off in *Settings → Player* or from the player's gear menu)
    - Arabic, Hebrew and other right-to-left text is shown in the right order
    - Shorts follow your account's recommendations when you're signed in, or start from the Shorts you watched last

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  EmpressRevolution/aion-2-trainer-tool
    ⭐ 362 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-06-26
    🔗 https://github.com/EmpressRevolution/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, developer-tools
    📝 Aion 2, an advanced AI language model repository for prompt engineering, offers a pre-configured environment optimized for rapid deployment...

    README 摘要:
    # Aion 2 Cheat - Windows 10 & 11
    
    ## Introduction
    
    Aion 2 Cheat is a specialized tool designed for players looking to enhance their experience in the popular MMORPG, Aion 2. This software addresses common challenges that players often face, including difficulties in navigating certain game mechanics, optimizing gameplay performance, and automating repetitive tasks. By utilizing this tool, players can enjoy a more streamlined gaming experience, enabling them to focus on strategy and enjoyment rather than tedious tasks that can detract from the overall fun of the game.
    
    With Aion 2 Cheat, users can expect practical capabilities that allow for easier access to game features, improved character performance, and the ability to automate repetitive tasks. This program is geared towards enhancing the overall gaming experience without compromising the integrity of the gameplay. By providing tools that help players maximize their character's potential and automate time-consuming activities, Aion 2 Cheat aims to create a more enjoyable and efficient gaming environment.
    
    ---
    
    ## System Requirements
    
    | Requirement                  | Details                                         |
    |------------------------------|-------------------------------------------------|
    | **Supported Windows Versions** | Windows 10, Windows 11                          |
    | **Architecture**             | x64                                            |
    | **Processor**                | Not specified; a modern multi-core processor is recommended for optimal performance. |
    | **RAM**                      | Not specified; at least 8 GB is recommended for smooth operation. |
    | **Storage**                  | Not specified; ensure sufficient space is available for installation and updates. |
    | **Permissions**              | Requires administrative privileges for installation and certain features. |
    | **Internet Connection**      | Not specified; a stable internet connection is recommended for real-time updates and community support. |
    | **Dependencies**             | Not specified; ensure Windows is updated to the latest version for best compatibility. |
    
    ### Additional Notes on System Requirements
    
    While the specific hardware requirements are not disclosed, it is important to note that running Aion 2 Cheat effectively will depend on the overall performance of your PC. A system with a modern multi-core processor, at least 8 GB of RAM, and an SSD for faster loading times is sugg
