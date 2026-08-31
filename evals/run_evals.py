import json

from app.llm import get_ai_response


with open("evals/test_cases.json", "r", encoding="utf-8") as file:
    test_cases = json.load(file)


for case in test_cases:
    print("=" * 80)
    print(f"TEST ID: {case['id']}")
    print(f"QUESTION: {case['question']}")

    response = get_ai_response(case["question"])

    print(f"RESPONSE: {response}")
    print("EXPECTED BEHAVIOR:")

    for item in case["expected_behavior"]:
        print(f"- {item}")