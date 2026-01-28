def generate_response(prompt):
    """
    Mock LLM response function.
    This simulates an AI response for evaluation purposes.
    """
    responses = {
        "hello": "Hello! How can I help you today?",
        "what is cloud computing": "Cloud computing is the delivery of computing services over the internet.",
        "bye": "Goodbye! Have a great day."
    }

    return responses.get(prompt.lower(), "I'm not sure about that.")


test_cases = [
    {
        "name": "Greeting test",
        "prompt": "hello",
        "expected_keyword": "help"
    },
    {
        "name": "Cloud knowledge test",
        "prompt": "What is cloud computing",
        "expected_keyword": "internet"
    },
    {
        "name": "Fallback test",
        "prompt": "random question",
        "expected_keyword": "not sure"
    }
]


def run_evaluation():
    print("Running LLM evaluation...\n")

    for case in test_cases:
        response = generate_response(case["prompt"])
        passed = case["expected_keyword"].lower() in response.lower()

        status = "PASS" if passed else "FAIL"

        print(f"Test: {case['name']}")
        print(f"Prompt: {case['prompt']}")
        print(f"Response: {response}")
        print(f"Result: {status}\n")


if __name__ == "__main__":
    run_evaluation()
