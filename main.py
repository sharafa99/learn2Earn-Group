import os
import secrets
import hashlib
from auth import create_auth, load_auth, save_auth

from vault import save_vault, load_vault
from generator import generate_password

def clear_terminal():
    # 'nt' is for Windows, 'posix' is for Mac and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def top_heading(content):
    print("===================================")
    print(f"         {content}           ")
    print("===================================\n")

def add_credential(vault):
    credential = {}
    credential["site"] = input("Site name: ")
    credential["username"] = input("Username/email: ")

    print("\nPassword:\n1. Enter manualy\n2. Generate password")
    while True:
        try:
            pass_choice = int(input("Choose: "))

            if pass_choice not in (1, 2):
                print("Please choose between 1 or 2")
                continue
    
            break

        except ValueError:
            print("Please enter a number.")
            continue

    if pass_choice == 2:
        while True:
            password = generate_password()
            if password is None:
                print("Please select at least one character category for the password generation.")

                continue

            else:
                print(password)
                break

    elif pass_choice == 1:
        password = input("Insert your intended password: ")

    credential["password"] = password

    vault.append(credential)
    save_vault(vault, "vault.json")

def get_credentials(vault, site_name):

    for credential in vault:
        if credential["site"] == site_name:
            return credential
        
    return None

def verify_password(entered_password, auth_data):
    entered_password_byte = entered_password.encode()

    stored_salt = auth_data["salt"]
    stored_salt_byte = bytes.fromhex(stored_salt)

    new_hashed_password = hashlib.pbkdf2_hmac(
        "sha256",
        entered_password_byte,
        stored_salt_byte,
        600_000
    )

    new_hashed_password_hex = new_hashed_password.hex()
    return secrets.compare_digest(
        new_hashed_password_hex,
        auth_data["password_hash"]
    )

auth_data = load_auth("auth.json")

if not auth_data:
    clear_terminal()
    top_heading("PASSWORD MANAGER")

    print("Welcome to your password manager app\n")

    password = input('Type in your master password: ')
    auth_data = create_auth(password)
    print(f"Your master password is {password}")
    save_auth(auth_data, "auth.json")

while True:
    clear_terminal()
    top_heading("PASSWORD MANAGER")
    master_pass = input("Enter master password here:  \n")

    access = verify_password(master_pass, auth_data)

    if access:
        print("Vault unlocked successfully!")
        break

vault = load_vault("vault.json")
while True:
    clear_terminal()
    top_heading("PASSWORD MANAGER")

    print("1. Add credential\n2. Get credential\n3. Exit")

    while True:

        try:
            choice = int(input("\nchoose an option: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if choice not in (1, 2, 3):
            print("Please choose 1, 2, or 3.")
            continue

        break

    if choice == 1:
        clear_terminal()
        top_heading("ADDING CREDENTIALS")
        add_credential(vault)

    elif choice == 2:
        clear_terminal()
        top_heading("GET CREDENTIALS")

        site_name = input("Which site are you looking for? ")
        credential = get_credentials(vault, site_name)

        if credential is not None:
            username = credential["username"]
            password = credential['password']
            print("Credential found!\n")
            print(f"Username: {username}\nPassword: {password}")
                    
        else:
            print("The credential site could not be found in the vault")
    
    elif choice == 3:
        break