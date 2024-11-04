import random  # Module for generating random numbers
import string  # Module containing string constants
import bcrypt   # Module for hashing passwords

def generate_password(length=12, use_special_chars=True):
    """
    Generate a strong, random password.

    Parameters:
    - length (int): Desired length of the password (default is 12).
    - use_special_chars (bool): Include special characters if True (default is True).

    Returns:
    - str: A randomly generated password.
    """
    
    # Define character sets for password creation
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    special_chars = string.punctuation if use_special_chars else ''  # Special characters

    # Combine all character sets into one
    all_chars = lowercase + uppercase + digits + special_chars

    # Start creating the password with at least one character from each required set
    password = [
        random.choice(lowercase),  # Add one lowercase letter
        random.choice(uppercase),  # Add one uppercase letter
        random.choice(digits)      # Add one digit
    ]

    # Optionally, add one special character
    if use_special_chars:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle the password list to ensure a random order
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def hash_password(plain_password):
    """
    Hash a plain text password using bcrypt.

    Parameters:
    - plain_password (str): The password to hash.

    Returns:
    - bytes: The hashed password.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed

def save_passwords_to_file(passwords, filename='passwords.txt'):
    """
    Save passwords and their hashed versions to a file.

    Parameters:
    - passwords (list): List of plain text passwords.
    - filename (str): The name of the file to save the passwords (default is 'passwords.txt').
    """
    with open(filename, 'w') as file:
        for password in passwords:
            hashed_password = hash_password(password)
            # Write the password and its hash to the file
            file.write(f"Password: {password}\n")
            file.write(f"Hashed: {hashed_password.decode('utf-8')}\n\n")

if __name__ == "__main__":
    # This block runs only when the script is executed directly
    print("Welcome to the Password Generator and Hasher!")
    
    # Ask the user for the number of passwords to generate
    num_passwords = int(input("How many passwords would you like to generate? "))
    
    # Ask the user for the desired length of each password
    password_length = int(input("Enter the desired password length (minimum 4): "))
    
    # Validate the password length
    if password_length < 4:
        print("Error: Password length should be at least 4 characters.")
    else:
        # Generate the specified number of passwords
        generated_passwords = [generate_password(password_length) for _ in range(num_passwords)]
        
        # Save the generated passwords and their hashes to a file
        save_passwords_to_file(generated_passwords)

        print(f"Successfully generated {num_passwords} passwords and saved them to 'passwords.txt'.")
        print("Thank you for using the Password Generator and Hasher!")

