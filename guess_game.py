import random

# Set the secret number
secret_number = random.randint(1, 10)

# Set the number of trials
trials = 3

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 trials to guess it.")

while trials > 0:
    # Ask the user for their guess
    user_guess = int(input("Enter your guess: "))

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(" Congratulations! You guessed it!")
        break
    else:
        print(" Sorry, that's not correct.")
        trials -= 1
        print(f"You have {trials} trials left.")

if trials == 0:
    print(f"Game over! The secret number was {secret_number}.")