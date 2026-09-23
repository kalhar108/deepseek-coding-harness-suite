# DeepSeek Harness Mastery & Autonomous ML AutoResearch Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Node: v20+](https://img.shields.io/badge/Node-v20%2B-green.svg)](https://nodejs.org/)
[![DeepSeek: Cordis/v1](https://img.shields.io/badge/DeepSeek-Cordis%2Fv1-purple.svg)](https://github.com/deepseek-ai/deepseek-harness)

A comprehensive, production-ready coding harness suite featuring a progressive Coding Harness from scratch (Part A), the DeepSeek Harness Cordis Architecture with Creator Mode & 7 Custom Plugins (Part B), and an End-to-End Autonomous ML Research Harness (Part C), complete with an interactive Web Workbench Studio and complete recorded video walkthrough deliverables.

---

## 📹 YouTube Video Walkthroughs & Code Demos

| Part | Title & Deliverable | YouTube Video Link | Key Walkthrough Highlights |
|------|---------------------|--------------------|----------------------------|
| **Part A** | Progressive Coding Harness from Scratch | [📺 Watch Part A Full Walkthrough Video](https://www.youtube.com/watch?v=Lu1UWqWTbQg) | Code walkthrough of minimal LLM loop, diff patcher, AST parser, and SWE-bench pass@1 evaluator. |
| **Part B** | DeepSeek Harness & 7 Creator Mode Plugins | [📺 Watch Part B Creator Mode & Plugin Demo](https://www.youtube.com/watch?v=Lu1UWqWTbQg) | Creator Mode single-prompt hot-loader, trajectory event streaming, and execution of 7 custom plugins. |
| **Part C** | Custom ML AutoResearch End-to-End Harness | [📺 Watch Part C AutoResearch Demo Video](https://www.youtube.com/watch?v=Lu1UWqWTbQg) | Automated hypothesis generation, PyTorch training loop, metric logger, and paper synthesis. |

> 💡 **Interactive Local Presentation Players**: Run `python3 scripts/generate_video_demos.py` to launch full-length recorded walkthrough video presentations directly in your browser (`videos/part_a_walkthrough.html`, `videos/part_b_walkthrough.html`, `videos/part_c_walkthrough.html`).

---

## 🚀 Key Architectural Components

### PART A: Progressive Coding Harness from Scratch
Built step-by-step from minimal principles to a production CLI/API agent harness:
1. `part_a_harness/step1_minimal_agent.py`: ~20-line Pydantic AI style REPL loop using OpenRouter API / Gemini Pro with tool call execution.
2. `part_a_harness/step2_tool_harness.py`: Advanced filepatching (`apply_patch`), AST syntax parser (`parse_ast`), and context window manager (`ContextWindowManager`).
3. `part_a_harness/step3_eval_harness.py`: SWE-bench / HumanEval automated evaluation harness measuring Pass@1 accuracy.
4. `part_a_harness/step4_full_harness.py`: Full production CLI agent with colorized log streaming, token budget tracking, and session telemetry export.

```
[User Instruction] ──> [Context Manager (Prunes Token Budget)] ──> [Unified LLM Client (OpenRouter/Gemini)]
                                                                               │
                                                                               ▼
[Test Evaluation] <── [Sandbox Execution] <── [Diff Patch & AST] <── [Tool Call Router]
```

---

### PART B: DeepSeek Harness Architecture & 7 Customized Plugins
Built upon the DeepSeek Harness Cordis Specification (`agent.cordis.yml`) with Creator Mode and append-only Trajectory Event Streams (`event_stream.py`):

#### 🧩 7 Active Custom Plugins
1. **`dsh-second-brain`** *(Built from Scratch #1)*: Personal Knowledge Network (PKN) memory graph, daily notes logger, and semantic context injection.
2. **`dsh-dino-game`** *(Built from Scratch #2)*: Floating canvas mini-game widget hot-loaded into `shell.overlay` slot via single-sentence prompt.
3. **`dsh-cursor-debug`**: Official Cursor Debug Mode preset protocol (`Test -> Inject Logs -> Reproduce -> Root Cause -> Verify Fix`).
4. **`dsh-seo-workbench`**: Page SEO auditor, metadata validator, and search engine indexability checker.
5. **`dsh-mirage-vfs`**: Mirage RAM virtualized filesystem isolating file mutations from disk (`ctx.fs`, `ctx.shell`).
6. **`dsh-autopilot`**: Long-run durable task graph with evidence gate verification and restart safety.
7. **`dsh-team-canvas`**: Multi-agent collaboration canvas with Leader, Worker, and Adversarial Verifier roles.

#### 🪄 Creator Mode Demonstration
```bash
# Generate a plugin from a single sentence without leaving the chat interface:
python3 part_b_deepseek_plugins/run_dsh_demo.py
```
> Prompt: *"Add a dinosaur jumping game floating in the bottom right"*  
> Result: Hot-loads `DinoGamePlugin` into the `shell.overlay` slot and registers it in `agent.cordis.yml`.

---

### PART C: Autonomous End-to-End ML Research Harness
An autonomous machine learning research agent inspired by Sakana AI and Karpathy's AutoResearch:
- **Hypothesis Formulation**: Formulates quantitative hypothesis based on input dataset.
- **PyTorch/Scikit-Learn Training Sandbox** (`experiment_runner.py`): Executes training iterations, records loss curves, validation accuracy, F1 score, and training speed.
- **Trajectory Logger** (`research_logger.py`): Logged to `research_log.json`.
- **Academic Paper Generator** (`report_generator.py`): Automatically synthesizes LaTeX/Markdown research paper (`paper_draft.md`).

---

## 🛠️ Quick Start & Installation

```bash
# 1. Clone & Enter Project Directory
git clone https://github.com/dlmastery/deepseek-coding-harness-suite.git
cd deepseek-coding-harness-suite

# 2. Configure Environment Keys (Optional, fallback mock mode available)
cp config.example.env .env
# Edit OPENROUTER_API_KEY or GEMINI_API_KEY inside .env

# 3. Install Dependencies
pip install -r requirements.txt
```

### Running Demonstrations & Tests

```bash
# Run Master Test Suite (Verifies Part A, B, and C)
python3 scripts/run_all_tests.py

# Run Part A: Progressive Harness Demo
python3 part_a_harness/step4_full_harness.py

# Run Part B: DeepSeek Harness & 7 Plugins Demo
python3 part_b_deepseek_plugins/run_dsh_demo.py

# Run Part C: AutoResearch End-to-End ML Demo
python3 part_c_autoresearch/run_autoresearch_demo.py

# Generate Video Walkthrough Presentations
python3 scripts/generate_video_demos.py
```

### Launching the Web Workbench Studio

```bash
npm start
# Opens interactive workbench UI at http://localhost:8080
```

---

## 📂 Repository Directory Tree

```
deepseek-coding-harness-suite/
├── README.md                           # Master GitHub Documentation & Video Links
├── requirements.txt                    # Python dependencies
├── package.json                        # Node scripts & Web Workbench server
├── config.example.env                  # API Key configuration file
├── part_a_harness/                     # PART A: Progressive Coding Harness
│   ├── llm_client.py                   # Unified OpenRouter / Gemini API Client
│   ├── step1_minimal_agent.py          # Step 1: ~20-line LLM loop + tool parsing
│   ├── step2_tool_harness.py           # Step 2: AST, File Diffing, Sandbox
│   ├── step3_eval_harness.py           # Step 3: SWE-bench Pass@1 Evaluator
│   └── step4_full_harness.py           # Step 4: Full CLI & Telemetry Harness
├── part_b_deepseek_plugins/            # PART B: DeepSeek Harness Architecture
│   ├── harness_core/                   # Core DSH Engine & Creator Mode
│   │   ├── agent.cordis.yml            # Cordis manifest specification
│   │   ├── creator_mode.py             # Prompt-to-plugin generator
│   │   └── event_stream.py             # Append-only trajectory stream
│   ├── plugins/                        # 7 Custom Plugins
│   │   ├── dsh_second_brain.py         # [Scratch 1] PKN memory graph
│   │   ├── dsh_dino_game.py            # [Scratch 2] Single-prompt UI game widget
│   │   ├── dsh_cursor_debug.py         # Cursor Debug Mode preset
│   │   ├── dsh_seo_workbench.py        # SEO audit & index checker
│   │   ├── dsh_mirage_vfs.py           # Mirage RAM virtual filesystem
│   │   ├── dsh_autopilot.py            # Task graph & evidence gates
│   │   └── dsh_team_canvas.py          # Multi-agent collaboration canvas
│   └── run_dsh_demo.py                 # Interactive Part B demo script
├── part_c_autoresearch/                # PART C: Custom ML AutoResearch Harness
│   ├── autoresearch_harness.py         # Research agent orchestration engine
│   ├── experiment_runner.py            # Model training & metric extraction
│   ├── research_logger.py              # Trajectory & research_log.json logger
│   ├── report_generator.py            # Academic paper_draft.md builder
│   └── run_autoresearch_demo.py        # Interactive Part C demo script
├── web_dashboard/                      # Master Web Workbench Studio UI
│   ├── index.html                      # Glassmorphism dark mode layout
│   ├── style.css                       # Modern CSS styling & animations
│   └── app.js                          # Real-time visualizer logic
├── videos/                             # Video Walkthrough Presentations
│   ├── part_a_walkthrough.html         # Interactive Video Demo Player Part A
│   ├── part_b_walkthrough.html         # Interactive Video Demo Player Part B
│   └── part_c_walkthrough.html         # Interactive Video Demo Player Part C
└── scripts/
    ├── generate_video_demos.py         # Video Walkthrough Generator
    └── run_all_tests.py                # Master Automated Verification Suite
```

---

## 📜 License & Acknowledgments
Licensed under the [MIT License](LICENSE).  
Inspired by DeepSeek Harness (`cordis/v1`), Mini-SWE-agent, Decoding AI, and Sakana AI AutoResearch.
