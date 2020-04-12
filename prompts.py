from Question import Questions

question_prompts = [
    "What does NATO stand for?\n(a) North Atlantic Treaty Organization\n(b) North America Treaty Organization\n(c) North Atlantic Trust Organization\n(d) North Alliance Treaty Organization\n\n",
    "Which is the smallest country in the world?\n(a) Vanuatu\n(b) Vatican City\n(c) Luxembourg\n(c) Monaco\n\n",
    "Which is the largest country in the world in terms of land area?\n(a) Russia\n(b) Canada\n(c) USA\n(d) China\n\n",
    "What is thr capital of Estonia?\n(a) Asmara\n(b) Talinn\n(c) Malabo(d) \n Helsinki\n\n",
    "which of the following countries is the most populous?\n(a) Indonisia\n(b) USA\n(c) India\n(d) China\n\n",
    "Which of following countries has the highest per capita income in the world?\n(a) Qatar\n(b) Luxembourg\n(c) Macau\n(d) Liechtenstein\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "a"),
    Questions(question_prompts[3], "b"),
    Questions(question_prompts[4], "d"),
    Questions(question_prompts[5], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)
















