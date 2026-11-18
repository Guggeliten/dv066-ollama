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

# f"Please judge the answer to the question: '{prompt.format(country=country)}' "

# f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "

# f"The model's answer is: '{answer}'. "

# "Please provide a brief evaluation of the answer's correctness and accuracy."

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

Run 1: Model llama3.2 answer: The word "lullaby" contains 1 "L".
Run 1: Model qwen2.5:0.5b evaluation: Yes.
Run 1: Model gemma3:1b evaluation: No.

Run 2: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 2: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct.
Run 2: Model gemma3:1b evaluation: Yes

Run 3: Model llama3.2 answer: The word "lullaby" contains 2 L's.
Run 3: Model qwen2.5:0.5b evaluation: Yes.
Run 3: Model gemma3:1b evaluation: Yes

Run 4: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 4: Model qwen2.5:0.5b evaluation: No, the model's answer is incorrect. There are 2 L's in the word "lullaby".
Run 4: Model gemma3:1b evaluation: Yes

Run 5: Model llama3.2 answer: There are 3 L's in the word "lullaby".
Run 5: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct. "Lullaby" contains 3 syllables, with the first syllable being "l", the second being "ull", and the third being "aby." The expected answeris "3", which matches the model's answer.
Run 5: Model gemma3:1b evaluation: Yes

Run 6: Model llama3.2 answer: There are 3 L's in the word "lullaby".
Run 6: Model qwen2.5:0.5b evaluation: Yes, the answer provided by the model 'llama3.2' is correct. The word "lullaby" has 3 letters.
Run 6: Model gemma3:1b evaluation: Yes

Run 7: Model llama3.2 answer: There is one "L" in "lullaby".
Run 7: Model qwen2.5:0.5b evaluation: No, the model's answer is not correct. According to the information provided in the question, there is one "L" in "lullaby".
Run 7: Model gemma3:1b evaluation: Yes

Run 8: Model llama3.2 answer: There are 3 L's in the word "lullaby".
Run 8: Model qwen2.5:0.5b evaluation: Yes.
Run 8: Model gemma3:1b evaluation: Yes

Run 9: Model llama3.2 answer: There are 6 letters in the word "lullaby".
Run 9: Model qwen2.5:0.5b evaluation: Yes. The answer of "There are 6 letters in the word "lullaby"." is correct.
Run 9: Model gemma3:1b evaluation: No.

Run 10: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 10: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct and accurate.
The word "lullaby" consists of 3 letters: "l" and "u".
Run 10: Model gemma3:1b evaluation: Yes

PS C:\Users\brand\source\repos\dv066> & 'C:\Users\brand\AppData\Local\Python\pythoncore-3.14-64\python.exe' '"c:/Users/brand/source/repos/dv066/tutoriaLLM/group 8/assignment2.py"'
Run 1: Model llama3.2 answer: There are 3 "L"s in the word "lullaby".
Run 1: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct.
Run 1: Model gemma3:1b evaluation: Yes

Run 2: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 2: Model qwen2.5:0.5b evaluation: Yes.
Run 2: Model gemma3:1b evaluation: Yes

Run 3: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 3: Model qwen2.5:0.5b evaluation: No, the model's answer is incorrect. The word "lullaby" contains 3 L's, not 2.
Run 3: Model gemma3:1b evaluation: Yes

Run 4: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 4: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct. The word "lullaby" contains 2 L's in the word "lull" and 1 L in the word "aby."
Run 4: Model gemma3:1b evaluation: Yes.

Run 5: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 5: Model qwen2.5:0.5b evaluation: No, the answer provided by the model 'llama3.2' is incorrect. The word "lullaby" contains 3 L's.
Run 5: Model gemma3:1b evaluation: Yes.

Run 6: Model llama3.2 answer: There are 2 L's in the word "lullaby".
Run 6: Model qwen2.5:0.5b evaluation: No, the answer is not correct. The word "lullaby" does not contain any 'L' characters. Therefore, the model's answer "There are 2 L's in the word "lullaby"" is incorrect.
Run 6: Model gemma3:1b evaluation: Yes.
Run 7: Model llama3.2 answer: There are 7 letters in "lullaby".
Run 7: Model qwen2.5:0.5b evaluation: No, the answer provided by the model 'llama3.2' is incorrect. The model suggests that there are 7 letters in "lullaby". However, "lullaby" has a total of 30 letters.
Run 7: Model gemma3:1b evaluation: No.

Run 8: Model llama3.2 answer: There is 1 "L" in the word "lullaby".
Run 8: Model qwen2.5:0.5b evaluation: Yes. The model's answer is correct, and it states that "There is 1 'L' in the word 'lullaby'".
Run 8: Model gemma3:1b evaluation: Yes.

Run 9: Model llama3.2 answer: There are 3 L's in the word "lullaby".
Run 9: Model qwen2.5:0.5b evaluation: Yes, the answer provided by the model 'llama3.2' is correct. The word "lullaby" contains 3 'l's.
Run 9: Model gemma3:1b evaluation: Yes

Run 10: Model llama3.2 answer: There is 1 "L" in "Lullaby".
Run 10: Model qwen2.5:0.5b evaluation: Yes.
Run 10: Model gemma3:1b evaluation: Yes

Run 1: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 1: Model qwen2.5:0.5b evaluation: Yes, the answer provided by the model 'The capital of Sweden is Stockholm.' is correct and accurate. Stockholm is indeed the capital of Sweden.
Run 1: Model gemma3:1b evaluation: Yes

Run 2: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 2: Model qwen2.5:0.5b evaluation: Yes, the provided answer is correct. Stockholm is the capital of Sweden.
Run 2: Model gemma3:1b evaluation: Yes

Run 3: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 3: Model qwen2.5:0.5b evaluation: Yes.
Run 3: Model gemma3:1b evaluation: Yes

Run 4: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 4: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct and accurate. Stockholm is indeed the capital of Sweden, and it's located on the island of Öland. The model's answer accurately representsthis information.
Run 4: Model gemma3:1b evaluation: Yes

Run 5: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 5: Model qwen2.5:0.5b evaluation: Yes, the answer is correct. The capital of Sweden is indeed Stockholm.
Run 5: Model gemma3:1b evaluation: Yes

Run 6: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 6: Model qwen2.5:0.5b evaluation: Yes.
Run 6: Model gemma3:1b evaluation: Yes

Run 7: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 7: Model qwen2.5:0.5b evaluation: Yes.
Run 7: Model gemma3:1b evaluation: Yes

Run 8: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 8: Model qwen2.5:0.5b evaluation: Yes.
Run 8: Model gemma3:1b evaluation: Yes

Run 9: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 9: Model qwen2.5:0.5b evaluation: Yes.
Run 9: Model gemma3:1b evaluation: Yes

Run 10: Model llama3.2 answer: The capital of Sweden is Stockholm.
Run 10: Model qwen2.5:0.5b evaluation: Yes, the model's answer is correct and accurate. Stockholm is indeed the capital of Sweden.
Run 10: Model gemma3:1b evaluation: Yes.

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

        if __name__ == "__main__":

    unittest.main(exit=False)

    for run in range(1, RUNS + 1):
        answer = ask_capital(country, modelLlama)
        print(f"Run {run}: Model {modelLlama} answer: {answer}")

        first_response_judge = llm_as_a_judge(modelQwen, modelLlama, prompt, answer, expected_answer)
        print(f"Run {run}: Model {modelQwen} evaluation: {first_response_judge}")

        second_response_judge = llm_as_a_judge(modelGemma, modelLlama, prompt, answer, expected_answer)
        print(f"Run {run}: Model {modelGemma} evaluation: {second_response_judge}")

Run 1: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 1: Model qwen2.5:0.5b evaluation: True
Run 1: Model gemma3:1b evaluation: True
Run 2: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 2: Model qwen2.5:0.5b evaluation: True
Run 2: Model gemma3:1b evaluation: True
Run 3: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 3: Model qwen2.5:0.5b evaluation: True
Run 3: Model gemma3:1b evaluation: True
Run 4: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 4: Model qwen2.5:0.5b evaluation: True
Run 4: Model gemma3:1b evaluation: True
Run 5: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 5: Model qwen2.5:0.5b evaluation: True
Run 5: Model gemma3:1b evaluation: True
Run 6: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 6: Model qwen2.5:0.5b evaluation: True
Run 6: Model gemma3:1b evaluation: True
Run 7: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 7: Model qwen2.5:0.5b evaluation: True
Run 7: Model gemma3:1b evaluation: True
Run 8: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 8: Model qwen2.5:0.5b evaluation: True
Run 8: Model gemma3:1b evaluation: True
Run 9: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 9: Model qwen2.5:0.5b evaluation: True
Run 9: Model gemma3:1b evaluation: True
Run 10: Model llama3.2:1b answer: The capital of Australia is Canberra.
Run 10: Model qwen2.5:0.5b evaluation: True
Run 10: Model gemma3:1b evaluation: True

Original question: What is the capital of Australia?
Answer: Canberra
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
.Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 1: The capital of Australia is Canberra.
Judge says correct: True
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 2: The capital of Australia is Canberra.
Judge says correct: True
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 3: The capital of Australia is Canberra.
Judge says correct: True
.Original question: What is the capital of Australia?
Answer: Sydney
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
FAustralia answer 1: The capital of Australia is Canberra.
Australia answer 2: The capital of Australia is Canberra.
Australia answer 3: The capital of Australia is Canberra.
.Answer 1: The capital of Sweden is Stockholm.
Answer 2: The capital of Sweden is Stockholm.
Answer 3: The capital of Sweden is Stockholm.
..
======================================================================
FAIL: test_judge_rejects_wrong_answer (**main**.testmethods.test_judge_rejects_wrong_answer)

---

Traceback (most recent call last):
File "c:\school\Data\AI\dv066-ollama\group 8\assignment2.py", line 100, in test_judge_rejects_wrong_answer
self.assertFalse(result)
~~~~~~~~~~~~~~~~^^^^^^^^
AssertionError: True is not false

---

Ran 6 tests in 10.919s

FAILED (failures=1)
Run 1: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 2: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 3: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 4: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 5: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 6: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 7: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 8: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 9: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 10: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Original question: What is the capital of Australia?
Answer: Canberra
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
.Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 1: The capital of Australia is Canberra.
Judge says correct: True
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 2: The capital of Australia is Canberra.
Judge says correct: True
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Answer 3: The capital of Australia is Canberra.
Judge says correct: True
.Original question: What is the capital of Australia?
Answer: Sydney
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: NO
.Australia answer 1: The capital of Australia is Canberra.
Australia answer 2: The capital of Australia is Canberra.
Australia answer 3: The capital of Australia is Canberra.
.Answer 1: The capital of Sweden is Stockholm.
Answer 2: The capital of Sweden is Stockholm.
Answer 3: The capital of Sweden is Stockholm.
..

---

Ran 6 tests in 11.106s

OK
Run 1: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 2: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 3: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 4: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 5: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 6: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 7: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 8: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 9: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES

Run 10: Model llama3.2:1b answer: The capital of Australia is Canberra.
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: qwen2.5:0.5b
Judge awnser: YES
Original question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
Expected answer: Canberra
Judge model: gemma3:1b
Judge awnser: YES
