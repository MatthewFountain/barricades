#import randomizing algorithm to help generate a word below.
import random

#tells you what game you're playing and taunts you.
def greeting():
    greet= raw_input("Welcome to Hangman! We hope you'll stay forever. Press Enter to begin.")
    return greet


#Create a function that will pick a random word from a prescribed list of words.
def generator():
    possible_words = ["cat", "dog", "mouse", "taser", "treacherous"]
    secret_word = possible_words[random.randrange(0, len(possible_words))]
    return secret_word


#Player is prompted to pick a letter.
def choose():
    choose_letter = raw_input("Pick a letter.")
    return choose_letter

#This function checks whether or not the chosen letter is inside the secret word.
def check(guess, secret_word, mask):
    #print "check %s, %s, %s" % (guess, secret_word, mask)
    if guess in secret_word:
        return find_replace(char=guess, secret=secret_word, mask=mask)

#This function replaces the masked letters with the revealed letters.
def find_replace(char, secret, mask):
    #print "find_replace %s, %s, %s" % (char, secret, mask)
    for index, letter in enumerate(secret):
        if char == letter:
            mask[index] = char
    return mask

#Graphics function creates a picture of a hanging man via a series of lists. Each wrong answer adds a number to a list
#of strikes, and the higher the number, the bigger the fraction of the picture is revealed.

def graphics(fail):
    picture = [
    '----------\n',
    '|        |\n',
    '|        0\n',
    '|       / |\n',
    '|        |\n',
    '|       / |\n',
    '|\n',
    '|\n']

    if len(fail) == 1:
        print picture[0] + picture[1] + picture[2]
    elif len(fail)== 2:
        print picture[0] + picture[1] + picture[2] + picture[3]
    elif len(fail)== 3:
        print picture[0] + picture[1] + picture[2] + picture[3] + picture[4]
    elif len(fail)== 4:
        print picture[0] + picture[1] + picture[2] + picture[3] + picture[4] + picture[5]
    elif len(fail)== 5:
        print picture[0] + picture[1] + picture[2] + picture[3] + picture[4] + picture[5] + picture[6] + picture[7]
        print "Sorry you died. U mad bro?"
        replay()


def replay():
    ask_user = raw_input("play again?\n type 'y' for yes or 'n' for no.").lower()
    if ask_user == 'y':
        main()
    else:
        exit()

#Greeting is called, then an empty list for strikes to be added to later. Strikes currently equals zero. Generator
#function is called, and within this function, secret is the generator.  A ternary expression is used to turn each
#character of the generated word into an underscore. This new list of underscores is called the mask.

def main():
    greeting()
    total_strikes = []
    strikes = 0
    secret = generator()
    mask = ['_' for character in secret]
    print mask

#Player has 5 strikes. We tell them how many player currently has. If the check function checks the player's guess
    # against the secret word and is correct, and within the if statement "true", print "good guess", print the new mask
    #with the revealed letters. Then there's a conditional statement for when there are no blanks left, we congratulate
    # the winner and ask if they want to play again. If the check function comes up false, we add a strike, then append that strike to a list of strikes.
    #Then we call the graphics function with an argument for the number of total_strikes. Then we say "bad guess" and
    #print the mask again.

    while strikes < 6:
        print("you have %i strikes" % strikes)
        guess = choose()
        if check(guess=guess, secret_word=secret, mask=mask):
            print ("good guess")
            print mask
            if mask.__contains__('_'):
                pass
            else:
                print "Congratulations!  You win!!"
                replay()
        else:
            strikes += 1
            total_strikes.append(strikes)
            print total_strikes
            graphics(total_strikes)
            print ("bad guess")
            print mask


main()



