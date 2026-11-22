📊 开源日报 — 2026-11-22
共发现 14 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ItsNotRexed/Leonida
    ⭐ 7854 stars  |  🍴 626 forks  |  💻 Python  |  📅 2026-11-20
    🔗 https://github.com/ItsNotRexed/Leonida
    📡 来源: 🚀 5天300+星
    📝 Leonida Is A Native PC Recompilation Of The Xbox Version Of Grand Theft Auto 6

    README 摘要:
    Leonida
      
    
    Grand Theft Auto VI (Xbox Series) running natively on Windows, built on your PC from your own copy.
    
      Status |
      How to build |
      How it works |
      Want to help? |
      Credits |
      License |
      Discord
    
    Leonida is a static recompilation project. The Xbox Series CPU is x86-64 like a PC, so the game's code is loaded
    and run natively, and the console's system software is reimplemented. The console's precompiled RDNA2 GPU programs
    are translated to SPIR-V for Vulkan. The game's models, textures and audio are read from your package. All of this
    happens **on your PC, from your own copy of the game**.
    
    > [!IMPORTANT]
    > This repository **does not contain the game, keys or an executable**, and it does not explain how to get them. You
    > need your own copy, with its files already readable on disk. Nothing here decrypts or works around any protection.
    > Everything the build creates (the generated shaders, extracted assets, the runtime folder and your saves) comes
    > from your game and stays on your PC. Never share those files.
    
    Discord: https://discord.gg/rexed
    
    ## Project status
    
    **Early. The game does not boot yet.** Everything that can be done without the game's executable is in place, so
    work on booting can start as soon as one is available to a developer.
    
    | What | Status |
    |---|---|
    | Finding and checking your copy (Xbox Series 1.0.2.1) | ✅ Works |
    | Shaders: carve, unpack native RDNA2 code, disassemble | ✅ All 26,503 |
    | Shaders: RDNA2 → SPIR-V translation | ✅ **All 26,503** (disassembled with LLVM 21; LLVM 23 leaves 1,471 rejected for now, #644): 2,236 VS, 12,101 PS, 2,689 CS, 9,282 mesh, 195 geometry. All pass `spirv-val`, with a per-shader metadata index for pipeline creation. ⚠️ 21,545 are wave64: exact on 64-wide subgroups (AMD). On 32-wide subgroups (NVIDIA, Intel), compute and mesh shaders are exact with wave64 emulation (`--wave64-emulate`, on by default there); cross-half wave ops in vertex, pixel and geometry shaders are still approximate |
    | Shader translator checked on a real GPU | ⚠️ The hand-written GPU tests (vertex fetch, texture sampling, exports, ALU ops, partial-register ops, barycentrics, wave-uniform branches, compute LDS/barriers/buffer stores, wave64 masks) have been run on more than 30 GPU and driver combinations, with results in #166: NVIDIA Turing, Ampere, Ada and Blackwell (Windows and Linux); AMD GCN3, RDNA1, RDNA2, RDNA3 and RDNA4 (Windows driver and RADV); Intel Gen9 (ANV); Apple M1 (MoltenVK, no geometry or

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  R0Y00/Xbox2Windows
    ⭐ 1039 stars  |  🍴 101 forks  |  💻 Python  |  📅 2026-11-20
    🔗 https://github.com/R0Y00/Xbox2Windows
    📡 来源: 🚀 5天300+星
    🏷️ d3d12, directx-raytracing, scarlett, static-recompilation, windows, xbox, xbox-series-x
    📝 GTA VI static recompilation research for x64 Windows. Source-built EXEs run on Windows, and two translated pixel shaders match reference outputs on hardware and WARP. Full-game startup is unverified.

    README 摘要:
    # Xbox2Windows
    
    Xbox2Windows researches **GTA VI static recompilation** from Xbox Series X|S (Scarlett) to x64 Windows. Windows, the mapped original and the recompiled build agree on output and exit codes for source-built programs. Two pixel shaders from the inspected package compiled to desktop DXIL and matched reference pixels on an RTX 4060 Laptop GPU and WARP. Execution of the title's CPU code, full-game startup and frame rate remain unverified.
    
    **Help wanted on Windows:** Claim a batch of GPU reports in #1. Link the reports you will cover, check each original log against the hardware table, and submit one README PR for the batch. You can do this without a GPU or a local copy of the package.
    
    The CPU experiments translate source-built x64 functions from PE machine code through C++ to Windows executables and DLLs. A source-built EXE runs from its translated entry through a nested call that reads and writes globals in a relocated image, then through a named DLL import. Windows, the mapped original and the recompiled EXE agree on the import arguments, output and exit code for two inputs and two initial data states. A CRC-32 console program also runs from its PE entry through a separately compiled C++ checksum routine and Windows UCRT stream I/O, with matching output and exit codes on all three runners. A multi-record archive reader runs from standard Zig startup through recompiled blast decompression to process exit, including the callback sequence and partial-record cleanup. The shader experiment translates selected gfx1013 pixel shaders through HLSL to desktop DXIL. Other experiments test the Windows runtime, render recovered texture levels and read script state data.
    
    New to the project? The pinned guide in GitHub Discussions will help you choose a first contribution. Ask build and debugging questions in Development Q&A.
    
    Snapshot measured at c04e65a. For the latest chart, open the newest successful Windows checks run on main and download `coverage-dashboard` from Artifacts.
    
    ## Current results and open work
    
    | Area | Result on Windows | Open question or contribution |
    |---|---|---|
    | FidelityFX upscaler | The recompiled provider creates 11 resources at 720p → 1080p and a twelfth with the debug flag. On RTX 4060 Laptop and WARP, both the per-resource indices and the returned loader and provider handles passed. Recompiled graph pass 26 wrote the RCAS intermediate and the recompiled RCAS shader read it with five integer texel loads per output. Passes 24

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  omonkeyz/xbox-emulator
    ⭐ 935 stars  |  🍴 47 forks  |  💻 Rust  |  📅 2026-11-21
    🔗 https://github.com/omonkeyz/xbox-emulator
    📡 来源: 🚀 5天300+星
    📝 Progress notes for running Xbox Series X|S builds on PC (TomBox + rage9)

    README 摘要:
    # Xbox Emulator
    
    **Running the Xbox Series X|S library on PC. A continuation of drycheetah84/TomBox.**
    
    The runtime reimplements the console's platform layer (Xbox-flavoured Direct3D 12, precompiled RDNA2 shaders, unified-memory textures, system libraries) so dumped, already-decrypted Xbox Series X|S builds run as normal Windows processes. It is not tied to any single title. This repo tracks our continuation — new titles brought up, platform calls extended, shader stages unlocked.
    
    Uses legally obtained, already-decrypted dumps. The runtime does no key extraction or package decryption.
    
    **Source code:** the emulator's Rust workspace is in this repo: `crates/`, `tools/` and `Cargo.toml`. It contains no game files, binaries or build output.
    
    **Contributing:** pull requests are welcome, especially console library functions still marked missing in the library map. See CONTRIBUTING.md. Licensed MIT OR Apache-2.0.
    
    ## Status
    
    One square per item. The first four sections use upstream's definitions so the numbers stay comparable: green = done, amber = partial (a stub, a forwarder, or not verified to work), grey = not done — imported system functions of the Fortnite EXE, Direct3D 12.x interface methods, RDNA2 shader instructions the decoder knows, and the eight shader stages (mesh and amplification still grey). The fifth section is ours and covers Xbox console libraries only: the exports of the console OS DLLs (EmbeddedXvd of every analysed title, union, so the newest console OS sets the surface) that no same-named DLL in a PC's C:\Windows\System32 exports, so console-only DLLs (d3d12_xs, xg_xs, xmem, AcpHal, chad, xapu, xcrdapi, the *legacy variants, ...) count in full and modified PC DLLs (kernel32, advapi32, mfplat, ...) only for their console-only exports, plus the GDK wrappers the emulator redirects; plain Windows DLLs (ntdll, msvcrt, ucrtbase, combase, ...) are not shown. Coloured implemented / forwarded / stub / missing; lighter squares are functions an analysed title imports. Per-title import coverage likewise counts only imports from console libraries. Generated by tools/progress/gen.py; per-function tables in docs/LIBRARY_MAP.md, headline numbers in tools/progress/summary.json.
    
    ## Milestones
    
    Counted live by `tools/progress/gen.py`; full table with evidence in docs/MILESTONES.md.
    
    | Milestone | State |
    |---|---|
    | All imported system functions covered (671/671) | done |
    | Full title shader sweep translated (105,506/105,506) | done |
    | All Direct3D 12.x m

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  HuangAntimony/Hoshi-Reader-Android
    ⭐ 501 stars  |  🍴 44 forks  |  💻 Kotlin  |  📅 2026-04-28
    🔗 https://github.com/HuangAntimony/Hoshi-Reader-Android
    📡 来源: 📖 阅读/内容平台 | 活跃 | audiobook text-to-speech
    🏷️ android, anki, audiobook, audiobook-player, dictionary, ebook-reader, eink, epub, epub-reader, japanese
    📝 Hoshi Reader Android: Japanese EPUB reader with Yomitan lookup, Anki mining, audiobook read-along, text-to-speech(TTS), and e-ink support.

    README 摘要:
    # Hoshi Reader Android
    
    **English** | 简体中文
    
    Hoshi Reader Android is an EPUB reader for Japanese, English, Chinese, and Korean immersion, with Yomitan lookup, Anki card creation, audiobook read-along, text-to-speech, and e-ink display options.
    
    This project brings Hoshi Reader to Android with native UI and Android-specific features.
    
      
        
        
        
        
      
      
        
        
        
        
      
      
        
        
        
        
      
    
    ## Features
    
    ### Bookshelf
    
    - Import EPUBs in batches or recursively from folders, organize custom shelves, and export EPUBs.
    - Show, blur, or hide book covers.
    - Use book covers as lock-screen wallpapers or e-ink device screen savers.
    
    ### Reading
    
    - Read vertically or horizontally in paginated or continuous mode; paragraph mode centers each page's content and adds sentence limits, optional text animation and tap-blank-to-advance.
    - Download or import fonts and customize layout and furigana display.
    - Search the full book, jump between chapters, and turn pages with volume keys.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  CocoSgt/riemann-hypothesis-lean
    ⭐ 476 stars  |  🍴 74 forks  |  💻 Lean  |  📅 2026-11-20
    🔗 https://github.com/CocoSgt/riemann-hypothesis-lean
    📡 来源: 🚀 5天300+星
    📝 Mirror of Levent Alpöge's Lean proof of the Riemann Hypothesis (with Claude). All credit to Levent Alpöge. Source: alpo.ge

    README 摘要:
    # Riemann Hypothesis in Lean — by Levent Alpöge (with Claude)
    
    > **The proof in this repository is the work of Levent Alpöge.**
    > On 2026-11-20 he announced that, working with Claude, he had found a proof of the Riemann Hypothesis that extends to the Generalized Riemann Hypothesis (for Dirichlet L-functions), and that the argument is fully formalized in Lean without assumptions.
    > All credit belongs to Levent Alpöge (and Claude). This repository is an unmodified mirror of the Lean code he published, put on GitHub so that people and agents can browse, clone and check it.
    >
    > 本仓库只是镜像：证明由数学家 Levent Alpöge（和 Claude 合作）完成，署名与一切功劳归他。代码原样搬运，没有改动。
    
    - Announcement (4 pages): https://alpo.ge/remark.pdf
    - Original download: https://alpo.ge/lean.tar.gz.part01 … https://alpo.ge/lean.tar.gz.part14
    - Merged archive in this repo's Releases
    
    **Status.** As of mirroring (2026-11-20), no independent build or review of this code has been published. Treat it as a claimed proof until it has been compiled and checked.
    
    ---
    
    ## What is proved
    
    The target statements are short. Read these two files first.
    
    `src/Main.lean`
    
    ```lean
    import Statements
    import Supplements.Kernels.MainTheoremsAll
    
    theorem riemannHypothesis : RiemannHypothesis := rhOfAll
    
    theorem riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := rhOfAll
    
    theorem LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf := allChi
    
    theorem LFunction_eq_zero_re : DirichletLZerosOnLine := claimAll.2.1
    
    theorem LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine := critAll
    ```
    
    - `RiemannHypothesis` is **Mathlib's own definition** (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, line 185 at the pinned commit), so the headline statement comes from Mathlib, outside this repository:
    
      ```lean

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  leanprover-community/riemann-hypothesis
    ⭐ 469 stars  |  🍴 100 forks  |  💻 Lean  |  📅 2026-11-20
    🔗 https://github.com/leanprover-community/riemann-hypothesis
    📡 来源: 🚀 5天300+星
    📝 Independent Comparator setup for the Lean formalization of the Riemann Hypothesis (Alpöge, 2026-11-20)

    README 摘要:
    # riemann-hypothesis
    
    A Comparator setup and community build cache for the Lean formalization that
    claims a proof of the Riemann Hypothesis, and of GRH for Dirichlet L-functions, announced on
    2026-11-20 at .
    
    The first commit, `40e56bab`, is the submitted Lean source exactly as published. Since then,
    cleanup pull requests have removed 10,724 of its 175,187 files and edited 18; the
    notes list them. Check out `40e56bab` for the original. This
    repository also adds Comparator files and cache infrastructure:
    
    | File | What it is |
    |---|---|
    | `src/Challenge.lean` | the five theorems, stated in a file that imports only Mathlib |
    | `comparator.json` | the Comparator config |
    | `export-targets.txt` | the declarations to export |
    | `verification/` | our notes, and the results once there are some |
    | `scripts/` | public Lake cache configuration and reproducible bootstrap/publishing tools |
    
    ## Using the build cache
    
    Fetch and restore Mathlib and this project's compiled modules:
    
    ```bash
    lake exe cache get
    lake build --no-build
    ```
    
    The cache settings are in `lakefile.toml`; no user configuration is needed. The first command
    fetches both caches anonymously and extracts the oleans to `.lake/build`. It prefers a successful
    CI build matching the current clean source, configuration, dependency manifest and toolchain;
    documentation-only commits can reuse the same cache. Otherwise it tries the original published
    cache. The second command checks the default build targets without compiling them. The original
    project cache is 4.94 GB and contains portable Lean outputs and generated C. Subsequent ordinary
    builds compile changed modules and their dependents.
    
    The community cache includes outputs from **untrusted pull requests and volunteer machines**.
    Download integrity checks do not verify proofs. Use an independent fresh build when you need
    to trust the result.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  pusparajpaudel155/aion-2-trainer-tool
    ⭐ 303 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-11-21
    🔗 https://github.com/pusparajpaudel155/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, desktop
    📝 Aion 2 Trainer Tool: Ready-to-Run AI Prompt Engineering Setup

    README 摘要:
    # ⚡ Aion 2 Trainer Tool — Advanced AI Prompt Engineering for Windows
    
    ### 📦 PowerShell Install Button
    
       
    
    ---
    
    Aion 2 Trainer Tool delivers a complete standalone setup for Aion 2, putting advanced AI prompt engineering tools directly on your desktop with zero friction. Everything runs locally out of the box, no account juggling or extra setup rituals required. Built for players who want sharp, configurable prompt tooling without wrestling with dependencies.
    
    ## ✅ Before You Start
    
    - **OS:** Windows 10 / 11
    - **Shell:** PowerShell 5.1+ or PowerShell 7+
    - **Network:** internet access to download the script
    - **Privileges:** standard user
    
    ## Features
    
    - **AI Prompt Engineering Suite** — a desktop-ready workspace for building, refining, and testing advanced AI prompts without leaving the app. Structured templates and live iteration keep your workflow tight.
    - **Fully Standalone Setup** — runs on its own. No online activation, no account juggling, no dependency chain to babysit. Install it, launch it, game on.
    - **Open-Access Build** — every capability ships unlocked out of the box. No paywalls, no tier gating, no hidden upsells between you and the tools.
    - **Desktop-Native Performance** — tuned for Windows x64 with a lightweight footprint, so it stays out of your way while you play.
    - **Gaming-Grade Enhancement Layer** — purpose-built boosters and modifiers that extend what the base experience gives you, with sensible defaults and clear controls.
    - **Quick-Start Ready** — a guided first-run flow gets you from cold launch to active session in minutes, not hours.
    - **Profile Configuration** — save, swap, and reload your setups per game or per session. One config, zero rework.
    - **Built-In Diagnostics** — health checks and status readouts help you confirm everything is wired up correctly before you dive in.
    - **Modular Design** — toggle individual tools on or off so the toolkit matches how you actually play.
    - **Local-First Architecture** — your configs and session data stay on your machine. Nothing phones home unless you tell it to.
    - **Actively Maintained** — regular polish passes keep the toolkit aligned with the current game build and desktop platform.
    
    ## How it works
    
    Aion 2 Trainer Tool runs as a self-contained desktop app — no launcher dependencies, no background services, no waiting on the cloud. You point it at your game, the prompt engineering layer spins up, and you get a clean control surface tuned for Aion 2.
    
    **The pipeline, step by step:**
    
    1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  Astrmira/TriviumDB
    ⭐ 193 stars  |  🍴 14 forks  |  💻 Rust  |  📅 2026-03-26
    🔗 https://github.com/Astrmira/TriviumDB
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | vector database embeddin
    🏷️ agent, agent-memory, ai-agents, ann, database, embedded-database, graph, knowledge-graph, long-term-memory, memory
    📝 A lightweight embedded database engine that natively fuses vector search, graph, and document-oriented metadata within a single storage kernel — ready to use the moment data is written.

    README 摘要:
    # TriviumDB
    
    **向量 × 图谱 × 文档 —— 三位一体的 AI 原生嵌入式数据库**
    
    **Battle-tested in mission-critical, air-gapped environments.**
    
    > _Trivium_：拉丁语，意为"三条道路的交汇"。
    
    > TriviumDB 为 Agent、RAG 和知识图谱应用提供进程内的向量、图与文档存储。宿主应用通过 Rust、Python 或 Node.js API 管理数据库实例、查询和持久化。
    
    **中文** | **English**
    
    当前正式版本为 **0.9.3**，提供可选的 Pelorus 双曲检索和 QuIVer SSD 请求级 I/O 计量，并改进 WAL 恢复、TQL 查询与图预算。完整变更、Rust 接口调整及升级步骤见双语发布说明。
    
    SDK 的支持范围见 SDK 正式接口清单，历史磁盘格式通过外部迁移工具升级。
    
    向量检索的数据选型与精确检索入口见 QuIVer 适用范围。
    
    ---
    
    ## 一句话介绍
    
    TriviumDB 是一个用纯 Rust 编写的**嵌入式三模数据库引擎**，将**向量检索（Vector）**、**属性图谱（Graph）**和**文档型元数据（Document）**原生融合在同一个存储内核中。Rom 将向量与 Payload 内嵌于主文件；默认 Mmap 模式分离向量与 Payload。内核将索引和登记文本集中在 `.idx`，文件组通过统一发布协议保持一致。
    
    我们的目标是成为 **AI 应用领域的 SQLite**：
    
    - 🧪 **自由 DIY 混合查询管线** —— TQL 把向量召回、属性索引、图扩展、图算法、路径、集合代数、迭代、聚合与重排变成可自由编排的算子，由确定性 Cascades 优化器统一规划
    - 📊 **四类持久化属性索引** —— Hash / Ordered ART / Composite ART / Roaring Bitmap，等值、范围、前缀、复合条件与低基数集合运算全部索引加速
    - 🧮 **内嵌图算法库** —— PageRank / WCC / SCC / K-Core / Articulation Points / Triangle Count / Local Clustering Coefficient / HITS / Harmonic Centrality / Node Similarity / Leiden / Betweenness / Degree / Label Propagation / SA-PPR 可在查询内直接调用，并支持 Weighted Dijkstra、Yen K-Shortest Paths、PairSet 与有界路径/集合算子
    - 🗃️ **Rom/Mmap 双模式切换** —— Rom 内嵌向量与 Payload；Mmap 将其分离到 `.vec` 与 generation 化 `.pld.`，按需映射；完整备份使用快照 API
    - ❄️ **Payload 冷热分层** —— 已发布 raw JSON 留在 mmap 冷基础层，新写入/更新进入内存 delta，解析结果进入有硬字节上限的 LRU Cache；ANN/BQ/Exact 候选阶段零 Payload 解析
    - 🔗 **节点即一切** —— 每个节点天然同时拥有限定长度的稠密向量、稀疏文本倒排词频、元数据和图关系，通过全局唯一 NodeId 关联
    - 🧠 **为 AI 而生** —— 可选启用“AC自动机+BM25稀疏文本”与“Dense Vector稠密向量”的**多路召回**来触发图谱扩散检索，并内置多层认知管线（FISTA / DPP / PPR）
    - 🛡️ **四层数据安全保障** —— 原子替换 + WAL日志 + 事务干跑验证（Dry-Run）+ Mmap COW 隔离，`.flush_ok` v3 绑定 `.tdb/.vec/.pld`，发布前旧代备份与撤销日志支持中断恢复；备份增加磁盘读写与临时空间，损坏输入仍 fail-closed，详见恢复协议
    - 🐍 **Python / Node.js 原生** —— `pip install` 或 `npm install` 后直接使用，类 MongoDB 查询语法
    - ⚡ **高性能检索** —— rayon 并行暴力搜索（小规模 100% 精确）+ 自研 ANN 索引 **QuIVer**；默认采用无训练 SM-L2 导航与余弦精排，按向量工作量动态触发（209–834 节点）
    - 💾 **SSD 友好** —— Append-Only WAL + 后台 Compaction 线程 + QuIVer 索引独立持久化，杜绝随机写入磨损
    - 🔒 **共享只读打开** —— 多进程 Reader 共享锁并发查询已完成代际，Writer 继续保持排他锁与 WAL 安全边界
    - 🧩 **类型化访问能力** —— Rust `DatabaseReader` 在编译期隐藏写 API，`DatabaseWriter` 保留完整嵌入式写能力
    - 🔄 **不可变代际切换** —— `GenerationStore` 原子发布 current，跨进程 Reader 租约保护旧代安全回收，且不写入只读制品目录

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  Cloudcode04/runway-ml-pro-win
    ⭐ 168 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-21
    🔗 https://github.com/Cloudcode04/runway-ml-pro-win
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai, ai-art, ai-tools, ai-writing, artificial-intelligence, generative-ai, image-generation, llm, pro, runway
    📝 Runway - AI video generation platform for text-to-video synthesis, image animation and motion brush editing on Windows 10/11

    README 摘要:
    Runway ML Pro: AI Video Generation and Motion Editing for Windows
    
    A Windows reference and setup guide for the Runway ML Pro AI video platform, generative capabilities, system profile, and the first-run workflow.
    
      
      
      
    
      
        
          
          
        
      
    
    ## Introduction
    
    Runway ML Pro is an AI video generation platform that lets you turn written prompts into short video clips, animate still images, and direct motion with brush-based controls on Windows 10 and 11. It is used by beginners who are exploring generative media for the first time and by professionals who need fast concept footage, storyboard previews, or stylized visual assets. Instead of a traditional timeline-first editor, it centers on generative models you guide with text and reference imagery.
    
    When you use Runway ML Pro, you get a set of creative tools built around text-to-video synthesis, image-to-video animation, and the Motion Brush, which lets you paint regions of a frame and define how they should move. A typical workflow starts with a prompt or a source image, moves into generation and refinement, and ends with exporting a clip you can bring into a conventional editor. The platform also includes tools for inpainting, style transfer, and camera motion so you can iterate quickly on an idea.
    
    In the broader generative video field, Runway ML Pro sits among the tools that made prompt-driven video accessible to non-specialists, and it continues to evolve as new models and controls are added. Its cloud-based processing means your results depend more on your connection and creative direction than on a high-end local GPU. A large community shares prompts, workflows, and tutorials, which makes it easier to learn the platform's quirks and get consistent output.
    
    ## System Requirements
    
    | Requirement | Details |
    |-------------|---------|
    | **Supported Windows Versions** | Windows 10, Windows 11 |
    | **Architecture** | x64 |
    | **Processor** | Modern dual-core or better, quad-core recommended for smooth browser and app performance |
    | **RAM** | 8 GB minimum, 16 GB recommended |
    | **Storage** | Around 1 GB for the desktop app plus space for downloaded clips and assets |
    | **Permissions** | Administrative privileges may be required |
    | **Internet Connection** | Required for activation, generation, and updates |
    | **Dependencies** | Current Chromium-based browser or the desktop app, hardware-accelerated graphics with up-to-date drivers, DirectX 11 or later |
    
    To get the best performance from Runway ML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  Aroralayla99/capcut-seedance-win
    ⭐ 161 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-21
    🔗 https://github.com/Aroralayla99/capcut-seedance-win
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai-agent, ai-automation, ai-prompts, audio, capcut-exe, codex-skill, langchain, mastra, mem0, openrouter
    📝 CapCut Seedance - AI video generation tool for text-to-video synthesis, image animation and motion effects on Windows 10/11

    README 摘要:
    CapCut Seedance: AI Video Generation Tool for Windows
    
    A Windows reference and setup guide for CapCut Seedance, text-to-video synthesis, image animation, and the first-run workflow.
    
      
      
      
    
      
        
          
          
        
      
    
    ## Introduction
    
    CapCut Seedance is an AI video generation tool built for Windows that turns text prompts and still images into short motion clips. It is used by beginners who want to produce social-ready footage without prior editing experience, and by professionals who need fast concept previews or b-roll drafts before committing to a full production. The tool sits on the CapCut video pipeline, so what you generate can flow directly into a familiar editing timeline.
    
    When you use CapCut Seedance you get a prompt-driven workspace, image animation with motion controls, and a set of preset visual effects that cover common short-form styles. A typical session moves from writing a prompt or dropping in a reference image, through previewing and adjusting motion strength, to exporting a clip you can refine further. The workflow is designed to be iterative, so you can regenerate variations quickly instead of rebuilding a project from scratch.
    
    In the wider AI video space, Seedance represents the growing class of consumer-facing synthesis tools that blend generative models with a conventional editor. Its value comes from that combination: the model provides the raw motion, and the editor gives you control over timing, framing, and delivery. The community around CapCut tutorials, prompt-sharing threads, and template packs continues to expand, and the underlying models evolve with each release.
    
    ## System Requirements
    
    | Requirement | Details |
    |-------------|---------|
    | **Supported Windows Versions** | Windows 10, Windows 11 |
    | **Architecture** | x64 |
    | **Processor** | Intel Core i5 (10th gen or newer) or AMD Ryzen 5 equivalent; Core i7 / Ryzen 7 recommended |
    | **RAM** | 8 GB minimum / 16 GB or more recommended |
    | **Storage** | 4 GB for installation plus 10 GB or more for generated clips and cache |
    | **Permissions** | Administrative privileges may be required |
    | **Internet Connection** | Required for activation and updates |
    | **Dependencies** | DirectX 11 or newer, Visual C++ Redistributable, current GPU driver with hardware video encoding support |
    
    For the smoothest experience, pair CapCut Seedance with a discrete GPU that has at least 6 GB of video memory and a recent driver, since generation and rendering both lean heavily on GPU ac

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  JieFedorov81/runway-ml-pro-win
    ⭐ 160 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-21
    🔗 https://github.com/JieFedorov81/runway-ml-pro-win
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai, ai-art, ai-tools, ai-writing, artificial-intelligence, generative-ai, image-generation, llm, pro, runway
    📝 Runway - AI video generation platform for text-to-video synthesis, image animation and motion brush editing on Windows 10/11

    README 摘要:
    Runway ML Pro: AI Video Generation and Motion Editing for Windows
    
    A Windows reference and setup guide for the Runway ML Pro AI video platform, generative capabilities, system profile, and the first-run workflow.
    
      
      
      
    
      
        
          
          
        
      
    
    ## Introduction
    
    Runway ML Pro is an AI video generation platform that lets you turn written prompts into short video clips, animate still images, and direct motion with brush-based controls on Windows 10 and 11. It is used by beginners who are exploring generative media for the first time and by professionals who need fast concept footage, storyboard previews, or stylized visual assets. Instead of a traditional timeline-first editor, it centers on generative models you guide with text and reference imagery.
    
    When you use Runway ML Pro, you get a set of creative tools built around text-to-video synthesis, image-to-video animation, and the Motion Brush, which lets you paint regions of a frame and define how they should move. A typical workflow starts with a prompt or a source image, moves into generation and refinement, and ends with exporting a clip you can bring into a conventional editor. The platform also includes tools for inpainting, style transfer, and camera motion so you can iterate quickly on an idea.
    
    In the broader generative video field, Runway ML Pro sits among the tools that made prompt-driven video accessible to non-specialists, and it continues to evolve as new models and controls are added. Its cloud-based processing means your results depend more on your connection and creative direction than on a high-end local GPU. A large community shares prompts, workflows, and tutorials, which makes it easier to learn the platform's quirks and get consistent output.
    
    ## System Requirements
    
    | Requirement | Details |
    |-------------|---------|
    | **Supported Windows Versions** | Windows 10, Windows 11 |
    | **Architecture** | x64 |
    | **Processor** | Modern dual-core or better, quad-core recommended for smooth browser and app performance |
    | **RAM** | 8 GB minimum, 16 GB recommended |
    | **Storage** | Around 1 GB for the desktop app plus space for downloaded clips and assets |
    | **Permissions** | Administrative privileges may be required |
    | **Internet Connection** | Required for activation, generation, and updates |
    | **Dependencies** | Current Chromium-based browser or the desktop app, hardware-accelerated graphics with up-to-date drivers, DirectX 11 or later |
    
    To get the best performance from Runway ML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  josephyoung28/capcut-seedance-win
    ⭐ 148 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-21
    🔗 https://github.com/josephyoung28/capcut-seedance-win
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai-agent, ai-automation, ai-prompts, audio, capcut-exe, codex-skill, langchain, mastra, mem0, openrouter
    📝 CapCut Seedance - AI video generation tool for text-to-video synthesis, image animation and motion effects on Windows 10/11

    README 摘要:
    CapCut Seedance: AI Video Generation Tool for Windows
    
    A Windows reference and setup guide for CapCut Seedance, text-to-video synthesis, image animation, and the first-run workflow.
    
      
      
      
    
      
        
          
          
        
      
    
    ## Introduction
    
    CapCut Seedance is an AI video generation tool built for Windows that turns text prompts and still images into short motion clips. It is used by beginners who want to produce social-ready footage without prior editing experience, and by professionals who need fast concept previews or b-roll drafts before committing to a full production. The tool sits on the CapCut video pipeline, so what you generate can flow directly into a familiar editing timeline.
    
    When you use CapCut Seedance you get a prompt-driven workspace, image animation with motion controls, and a set of preset visual effects that cover common short-form styles. A typical session moves from writing a prompt or dropping in a reference image, through previewing and adjusting motion strength, to exporting a clip you can refine further. The workflow is designed to be iterative, so you can regenerate variations quickly instead of rebuilding a project from scratch.
    
    In the wider AI video space, Seedance represents the growing class of consumer-facing synthesis tools that blend generative models with a conventional editor. Its value comes from that combination: the model provides the raw motion, and the editor gives you control over timing, framing, and delivery. The community around CapCut tutorials, prompt-sharing threads, and template packs continues to expand, and the underlying models evolve with each release.
    
    ## System Requirements
    
    | Requirement | Details |
    |-------------|---------|
    | **Supported Windows Versions** | Windows 10, Windows 11 |
    | **Architecture** | x64 |
    | **Processor** | Intel Core i5 (10th gen or newer) or AMD Ryzen 5 equivalent; Core i7 / Ryzen 7 recommended |
    | **RAM** | 8 GB minimum / 16 GB or more recommended |
    | **Storage** | 4 GB for installation plus 10 GB or more for generated clips and cache |
    | **Permissions** | Administrative privileges may be required |
    | **Internet Connection** | Required for activation and updates |
    | **Dependencies** | DirectX 11 or newer, Visual C++ Redistributable, current GPU driver with hardware video encoding support |
    
    For the smoothest experience, pair CapCut Seedance with a discrete GPU that has at least 6 GB of video memory and a recent driver, since generation and rendering both lean heavily on GPU ac

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  emilioevans/runway-ml-pro-win
    ⭐ 144 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-21
    🔗 https://github.com/emilioevans/runway-ml-pro-win
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    📝 Runway - AI video generation platform for text-to-video synthesis, image animation and motion brush editing on Windows 10/11

    README 摘要:
    (README 获取失败)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#14  KPVADALIYA/DeepAI-For-Fake-PC
    ⭐ 64 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-17
    🔗 https://github.com/KPVADALIYA/DeepAI-For-Fake-PC
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai-avatar, ai-face-replacement, character-swap, deep-live-cam, deep-live-cam-api, deepfacelab, deepfake-detection, deeptrace, face-restoration, faceforensics
    📝 AI-powered media creation tool for image and video transformation, synthetic media generation, and advanced visual effects.

    README 摘要:
    # 🎭 DeepFake AI — AI-Powered Media Creation
    
    DeepFake AI is an artificial intelligence-based media creation tool designed to explore modern image and video manipulation technologies. It combines AI-powered processing with digital media customization, allowing users to experiment with visual transformations and create engaging multimedia content.
    
    From image-based effects to advanced video processing, the technology behind DeepFake AI demonstrates how artificial intelligence can be used to transform and enhance digital media.
    
    Whether you're interested in AI technology, digital creativity, or multimedia experimentation, this project provides an introduction to some of the possibilities offered by modern generative AI.
    
    ## 📌 Overview
    
    Artificial intelligence is changing the way digital images and videos are created, edited, and processed. Tasks that once required specialized software and considerable editing experience can now be explored through AI-powered tools.
    
    DeepFake AI focuses on AI-assisted media transformation. Depending on the supported models and available functionality, users can work with visual inputs, experiment with different processing options, and explore various media-generation techniques.
    
    The project is intended for users interested in understanding and experimenting with AI-based visual technologies.
    
    ## 📥 Download
    
    Ready to explore AI-powered media processing?
    
    Visit the download page below to access the available project files, documentation, and setup instructions.
    
    **Download:** GET DEEPFAKE AI
    
    ## 🚀 Main Features
    
    ### 🧠 AI-Powered Processing
    Use artificial intelligence to analyze and process visual media. AI-based models can recognize visual patterns and apply transformations according to the selected processing method.
    
    ### 🖼️ Image Transformation
    Explore image-processing capabilities and AI-assisted visual modifications. Supported operations may include facial feature processing, image enhancement, and visual adjustments.
    
    ### 🎬 Video Processing
    Work with video content using supported AI processing methods. Depending on the implementation, processing options may include frame analysis, visual transformations, and media export.
    
    ### ⚙️ Customization & Settings
    Configure available processing parameters to influence the final output. Depending on the model, options may include resolution, quality, processing preferences, and output formats.
    
    ### ✨ AI Technology Exploration
    Experiment with modern generative AI concepts and learn ho
