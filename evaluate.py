import os
import requests


def generate_response(prompt):
    """
    Generates a response using either:
    - Mock LLM (default)
    - Real LLM (if API key is provided)
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # -------- MOCK MODE (default & safe) --------
    if not api_key:
        responses = {
            "hello": "Hello! How can I help you today?",
            "what is cloud computing": "Cloud computing is the delivery of computing services over the internet.",
            "explain ci cd": "CI/CD automates building, testing, and deploying applications.",
            "bye": "Goodbye! Have a great day."
        }
        return responses.get(prompt.lower(), "I'm not sure about that.")

    # -------- REAL LLM MODE --------
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

test_cases = [
    {
        "name": "Greeting",
        "prompt": "hello",
        "criteria": ["help"]
    },
    {
        "name": "Cloud knowledge",
        "prompt": "What is cloud computing",
        "criteria": ["internet", "services"]
    },
    {
        "name": "CI/CD understanding",
        "prompt": "Explain CI CD",
        "criteria": ["automates", "deploy"]
    },
    {
        "name": "Fallback behavior",
        "prompt": "random question",
        "criteria": ["not sure"]
    }
]


def evaluate_response(response, criteria):
    """
    Scores a response based on how many criteria keywords are met.
    """
    score = 0
    for keyword in criteria:
        if keyword.lower() in response.lower():
            score += 1

    return score, len(criteria)


def run_evaluation():
    print("\nRunning advanced LLM evaluation...\n")

    total_score = 0
    total_possible = 0

    for case in test_cases:
        response = generate_response(case["prompt"])
        score, possible = evaluate_response(response, case["criteria"])

        total_score += score
        total_possible += possible

        print(f"Test: {case['name']}")
        print(f"Prompt: {case['prompt']}")
        print(f"Response: {response}")
        print(f"Score: {score}/{possible}")

        if score == possible:
            print("Result: PASS\n")
        else:
            print("Result: PARTIAL / FAIL\n")

    print("========== SUMMARY ==========")
    print(f"Total Score: {total_score}/{total_possible}")
    print(f"Accuracy: {(total_score / total_possible) * 100:.2f}%\n")


if __name__ == "__main__":
    run_evaluation()
