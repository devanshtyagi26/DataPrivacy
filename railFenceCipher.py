def encrypt_rail_fence(text, key):
    # Create a 2D list initialized with empty strings
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    
    direction_down = False  # Direction of the zigzag movement
    row, col = 0, 0         # Starting position

    # Place characters in the rails following a zigzag pattern
    for char in text:
        rail[row][col] = char
        col += 1

        # Change direction if we reach the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        
        # Move up or down based on the direction
        row += 1 if direction_down else -1

    # Read the rails row by row to construct the encrypted text
    result = ""
    for i in range(key):
        result += "".join(rail[i])
    
    return result


def decrypt_rail_fence(cipher, key):
    # Create a 2D list initialized with None
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]
    
    direction_down = None  # Zigzag direction
    row, col = 0, 0

    # Mark the positions in the grid where characters will be placed
    for _ in range(len(cipher)):
        rail[row][col] = '*'
        col += 1

        # Change direction at the top or bottom rail
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Move up or down
        row += 1 if direction_down else -1

    # Fill the marked positions with characters from the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the text following the zigzag pattern
    result = ""
    row, col = 0, 0
    for _ in range(len(cipher)):
        result += rail[row][col]
        col += 1

        # Change direction at the top or bottom rail
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Move up or down
        row += 1 if direction_down else -1

    return result


# Main program loop for encryption and decryption
flag = True  # Initialize a flag to control the loop
while flag:
    print("\nEncryption and Decryption using Rail Fence Cipher")
    choice = input("Do you want to Encrypt or Decrypt? ")  # Ask the user for their choice
    enc = "encrypt"
    dec = "decrypt"

    # Check if the user wants to encrypt
    if choice in [enc, enc.upper(), enc.capitalize(), "E", "e"]:
        string = input("Enter the message to Encrypt: ")  # Input the message to encrypt
        key = int(input('Enter the key: '))  # Input the encryption key

        output = encrypt_rail_fence(string, key)  # Call the encrypt function
        print("The Encrypted message is:", output, "\n")

    # Check if the user wants to decrypt
    elif choice in [dec, dec.upper(), dec.capitalize(), "D", "d"]:
        string = input("Enter the Cipher to Decrypt: ")  # Input the cipher text to decrypt
        key = int(input('Enter the key: '))  # Input the decryption key

        output = decrypt_rail_fence(string, key)  # Call the decrypt function
        print("The Decrypted message is:", output, "\n")

    # Handle invalid inputs
    else:
        print("Invalid Input, Try Again!!\n")

    # Ask the user if they want to exit
    exit = input("Do you want to Exit? (Y/N) ")
    if exit == "Y" or exit == "y" or exit == "yes" or exit == "Yes":
        flag = False  # Set the flag to False to exit the loop
print("Exit")