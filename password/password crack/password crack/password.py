import hashlib

def convert_text_file_to_sha1(text):
    # Use SHA-1 to hash the text
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest 

def main():
    # Asking the user to input SHA-1 value 
    user_sha1 = input("Enter the hash to crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()
    
    # List of password files to check
    password_files = [
        './my_password.txt',
        './my_password1.txt',
        './my_password2.txt',
        './my_password3.txt',
        './my_password4.txt'
    ]
    
    # Loading passwords from multiple files
    found_password = False  # Flag to check if password is found
    for filename in password_files:
        try:
            with open(filename) as passw:
                for line in passw:
                    password = line.strip()
                    converted_sha1 = convert_text_file_to_sha1(password)  # Convert password to SHA-1
                    
                    if cleaned_user_sha1 == converted_sha1:
                        print(f"Password found: {password}")  # Print found password
                        found_password = True
                        break  # Stop searching after finding the password
                
                if found_password:
                    break  # Stop searching through files if password is found
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Skipping.")

    if not found_password:
        print("Oops! Password is not listed.")  # This executes if the password wasn't found in any file

if __name__ == "__main__":  
    main()  

