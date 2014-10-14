__author__ = 'student'
import random

# Quiz question banks.
Boolean_tables_questions = [
    ('True or True', 'True'), ('False and False', 'False'), ('True or False', 'True'),
    ('True and True', 'True')]

BuiltInFunctions = [
    ("""x = 3
y = 4
print cmp(x, y)
What will print?
a) -1  b) 1  c) 2""", 'a'),
    ("""x = 5
y = 3
print pow(5, 3)
What will print?
a)243  b) 125  c)  34,  d) 1""", 'b'),
    ("""'print tuple("cat")
What will print?
a) ('ca', 't')  b) ('cat', 'cat')  c) (('c', 'a'), t)  d) ('c', 'a', 't')""", 'd'),
    ("""x = [5, 6, 7, 100]
print len(x)
What will print?
a) 4  b) 3  c) 95  d) Error""", 'd')]


# Player is initialized.
class Player():
    def __init__(self, score=0):
        self.score = score


"""After a greeting, Player is asked three questions chosen from the first category bank above. Then ditto the
econd category bank. After all six questions, Player's score is tallied."""
def new_game():
    greeting()
    bools = Category("Boolean Questions", Boolean_tables_questions)
    bools.pick_questions()
    ask_questions(bools)
    builtins = Category("Builtin Functions", BuiltInFunctions)
    builtins.pick_questions()
    ask_questions(builtins)
    print "Your final score is " + str(player1.score)


def greeting():
    print("Welcome to Test Your Python Knowledge!  Dare to try?\n")
    print("There are 6 questions.  60 is a perfect score.\n"
          "You'll be tested on Booleans and Built-in Functions. Ready?\n")


"""Player's score is presented before each question. Each of the three questions picked (out of a bank of
four) is asked one by one. Player's answer is verified and they're told whether or not they're right."""
def ask_questions(category):
    for i in range(len(category.all_bank)):
        print "Your score is currently " + str(player1.score)
        print category.all_bank[i][0]
        user_answer = raw_input('type answer here: ')
        if user_answer == category.all_bank[i][1]:
            print  "Correct"
            player1.score += 10
        else:
            print "You are wrong."
            player1.score -= 5


#Each time this category is called, it selects three random questions from a bank and adds it to a new list.#
class Category():
    def __init__(self, name, all_questions):
        self.name = name
        self.all_questions = all_questions
        self.all_bank = []

    def pick_questions(self):
        for i in range(3):
            b = random.choice(self.all_questions)
            self.all_bank.append(b)
            self.all_questions.remove(b)


player1 = Player()
new_game()
