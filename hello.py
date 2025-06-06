import hashlib
import getpass

def greet_user():
    print("Welcome to the Cyber Security Demo!")

def hash_password(password):
    # Securely hash the password using SHA-256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def main():
    greet_user()
    username = input("Enter your username: ")
    # Use getpass to hide password input
    password = getpass.getpass("Enter your password (input hidden): ")

    hashed_pw = hash_password(password)
    print(f"\nUser '{username}' registered successfully.")
    print(f"Stored password hash (never store plaintext!): {hashed_pw}")

if __name__ == "__main__":
    main()
