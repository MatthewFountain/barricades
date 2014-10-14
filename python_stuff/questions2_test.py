__author__ = 'student'
__author__ = 'student'
import random
import shuffle

Operators = {}

# BuiltInFunctions = {1: ('Q1', 'A1'), 2: ('Q2', 'A2'), 3: ('Q3', 'A3'), 4: ('Q4', 'A4')}
#
# Boolean_tables_questions = {1: ('Q1', 'A1'), 2: ('Q2', 'A2'), 3: ('Q3', 'A3'), 4: ('Q4', 'A4')}

#btq = [[1, ('Q1', 'A1')], [2, ('Q2', 'A2')], [3, ('Q3', 'A3')], [4, ('Q4', 'A4')], [5, ('Q5', 'A5')]]
btq = [('Q1', 'A1'), ('Q2', 'A2'), ('Q3', 'A3'), ('Q4', 'A4'), ('Q5', 'A5')]
bif = [('Q1', 'A1'), ('Q2', 'A2'), ('Q3', 'A3'), ('Q4', 'A4'), ('Q5', 'A5')]


class Category():
    def __init__(self, name, all_questions):
        self.name = name
        self.all_questions = all_questions
        self.testing_bank = {}
        self.pick(self.all_questions)

    def pick(self, all_questions):
        random.shuffle(all_questions)
        del all_questions[3:]
        print all_questions

        # q1 = random.choice(all_questions.keys())
        # q2 = random.choice(all_questions.keys())
        # q3 = random.choice(all_questions.keys())
        # for rand_key in [q1, q2, q3]:
        #     for qa_pair in all_questions.values():
        #         print(rand_key)




