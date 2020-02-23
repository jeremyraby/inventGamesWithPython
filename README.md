# README

I'm working through Al Sweigart's "Invent Your Own Computer Games with Python" to try to build on what programming skills I've gained from multiple sources. I've felt like I'm just floating from one syntax tutorial to another without much to show for it. Hopefully this book will help me synthesize what I've learned and improve where I'm deficient on the basics.


## Number guessing game 

I read the description and tried to build it myself. I started with breaking the program into conceptual steps and writing those in as comments `# Ask the user to guess a number betwen 1 and 20`. Next, I just started building those bits of the program one by one until I’d created the variables and collected user input and made some if/elif branches and realized I put the “can only make 6 guesses” criterion at the bottom when it should have been earlier so as to include a loop. That’s where I had a bit of trouble. I started with trying a while loop `while guesses_made < 6` which only took my guess, told me I was wrong 5 more times and then told me the correct number. I then tried a for loop but couldn’t remember the correct syntax `for x in range(y)`, but that didn’t fare any better. I finally looked in the book and saw that my guesses_made variable was written outside the loop instead of inside it. Everything worked correctly after I made that small change.

## Jokes

This program was mainly about introducing the escape character `\` in order to use single and double quotes, as in `print('Who\'s in charge here?')` or `print("I do not say \"bleh bleh bleh\"")`. Since I read the description and tried to build it on my own first, I didn't actually do that, opting to use single quotes inside of double quotes as in `print('I do not say "bleh bleh bleh"')` mainly because I don't like how it looks to have a bunch of backslashes everywhere. I'm not sure how pythonic this practice is, though, and may change my ways as I get more used to PEP 8. 

The last joke, the knock-knock one, was a bit troubling for me as I thought maybe it was supposed literally interrupt the user. I guess I was mistaken as that's not how Sweigart wrote the program. In any case, I couldn't figure out how to do that and I'll have to revisit this later when I get more experience with the `time` module. _For reference, I tried to reassign a variable by calling the `time.seconds()` function._