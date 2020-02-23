import time

# Introduction to the game
print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
player_choice = int(input('Which cave will you enter? (1 or 2) \n'))
# Create a loop for the game to run
play_again = True
while play_again == True:
    print('You approach the cave...')
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in fron of you! He opens his jaws and ...")
    time.sleep(2)
# If/elif player goes in "hungry" or "friendly" cave
    if player_choice == 1:
        print('Gobbles you down in one bite!')
    elif player_choice == 2:
        print('... says "How\'s it going? Want some pizza?"')
# Ask to play again
    play_again = input('Want to play again? (y or n) \n')
    if play_again.lower() == 'y':
        play_again = True
    elif play_again.lower() == 'n':
        print('Thanks for playing!')
        break
