import ollama



modelLlama = "llama3.2"
modelQwen="qwen2.5:0.5b "
modelGemma = "gemma3:1b"
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
            "Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
        )
            responsejudge = ollama.chat(model=modelQwen, messages=[{"role": "user", "content": judge_prompt}])
            print(f"Run {run}: Model {modelQwen} evaluation: {responsejudge['message']['content']}")

            second_judge_prompt =( 
                    f"Please judge the answer to the question: '{prompt.format(country=country)}' "
                    f"provided by the model '{modelLlama}'. The expected answer is '{expected_answer}'. "
                    f"The model's answer is: '{answer}'. "
                    # "Please provide a yes or no answer if this was correct and accurate."
                    "Please provide a yes or no answer if this was correct and accurate and if its correct to the {expected_answer}."
            )
            second_responsejudge = ollama.chat(model=modelGemma, messages=[{"role": "user", "content": second_judge_prompt}])
            print(f"Run {run}: Model {modelGemma} evaluation: {second_responsejudge['message']['content']}")