import unittest
from math_quiz import generateRandomInt, generateRandomOperator, buildMathProblem


class TestMathGame(unittest.TestCase):

    def test_generateRandomInt(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateRandomInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generateRandomOperator(self):
        # Test if random generated operators are valid
        valid_operators = ['+', '-', '*']
        for _ in range(100): 
            operator = generateRandomOperator()
            self.assertIn(operator, valid_operators)

    def test_buildMathProblem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3,2,'-','3-2',1),
                (4,5,'*','4*5',20)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = buildMathProblem(num1,num2,operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer,expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()

