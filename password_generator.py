import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 1:
        return "Password length must be at least 1."
 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 1): "))
            if length < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    generated_password = generate_password(length)
    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
