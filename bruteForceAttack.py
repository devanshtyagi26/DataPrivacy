import random  # Importing the random module to generate random choices
import string  # Importing the string module for predefined character sets (letters, digits, punctuation)
import time  # Importing the time module to measure how long the brute-force attack takes

# Define the character set that includes all uppercase, lowercase letters, digits, and punctuation
char_set = string.ascii_letters + string.digits + string.punctuation

# Convert the character set into a list of individual characters
charData = list(char_set)

# Prompt the user to input the target password
password = str(input("Enter the password: "))

# Initialize the variable to store the current guess as an empty string
myGuess = ""

# Initialize the iteration count to 0
iterations = 0

# Record the start time to calculate how long the attack takes
startTime = time.time()

# Begin the brute-force loop: keep generating guesses until the correct password is found
while(myGuess != password):
    # Generate a random guess of the same length as the target password
    myGuess = random.choices(charData, k=len(password))
    
    # Increment the number of iterations (attempts)
    iterations += 1

    # Print the current guess and the number of iterations
    print(myGuess, "Iterations: ", iterations)
    
    # Convert the list of characters into a string
    myGuess = "".join(myGuess)

# Once the correct password is found, stop the loop and record the end time
endTime = time.time()

# Print the successfully guessed password
print("Your password is:", myGuess)

# Print the total time taken to guess the password and the number of iterations
print(f"Time taken: {endTime - startTime:.4f} seconds")
