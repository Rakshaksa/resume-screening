# 🤖 AI Resume Screener

An intelligent resume screening pipeline that automatically evaluates candidates against a job description — providing a fit score and human-readable explanation for every decision.

---

## ✨ Features

- 📄 **Skill Extraction** — Pulls skills, experience, and tools directly from resume text
- 🔍 **Job Matching** — Compares candidate profile against job requirements
- 📊 **Fit Scoring** — Assigns an objective score from 0 to 100
- 💬 **Explainability** — Every score comes with clear reasoning and a hiring recommendation
- 🔁 **Full Tracing** — Every pipeline run is tracked and debuggable via LangSmith

---

## 🧠 How It Works

```
Resume + Job Description
        ↓
  Skill Extraction
        ↓
   Job Matching
        ↓
     Scoring
        ↓
   Explanation
        ↓
  LangSmith Trace
```

---

## 🗂️ Project Structure

```
ai-resume-screener/
│
├── prompts/                  # LangChain PromptTemplates
│   ├── extraction_prompt.py
│   ├── matching_prompt.py
│   ├── scoring_prompt.py
│   └── explaination_prompt.py
│
├── chains/                   # LCEL chain definitions
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   └── explaination_chain.py
│
├── data/                     # Sample resumes and job description
│   ├── resumes.py
│   └── job_description.py
│
├── main.py                   # Entry point
├── .env.example              # Environment variable template
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Groq API key → [console.groq.com](https://console.groq.com)
- LangSmith API key → [smith.langchain.com](https://smith.langchain.com)

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/ai-resume-screener.git
cd ai-resume-screener

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=ai-resume-screener
```

### Run

```bash
python main.py
```

---

## 📦 Requirements

```
langchain
langchain-groq
langsmith
python-dotenv
```

Install all at once:
```bash
pip install langchain langchain-groq langsmith python-dotenv
```

---

## 🖥️ Sample Output

```
Processing: Candidate A
──────────────────────────────────────

[Step 1] Extracting skills...
Skills: Python, TensorFlow, PyTorch, SQL, AWS
Experience: 5 years — Data Scientist
Tools: Docker, AWS, Git

[Step 2] Matching...
Matched: Python, SQL, TensorFlow, AWS, 5 years experience
Missing: None
Partial: Soft skills not verifiable from resume

[Step 3] Score: 92/100

[Step 4] Explanation...
This candidate is a strong match for the role. They meet all technical
requirements including deep learning frameworks, cloud experience, and
SQL proficiency. Minor gap in verifiable soft skills.
Recommendation: ✅ Strong Yes
```

---

## 🛠️ Built With

| Technology | Role |
|-----------|------|
| [LangChain](https://langchain.com) | Pipeline orchestration (LCEL) |
| [Groq](https://console.groq.com/) | LLM inference (LLaMA 3.1) |
| [LangSmith](https://smith.langchain.com) | Tracing & debugging |
| Python | Core language |

---
