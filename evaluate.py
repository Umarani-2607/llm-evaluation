def generate_response(prompt):
    """
    Mock LLM response function.
    Replace this later with a real LLM if needed.
    """
    responses = {
        "hello": "Hello! How can I help you today?",
        "what is cloud computing": "Cloud computing is the delivery of computing services over the internet.",
        "explain ci cd": "CI/CD automates building, testing, and deploying applications.",
        "bye": "Goodbye! Have a great day."
    }

    return responses.get(prompt.lower(), "I'm not sure about that.")


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
