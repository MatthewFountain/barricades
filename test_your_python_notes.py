__author__ = 'student'
import Tkinter
import random
# greeting = raw_input("Welcome to Test Your Python Knowledge...")
# snd = Sound()
# snd.read('hiss.wav')
# snd.play
# topics = raw_input("You'll be tested on:")
#
# hurrahs = ["Way to go!", "You rock!"]
# jeers = ["Study up, motherfucker!", "Ha! Not even cah-loase!"]
#
# question = raw_input("What is the following? [1, 2, 3, 4] a) list; b) dictionary; c) tuple; or d) string?")
#
# if question == "a":
#     print random.choice(hurrahs)
# else:
#     print random.choice(jeers)
mGui = Tkinter()
mGui.geometry('450 x 450')

Category_tags = []
Category_tags = []


def q_compiler():
    #Checks to see if the key/category of the asked question is from Total_multiple_choice_questions
    #super-category. If so, this function adds that question to its assigned dictionary within the
    Multiple_choice_questions[].
    #This dictionary should be filled with 3 questions from each of the 16 categories.


#But how does it know it’s dropping the question into the right bank? It has to know by the key value.

def pick(category):
    q1 = random.randrange(len(category))
    q2 = random.randrange(len(category))
    q3 = random.randrange(len(category))
    return [category[q1], category[q2], category[q3]]