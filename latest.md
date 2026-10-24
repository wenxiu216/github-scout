📊 开源日报 — 2026-10-24
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  Renhuai123/ziwei-doushu
    ⭐ 7003 stars  |  🍴 1428 forks  |  💻 TypeScript  |  📅 2026-05-01
    🔗 https://github.com/Renhuai123/ziwei-doushu
    📡 来源: trending-daily
    🏷️ bazi, chinese-astrology, divination, fortune-telling, nextjs, open-source, purple-star-astrology, typescript, zi-wei-dou-shu, ziwei-doushu
    📝 紫微斗数开源排盘引擎 — 基于倪海厦《天纪》体系，含完整排盘算法、四化系统、格局知识库、古籍原文数据

    README 摘要:
    # 紫微斗数 · 开源排盘引擎
    
    ### 算法是公开的传统智慧，不应该被锁在围墙里
    
    **中文** · English
    
    **一、项目理念**：紫微斗数是中国传统命理学的瑰宝，倪海厦老师在《天纪》中系统梳理了正宗的紫微斗数体系。我们希望通过技术手段让更多人接触和学习这门学问。
    
    开源排盘算法和知识库，是因为我们相信：**算法是公开的传统智慧，不应该被锁在围墙里**。真正的价值在于解读的深度、用户体验的打磨、以及持续运营的积累。
    
    **二、项目信息**：基于倪海厦《天纪》教学体系的紫微斗数排盘系统，包含完整排盘算法、四化系统、格局知识库、古籍原文数据，以及一套完整开源的紫微斗数解读数据：**v4.0 解读数据集——67.5 万张命盘 × 13 维 = 877 万段解读，正文约 204 亿字，解压后 56.6 GB**（2026-10-15 发布）。
    
    | 数据集 | 命盘 | 解读段数 | 解压后 | 覆盖年份 | 每张盘解读字数 |
    |---|---|---|---|---|---|
    | **v4.0 解读数据集**（2026-10-15） | **674,976** | **8,774,688** | **56.6 GB** | **1950–2026**（只含真实日期） | **约 3.0 万字** |
    | v3.0 样本数据集 | 518,400 | 6,739,200 | 33.1 GB | 1924–1983 | 约 2.1 万字 |
    | 变化 | +30% | +30% | **+71%** | +17 年 | +44% |
    
    v3.0 每张盘解读字数按 2,160 张盘抽样估算，其余数字为全量统计；两版每张盘都是 13 维。
    
    在线体验：metisziwei.com，排盘、AI 解读、命盘历史全部开放。
    
    > **注：关于六亲判断**
    >
    > 紫微斗数在六亲（父母、兄弟、子女等）判断上存在一定局限。倪师在《天纪》中指出：“斗数批六亲本来就比较差一点。”（2上 · 00:25:27）在传统术数中，铁板神数在核对六亲方面有其独特优势（2上 · 00:03:15）；倪师仍以紫微斗数为核心，是因为它能结合地理、环境与人事进行综合判断，形成“上知天文、下知地理、中知人事”的完整体系（2上 · 00:25:43）。因此，与六亲相关的分析仅供参考；metisziwei.com 上父母、兄弟、子女三个维度也附有同样的说明。
    
    ---
    
    ## 目录
    
    | | 章节 | 一句话 |
    |---|------|--------|
    | 一 | 本轮更新 | 13 维断语按倪师原话与《全书》逐句校正，发布 67.5 万命盘 × 13 维解读数据集 v4.0 |
    | 二·新 | 13 维解读数据集 v4.0 | 2026-10-15 新版断语，67.5 万命盘，按年份下载 |
    | 二 | 51.8 万命盘样本数据集 | 规格、下载、用途、许可 |
    | 三 | 快速开始 | 克隆到跑起来 |
    | 四 | 排盘引擎 | 能做到什么、文件怎么分、古籍数据 |
    | 五 | 倪师《天纪·紫微斗数》原话 | 14 讲 + 2 段补充、1848 条，一图看全，每条可回放 |
    | 六 | 界面是一份 Demo | 不是线上那套，差距写明 |
    | 七 | 开源边界 | 什么开源、什么不开源 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  wesbos/3d-model-anything
    ⭐ 1211 stars  |  🍴 202 forks  |  💻 Swift  |  📅 2026-10-21
    🔗 https://github.com/wesbos/3d-model-anything
    📡 来源: 🚀 5天300+星
    📝 Capture iPhone LiDAR and photos, reconstruct editable Three.js rooms, and explore them in a browser.

    README 摘要:
    # 3D Model Anything
    
    Capture a room on an iPhone, then use its geometry and photographs to build an editable Three.js scene with an AI coding agent.
    
    Open the office viewer · App support
    
    This repository includes the **3D Model Anything iPhone app**, a **Three.js viewer**, the **scan-to-threejs agent skill**, and **Wes’s detailed office demo**.
    
    The app records the evidence. The skill guides an agent through measurement, modeling and matched-camera visual comparisons. This is an iterative reconstruction workflow, not a one-click scan-to-perfect-model converter. The current workflow focuses on rooms and interiors.
    
    ## Run the viewer
    
    Use Node.js 22.12+ (or a newer supported release).
    
    ```sh
    npm ci
    npm run dev
    ```
    
    Open http://localhost:5188. Explore the office in dollhouse, walking, overhead, wireframe and knolling views. The playground is at `/play.html?room=office-v4&mode=fpv`.
    
    ```sh
    npm run build
    npm run preview
    ```
    
    The demo includes the reconstructed office and selected textures. Original scans and photo collections are not distributed; Scan and Overlay are disabled for this example. Those modes remain available for your own rooms with reference assets.
    
    ## Capture your own space
    
    See the iPhone app for building with Xcode, device requirements, scanning and sharing. Scanning needs a LiDAR-equipped iPhone or iPad. Non-LiDAR devices can import and review scans.
    
    The app is source-available here; an App Store release is a separate distribution step. Do not assume an App Store download is available yet.
    
    Export a room or session through the system share sheet and extract it into an ignored `data/captures-in//` directory. Exports keep the existing `house-capture/5` contract; changing the app name does not change the files.
    
    ## Use the skill
    
    The skill lives at `.agents/skills/scan-to-threejs/SKILL.md`. Open this repository in an agent that supports local skills and ask it to use **scan-to-threejs** with your extracted export. You can also copy that skill directory into your agent's skill directory; the companion viewer/runtime in this repo is still needed for its capture workflow.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  ⚠️风险  oosexgang/hackios-xnu-kernel
    ⚠️ 命中风险词: poc —— 默认归排除区，需人工确认
    ⭐ 1146 stars  |  🍴 195 forks  |  💻 C  |  📅 2026-10-22
    🔗 https://github.com/oosexgang/hackios-xnu-kernel
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # HackiOS — XNU kernel
    
    **HackiOS** boots Apple's open-source **XNU kernel** (`xnu-8796.121.2`, the kernel of iOS 16.5) on Android phone
    hardware and runs the **unmodified iOS 16.5 user space** on top of it: launchd → backboardd → SpringBoard →
    apps. Our own EFI loader, our own replacements for Apple's closed drivers, a UEFI port, and a Linux Wi-Fi driver
    on a compatibility layer make that possible.
    
    It runs in two places:
    
    - **POCO X5 Pro 5G (redwood, Snapdragon 778G)** — nothing is flashed: the UEFI is started with `fastboot boot`,
      the whole system lives in RAM, and after a reboot the phone is back in Android;
    - **QEMU** (`virt`, aarch64) — the same thing on any Linux computer, no phone needed.
    
    This repository is half of the project:
    
    | Repository | What |
    |---|---|
    | **hackios-xnu-kernel** (this one) | XNU patches, the EFI loader, the UEFI port, Wi-Fi, QEMU scripts, `xl`, prebuilt kernel/loader/UEFI, `common/` scripts |
    | hackios-xnu-userland | our init, injected libraries, launchd jobs, the APFS image builder, the scripts that take iOS out of Apple's IPSW, Metal/Mesa work |
    
    > **No Apple files are in either repository.** `ios165/fetch.sh` downloads the iOS 16.5 IPSW from Apple's own CDN
    > to *your* machine and extracts what is needed there. HackiOS is an independent research project by OOSEX GANG and
    > is not affiliated with, authorised or endorsed by Apple Inc. iOS, iPhone and Apple are trademarks of Apple Inc.
    
    Photographed on the phone, the Adreno GPU drawing (`gpu=1`). More in Screenshots.
    
    ## What works
    
    | Works | Does not work (yet) |
    |---|---|
    | Lock screen, swipe to unlock, home screen with all icons (two pages), stock iOS 16 wallpapers | Cellular, Bluetooth |
    | System gestures: swipe up (home, app switcher), edge swipe (back), Control Center | Charging under our kernel (the phone only discharges) |
    | Apps: Settings, Clock, Calendar, Photos, Notes, Safari and more; widgets (Weather, Calendar) on the phone | Metal for apps (in progress: 293 of 456 system shaders already run on the Adreno, see `docs/air.md` in hackios-xnu-userland) |
    | Phone touchscreen (Goodix GT9916), multitouch, wake on touch; real power and volume keys | App Store content and Apple ID sign-in (no Secure Enclave; FairPlay daemon exits) |
    | Up to 8 CPU cores (`cpus=8`), big core at 2.4 GHz, ~20 s to the lock screen | Video and Live Photo recording |
    | Adreno 642L GPU through Mesa/freedreno (`gpu=1`, OpenGL ES for CoreAnimation) | |
    | Wi-Fi (WCN6750, ath11k): join from Settin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  xevrion/hatchzip
    ⭐ 1110 stars  |  🍴 22 forks  |  💻 Rust  |  📅 2026-10-21
    🔗 https://github.com/xevrion/hatchzip
    📡 来源: 🚀 5天300+星
    🏷️ 7z, archive, cli, crash-safe, disk-space, extract, extractor, gui, rust, tar
    📝 Extract huge archives in place: the archive shrinks as your files hatch, so you only need room for the output. ZIP, 7z, tar, split archives.

    README 摘要:
    HatchZip
    
      Extract huge archives in place. The archive shrinks as your files hatch,
      so you only need free space for the output, not for the output and the archive.
    
      Installation |
      Usage |
      Safety |
      How it works |
      Contributing
    
      
      
      
    
      
    
    A 180 GB game download that unpacks to 200 GB needs 380 GB of disk with WinRAR, 7-Zip or `unzip`, because the archive and everything extracted from it have to exist at the same time. HatchZip needs a little over 200 GB. It extracts the archive from the end and cuts each finished part off the archive file as it goes, so the space the archive gives back is reused for the next files.
    
    It checks that the extraction will fit before it changes anything, keeps a safety margin of free space the whole way through, and can be stopped or crash at any moment and pick up where it left off. It reads ZIP, 7z, tar, `.tar.gz` and split archives.
    
    ### Get it
    
    No coding needed. **Download for Windows** (Windows 10 and 11), or for macOS (Apple Silicon), macOS (Intel) and Linux.
    
    1. Run the installer. Windows may show "Windows protected your PC" because HatchZip is not code-signed yet: choose **More info**, then **Run anyway**.
    2. Right-click the archive, choose **HatchZip**, then **Extract here**. On Windows 11 the menu is under **Show more options**.
    3. Or open HatchZip from the Start menu, open the archive, and choose **Extract**.
    
    HatchZip shows whether the files will fit before it changes anything. The archive is used up as the files come out, so when it finishes, only the extracted files are left.
    
    ## Highlights
    
    The same 200 MB of game data (21 files), packed by the real tools, extracted on a 220 MiB disk with about 50 MB free:
    
    | Archive | `unzip` / 7-Zip | HatchZip |
    |---|---|---|
    | ZIP, 180 MB | `unzip` ran out of space at file 6 of 21 | Finished, every file byte-identical |
    | 7z from 7-Zip 25.01, `-ms=20m` (10 solid blocks) | Needs 380 MB | Finished in 0.64 s, every file byte-identical |
    | 7z split into 5 volumes of 40 MB | Needs 380 MB | Finished; volumes deleted one at a time, peak 210 MB used |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  colinhacks/reylo
    ⭐ 1080 stars  |  🍴 8 forks  |  💻 Rust  |  📅 2026-10-21
    🔗 https://github.com/colinhacks/reylo
    📡 来源: 🚀 5天300+星
    📝 Import .sql files into TypeScript with full type inference and zero codegen.

    README 摘要:
    Import .sql files into your TypeScript code with full type inference
    
      
      
      
      
    
      Read the docs →
    
      
    
    If you have a file like this:
    
    ```sql
    -- get_author.sql
    select u.id, u.name, count(p.id)::int as post_count
    from users u
    left join posts p on p.user_id = u.id
    where u.id = :id::int
    group by u.id
    ```
    
    You can import it directly from a TypeScript file like this:
    
    ```ts
    // main.ts
    import postgres from "postgres";
    import getAuthor from "./get_author.sql";
    
    const db = postgres(process.env.DATABASE_URL);
    
    const author = await getAuthor.run(db, { id: 1 });
    // { id: number; name: string; post_count: number } | null
    ```
    
    Reylo is powered by TypeScript content mappers, introduced in TypeScript 7.1 (currently in beta), which let you dynamically define static types for external file types and integrate them directly into TypeScript compilation.
    
    Reylo is the perfect option for the agent era:
    
    - 💪 **The full power of SQL** — any statement, function, operator or syntax your database supports, in its own dialect.
