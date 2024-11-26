import hashlib  # Import the hashlib library for hashing functions

def hash_password(password):
    # Encode the password to bytes, as hashing functions require byte input
    password_bytes = password.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the encoded password
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password


# Main program loop for encryption and decryption
flag = True  # Initialize a flag to control the loop
while flag:
    print("\nEncryption and Decryption using Rail Fence Cipher")
    # Take password input from the user
    password = input("Enter the password to hash: ")

    # Get the hashed representation
    hashed = hash_password(password)

    # Print the hashed password
    print("SHA-256 Hashed Password:", hashed)
    # Ask the user if they want to exit
    exit = input("Do you want to Exit? (Y/N) ")
    if exit == "Y" or exit == "y" or exit == "yes" or exit == "Yes":
        flag = False  # Set the flag to False to exit the loop
print("Exit")