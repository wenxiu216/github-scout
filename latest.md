📊 开源日报 — 2026-10-18
共发现 6 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  tangency-labs/solidcraft
    ⭐ 4445 stars  |  🍴 529 forks  |  💻 Rust  |  📅 2026-10-07
    🔗 https://github.com/tangency-labs/solidcraft
    📡 来源: 🚀 两周800+星
    🏷️ 3d-modeling, brep, cad, egui, mcp, parametric-cad, rust, step, wasm
    📝 SolidCraft: an open-source parametric 3D CAD application built in pure Rust. Desktop, web, and automation through MCP.

    README 摘要:
    SolidCraft
    
      An open-source parametric 3D CAD application built in pure Rust.
      Sketch, constrain, and build solids with a parametric feature timeline. Change a dimension
      and watch your model rebuild. Run it on your desktop, in your browser, or let AI agents
      model through the built-in MCP server.
    
    [![Download for Windows][badge-windows]][windows-msi]
    [![Download for macOS][badge-macos]][macos-dmg]
    [![Download for Linux][badge-linux]][linux-appimage]
    [![Get it from the Snap Store][badge-snap]][snap-store]
    [![Try it in your browser][badge-web]][web-app]
    
      Website ·
      Download ·
      Try it in the browser ·
      Documentation ·
      Discord ·
      SolidCore
    
      
      
      
      
      
      
      
    
    *A Raspberry Pi 4 case from an empty design: a sketch dimensioned with the board's parameters, extrude, fillet, shell, the rim rounded in one pick, an M2.5 standoff patterned on the 58 × 49 mm hole rectangle, port cut-outs, vent slots, "Pi 4" engraved in DejaVu Sans Bold and a PETG material defined in the design, with its mass in Properties, then height 24 → 32 mm in Parameters and it all rebuilds. 9× playback. Full video, recorded with the demo script.*
    
    ## Download
    
    - **Windows:** download and run the [installer][windows-msi].
      Also for [ARM64][windows-arm64-msi] and [32-bit][windows-x86-msi] PCs, or as a
      [portable zip][windows-portable] that runs without installing.
      With WinGet:
      `winget install bherbruck.SolidCraft`.
    - **macOS:** open the [disk image][macos-dmg] and drag SolidCraft into Applications
      (Apple silicon and Intel).
    - **Linux:** download the [AppImage][linux-appimage], allow it to run as a program and open it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  xscreensaver-official/xscreensaver
    ⭐ 750 stars  |  🍴 20 forks  |  💻 None  |  📅 2026-10-16
    🔗 https://github.com/xscreensaver-official/xscreensaver
    📡 来源: 🚀 5天300+星
    📝 There is no official XScreenSaver GitHub repository.

    README 摘要:
    # There is no official XScreenSaver GitHub repository.
    I am jwz, the author of XScreenSaver, and I do not publish a public source code repository. I publish releases as tar files on the official web site and only there. If you see any other XScreenSaver repository (on GitHub or elsewhere) that has nothing to do with me and you should not trust it.
    
    I welcome submissions and change requests via email. It's fine. You'll get over it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Leonxlnx/earshot
    ⭐ 702 stars  |  🍴 42 forks  |  💻 Python  |  📅 2026-10-15
    🔗 https://github.com/Leonxlnx/earshot
    📡 来源: 🚀 5天300+星
    🏷️ ai-agents, audio, claude-code, mcp, sound-design
    📝 Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

    README 摘要:
    # earshot
    
    **Ears for coding agents.**
    
    **Watch the 22 s launch film** - every sound in it was made
    in code by `earshot forge`; no recordings, no music track.
    
    AI coding agents can now write the code that renders a film, a product demo or a game. They still cannot hear what
    they made. They cannot tell a premium key press from a cheap one, notice that a hit lands 80 ms after the cut, or
    hear that the music swells in the wrong place.
    
    earshot turns sound into evidence an agent can reason about: what a file sounds like in words, how well it fits a
    description, the best moment inside a long recording, whether it is a real recording or code-synthesized, a
    second-by-second listening transcript of a whole film, an annotated picture of it, and a scorecard against
    professional launch films. It runs locally on CPU, as a CLI, a Python API and an MCP server.
    
    With ears, an agent can also **make its own sounds in code** and improve them by listening (`earshot forge`), and
    **translate a recording into code** it can vary (`earshot fit`). Both below.
    
    ```
    $ earshot describe enter.ogg
      0.56 s short transient (attack 3 ms, decays in 190 ms). Sounds most like: a single mechanical keyboard key press
      (z +5.4), a soft key release click (z +3.6) ... [clear reading]. peak -0.1 dBFS, brightness 1.5 kHz ...
    
    $ earshot match key.ogg "a deep thocky mechanical keyboard press" --alts "a clicky blue switch keyboard" "a mouse click"
      -> strong (z +3.7; would rank #2 among 322 vocabulary descriptions) ...
    
    $ earshot find keys.ogg "a single mechanical key press" --top 4
      0:03.94-0:04.19 (0.24 s stroke, z +4.1 strong); 0:10.60-0:10.86 ...
    
    $ earshot critique film.mp4
      VERDICT: close - 21 of 23 scored metrics in range ... FIX FIRST: 1. [major] nothing reaches body level until 0:01.01 ...
    ```
    
    ## What it does
    
    | command | what an agent gets |
    |---|---|
    | `describe FILE` | what it sounds like: calibrated tags (z) with the closest alternative readings, AudioSet labels, measurements |
    | `match FILE QUERY [--alts ...]` | how well a description fits: cosine, z among the vocabulary, a verdict (strong / plausible / weak / no match) with held-out evidence |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  MyLuxy/overdrive
    ⭐ 677 stars  |  🍴 160 forks  |  💻 C++  |  📅 2026-10-14
    🔗 https://github.com/MyLuxy/overdrive
    📡 来源: 🚀 5天300+星
    🏷️ exfat, game-store, homebrew, jailbreak, ps5, ps5-homebrew, reverse-engineering, shadowmountplus
    📝 Overdrive, a PS5 homebrew game store with 1,800+ games.

    README 摘要:
    English ·
      Русский
    
      Your PS5 game store.
      Back from the dead, rebuilt from its own binary, with every line of source in the open.
    
      
      
      
    
      Install ·
      Features ·
      Updates ·
      Troubleshooting ·
      Build it yourself
    
    > [!NOTE]
    > The original Overdrive project has been shut down so I decompiled the last released build,
    > recovered the complete source and rebuilt it.
    
      
    
      
      
    
    ## Features
    
    - **1,800+ games** to discover, with **Top rated**, **New releases** and a featured spotlight
    - **Browse the whole library** with filters, sorting, scores and download sizes at a glance
    - **Downloads straight to the console**, to internal storage or any USB drive, with live speed and storage stats
    - **Favorites**, **search** with an on-screen keyboard, and a **Files** page to see and clean up what's on your drives
    - **13 languages**: English, Deutsch, Español, Français, Português (Brasil), Русский, Bahasa Indonesia, 日本語, 简体中文, العربية, اردو, हिन्दी, বাংলা
    - **Updates itself**: a new version installs from the console, no PC needed
    - Made for the controller: L1 R1 to switch sections, ✕ to select, ○ to go back
    
    ## Install in four steps
    
      
    
    ### Before you start

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  anujasid/blender-ai-mcp-addon
    ⭐ 654 stars  |  🍴 188 forks  |  💻 Python  |  📅 2026-10-15
    🔗 https://github.com/anujasid/blender-ai-mcp-addon
    📡 来源: 🚀 5天300+星
    🏷️ ai-assistant, blender, blender-addon, blender-ai, blender-automation, blender-extension, blender-mcp, blender-plugin, blender-python, blender-scripting
    📝 AI assistant and MCP server for Blender: visual chat, scene tools, multi-agent workflows. Works with OpenAI, ChatGPT, Claude, Gemini, Ollama, OpenCode. Blender AI addon and plugin, copilot for 3D, bpy Python scripting, MCP integration.

    README 摘要:
    # mcp-for-blender-pro
    
    ### Your Blender scene. Your AI models. One creative workspace.
    
    **An AI assistant for Blender that can inspect your scene, build objects, edit materials, find assets and carry out multi-step workflows—with a visual chat workspace and a built-in Model Context Protocol (MCP) server.**
    
    Download · Getting started · Connections and agents
    
    ## Turn a creative brief into scene operations
    
    Start with an idea. Ask the assistant to inspect your scene, create a product-display layout, arrange objects, assign materials or prepare an export. Follow its actions in the conversation and inspect the result in the viewport preview. Keep working in Blender throughout the process.
    
    **mcp-for-blender-pro brings conversation, scene tools, model choice and agent workflows together.** It is designed for artists who want faster iteration, technical artists who automate repetitive work, and developers connecting AI tools to Blender.
    
    ## Why choose mcp-for-blender-pro?
    
    | Capability | What it gives you |
    |---|---|
    | **Blender-aware assistance** | Scene and object inspection gives the assistant context before it acts. |
    | **A visual Studio workspace** | Chat, scene objects, viewport snapshots, approvals and a task board in a companion window. |
    | **Your choice of AI** | Connect supported cloud providers, local Ollama models or compatible custom endpoints. |
    | **Saved connections** | Keep work and personal connections separate, including multiple keys for the same provider. |
    | **One assistant or a team** | Use a single model for quick changes, or managers, workers and reviewers for structured tasks. |
    | **Built-in MCP server** | Connect OpenCode and other clients supporting authenticated Streamable HTTP MCP. |
    | **21 scene tools** | Create, inspect, edit, capture, search assets, consult Blender APIs and export scenes. |
    | **Multilingual menus** | Choose English, German, French, Spanish or Chinese for the main interface. |
    
    ## From a quick edit to an agent team
    
    Use **Single assistant** for direct, conversational work. For larger tasks, configure a **Team chain** with individual responsibilities, instructions and models.
    
    - **Manager:** breaks the request into assignments and acceptance criteria.
    - **Workers:** perform the assigned scene operations.
    - **Reviewers:** inspect results and approve work or return specific findings.
    
    Tasks run sequentially so scene edits stay ordered. A blocked task gets one correction attempt; a second failed review stops the workf

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  Tencent-Hunyuan/Hy-Memory
    ⭐ 615 stars  |  🍴 59 forks  |  💻 Python  |  📅 2026-10-15
    🔗 https://github.com/Tencent-Hunyuan/Hy-Memory
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    Hy Memory
    
    Production-grade dual-system cognitive memory for LLM agents.
    
      
      
      
      
      
      
      
      
      
      
    
    English | 中文
    
    **Hy Memory** (Official Website) is a production-grade dual-system cognitive memory engine and Python SDK (`hy-memory`) for self-evolving LLM agents, providing specialized memory pipelines across three task scenes: hierarchical long-term cognitive memory for **Chat**, two-layer fact and reusable-experience memory for **Working**, and version-evolution diff-chain tracking for **Coding**. Built on top of Hy Memory, **MemHub** is a local-first desktop and CLI product that unifies conversation history and coding traces from user-authorized AI applications (such as Claude Code, Cursor, Codex, OpenCode, and Qwen Code) into a single managed runtime and local data directory, enabling governed cross-application memory recall.
    
      
      MemHub Demo Video
    
    ---
    
    ## Latest News
    
    * *[new]* 🔥🔥🔥 **[2026-10]**: 🚀 **Released** **Hy Memory 2.0 (`hy-memory==2.0.3`)** on PyPI and open-sourced the **Hy-Memory** monorepo together with **MemHub**!
    * *[new]* 🔥🔥🔥 **[2026-10]**: 🚀 **Open-sourced** **Hy-Memory-30B-A3B** on Hugging Face along with its technical report on attributed reinforcement learning for long-term memory writing!
    * *[new]* 🔥🔥 **[2026-09]**: 📊 **Released** **CMB: A Coding Memory Benchmark for Long-Horizon and Interleaved Coding Agents** (submitted to **ICLR 2027**).
    * *[new]* 🔥🔥 **[2026-08]**: 🎉 **Accepted** at **EMNLP 2026**: **Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents**!
    * 🔥 **[2026-05]**: 🌟 **Initial Release** Released **Hy Memory 1.0**, our first-generation dual-system cognitive memory framework for self-evolving LLM agents.
    
    ---
    
    ## Papers
    
    Welcome to the **Hy Memory Research Family**, covering cognitive chat memory, long-horizon coding memory, and RL-trained memory writing models:
    
    > **Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents** *(Accepted at **EMNLP 2026**)*  
    > **TL;DR:** Proposes the dual-process (System 1 + System 2) cognitive memory architecture for **Chat**, organizing personal memory into an 8-layer hierarchy (raw dialogues, atomic facts, summaries, schemas, and prospective intentions) with conflict reconciliation and cross-domain schema induction.  
