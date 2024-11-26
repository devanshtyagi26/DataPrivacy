import random

def load_dictionary(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines, strip whitespace, and return the words
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def generate_password(word_list, num_words=4):
    if len(word_list) < num_words:
        print("Error: Not enough words in the dictionary file to generate the password.")
        return None

    # Randomly select the specified number of words from the word list
    selected_words = random.sample(word_list, num_words)

    # Combine the words into a password (e.g., using hyphens for separation)
    password = ''.join(selected_words)
    return password

# Specify the dictionary file
filename = input("Enter the path to the dictionary file: ")

 # Load the dictionary file
word_list = load_dictionary(filename)

# Generate and display the password
if word_list:
    num_words = int(input("Enter the number of words for the password: "))
    password = generate_password(word_list, num_words)
    if password:
        print(f"Generated Password: {password}")
