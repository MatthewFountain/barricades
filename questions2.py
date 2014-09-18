__author__ = 'student'
import random

Operators = {}

BuiltInFunctions = {1: ('Q1', 'A1'), 2: ('Q2', 'A2'), 3: ('Q3', 'A3'), 4: ('Q4', 'A4')}

Boolean_tables_questions = {1: ('Q1', 'A1'), 2: ('Q2', 'A2'), 3: ('Q3', 'A3'), 4: ('Q4', 'A4')}


class Category():
    def __init__(self, name, all_questions):
        self.name = name
        self.all_questions = all_questions
        self.testing_bank = []
        self.pick(self.all_questions)

    def pick(self, all_questions):
        q1 = random.choice(all_questions.keys())
        self.all_questions.pop(q1)
        q2 = random.choice(all_questions.keys())
        self.all_questions.pop(q2)
        q3 = random.choice(all_questions.keys())
        self.all_questions.pop(q3)
        for i in [q1, q2, q3]:
            self.testing_bank.append(i)


            #
            # , {BuiltInFunctions : [(Q1, A1), (Q2, A2)]}]
            # #Consists of 16 categories, and for each category, 9 questions
            # Boolean_tables_questions = [{Booleans : (Q1, A1), (Q2, A2)}]
            #           #Consists of 10 questions
            # Debugging_syntax_questions = [{Debuggers : (Q1, A1), (Q2, A2)}]
            #           #Consists of 10 questions
            # PEP8_DRY_questions = [{PEP8 : (Q1, A1), (Q2, A2)}]
            #           #Consists of 10 questions
            # Prove_You_Can_Code_questions = [{Prove_It : (Q1, A1), (Q2, A2)}]
            #           #Consists of 10 questions
            #
            # Total_Test = [Total_Multiple_choice_questions, Total_Boolean_tables_questions, Total_Debugging_syntax_questions,
            #               Total_PEP8_DRY_questions, Total_Prove_You_Can_Code_questions]
            #
            #
            #
            #
            # import random
            # categories = [1, 2, 3]
            # questions = [1, 2, 3, 4]
            #
            # def get_random_category():
            #         return random.randrange(len(categories))
            #
            # def ask_question_from_category():
            #     cat = get_random_category()
            #     return question[cat]
            #
            #
            # mcq = [{'cat0': [(1, "what day is it")], 'cat1': [(1, "fav color?"), (2, "fav food?")]}]
            #
            #
            #
            # print (mcq[0]['cat1'][0][1])
            #
            #
            #
            # the 0 being the question part of the tuple
            #
            #
            #
            # class Category():
            #     def __init__(self, name):
            #         self.name = name
            #
            #
            #
            # class Category():
            #     def __init__(self, name):
            #         self.name = name
            #         self.randoms = #pick 3 random number #(random.rangerange(len(all_bank))
            #         self.all_bank = [("question", ...)]
            #         self.test_bank =
            #
            #     def generate_randoms():
            #         #return 3 unique numbers
            #
            # boolean = Category("booleans")
            # boolean.test_bank[0]
            # boolean.test_bank[1]
            # boolean.test_bank[2]
            #
            #
            #
            # boolean = Category("Booleans")
            # boolean.test_bank[0]