import unittest
import sys
import ollama
from pathlib import Path

modelLlama = "llama3.2:1b"
modelQwen = "qwen2.5:0.5b"
modelGemma = "gemma3:1b"

# prompt = "What is the capital of Småland?"
country = "Australia"
prompt = f"What is the capital of {country}?"
expected_answer = "Canberra"

# string = "lullaby"
# prompt=f"how many l are in {string}?"
# expected_answer = "3"
RUNS = 10

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from LLMcalls import chat_ollama

def ask_capital(country, model):
    prompt = f"What is the capital of {country}?"
    response = chat_ollama(model, prompt, verbose=False)
    return response['message']['content']


def llm_as_a_judge(judgeModel, original_model, prompt, answer, expected_answer):
    judge_prompt = (
        f"Please judge the answer to the question: '{prompt}' "
        f"provided by the model '{original_model}'. "
        f"The expected answer is '{expected_answer}'. "
        f"The model's answer is: '{answer}'. "
        "Answer only YES if correct or NO if incorrect."
    )

    verdict = chat_ollama(judgeModel, judge_prompt, verbose=False)
    judgment = verdict['message']['content'].strip().lower()

    print(f"Original question: {prompt}")
    print(f"Answer: {answer}")
    print(f"Expected answer: {expected_answer}")
    print(f"Judge model: {judgeModel}")
    print(f"Judge awnser: {verdict['message']['content']}")

    if judgment.startswith("yes"):
        return True
    elif judgment.startswith("no"):
        return False
    else:
        raise ValueError(f"Invalid judge response: {judgment}")




class testmethods(unittest.TestCase):

    def test_unknown_model_returns_failure(self):
        response = ask_capital("Sweden", "no-such-model")
        self.assertEqual(response, "Failure.")

    def test_knows_capital_of_sweden(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Sweden", "llama3.2:1b")
            print(f"Answer {i + 1}: {answer}")
            if "Stockholm" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)


    def test_knows_capital_of_australia(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Australia", modelLlama)
            print(f"Australia answer {i + 1}: {answer}")
            if "Canberra" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

    def test_judge_accepts_correct_answer(self):
        result = llm_as_a_judge(
            modelQwen,
            modelLlama,
            "What is the capital of Australia?",
            "Canberra",
            "Canberra"
        )
        self.assertTrue(result)

    def test_judge_rejects_wrong_answer(self):
        result = llm_as_a_judge(
            modelQwen,
            modelLlama,
            "What is the capital of Australia?",
            "Sydney",
            "Canberra"
        )
        self.assertFalse(result)

    def test_judge_consistency_australia(self):
        correct = 0

        for i in range(3):
            answer = ask_capital("Australia", modelLlama)

            result = llm_as_a_judge(
                modelQwen,
                modelLlama,
                "What is the capital of Australia?",
                answer,
                "Canberra"
            )

            print(f"Answer {i + 1}: {answer}")
            print(f"Judge says correct: {result}")

            if result:
                correct += 1

        self.assertGreaterEqual(correct, 2)






# response = ollama.chat(model=modelLlama, messages=[{"role": "user", "content": prompt}])
# answer = response['message']['content']
# print(f"Model {modelLlama} answer: {answer}")

# judge_prompt =(
#     f"Please judge the answer to the question: '{prompt.format(country=country)}' "
#     f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
#     f"The model's answer is: '{answer}'. "
#     "Please provide a brief evaluation of the answer's correctness and accuracy."
# )
# responsejudge = ollama.chat(model=modelQwen, messages=[{"role": "user", "content": judge_prompt}])
# print(f"Model {modelQwen} evaluation: {responsejudge['message']['content']}")


if __name__ == "__main__":

    unittest.main(exit=False)

    for run in range(1, RUNS + 1):
        answer = ask_capital(country, modelLlama)
        print(f"Run {run}: Model {modelLlama} answer: {answer}")

            # judge_prompt = (
            #     f"Please judge the answer to the question: '{prompt.format(country=country)}' "
            #     f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
            #     f"The model's answer is: '{answer}'. "
            #     #  "Please provide a yes or no answer if this was correct and accurate."
            #     f"Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
            # )

        first_response_judge = llm_as_a_judge(modelQwen, modelLlama, prompt, answer, expected_answer)
        # print(f"Run {run}: Model {modelQwen} evaluation: {first_response_judge}")

        second_response_judge = llm_as_a_judge(modelGemma, modelLlama, prompt, answer, expected_answer)
        # print(f"Run {run}: Model {modelGemma} evaluation: {second_response_judge}")

            # second_judge_prompt = (
            #     f"Please judge the answer to the question: '{prompt.format(country=country)}' "
            #     f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
            #     f"The model's answer is: '{answer}'. "
            #     # "Please provide a yes or no answer if this was correct and accurate."
            #     f"Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
            # )

            # second_responsejudge = ollama.chat(
            #     model=modelGemma,
            #     messages=[{"role": "user", "content": second_judge_prompt}]
            #  )
            # print(f"Run {run}: Model {modelGemma} evaluation: {second_responsejudge['message']['content']}")
