import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    characters = list(string.ascii_lowercase)
    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{}<>?")

    if not characters:
        raise ValueError("No character types selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 StrongPass - Password Generator")
    try:
        length = int(input("Enter password length (8-32): "))
        if length < 8 or length > 32:
            raise ValueError
    except ValueError:
        print("Invalid length. Please enter a number between 8 and 32.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_numbers, use_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
