# README

I'm working through Al Sweigart's "Invent Your Own Computer Games with Python" to try to build on what programming skills I've gained from multiple sources. I've felt like I'm just floating from one syntax tutorial to another without much to show for it. Hopefully this book will help me synthesize what I've learned and improve where I'm deficient on the basics.


## Number guessing game 

I read the description and tried to build it myself. I started with breaking the program into conceptual steps and writing those in as comments {include comment example}. Next, I just started building those bits of the program one by one until I’d created the variables and collected user input and made some if/elif branches and realized I put the “can only make 6 guesses” criterion at the bottom when it should have been earlier so as to include a loop. That’s where I had a bit of trouble. I started with trying a while loop (while guesses_made < 6) which only took my guess, told me I was wrong 5 more times and then told me the correct number. I then tried a for loop but couldn’t remember the correct syntax (for x in range(y)), but that didn’t fare any better. I finally looked in the book and saw that my guesses_made variable was written outside the loop instead of inside it. Everything worked correctly after I made that small change.