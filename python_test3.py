__author__ = 'student'
import Tkinter
import random
import questions2 as q

correct_answers = []
questions_asked = []

bools = q.Category("testing boolean knowledge", q.Boolean_tables_questions)

# print(bools.testing_bank)
# This is an empty bank
#Multiple_choice_questions = [{Category-Key:[(Q&A-tuple), (Q&A-tuple2)]}]

def greeting():
    #Cue music and greeting-voice-over
    #Cue snake hissing
    print("Welcome to Test Your Python Knowledge!  Dare to try?")
    print("There are 64 questions.  You must answer 45 to pass.  If you do not pass, you fail."
          "  You'll be tested on Operators, Stacks and Qeues, Built-in Functions, Modules, Commands, Packages,"
          "Imports, Decorators, String Operators, Boolean Values, Arguments, Conditions, Loops, Classes, I/O "
          "Methods, PEP 8 and DRY. Ready?")


class Test():
    def __init__(self, name):
        self.name = name
        #list storing category instances
        self.questions = [bools]
        self.correct_answers = 0.0
        self.total_answers = len(self.questions)
        self.score = self.correct_answers / self.total_answers

    #create category instances and put them into self.questions list
    def load_questions(self):
        pass

    def ask_question(self, category):
        for question in category.testing_bank:
            print(question)
            answer = raw_input('type your answer here: ')
            if answer == category.testing_bank[question][1]:
                self.correct_answers += 1.0


m = Test("matthew's test")




#
# m = Test("matthew's test")
# print(m.correct_answers)
# print(m.questions)
# print(m.total_answers)
# print(m.score)
# print(m.name)
# m.ask_question(bools)




#Method1: Inventory
#Method2: Question
#Method3: Verify
#Method4: Scorecard()


# Test():
#     While
#     questions_asked < 56:
#     Inventory()
#     Question()
#     Verify()
#     Scorecard()


#def inventory():
#if len(questions2.) > 0:
#terms_categories()
#Below, this just checks to see if 2 questions from each remaining "super" category have been asked.
#If not, the tester gets another question from that super-category. If so, it skips that super-category.
#Elif boolean_tables_questions[] > 8:
#Send the [1] offset from Total_test to question() as an argument, because [1]
#represents Total_Boolean_questions[].
#Elif debugging_syntax_questions[] > 8:
#Send the [2] offset from Total_test to question() as an argument, because [2]
#represents Total_Debugging_questions[].
#Elif Pep8_DRY questions[] > 8:
#Send the [3] offset from Total_test to question() as an argument, because [3]
#represents Total__questions[].
#Elif Prove_You_Can_Code[] > 8:
#Send the [4] offset from Total_test to question() as an argument, because [4]
#represents Total__questions[].

#Create a for_loop for above, maybe with every value in Total_Test.

#inventory()

