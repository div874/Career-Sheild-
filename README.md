# CareerShield AI 🛡️

> **Personal AI Career Intelligence Layer for Students & Job Seekers**
> *Discover relevant opportunities, verify trust/risk signals, evaluate matching evidence, and manage career search funnels.*

---

## 📌 Project Overview
CareerShield AI is an AI product and structured learning project designed to solve key challenges faced by job and internship seekers:
- Opportunity fragmentation across portals & platforms.
- Skill match uncertainty & generic resumes.
- Fraudulent or high-risk internship/job postings.
- Manual contact identification and repetitive outreach writing.
- Lack of career funnel analytics and market intelligence.

---

## 🎯 10-Step Learning Methodology
1. Identify the problem.
2. Understand why the current/simple solution is insufficient.
3. Learn the concept that solves the problem.
4. Understand alternative approaches.
5. Decide why a particular technology is appropriate.
6. Implement it in Python.
7. Test it.
8. Identify limitations.
9. Improve the system.
10. Only then move to the next major concept.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ installed

### 2. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running tests
```bash
pytest
```

---

## 📁 Repository Structure
```
careershield-ai/
├── app/
│   ├── config.py           # Application settings
│   ├── main.py             # FastAPI entrypoint
│   ├── resume/             # PDF parsing & candidate profile schemas
│   ├── jobs/               # Job ingestion, normalization & dataset schemas
│   ├── matching/           # Keyword & semantic matching engines
│   └── risk/               # Trust verification rules & risk scores
├── data/                   # Sample datasets & mock files
├── tests/                  # Automated test suite
├── .env.example            # Sample environment variables
├── requirements.txt        # Python package dependencies
└── README.md               # Documentation
```
