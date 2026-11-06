from questions import data
import os
import random
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text1, text2):
    space1 = int((70-len(text1))/2)
    space2 = int((70-len(text2))/2)
    print("="*70,)
    print(" "*space1, end="")
    print(f"{text1}")
    print()
    print(" "*space2, end="")
    print(f"{text2}")
    print("="*70)

def question_quantity(diff_level):
    if diff_level == "Easy":
        return 5
    elif diff_level == "Medium":
        return 10
    else:
        return 15

def all_subject_selection(diff_level):
    selected_questions= []
    subjects = ["Mathematics", "English", "Physics"]
    for subject in subjects:
        if subject == "Mathematics" or subject == "English":
            subject_questions = data[subject][diff_level]
            random_selection = random.sample(subject_questions, round(question_quantity(diff_level)/len(subjects)))
            selected_questions.extend(random_selection)
        else:
            subject_questions = data[subject][diff_level]
            random_selection = random.sample(subject_questions, (question_quantity(diff_level)-(2 * round(question_quantity(diff_level)/len(subjects)))))
            selected_questions.extend(random_selection)
    random.shuffle(selected_questions)
    return selected_questions

def selected_questions(subject, diff_level):
    if subject == "All subjects":
        return all_subject_selection(diff_level)
    else:
        question_pool = data[subject][diff_level]
        return random.sample(question_pool, question_quantity(diff_level))

def question_modifier(question):
    modified_question = {}
    modified_question.update(question)
    modified_option = []
    modified_option.extend(modified_question["options"])
    random.shuffle(modified_option)
    modified_question["options"] = modified_option
    return modified_question

def option_generator(options):
    label = ["A", "B", "C", "D"]
    for i, option in enumerate(options):
        print(f"{label[i]}. {option}")

def get_answer(options):
    labels = ["A", "B", "C", "D"]
    while True:
        try:
            answer = input("Your answer: ").strip().upper()

            if not answer:
                raise ValueError("Invalid input! Numbers or empty text are not allowed")

            if answer not in labels:
                raise ValueError(f"Please choose from {', '.join(labels)}")
            
        except ValueError as e:
            print(f"Error: {e}")
            continue

        break

    index = labels.index(answer)
    return options[index]

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def play_one_question(question):

    modified_question = question_modifier(question)

    print(modified_question["question"])

    option_generator(modified_question["options"])
    print()
    user_answer = get_answer(modified_question["options"])

    result = check_answer(
        user_answer,
        modified_question["answer"]
    )
    print()
    if result:
        print("Correct")
        time.sleep(1)
    else:
        print("You missed it")
        time.sleep(1)

    return result

def play_quiz(questions,subject):
    
    correct_answers = 0
    start_time = time.time()
    for i, question in enumerate(questions):
        clear_terminal()
        text1 = f"{subject} Quiz Game "
        text2 = f"Question {i+1} of {len(questions)}"
        header(text1, text2)
        print()
        result = play_one_question(question)
            
        if result:
            correct_answers += 1
    end_time = time.time()
    duration = end_time - start_time
    return correct_answers, round(duration,2)

def time_converter(given_time):
    hour = given_time // 3600
    minute = (given_time % 3600) // 60
    seconds = (given_time % 3600) % 60
    return hour, minute, seconds

def display_result(result):
    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)


    print(f"\nPlayer : {result['user_name']}")
    print(f"Subject : {result['subject']}")
    print(f"Difficulty : {result['diff_level']}")
    print(f"\nCorrect answers : {result['correct_answers']}")
    print(f"Wrong answers   : {result['wrong_answers']}")
    print(f"Total questions : {result['total_questions']}")
    print(f"\nScore      : {result['percentage']}%")
    print(f"Time taken      : {result['time_taken']}")
    print()

    print("=" * 40)

