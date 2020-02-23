import time, random


def display_intro():
    # Introduction to the game
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')

def choose_cave():
    # Player chooses which cave to enter
    cave = ''
    while cave != 1 and cave != 2:
        cave = int(input('Which cave will you enter? (1 or 2)'))
    return cave

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and ...")
    time.sleep(2)

    # If/else player goes in "hungry" or "friendly" cave
    friendly_cave = random.randint(1, 2)

    if chosen_cave == friendly_cave:
        print('... says "How\'s it going? Want some pizza?"')
    else:
        print('Gobbles you down in one bite!')

# Create a loop for the game to run
play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)
    print('Do you want to play again? (yes or no)')
    play_again = input()



