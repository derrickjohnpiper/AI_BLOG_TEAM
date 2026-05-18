<div align="center">

<!-- LOGO -->
<img src="Banner-Trans-PenInk.png" alt="EchoInk Logo" width="300"/>

# 🖊️ EchoInk — The Blog Team

### *Your words. Your voice. Autonomously written.*

> **A fully autonomous, AI-powered blog writing pipeline** that researches, outlines, writes, and edits long-form content in your exact personal style — while you sleep.

---

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)](https://crewai.com)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-4ECDC4?style=for-the-badge&logo=llm&logoColor=white)](https://ollama.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Open Source](https://img.shields.io/badge/Models-100%25%20Open%20Source-00C851?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://huggingface.co)

</div>

---

## 🌑 What Is EchoInk — The Blog Team?

EchoInk runs a **dark factory** — a fully automated, night-shift AI writing operation powered by five specialized agents. You give them a topic. They give you a 2,500–3,500 word blog post that sounds **exactly like you wrote it.**

No generic AI slop. No cookie-cutter structure. Pure, personalized, publication-ready content.

The crew studies your writing samples, researches the web, builds an outline, drafts every word, and polishes it to perfection — all **without you lifting a finger.**

---

## 🤖 Meet The Crew — Your 5 AI Agents

```
┌─────────────────────────────────────────────────────────────────────┐
│                     THE BLOG TEAM PIPELINE                         │
│                                                                     │
│  [Style Analyst] → [Researcher] → [Outliner] → [Writer] → [Editor] │
│       🎨               🔍            📋           ✍️          ✅     │
└─────────────────────────────────────────────────────────────────────┘
```

| # | Agent | Crew Name | Model | Role |
|---|-------|-----------|-------|------|
| 1 | 🎨 | `Crew_Style_Analyst` | Llama3.2 | Reads your writing samples & builds a Style Profile |
| 2 | 🔍 | `Crew_Researcher` | Qwen2.5-VL | Searches the web for fresh data & company context |
| 3 | 📋 | `Crew_Outliner` | Llama3.2 | Architects the structure — hooks, sections, flow |
| 4 | ✍️ | `Crew_Writer` | Qwen2.5-VL | Drafts the full 2,500–3,500 word post in your voice |
| 5 | ✅ | `Crew_Editor` | Llama3.2 | Polishes length, SEO, style match & final quality |

---

### 🎨 Crew_Style_Analyst
> *"I am the keeper of your voice."*

Reads every sample in your `/samples` directory and creates a detailed **Style Profile** — capturing tone, sentence rhythm, vocabulary, paragraph structure, storytelling patterns, and humor. Every other agent must follow this profile exactly.

- **Model:** `Llama3.2-AgentHermes-Coder-3B` (High-level analysis & management)
- **Tools:** `DirectoryReadTool` (samples folder)
- **Context Window:** 32,000 tokens
- **Max Execution:** 300 seconds

---

### 🔍 Crew_Researcher
> *"Fresh facts. Zero hallucinations."*

Pulls real-time web data, industry stats, company angles, and supporting examples for the given topic. Provides clean research notes with cited sources so the writer never has to guess.

- **Model:** `Qwen2.5-VL-7B-Instruct` (Precision worker, instruction-following)
- **Tools:** `SerperDevTool` (Web Search), `FileReadTool`
- **Context Window:** 32,000 tokens
- **Max Execution:** 300 seconds

---

### 📋 Crew_Outliner
> *"Structure is half the battle."*

Takes the research and style profile to architect a detailed outline — strong hook, logical sections, subheadings, and a compelling CTA. Estimates word count per section and notes which examples to weave in.

- **Model:** `Llama3.2-AgentHermes-Coder-3B` (Strategic thinking)
- **Tools:** None (pure reasoning)
- **Context Window:** 32,000 tokens
- **Max Execution:** 300 seconds

---

### ✍️ Crew_Writer
> *"I am you. I write like you. I think like you."*

Drafts the complete blog post — first person, your voice, your cadence. Short-to-medium paragraphs, personal anecdotes, conversational authority. Never goes below 2,500 words.

- **Model:** `Qwen2.5-VL-7B-Instruct` (High-output precision drafting)
- **Tools:** `FileReadTool` (style profile access)
- **Context Window:** 32,000 tokens
- **Max Execution:** 300 seconds

---

### ✅ Crew_Editor
> *"Nothing ships until it's perfect."*

The final gate. Reviews the draft for length, flow, SEO optimization, style match, factual accuracy, and publication readiness. Adds a meta description and keyword recommendations.

- **Model:** `Llama3.2-AgentHermes-Coder-3B` (Quality management)
- **Tools:** None (editorial review)
- **Context Window:** 32,000 tokens
- **Max Execution:** 300 seconds

---

## 📁 Project Structure

```
AI_BLOG_TEAM/
├── 📂 src/blog_team/           ← CORE APPLICATION (source of truth)
│   ├── crew.py                 ← Agent & task orchestration
│   ├── main.py                 ← CLI entry point
│   ├── __init__.py
│   ├── 📂 config/
│   │   ├── agents.yaml         ← Agent definitions (role, goal, backstory)
│   │   └── tasks.yaml          ← Task definitions & expected outputs
│   └── 📂 tools/               ← Custom tool integrations
│
├── 📂 modelfiles/              ← Ollama Modelfiles for each crew member
│   ├── Crew_Style_Analyst.Modelfile
│   ├── Crew_Researcher.Modelfile
│   ├── Crew_Outliner.Modelfile
│   ├── Crew_Writer.Modelfile
│   └── Crew_Editor.Modelfile
│
├── 📂 samples/                 ← YOUR writing samples (feeds Style Analyst)
│   └── 📂 derrick/             ← Derrick-John's blog posts & writings
│
├── 📂 Website_echoink/         ← EchoInk marketing website
│   ├── index.html
│   ├── ecommerce.html
│   ├── blog.html
│   ├── style.css
│   └── script.js
│
├── 📂 Logo_Asests/             ← Brand assets & logos
│   └── 📂 Logo_EchoInk_Blots/
│
├── streamlit_app.py            ← One-click Streamlit UI
├── pyproject.toml              ← Package config & scripts
├── requirements.txt            ← Python dependencies
└── .env                        ← API keys (never commit this!)
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- A [Serper](https://serper.dev) API key (free tier available)

### 1. Clone the Repository

```bash
git clone https://github.com/derrickjohnpiper/AI_BLOG_TEAM.git
cd AI_BLOG_TEAM
```

### 2. Set Up Python Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -e .
```

### 3. Configure Your Environment

Create a `.env` file in the root directory:

```env
SERPER_API_KEY=your_serper_api_key_here
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=ollama
OPENAI_MODEL_NAME=Crew_Writer
```

### 4. Load the Models into Ollama

```bash
# Build each crew member from their Modelfile
ollama create Crew_Style_Analyst -f modelfiles/Crew_Style_Analyst.Modelfile
ollama create Crew_Researcher    -f modelfiles/Crew_Researcher.Modelfile
ollama create Crew_Outliner      -f modelfiles/Crew_Outliner.Modelfile
ollama create Crew_Writer        -f modelfiles/Crew_Writer.Modelfile
ollama create Crew_Editor        -f modelfiles/Crew_Editor.Modelfile
```

### 5. Add Your Writing Samples

Drop your blog posts, articles, or any writing into:

```
samples/derrick/
```

The more samples the better — the Style Analyst uses everything it finds.

### 6. Launch the Crew

**Option A — Streamlit UI (Recommended):**

```bash
streamlit run streamlit_app.py
```

Open your browser to `http://localhost:8501`, enter your topic, and click **Run The Blog Team** ✨

**Option B — Command Line:**

```bash
python -m blog_team.main
# or
blog_team
```

---

## 🧠 AI Models Used

This project runs **100% open source, locally-hosted models** via Ollama — zero API costs, zero per-token fees.

| Model | File | Size | Role Assignment |
|-------|------|------|-----------------|
| `Llama3.2-AgentHermes-Coder-3B-Q4_K_M` | `.gguf` | ~2GB | Style Analyst, Outliner, Editor |
| `Qwen2.5-VL-7B-Instruct-mmproj-BF16` | `.gguf` | ~1.3GB | Researcher, Writer |

**Why these models?**
- **Llama 3.2 (Hermes)** — Exceptional high-level reasoning, persona management, and structured thinking. Perfect for the manager/editor roles.
- **Qwen 2.5-VL** — Outstanding instruction-following precision with vision capabilities. Ideal for research ingestion and long-form drafting.

Both models configured with:
- ✅ **32,000 token context window** — handles long documents without losing context
- ✅ **Tool calling enabled** — agents can use web search, file reading, and custom tools
- ✅ **No-think mode** — clean, direct output without verbose reasoning chains

---

## 🔧 Modelfile Overview

All modelfiles live in `/modelfiles/`. Each crew member has a dedicated file that configures:

```
modelfiles/
├── Crew_Style_Analyst.Modelfile   ← Llama3.2 | Style analysis | reads samples
├── Crew_Researcher.Modelfile      ← Qwen2.5  | Web research   | SerperDev tool
├── Crew_Outliner.Modelfile        ← Llama3.2 | Blog structure | strategic planner
├── Crew_Writer.Modelfile          ← Qwen2.5  | Long-form drafting | your voice
└── Crew_Editor.Modelfile          ← Llama3.2 | QA + SEO       | final gate
```

Each modelfile includes:
- Dedicated system prompt with role, goal, and backstory
- Tool calling configuration (JSON-schema format)
- Context window set to 32,000 tokens
- Temperature and parameter tuning per role
- Response format templates

---

## 🌐 The EchoInk Website

The marketing website lives in `/Website_echoink/`. It explains the EchoInk service to clients and includes:

- **Landing Page** (`index.html`) — Service overview with dark factory branding
- **E-Commerce Page** (`ecommerce.html`) — Blog packages & pricing
- **Blog Page** (`blog.html`) — Sample posts & "Submit a Blog" form

To view locally, just open `Website_echoink/index.html` in your browser.

---

## 🛠️ Configuration Files

### `src/blog_team/config/agents.yaml`
Defines each agent's **role**, **goal**, and **backstory** — the personality and directive for each crew member.

### `src/blog_team/config/tasks.yaml`
Defines each **task** — what to do, expected output format, which agent handles it, and what context it receives from prior tasks.

### `streamlit_app.py`
One-click browser UI. Enter a topic → click Run → watch the crew work in real time.

---

## 📊 The Pipeline Flow

```
Topic Input
    │
    ▼
🎨 Crew_Style_Analyst
    Reads /samples → Outputs Style Profile
    │
    ▼
🔍 Crew_Researcher
    Searches web → Outputs Research Notes
    │
    ▼
📋 Crew_Outliner ◄── receives: Style Profile + Research Notes
    Builds structure → Outputs Blog Outline
    │
    ▼
✍️ Crew_Writer ◄── receives: Style Profile + Research + Outline
    Drafts full post → Outputs ~3,000 word draft
    │
    ▼
✅ Crew_Editor ◄── receives: Full draft
    Polishes + SEO → Outputs: report.md (final post)
```

---

## 🔮 Coming Soon

- [ ] **Cloud Hosting** — Deploy models via free-tier cloud GPUs (Groq, Hugging Face Spaces, Replicate free tier)
- [ ] **Style Profile Caching** — Skip re-analysis when samples haven't changed
- [ ] **Multi-Author Support** — Maintain separate style profiles per author
- [ ] **Automatic Publishing** — Push finalized posts directly to WordPress / Ghost / Substack
- [ ] **SEO Score Integration** — Real-time keyword density and readability scoring
- [ ] **Web Dashboard** — Full EchoInk client portal

---

## 👤 About the Creator

**Derrick-John Piper** — Founder of EchoInk, builder of AI-powered creative systems, and firm believer that your authentic voice shouldn't have an expiration date just because you're busy.

> *"I built The Blog Team so my writing could keep showing up even when I can't. This is my dark factory — and it runs all night."*

---

## 📄 License

MIT License — See [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with 🖊️ by Derrick-John Piper | Powered by EchoInk**

*The dark factory never sleeps.*

</div>
