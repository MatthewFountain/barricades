#import Tkinter
import random

Boolean_tables_questions = [('Q1', 'A1'), ('Q2', 'A2'), ('Q3', 'A3'), ('Q4', 'A4')]

#print(bools.testing_bank)
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


class Category():
    def __init__(self, name, all_questions):
        self.name = name
        self.all_questions = all_questions
        self.all_bank = []

    def pick_questions(self):
        #self.randoms = (random.range(len(all_bank)))

        for i in range(3):
            b = random.choice(self.all_questions)
            self.all_bank.append(b)
            self.all_questions.remove(b)


class Test():
    def __init__(self, name):
        self.name = name
	self.load_questions()	
        #list storing category instances
        self.questions = []
        self.correct_answers = 0.0
        self.total_answers = len(self.questions)
        self.score = self.correct_answers / self.total_answers

    #create category instances and put them into self.questions list
    def load_questions(self, *categories):
        for category in categories:
	    self.questions.append(category)
    
    def ask_question(self):
        for category in self.questions:
            print(category.all_bank)

bools = Category("boolean questions", Boolean_tables_questions)

m = Test("matthew's test")
m.load_questions(bools)
print(m.questions[0].all_bank)



#Why is it printing a question that's NOT in the list?
#How do I get the test class to run?
#How do I get the test class to include the greeting?
#Will the test as it show the correct answers vs the total answers?






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

