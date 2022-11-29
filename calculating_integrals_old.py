from auto_integrals import (
    generate_integrals_of_order,
    path_integral_calculation_old
)


# path ordered from i = 0, ... , num_of_pieces
# any length path will work here, place 0 for zero derivatives and a string for other parts.
# Left column is time, right column is space
# simply writing A, B, C etc is probably most pracitcal


LT1 = [[' h ', 0], [0, ' W ']]
LT2 = [[' h ', 0], [0, ' W ']]

Strang = [[' h/2 ', 0],[0, ' W '],[' h/2 ', 0]]
Strang_ = [[' A ', 0],[0, ' B '],[' C ', 0]]


HS1= [[ ' (3-sqrt(3))/6 h ' , 0],
             [ 0, ' (W/2 + sqrt(3) H) ' ],
             [ ' sqrt(3)/3 h ' , 0], 
             [ 0, ' (W/2 - sqrt(3) H) ' ],
             [ ' (3-sqrt(3))/6 h ' , 0]
             ]

HS2 = [[0, ' (W/2 + H - C/2) '], [' h/2 ', 0], [0, ' C '], [' h/2 ', 0], [0, '(W/2 - H - C/2)']]

SO1 = [[0, ' (H + sqrt(h) * n /2) '], [' h ', ' (W - sqrt(h) * n) '], [0, '(- H + sqrt(h) * n /2)']]
SO2 = [[0, ' (W/2 + H - C/2) '], [' h ', ' C '], [0, '(W/2 - H - C/2)']]
SO3 = [[0, ' (W/2 + H) '], [' h ', 0], [0, '(W/2 - H)']]
SO4 = [[0, ' (H + 6K) '], [' h ', ' (W - 12K) '], [0, '(- H + 6K)']]


example_integral = [1, 0, 0] # 0 denotes time integral, 1 denotes space integral. This is ordered inside out, so dw dt dt = [1, 0, 0]

order = 6
print(f'Order {order}')
for integral in generate_integrals_of_order(order):
    print('---------------------------!!!!!!!!!')
    print(integral)
    print('LT1:')
    print(path_integral_calculation_old(LT1, integral))
    print('LT2:')
    print(path_integral_calculation_old(LT2, integral))
    print('Strang:')
    print(path_integral_calculation_old(Strang, integral))
    print('HS1:')
    print(path_integral_calculation_old(HS1, integral))
    print('HS2:')
    print(path_integral_calculation_old(HS2, integral))
    print('SO1')
    print(path_integral_calculation_old(SO1, integral))
    print('SO2')
    print(path_integral_calculation_old(SO2, integral))
    print('SO3')
    print(path_integral_calculation_old(SO3, integral))
    print('SO4')
    print(path_integral_calculation_old(SO4, integral))

