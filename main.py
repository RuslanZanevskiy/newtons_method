from math import *
from typing import Set, List, Callable


RANGE_LEFT = -50
RANGE_RIGHT = 50
RANGE_STEP = 1.555555
STEPS = 150
DELTA_X = 0.000001
FLOAT_NUM = 5
SOLUTION_TRESHOLD = 0.001


class Solver:
    @staticmethod
    def get_solutions(f: Callable, d: Callable) -> List[float]:
        solutions: Set[float] = set()

        X = RANGE_LEFT

        while X < RANGE_RIGHT:
            x = X

            for _ in range(STEPS):
                x -= f(x)/d(x)

            if abs(f(x)) <= SOLUTION_TRESHOLD:
                solutions.add(round(x, FLOAT_NUM))

            X += RANGE_STEP

        return list(solutions)
        
    @staticmethod
    def get_avr_error(f: Callable, solutions: List) -> float:
        if not solutions:
            return 0
        
        error = 0

        for sol in solutions:
            error += abs(f(sol))
        
        return error / len(solutions)

    @staticmethod
    def get_f_from_str(f_str: str) -> Callable:
        return lambda x: eval(f_str)
    
    @staticmethod
    def get_d_from_f(f: Callable, dx: float = DELTA_X) -> Callable:
        def d(x):
            dy = f(x+dx)-f(x)
            if dy:
                return dy / dx
            return dx

        return d


def main() -> None:
    is_default: bool = input('Use default settings(y/n)?: ').lower() != 'n'

    if not is_default:
        pass

    f_inp = input('Enter a function(x - variable, you can use other functions like sin, exp, max): ')
    f = Solver.get_f_from_str(f_inp)
    d = Solver.get_d_from_f(f)

    solutions = [*sorted(Solver.get_solutions(f, d))]
    #error = Solver.get_avr_error(f, solutions)

    if not solutions:
        print('Solutions for f(x) = 0 not found! May be try different settings.')
    else:
        print(f'Found {len(solutions)} solutions for f(x)=0: ' + ', '.join([str(i) for i in solutions]))
        #print(f'Average error: {error}')


if __name__ == '__main__':
    main()
