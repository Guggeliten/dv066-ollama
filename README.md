
# GROUP 8

## What models did we use?

For this assignment, we used Llama 3.2 and Qwen 2.5:0.5b.
We chose these two for convenience.

## How to run our code

To run our code, we created a new folder called **Group 8**. Inside this folder, you will find two more files. The file `assignment1.py` contains the code for this assignment. If you press Run from that window, the code should execute.
The answers we got are saved in the other file, `assignment1 answers`.
The `TESTS` folder contains nothing related to the assignment. It only contains some fun stuff we wanted to try.

## What we observed

When we started asking questions about Stockholm, both models gave more accurate answers and did not produce any hallucinated answers.
However, when we asked more difficult questions containing errors in the questions themselves, such as "What is the capital of Småland?", we noticed some clear differences!
Qwen started hallucinating a lot and producing answers that made very little sense. It also referred to Småland as its own country or province. It often declared Gothenburg to be its capital. It also invented or confused geographical information.
Llama was more accurate in its answers and could even tell us that Småland does not have a capital since it is a region. However, it also produced several hallucinated answers about the largest city and its location.
We could also see that Qwen seemed to be more "confident" in its answers, whereas Llama seemed a little more uncertain.
Qwen also gave much longer answers and tried to include "facts" (which were often incorrect).
For such simple questions, it seemed that the answers were generated at approximately the same speed as those from more commercial models.
Both models seemed to perform worse than models like ChatGPT, Claude, and Gemini. These models recognized Småland as a region in Sweden rather than its own country and understood that Småland does not have a formal capital. They also provided more alternatives for informal capitals, beyond Gothenburg, which was by far the most common answer given by Llama and Qwen.
However, it is also difficult to draw any firm conclusions based on only two questions.

