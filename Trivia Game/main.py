import os
import time
import quiz_manager
import score_manager
from logo import quiz_logo

def header(text):
    space = int((70-len(text))/2)
    print("="*70,)
    print(" "*space, end="")
    print(f"{text}")
    print("="*70)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_subject():
    clear_terminal()
    header("SELECT SUBJECT")
    subject = ("Mathematics", "English", "Physics", "All subjects")
    print()

    for i, value in enumerate(subject):
        print(f"{i+1}. {value}")
    print()

    while True:
        try:
            subject_name = int(input('choose a subject: ').strip())

        except ValueError:
            print("Please enter a number.")
            continue

        if subject_name not in (1, 2, 3, 4):
            print("Please choose 1, 2, 3, 4")
            continue
        break
    print(f"\nYour SUBJECT choice is {subject[subject_name - 1].upper()}")
    time.sleep(2)
    return subject[subject_name - 1]

def get_difficulty():
    clear_terminal()
    header("SELECT DIFFICULTY")
    levels = ("Easy", "Medium", "Hard")
    print()
    for i, level in enumerate(levels):
        print(f"{i+1}. {level}")
    print()

    while True:
        try:
            level_choice = int(input('choose difficulty: ').strip())

        except ValueError:
            print("Please enter a number.")
            continue

        if level_choice not in (1, 2, 3):
            print("Please choose 1, 2, 3")
            continue
        break
    print(f"Your difficulty level choice is {levels[level_choice - 1]}")
    time.sleep(2)
    return levels[level_choice - 1]

def get_name():
    while True:
        try:
            name = input("Enter your name: ").capitalize()

            if not name.strip() or any(char.isdigit() for char in name):
                raise ValueError("Invalid input! Numbers or empty space is not allowed")

        except ValueError as e:
            print(f"Error: {e}")
            continue
        break
    return name

def user_config():
    return {
        "user_name" : get_name(),
        "subject" : get_subject(),
        "diff_level" : get_difficulty()
    }

while True:
    clear_terminal()
    print(quiz_logo)

    print("1. Play Game")
    print("2. View High scores")
    print("3. Exit")
    print()

    while True:
        try:
            choice = int(input('choose an option: ').strip())

        except ValueError:
            print("Please enter a number.")
            continue

        if choice not in (1, 2, 3):
            print("Please choose 1, 2, 3")
            continue
        break

    if choice == 1:
        print()
        
        player_config = user_config()

        selected = quiz_manager.selected_questions(player_config["subject"], player_config["diff_level"])

        score, time_taken = quiz_manager.play_quiz(selected, player_config["subject"])

        time_taken = quiz_manager.time_converter(time_taken)

        percentage = score_manager.calculate_percentage(score, len(selected))

        result = score_manager.build_result(score, len(selected), percentage, time_taken, player_config)

        quiz_manager.display_result(result)
        time.sleep(5)

    elif choice == 2:
        pass
    else:
        break
        



    