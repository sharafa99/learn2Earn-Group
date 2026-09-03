import secrets
import string


def secure_shuffle(item):

    last_index = len(item)-1

    for i in range(last_index, 0, -1):
        random_index = secrets.randbelow(i+1)

        item[i], item[random_index] = item[random_index], item[i]

    return item

def generate_password():
    alph_upper, alph_lower, num, punc =string.ascii_uppercase, string.ascii_lowercase ,string.digits, string.punctuation

    characters = []
    password = []
    selected_categories = 0

    while True:
        try:
            password_length = int(input("Password length: "))

        except ValueError:
            print("Please enter a number.")
            continue
        if password_length < 8 or password_length > 20:
            print("Your password must not be less than 8 and it must also not be greater than 20")
            continue

        break

    uppercase_choice = input("Include uppercase? (y/n)").lower()
    if uppercase_choice == 'y':
        characters.extend(alph_upper)
        selected_categories += 1
        password.append(secrets.choice(alph_upper))

    lowercase_choice = input("Include lowercase? (y/n)").lower()
    if lowercase_choice == 'y':
        characters.extend(alph_lower)
        selected_categories += 1
        password.append(secrets.choice(alph_lower))

    number_choice = input("Include numbers? (y/n)").lower()
    if number_choice == 'y':
        characters.extend(num)
        selected_categories += 1
        password.append(secrets.choice(num))

    punctuation_choice = input("Include special characters? (y/n)").lower()
    if punctuation_choice == 'y':
        characters.extend(punc)
        selected_categories += 1
        password.append(secrets.choice(punc))

    # if characters == []:
    if not characters:
        return None

    for _ in range(password_length - selected_categories):
        password.append(secrets.choice(characters))

    final_password = secure_shuffle(password)
    return "".join(final_password)
