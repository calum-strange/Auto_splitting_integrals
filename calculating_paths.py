from auto_integrals import (
    generate_integrals_of_order,
    path_integral_calculation
)
from sympy import sqrt
from fractions import Fraction


LT1 = [
    [[[1, 'h']], 0],
    [0, [[1 ,'W']]]
]

LT2 = [
    [0, [[1 ,'W']]],
    [[[1, 'h']], 0]
]

Strang = [
    [[[Fraction(1,2), 'h']], 0],
    [0, [[1 ,'W']]],
    [[[Fraction(1,2), 'h']], 0]
]

HS1 = [
    [ [[Fraction(1, 2)-sqrt(3)*Fraction(1,6), 'h']] , 0],
    [0, [[Fraction(1,2), 'W'], [sqrt(3), 'H']]],
    [[[sqrt(3)*Fraction(1, 3), 'h']], 0],
    [0, [[Fraction(1,2), 'W'], [-sqrt(3), 'H']]],
    [[[Fraction(1, 2)-sqrt(3)*Fraction(1,6), 'h']], 0]
]

HS2 = [
    [0, [[Fraction(1,2), 'W'], [1, 'H'], [-Fraction(1,2), 'C']]],
    [[[Fraction(1, 2), 'h']] , 0],
    [0, [[1, 'C']]],
    [[[Fraction(1, 2), 'h']] , 0],
    [0, [[Fraction(1,2), 'W'], [-1, 'H'], [-Fraction(1,2), 'C']]]    
]

SO1 = [
    [0, [[1, 'H'], [Fraction(1,2), 'sqrt(h)*n']]],
    [[[1, 'h']], [[1, 'W'], [-1, 'sqrt(h)*n']]],
    [0, [[-1, 'H'], [Fraction(1,2), 'sqrt(h)*n']]]
]

SO2 = [
    [0, [[Fraction(1,2), 'W'], [1, 'H'], [-Fraction(1,2), 'C']]],
    [[[1, 'h']], [[1, 'C']]],
    [0, [[Fraction(1,2), 'W'], [-1, 'H'], [-Fraction(1,2), 'C']]],
]

SO2 = [
    [0, [[Fraction(1,2), 'W'], [1, 'H'], [-Fraction(1,2), 'C']]],
    [[[1, 'h']], [[1, 'C']]],
    [0, [[Fraction(1,2), 'W'], [-1, 'H'], [-Fraction(1,2), 'C']]],
]

SO3 = [
    [0, [[Fraction(1,2), 'W'], [1, 'H']]],
    [[[1, 'h']], 0],
    [0, [[Fraction(1,2), 'W'], [-1, 'H']]],
]

SO4 = [
    [0, [[1, 'H'], [6, 'K']]],
    [[[1, 'h']], [[1, 'W'], [-12, 'K']]],
    [0, [[-1, 'H'], [6, 'K']]],
]

paths = [['LT1', LT1], ['LT2', LT2],
        ['Strang', Strang],
         ['HS1', HS1], ['HS2', HS2],
         ['SO1', SO1], ['SO2', SO2],
         ['SO3', SO3], ['SO4', SO4] ]


order = 2

print(f'Order {order}')
for integral in generate_integrals_of_order(order):
    
    print()
    integral_label = '# integral I_' + str(integral) + ' #'
    print(len(integral_label)*'#')
    print(integral_label)
    print(len(integral_label)*'#')
    print()

    for label, path in paths:
        
        print(label) 
        result = path_integral_calculation(path, integral)
        for i, key in enumerate(result.keys()):
            
            print('(',result[key],')', key, end=' ')
            if i >= 0 and i < len(result.keys())-1:
                print('+', end=' ')
        print('')
        print('-----------------------------')