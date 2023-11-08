import unittest
import math

from main import Solver


EPSILON = 0.0001


class TestF(unittest.TestCase):
    def test_main(self):
        f_strings = ['x*x + 5',
                     'x**2 -3*x + 4']
        
        x = [[1, 2, -3],
             [1, 2, -3]]
        
        y = [[6, 9, 14],
             [2, 2, 22]]

        for f_num in range(len(f_strings)):
            f = Solver.get_f_from_str(f_strings[f_num])
            for x_num in range(len(x[f_num])):
                self.assertEqual(f(x[f_num][x_num]), y[f_num][x_num], 
                                 f'In function f(x)={f_strings[f_num]} for x={x[f_num][x_num]} ' + \
                                    f'y should be {y[f_num][x_num]} instead of {f(x[f_num][x_num])}.')


class TestD(unittest.TestCase):
    def test_main(self):
        fs = [lambda x: x**2 + 15,
              lambda x: x**2 -3*x + 4]

        f_strs = ['x**2 + 15',
                  'x**2 -3*x + 4'] # for output and debugging
        
        x = [[0, 1, -2],
             [0, 1, -2]]
        
        y = [[0, 2, -4],
             [-3, -1, -7]]

        for f_num in range(len(fs)):
            d = Solver.get_d_from_f(fs[f_num])
            for x_num in range(len(x[f_num])):
                self.assertTrue(abs(d(x[f_num][x_num]) - y[f_num][x_num]) <= EPSILON, 
                                 f'Derivative of function f(x)={f_strs[f_num]} for x={x[f_num][x_num]} ' + \
                                    f'should be {y[f_num][x_num]} instead of {d(x[f_num][x_num])}.')



class TestSolutions(unittest.TestCase):
    def test_main(self):
        linear = ['2*x + 5',
                  '-x - 10',
                  '1']
        
        linear_sol = [[-2.5],
                     [-10],
                     []]
        
        quadratic = ['x**2',
                     'x**2 -3*x -4',
                     'x**2 + 1',
                     '-3*x**2 + 10*x + 100']
        
        quadratic_sol = [[0],
                         [-1, 4],
                         [],
                         [-4.3426, 7.6759]]

        f_strs = linear + quadratic
        
        solutions = linear_sol + quadratic_sol


        for f_num in range(len(f_strs)):
            f = Solver.get_f_from_str(f_strs[f_num])
            d = Solver.get_d_from_f(f)

            sol = list(sorted(Solver.get_solutions(f, d)))
            error = 0

            for i in range(len(sol)):
                error = max(error, abs(sol[i] - solutions[f_num][i]))

            if len(sol):
                error /= len(sol)

            self.assertTrue(error <= EPSILON, f'Solutions of f(x)=0 for function f(x)={f_strs[f_num]} ' + \
                                f'should be {solutions[f_num]} instead of {set(Solver.get_solutions(f, d))}.')



if __name__ == '__main__':
    unittest.main()