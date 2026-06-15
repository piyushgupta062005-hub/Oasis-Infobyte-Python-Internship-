import random
import string


def generate_password():
    print("=== Random Password Generator ===")

    try:
        # Password ki length puchna
        length = int(input("Enter the desired password length (minimum 6): "))

        if length < 6:
            print("Password length should be at least 6 characters for security.")
            return

        # Characters sets define karna
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        # Sabhi characters ko ek sath milana
        all_characters = letters + digits + symbols

        # Randomly characters select karna
        password = "".join(random.choice(all_characters) for i in range(length))

        print(f"\nGenerated Secure Password: {password}")

    except ValueError:
        print("Please enter a valid number for length.")


if __name__ == "__main__":
    generate_password()
