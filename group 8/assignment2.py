import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from LLMcalls import chat_ollama


def ask_capital(country, model="llama3.2:1b"):
    prompt = f"What is the capital of {country}?"
    response = chat_ollama(model, prompt, verbose=True)
    return response['message']['content']


class testmethods(unittest.TestCase):

    def test_unknown_model_returns_failure(self):
        response = ask_capital("Sweden", "no-such-model")
        self.assertEqual(response, "Failure.")

    def test_knows_capital_of_sweden(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Sweden")
            print(f"Answer {i + 1}: {answer}")
            if "Stockholm" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

if __name__ == "__main__":
    unittest.main()
import ollama



modelLlama = "llama3.2"
modelQwen="qwen2.5:0.5b"
modelGemma ="gemma3:1b"
# prompt = "What is the capital of Småland?"
country = "sweden"
prompt = f"What is the capital of {country}?"
expected_answer = "stockholm"

# string = "lullaby"
# prompt=f"how many l are in {string}?"
# expected_answer = "3"
RUNS = 10



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

for run in range(1, RUNS + 1):
            response = ollama.chat(model=modelLlama, messages=[{"role": "user", "content": prompt}])
            answer = response['message']['content']
            print(f"Run {run}: Model {modelLlama} answer: {answer}")

            judge_prompt =(
            f"Please judge the answer to the question: '{prompt.format(country=country)}' "
            f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
            f"The model's answer is: '{answer}'. "
            #  "Please provide a yes or no answer if this was correct and accurate."
            f"Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
        )
            responsejudge = ollama.chat(model=modelQwen, messages=[{"role": "user", "content": judge_prompt}])
            print(f"Run {run}: Model {modelQwen} evaluation: {responsejudge['message']['content']}")

            second_judge_prompt =( 
                    f"Please judge the answer to the question: '{prompt.format(country=country)}' "
                    f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
                    f"The model's answer is: '{answer}'. "
                    # "Please provide a yes or no answer if this was correct and accurate."
                    f"Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
            )
            second_responsejudge = ollama.chat(model=modelGemma, messages=[{"role": "user", "content": second_judge_prompt}])
            print(f"Run {run}: Model {modelGemma} evaluation: {second_responsejudge['message']['content']}")
