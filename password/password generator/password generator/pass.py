import random  # To generate random values
import string  # To access string constants

def generate_password(length=12, use_special_chars=True):
    """
    Generate a secure random password.

    Parameters:
    - length (int): The desired length of the password. Default is 12.
    - use_special_chars (bool): Flag to include special characters in the password. Default is True.

    Returns:
    - str: A randomly generated password.
    """

    # Define character sets for password generation
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    special_chars = string.punctuation if use_special_chars else ''  # Special characters like !@#$%^&*

    # Combine all character sets into one for password generation
    all_chars = lowercase + uppercase + digits + special_chars

    # Create a password ensuring it has at least one character from each required character set
    password = [
        random.choice(lowercase),  # One random lowercase letter
        random.choice(uppercase),  # One random uppercase letter
        random.choice(digits)      # One random digit
    ]

    # If allowed, add a special character to the password
    if use_special_chars:
        password.append(random.choice(special_chars))

    # Fill the remaining password length with random choices from all available characters
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the list of characters to ensure randomness in the final password
    random.shuffle(password)

    # Join the list into a single string and return the result
    return ''.join(password)

if __name__ == "__main__":
    # Main execution block, runs only if the script is executed directly
    print("Welcome to the Password Generator!")
    
    # Prompt user for the desired password length
    password_length = int(input("Enter the desired password length (minimum 4): "))
    
    # Validate the password length
    if password_length < 4:
        print("Error: Password length should be at least 4 characters.")
    else:
        # Generate the password
        generated_password = generate_password(password_length)
        # Output the generated password
        print(f"Generated Password: {generated_password}")

    print("Thank you for using the Password Generator!")

