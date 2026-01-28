# LLM Evaluation Framework

A lightweight evaluation framework designed to test and score Large Language Model (LLM)
responses across multiple prompt scenarios.

This project focuses on **AI quality, testing, and evaluation**, rather than model training.

---

## 🚀 What This Project Demonstrates

- Designing evaluation workflows for LLM-based systems
- Scoring AI responses using keyword-based criteria
- Comparing expected vs actual behavior
- Supporting both mock and real LLM backends
- Secure handling of API keys using environment variables

---

## 🧠 How It Works

1. A set of test cases is defined with:
   - Prompt text
   - Evaluation criteria (keywords)
2. The evaluation engine:
   - Generates a response (mock or real LLM)
   - Scores the response against expected criteria
3. Each test produces:
   - PASS / FAIL result
   - Per-test score
4. A final summary reports overall accuracy

---

## 🔁 LLM Modes

### Mock Mode (Default)
- Uses predefined responses
- Safe and deterministic
- No external dependencies
- Ideal for CI and local testing

### Real LLM Mode (Optional)
- Uses a real LLM via API
- Enabled only when an API key is provided
- Securely reads the API key from environment variables
- No secrets are stored in code or repository

---

## ▶️ Running the Evaluation

```bash
python evaluate.py
