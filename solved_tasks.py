#!/usr/bin/env python3

def handle_task_1(n):
    return "Silence is golden\n" * n
    
def handle_task_2():
    return ' '.join(str(i) for i in range(1001, 1026))

def handle_task_3():
    from math import factorial
    return int(factorial(13) / factorial(4))
    
def handle_task_4():
    number = 11
    while sum(bool(number % i - 1) for i in range(2, 11)):
        number += 11
    # debug info
    #print( 'check:' )
    #print(number, ': ', tuple((number % i - 1) for i in range(2, 11)), 
    #    tuple(bool(number % i - 1) for i in range(2, 11)),
    #    sum(bool(number % i - 1) for i in range(2, 11)) )
    return number

def handle_task_5():
    alphabet_range = range(65, 65 + 26)
    alphabet = list(map(chr, alphabet_range))
    for i in range(len(alphabet)):
        if not (i + 1) % 5:
            alphabet[i] += '\n'
    return '\n ' + ' '.join(alphabet)
    
def handle_task_6():
    table = ''
    
    for n in range(1, 11):
        table += '\n\n'
        table += '\n'.join('{number} * {multiplicator} = {result}'.format(\
            number = n, multiplicator = m, result = n * m)\
            for m in range(1, 11) )
    
    return '\n=====TABLE OF MULTIPLICATIONS====' + table

def handle_task_7(n):
    initial_distance = 10.0 # km
    increment_percent = 10
    coef = 1 + increment_percent / 100
    text_result = ''
    
    text_result += '\nTreaning days: \n'
    everyday_distance = initial_distance
    for d in range(1, 11):
        text_result += \
            '\tday {day}:  distance {distance} km \n'\
            .format(day = d, distance = round(everyday_distance, 2))
        everyday_distance *= coef
        
    days = 7
    text_result += '\nTotal distance during {1} days: {0}\n'\
                   .format(round(initial_distance * (coef ** days), 2), days)
    
    text_result += '\nTotal distance during {1} days: {0}\n'\
                   .format(round(initial_distance * (coef ** n), 2), n)
    
    from math import log
    distance_limit = 80.0
    text_result +=\
        '\nSkiman have to stop at {0}-th day not to overcome {1} km distance limit\n'\
        .format(int(log(distance_limit / initial_distance, coef)), distance_limit)
    return text_result
    
    
def handle_task_8():
    return ' '.join(filter(lambda x: '5' not in x and '6' not in x, map(str, range(1000, 10000)) ))

def handle_task_9(character):
    base = ord('a')
    alphabet_len = ord('z') - base + 1
    letter_num = ord(character.lower())
    
    return ' '.join( chr(base + (letter_num - base + i) % alphabet_len ) for i in range(1, 4) )
    
def handle_task_10(pass_length):
    import random
    
    
    characters = tuple( range(33, 95) ) + tuple( range(96, 126) )
    
    upper_letters = tuple(range(65, 91))
    
    digits = tuple(range(48, 58))
    
    # _ is #95
    # 0-9 is in [48..57]

    password = []
    digits_count = 5
    previous_char = None
    
    for i in range(pass_length - 3):
        curent_char = random.choice(characters)
        
        if (curent_char in digits):
            if not digits_count or previous_char in digits :
                while (curent_char in digits):
                    curent_char = random.choice(characters)
            else:
                digits_count -= 1
        
        password.append(chr(curent_char))
        previous_char = curent_char
    
    addition = [random.choice(upper_letters), random.choice(upper_letters), 95]
    random.shuffle(addition)
    addition = map(chr, addition)
    
    for add_char in addition:
        rand_index = random.choice(range(len(password)))
        password.insert(rand_index, add_char)
        
    return ''.join(password)
    

def main():
    
    test_inputs = (
        (1, (5, )),
        (2, ()),
        (3, ()),
        (4, ()),
        (5, ()),
        (6, ()),
        (7, (10, )),
        (8, ()),
        (9, ('A', )),
        (9, ('y', )),
        (9, ('z', )),
        (10, (6, )),
        (10, (15, )),
        (10, (20, )),
    )
    
    for i, values in test_inputs:
        print('Task {0} '.format(i))
        print('Input: ' + str(*values))
        print('Output: ', end='')
        handler_name = 'handle_task_' + str(i)
        handler = globals()[handler_name]
        print(handler(*values))
        print('=================================')

  
if __name__ == '__main__':
    main()