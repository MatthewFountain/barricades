__author__ = 'student'

from questions2 import Category, Boolean_tables_questions

import unittest


class Category_test(unittest.TestCase):
    def test_pick_questions(self):
        x = Category("test", Boolean_tables_questions)
        x.pick_questions()
        self.assertIn(x.all_bank, [('Q1', 'A1'), ('Q2', 'A2'), ('Q3', 'A3'), ('Q4', 'A4')])


if __name__ == '__main__':
    unittest.main()
