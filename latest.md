📊 开源日报 — 2026-11-23
共发现 3 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  EL4CTEO/fast-anything
    ⭐ 2407 stars  |  🍴 151 forks  |  💻 Rust  |  📅 2026-11-21
    🔗 https://github.com/EL4CTEO/fast-anything
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, ai-agents, claude-code, claude-code-plugin, codex, developer-tools, ffi, mcp, mcp-server, napi-rs
    📝 Don't rewrite it in Rust. Rewrite the 5% that's slow: profile Python, Node or Ruby apps, port the hot functions with your coding agent, prove they behave the same.

    README 摘要:
    Don't rewrite it in Rust. Rewrite the 5% that's slow.
    
      
    
      
      
      
      
      
      
      
    
    Rewriting a whole app in Rust costs months, minute-long compiles and gigabytes of `target/`. Most of the runtime sits in a few functions anyway.
    
    **fast-anything** finds those functions, has your coding agent port *only them* to Rust, proves the port gives the same results on real recorded calls, and swaps it in. One command, fully reversible.
    
    ## Install
    
    ```sh
    npm i -g @el4cteo/fast-anything      # or: cargo install fast-anything
    ```
    
    Ports are compiled with your Rust toolchain (rustup).
    
    ## Use
    
    ```sh
    fast-anything go --agent claude -- python app.py     # or: -- node app.ts / bun app.ts / deno run -A app.ts / ruby app.rb / java App.java / mvn exec:java / gradle run / go run . / php app.php / clang -O2 main.c / Rscript app.R
    ```
    
    Or step by step:
    
    | command | what it does |
    |---|---|
    | `scan -- ` | profiles the app, ranks functions by time × how portable they are |
    | `port [id]` | records up to 500 real calls, creates a one-function Rust crate + `TASK.md` |
    | `verify` | release-builds the port and replays every recorded call |
    | `enable` / `disable` | swaps the Rust in or out (one marked block, removed byte for byte) |
    | `bench` | times the whole app, original vs Rust, interleaved runs |
    | `report` | markdown + SVG card for your PR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  os6/nospeaker
    ⭐ 697 stars  |  🍴 40 forks  |  💻 Swift  |  📅 2026-11-22
    🔗 https://github.com/os6/nospeaker
    📡 来源: 🚀 5天300+星
    🏷️ haptics, macos, swift, trackpad
    📝 make your macbook's trackpad talk using its haptic motor

    README 摘要:
    ```text
    ────────────────────────  a90.com presents  ─────────────────────────
    
        _   __ ____      _____  ____   ______ ___     __ __  ______ ____
       / | / // __ \    / ___/ / __ \ / ____//   |   / //_/ / ____// __ \
      /  |/ // / / /    \__ \ / /_/ // __/  / /| |  / ,
    
    ## 01 / before you start
    
    ```text
    [ mute your mac ]        it still talks; that's the point
    [ put it on a table ]    on your lap it's much quieter
    [ hands off the glass ]  until it asks you to touch it
    ```
    
    **Space** skips a part. **q** or **Ctrl-C** goes to the end.
    
    ## 02 / run it
    
    `[ one line ]`
    
    ```sh
    curl -fsSL a90.com/nospeaker | sh
    ```
    
    Downloads the latest release to `~/.local/bin/nospeaker` and starts the show. `a90.com/nospeaker` points
    to play.sh in this repo, so you can read what it runs first.
    
    `[ download ]`
    
    Grab `nospeaker.zip` from the latest release,
    unzip it and run `./nospeaker` in Terminal. Signed with a Developer ID and notarized by Apple.
    
    `[ from source ]`
    
    Needs Xcode or the Command Line Tools (`xcode-select --install`). Builds one program for Apple Silicon
    and Intel Macs.
    
    ```sh
    git clone https://github.com/os6/nospeaker

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  INK-Q/agy-fast
    ⭐ 643 stars  |  🍴 38 forks  |  💻 TypeScript  |  📅 2026-11-19
    🔗 https://github.com/INK-Q/agy-fast
    📡 来源: 🚀 5天300+星
    🏷️ ai-agent, ai-coding, antigravity, antigravity-cli, antigravity-ide, antigravity-plugins, coding-agent, context-optimization, developer-productivity, developer-tools
    📝 Non-invasive MCP accelerator plugin for Google Antigravity (CLI/Desktop/IDE): cuts LLM turns (-34%), token quota (-31%), and upload traffic (-40%) without affecting native UI or diffs.

    README 摘要:
    # agy-fast
    
    **Latency, Token-Quota & Tool-Call Accelerator Plugin for Google Antigravity**
    
    English · 简体中文 · Quick Start · Benchmarks · MCP Tools · Analysis Report · Changelog
    
    **`agy-fast`** is a zero-dependency, policy-compliant local MCP plugin for **Google Antigravity** (CLI `agy`, Desktop 2.0, and IDE). It cuts agent wall-clock latency, billable token quota, and upload traffic by consolidating high-frequency searches, multi-language symbol outlines, atomic multi-file edits, and build/test checks into batched local calls—and injecting a sub-50 ms workspace snapshot once per session—without altering Antigravity's native UI, diff viewer, modified-files list, checkpoints, or safety checks.
    
    | LLM Turns / 10 Actions | Est. Billable Quota | Tool-Return Upload | Spills & Native UI Impact |
    | :---: | :---: | :---: | :---: |
    | **-33.7%**`-38.2%` ≥150k ctx · `-58.8%` subagents | **-31.5%**`-36.5%` ≥150k ctx · `-54.0%` subagents | **-39.7%**`-53.7%` uncached fresh input | **0**`≤8.8 KB` inline cap · Native diff & UI untouched |
    
      
    
    ## Quick Start
    
    **Requirements:** **Node.js >= 20** (no `npm install` needed — pre-built, unminified zero-dependency ESM bundles are included in `dist/`). Optional: `ripgrep` (`rg`) for faster code search (automatically falls back to pure Node.js when absent).
    
    ### One-Command Install (Recommended)
    
    Installs runtime files to `~/.gemini/config/plugins/agy-fast`, runs `agy plugin validate --strict` and `agy plugin enable agy-fast` when `agy` is installed, and verifies both the MCP server and `SessionStart` hook live:
    
    **macOS / Linux:**
    ```bash
    curl -fsSL https://raw.githubusercontent.com/INK-Q/agy-fast/main/install.sh | sh
    ```
    
    **Windows (PowerShell):**
    ```powershell
    irm https://raw.githubusercontent.com/INK-Q/agy-fast/main/install.ps1 | iex
    ```
    
    > [!TIP]
    > **Activating in Desktop 2.0 / IDE:** Open **Customizations → Installed** in Antigravity, confirm `agy-fast` is enabled, and start a **new session** to load the `SessionStart` hook and MCP tools.
    >
    > **Launching `agy` CLI without approval prompts (optional):** To auto-approve `agy-fast` MCP calls and tool permissions without prompting on every step, start the CLI with:
    >
    > ```bash
    > agy --dangerously-skip-permissions
    > ```
