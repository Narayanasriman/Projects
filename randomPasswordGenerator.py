import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: No character types selected. Please enable at least one option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)

        if password:
            print("Generated Password:", password)

        another = input("Generate another password? (yes/no): ").lower()
        if another != "yes":
            break

if __name__ == "__main__":
    main()
