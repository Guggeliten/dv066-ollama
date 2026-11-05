import ollama

modelLlama = "llama3.2"
modelQwen="qwen2.5:0.5b "
# prompt = "What is the capital of Småland?"
prompt = "What is the capital of Sweden?"


# response = ollama.chat(model=modelLlama, messages=[{"role": "user", "content": prompt}])
# print(response['message']['content'])

# response = ollama.chat(model=modelQwen, messages=[{"role": "user", "content": prompt}])
# print(response['message']['content'])
RUNS = 10
models = [modelLlama, modelQwen]

for run in range(1, RUNS + 1):
  
        response = ollama.chat(model=modelLlama, messages=[{"role": "user", "content": prompt}])
        print(f"--- Run {run} | {modelLlama} ---")
        print(response['message']['content'])

for run in range(1, RUNS + 1):
  
        response = ollama.chat(model=modelQwen, messages=[{"role": "user", "content": prompt}])
        print(f"--- Run {run} | {modelQwen} ---")
        print(response['message']['content'])