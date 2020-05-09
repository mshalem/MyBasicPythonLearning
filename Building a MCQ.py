from Question_MCQ import question_class

questions_array = [
    "what color are apples?\n(a) Red\n(b) Yellow\n(c) Green\n\n",
    "What color are bananas?\n(a) Red\n(b) Yellow\n(c) Green\n\n",
    "What color are Guavas?\n(a) Red\n(b) Yellow\n(c) Green\n\n"
]

questions_object = [
    question_class(questions_array[0], "a"),
    question_class(questions_array[1], "b"),
    question_class(questions_array[2], "c")
]

def run_test(questions_loop):
    score = 0
    for questions_var in questions_loop:
        answer = input(questions_var.prompt + "\nPlease choose the correct option: ")
        if answer == questions_var.answer:
            score = score + 1
    print("you have got" + str(score) + "/" + str(len(questions_object)))
run_test(questions_object)