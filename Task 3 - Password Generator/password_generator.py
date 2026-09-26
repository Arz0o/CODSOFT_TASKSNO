import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("================================")
print("       PASSWORD GENERATOR")
print("================================")

while True:

    try:
        length = int(input("\nEnter desired password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Password Generator!")
        break