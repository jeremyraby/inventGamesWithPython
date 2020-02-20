# import randint 
from random import randint
secret_number = randint(1,20)

# Ask the user to guess a number betwen 1 and 20
player = input("Hello! What's your name? ")
print(f"Well, {player}, I'm thinking of a number between 1 & 20.")

# User can only make 6 guesses
for guesses_made in range(6):
    guess = int(input('Can you guess it? '))
# Compare user's guess to a randomly generated number   
    if guess == secret_number:
        print(f'Good job, {player}! You guessed my number in {guesses_made} guesses!')
        break
# If guess is too high, tell the user and let them guess again
    elif guess > secret_number:
        print('Sorry, that was too high. Guess again.')
        guesses_made += 1
# If guess is too low, tell the user and let them guess again
    elif guess < secret_number:
        print('Sorry, that was too low. Guess again.')
        guesses_made += 1

# Tell user the secret number
print(f'The secret number was {secret_number}.') 
