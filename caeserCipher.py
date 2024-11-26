# List of lowercase English alphabets
lowerAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of uppercase English alphabets created from the lowercase list
upperAlpha = [char.upper() for char in lowerAlpha]

# Function to encrypt a message using Caesar Cipher
def encrypt(text, key):
    output = ""  # Initialize the encrypted message
    for char in text:
        # Check if the character is uppercase
        if char.isupper():
            for j in range(len(upperAlpha)):  # Find the index of the character in the uppercase list
                if char == upperAlpha[j]:
                    index = j

            index += key  # Shift the index by the key
            index = index % 26  # Wrap around using modulo
            output += upperAlpha[index]  # Append the encrypted character to the output

        # Check if the character is lowercase
        elif char.islower():
            for j in range(len(lowerAlpha)):  # Find the index of the character in the lowercase list
                if char == lowerAlpha[j]:
                    index = j

            index += key  # Shift the index by the key
            index = index % 26  # Wrap around using modulo
            output += lowerAlpha[index]  # Append the encrypted character to the output

        # If the character is not alphabetic (e.g., space, punctuation), leave it as is
        else:
            output += char
    return output  # Return the encrypted message

# Function to decrypt a message using Caesar Cipher
def decrypt(text, key):
    output = ""  # Initialize the decrypted message
    for char in text:
        # Check if the character is uppercase
        if char.isupper():
            for j in range(len(upperAlpha)):  # Find the index of the character in the uppercase list
                if char == upperAlpha[j]:
                    index = j

            index -= key  # Reverse the shift by subtracting the key
            index = index % 26  # Wrap around using modulo
            output += upperAlpha[index]  # Append the decrypted character to the output

        # Check if the character is lowercase
        elif char.islower():
            for j in range(len(lowerAlpha)):  # Find the index of the character in the lowercase list
                if char == lowerAlpha[j]:
                    index = j

            index -= key  # Reverse the shift by subtracting the key
            index = index % 26  # Wrap around using modulo
            output += lowerAlpha[index]  # Append the decrypted character to the output

        # If the character is not alphabetic (e.g., space, punctuation), leave it as is
        else:
            output += char
    return output  # Return the decrypted message

# Main program loop for encryption and decryption
flag = True  # Initialize a flag to control the loop
while flag:
    print("\nEncryption and Decryption using Caesar Cipher")
    choice = input("Do you want to Encrypt or Decrypt? ")  # Ask the user for their choice
    enc = "encrypt"
    dec = "decrypt"

    # Check if the user wants to encrypt
    if choice in [enc, enc.upper(), enc.capitalize(), "E", "e"]:
        string = input("Enter the message to Encrypt: ")  # Input the message to encrypt
        key = int(input('Enter the key: '))  # Input the encryption key

        output = encrypt(string, key)  # Call the encrypt function
        print("The Encrypted message is:", output, "\n")

    # Check if the user wants to decrypt
    elif choice in [dec, dec.upper(), dec.capitalize(), "D", "d"]:
        string = input("Enter the Cipher to Decrypt: ")  # Input the cipher text to decrypt
        key = int(input('Enter the key: '))  # Input the decryption key

        output = decrypt(string, key)  # Call the decrypt function
        print("The Decrypted message is:", output, "\n")

    # Handle invalid inputs
    else:
        print("Invalid Input, Try Again!!\n")

    # Ask the user if they want to exit
    exit = input("Do you want to Exit? (Y/N) ")
    if exit == "Y" or exit == "y" or exit == "yes" or exit == "Yes":
        flag = False  # Set the flag to False to exit the loop
print("Exit")