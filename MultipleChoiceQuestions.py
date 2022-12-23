class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color is the sky?\n(a) blue,\n(b) green,\n(c) red\n\n",
    "What color is the grass?\n(a) blue,\n(b) green,\n(c) red\n\n",
    "What color is the stop sign?\n(a) blue,\n(b) green,\n(c) red\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)