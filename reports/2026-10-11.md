📊 开源日报 — 2026-10-11
共发现 6 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  storytold/effectcraft
    ⭐ 4710 stars  |  🍴 2165 forks  |  💻 Rust  |  📅 2026-10-01
    🔗 https://github.com/storytold/effectcraft
    📡 来源: 🚀 两周800+星
    📝 无描述

    README 摘要:
    EffectCraft
    
      Motion graphics and visual effects; an open-source, clean-room reimplementation of Adobe After Effects, rebuilt in pure Rust.
    
      A free, open-source compositor in the spirit of After Effects: compositions, layers,
      keyframes, 306 effects, layer styles, expressions, 3D cameras and lights, and a render queue, native on macOS,
      Windows and Linux, and in the browser. Young, moving fast, and already usable.
    
      
      
      
    
      
    
      EffectCraft on getartcraft.com ·
      ArtCraft ·
      All Crafting Apps
    
      
    
    > [!NOTE]
    > **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
    > games &mdash; if you make things, you're one of us. **Come say hi on Discord.**
    
      What it is ·
      Animate ·
      Effects ·
      3D ·
      Export ·
      Agents ·
      Get started ·
      Status ·
      How it's made ·
      Downloads ·
      The Crafting Apps ·
      License
    
    ## What EffectCraft is
    
    EffectCraft is for animated titles, motion graphics and compositing work: the kind of thing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  t4t5/omdrop-owl
    ⭐ 1659 stars  |  🍴 119 forks  |  💻 Shell  |  📅 2026-10-08
    🔗 https://github.com/t4t5/omdrop-owl
    📡 来源: 🚀 5天300+星
    🏷️ airdrop, omarchy, opendrop
    📝 airdrop for non-apple devices

    README 摘要:
    # omdrop-owl
    
    https://github.com/user-attachments/assets/b195ce4c-e078-49be-bc13-44a72b6dc189
    
    The radio half of omdrop for
    machines without Apple's Broadcom Wi-Fi. AWDL runs in userspace through
    OWL on a monitor interface, and omdrop's own
    receiver and sender run over it unchanged. First target: the MediaTek MT7925
    (`mt7925e`), as in the Framework 13, where AirDrop works in both directions
    while Wi-Fi stays connected. An Intel AX201 works in an "exclusive" mode that
    takes Wi-Fi away while the machine is visible.
    
    It is a sibling of omdrop-awdl,
    the Broadcom radio package, and plugs into omdrop the same way: helpers in
    `/usr/lib/omdrop` that the omdrop CLI and panel call. The contract is described
    in omdrop's `docs/radio-backend.md`.
    
    ## How it works
    
    The Wi-Fi station stays associated, and AWDL shares its channel:
    
    1. **AWDL runs on the access point's own channel**, which has to be 6, 44 or
       149 (AWDL's channels). An iPhone spends a large share of its AWDL time slots
       on those channels, so the radio never has to leave the AP.
    2. **A monitor interface carries the station's MAC**, and OWL runs on it with
       `-S intersect`, advertising only the phone's slots on that channel.
    3. **The MT7925 sends injected frames from the station's MAC regardless**, and
       the station interface ACKs the phone's unicast to that MAC, so no "active"
       monitor interface is needed.
    4. OWL creates `awdl0`. omdrop's receiver binds to it, and omdrop-awdl's
       `awdl-airdrop-adv.py --plain` announces `_airdrop._tcp` on it every few
       seconds (`--plain`, because OWL adds the AWDL encapsulation itself).
    
    Cards that can't share the AP's channel use exclusive mode
    instead.
    
    From omdrop-awdl we reuse, unmodified, the tools that only talk to `awdl0` or
    BlueZ: `send-to-peer`, `airdrop-send.py`, `ble-airdrop-adv.py`,
    `awdl-airdrop-adv.py`, `awdl-mdns-respond.py` and the modules they import. They
    are fetched at a pinned commit by `tools/stage.sh`, never committed here.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  storytold/deckcraft
    ⭐ 1515 stars  |  🍴 711 forks  |  💻 Rust  |  📅 2026-10-07
    🔗 https://github.com/storytold/deckcraft
    📡 来源: 🚀 5天300+星
    📝 Presentations and slide shows: an open-source, clean-room reimplementation of Microsoft PowerPoint in pure Rust. Part of the ArtCraft Crafting Apps.

    README 摘要:
    DeckCraft
    
      Presentations and slide shows; an open-source, clean-room reimplementation of Microsoft PowerPoint, rebuilt in pure Rust.
    
      Build decks with themes, layouts, shapes, pictures, tables, charts, transitions and animations,
      open and save PowerPoint files, and present them full screen. Native on macOS, Windows, Linux
      and FreeBSD, and in the browser. Every button is also a command that the CLI and AI agents
      (through MCP) can drive.
    
      
      
      
      
    
      
    
      DeckCraft on getartcraft.com ·
      ArtCraft ·
      All Crafting Apps
    
    > [!NOTE]
    > **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
    > filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
    > last week. If you make things, you're one of us. **Come say hi on Discord.**
    
      
    
      What works ·
      Getting started ·
      Agents, CLI and MCP ·
      Roadmap ·
      Downloads ·
      The Crafting Apps ·
      License
    
    ## What works today
    
    DeckCraft is in alpha, heading for beta (see the roadmap).
    Today it can:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  storytold/soundcraft
    ⭐ 1404 stars  |  🍴 750 forks  |  💻 Rust  |  📅 2026-10-07
    🔗 https://github.com/storytold/soundcraft
    📡 来源: 🚀 5天300+星
    📝 An open-source, clean-room reimplementation of Avid Pro Tools in pure Rust

    README 摘要:
    SoundCraft
    
      Recording, editing and mixing audio; an open-source, clean-room reimplementation of Avid Pro Tools, rebuilt in pure Rust.
    
      A complete digital audio workstation that runs natively on macOS, Windows, Linux and FreeBSD, and
      in the browser. Multitrack editing, a full mixer with plugins, sends and automation, MIDI, recording
      and bouncing, and every action scriptable from the command line or by an AI agent.
    
      
      
      
      
      
    
      
    
      SoundCraft on getartcraft.com ·
      ArtCraft ·
      All Crafting Apps
    
      
      
      The Edit window: tracks, waveforms, MIDI, rulers, markers and the transport, playing the built-in demo song (every sound in it is synthesised by SoundCraft itself).
    
    > [!NOTE]
    > **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
    > filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
    > last week. If you make things, you're one of us. **Come say hi on Discord.**
    
      What it does ·
      Getting started ·
      Agents &amp; scripts ·
      How it's built ·
      Status ·
      Downloads ·
      The Crafting Apps ·
      License
    
    ## What it does
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ranxianglei/billion-context
    ⭐ 804 stars  |  🍴 75 forks  |  💻 TypeScript  |  📅 2026-08-06
    🔗 https://github.com/ranxianglei/billion-context
    📡 来源: trending-weekly
    🏷️ dsh-plugin
    📝 A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single sessions (billions of tokens).上下文压缩插件，兼顾小窗口(100k上下文足矣)省token(省5倍token)和超长会话(数月级别几十亿token单会话)。billion-context is all you need

    README 摘要:
    # billion-context
    
    English | 中文
    
    Context-compression plugin — billion-context is all you need.
    
    small context windows (100K is enough) · 5× fewer tokens · month-long single sessions (billions of tokens) · high compression quality
    
    npm install -g billion-context --prefix=~/.local
    
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    &nbsp;
    
    ---
    
    > **Cache health at a glance:** a healthy session keeps a **95–97%** prefix-cache hit rate — compression itself costs ≤2%. Sustained lower? Check attribution with `/acp` or `/acp-cache` (see FAQ); usual causes, in order: upstream cache TTL expiry · model switch · a bili bug (please report) · other/unknown.
    
    ## Community
    
    QQ Group:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  koronto11/ludo-npc-ai
    ⭐ 31 stars  |  🍴 1 forks  |  💻 JavaScript  |  📅 2026-10-05
    🔗 https://github.com/koronto11/ludo-npc-ai
    📡 来源: 🎬 互动叙事/创作 | 新建 | branching narrative game
    🏷️ agent-skills, ai-tools, dialogue-editor, game, game-development, gamedev, interactive-fiction, narrative-design, npc, python
    📝 A visual workspace for game narratives and NPCs. Build worlds, arrange scenes and characters, edit branching dialogue, review AI drafts, and rehearse stories. Collaborate with your own AI through bilingual Skills.

    README 摘要:
    Build the world. Meet the cast. Play the conversation.
    
      A local narrative workbench for NPCs, branching dialogue and scene direction.
      Bring your own AI. Keep the author's final say.
    
      
      
      
      
      
    
      English · 简体中文
      Overview · Workbench · AI Skills · Quick start · Example · Your data · Docs
    
    ---
    
    ## A story deserves more than a wall of text
    
    **NPCs AI Studio turns a story outline into a visible authoring workspace.** Establish the world's facts, build a cast, place characters in scenes, connect dialogue choices and rehearse what the player encounters. Use it for RPG quests, interactive fiction, narrative prototypes and NPC dialogue planning.
    
    Your own AI can prepare the material through the bilingual Skills. The built-in model connection can generate focused candidates. Both workflows leave you in control of the final text.
    
    > **World brief → Characters → Scenes & appearances → Dialogue & events → Review → Rehearsal → Handoff**
    
    | Workspace | What you can create |
    | :--- | :--- |
    | **🌍 World & levels** | Shared world facts and writing style, with region details and local story premises kept in each level. |
    | **👥 Cast & relationships** | Key, supporting and background characters; editable profiles, knowledge, groups, quick notes and relationship connections. |
    | **🎬 Scene direction** | Scene tracks and time/plot-phase anchors. Place the same character several times without copying their profile. |
    | **💬 Dialogue cards** | NPC lines, player choices, conditions, effects, branches, shared destinations and endings in one connected canvas. |
    | **✦ AI & review** | Character, story, dialogue and text candidates; readable review cards, field differences and protected author facts. |
    | **▶ Play & delivery** | Temporary dialogue play, scene story flows, local records, reusable templates and JSON / Markdown / CSV exports. |
    
    ## Inside the workbench
    
    ### 01 · Direct the scene
    
    Arrange appearances along scene tracks and story time. NPC groups collect background characters while keeping each member's profile and dialogue independently editable. Muted green groups, plum events and copper character controls make the canvas easier to read.
    
    One level · two scenes · three characters · a once-only event. Actual application capture.
