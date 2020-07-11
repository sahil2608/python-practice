from Question import Question

question_prompts = [
    "What color is your bike? \n (a) Red\n (b) Green\n (c) blue\n\n",
    "What color is your car? \n (a) Red\n (b) Green\n (c) blue\n\n",
    "What color is your house? \n (a) Red\n (b) Green\n (c) blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)