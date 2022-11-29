import math
from fractions import Fraction

def find_strings_of_length(num_of_pieces, length):
    
    strings = []

    if length == 1:
        for i in range(num_of_pieces):
            strings.append([i])
    
    if length > 1:
        for i in range(num_of_pieces):
            for string in find_strings_of_length(num_of_pieces-i, length-1):
                string.append(i)
                strings.append(string)


    return strings

def find_value_of_string(string):
    
    ongoing_exponent = 1

    factor = 1
    
    for i in range(1, len(string)):
        if string[i] == 0:
            ongoing_exponent += 1
        else:

            factor = factor * math.factorial(ongoing_exponent)
            ongoing_exponent = 1
    factor = factor * math.factorial(ongoing_exponent)
    return factor
   
def path_integral_calculation_old(path, integral):
    results = []
    for string in find_strings_of_length(len(path), len(integral)):
        
        level = len(path)-1
        zero_val = False
        
        integral_factor = find_value_of_string(string)
        dv_factor = ''

        for i in range(len(integral)):
            level = level - string[i]
            # print(level)
            const = path[level][integral[len(integral) - (i+1)]] 
            if const == 0:
                zero_val = True
            elif dv_factor == '':
                dv_factor = const
            else:
                dv_factor = const + ' * ' + dv_factor

        if not zero_val:
            results.append('1 / '+str(integral_factor) + ' * ' + dv_factor)
    return results

def generate_integrals_of_order(p: int):
    if p < 1:
        print('p must be a positive integer')
        return 

    integrals = []
    
    if p == 1:
        integrals = [[1]]
    elif p == 2:
        integrals = [[0], [1,1]]
    else:
        for i, order in enumerate([2,1]):
            for integral in generate_integrals_of_order(p - order):
                integral.append(i)
                integrals.append(integral)

    return integrals

def multiply_factors(left_factor, right_factor):
    results = []
    for left_sign, left_const in left_factor:
        for right_sign, right_const in right_factor:
            results.append([left_sign*right_sign, left_const+'*'+right_const])
    return results

def path_integral_calculation(path, integral):

    results = {}
    
    for string in find_strings_of_length(len(path), len(integral)):
    
        level = len(path)-1
        zero_val = False
        
        integral_factor = find_value_of_string(string)

        dv_factor = ''

        h_factors = ''

        for i in range(len(integral)):
            level = level - string[i]
            const = path[level][integral[len(integral) - (i+1)]]
            if const == 0:
                zero_val = True    
            elif integral[len(integral) - (i+1)] == 0:
                if h_factors == '':
                    h_factors = const
                else:
                    h_factors = multiply_factors(const, h_factors)
                    
            else:
                if dv_factor == '':
                    dv_factor = const
                else:
                    dv_factor = multiply_factors(const, dv_factor)
        
        if not zero_val:
            
            if dv_factor == '':
                for sign, factor in h_factors:
                    if results.get(factor) is None:
                        results[factor] = 0
                    results[factor] += sign * Fraction(1, integral_factor)
            elif h_factors == '':
                for sign, factor in dv_factor:
                    if results.get(factor) is None:
                        results[factor] = 0
                    results[factor] += sign * Fraction(1, integral_factor)
            else:
                dv_factor = multiply_factors(h_factors, dv_factor)

                for sign, factor in dv_factor:
                    if results.get(factor) is None:
                        results[factor] = 0
                    # print(results)
                    results[factor] += sign * Fraction(1, integral_factor)


    return results







