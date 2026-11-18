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
