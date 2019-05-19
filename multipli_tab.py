"""
The program is used to learn or test use
the multiplication tables.
If you would like to finish instead of
answering type "exit" and press enter
"""

from random import shuffle, random, choice
import sys
import logging
import time
import re


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | line: %(levelno)s \
    | func_name: %(funcName)s | %(name)s | type: %(levelname)s \
    | Message: %(message)s')
file_handler = logging.FileHandler('tabMnoz.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def save(segment):
    '''
    the function saves in a file all incorrect
    calculations for the purpose of fixation
    '''
    try:
        def inside():
            with open('TabMnoz_v03.txt', 'a') as file:
                file.write(
                    '\n'+ eq + str(time.strftime('%Y-%m-%d %X')))

        if isinstance(segment, str):
            eq = '\n\tSTART | '
            return inside()
        elif isinstance(segment, (list)) and segment[1] <= 100:
            eq = '{:2} x {:2} = {:3} | writed: {:3} | '\
                  .format(segment[0][0], segment[0][1], segment[0][2], segment[1])
            return inside()
        else:
            print('Bad value!!!')

    except (UnboundLocalError, TypeError, IOError) as error:
        logger.error('method: save(): {}'.format(error))


def regenerate():
    '''
    When the program starts, it records the start time in a file,
    generates mul table and shuffles sentences for the purpose of tests
    '''
    save('-')
    LIST = [(k, v, k*v) for k in range(1, 11)
             for v in range(1, 11)]
    shuffle(LIST)
    return LIST


def choices(LIST):
    ''' 
    The function dowloads random task and saves
    for the purpose of list testing
    '''
    while LIST:
        try:
            RANDOM = choice(LIST)
            print(f'\nlen: {len(LIST):<10} \
                {RANDOM[0]} * {RANDOM[1]} =')
            input_enter(RANDOM)
            LIST.remove(RANDOM)
        except IndexError as error:
            logger.error('method: losuj(): {}'.format(error))


def input_enter(RANDOM):
    '''
    The function compares the users results to the results
    of the program. If the users calculations are incorect
    it sends information to the function that records the
    event with the correct calculations so the user
    can see later it's failures and the correct answers
    '''
    while True:
        tofile = []
        # Redex compile
        pattern = '\D+'
        my_re = re.compile(pattern)
        try:
            wynik = input('Enter = ')
            if wynik.isdigit() and int(wynik) == RANDOM[2]:
                return True
            elif wynik.isalpha() and str(wynik) == 'exit':
                end()
            else:
                print(f'equals: {RANDOM[2]}')
                # Redex check
                if my_re.match(wynik):
                    print('\tredex match: {}'.\
                          format(my_re.match(wynik)))
                    continue
                # save to file
                tofile.extend([RANDOM, int(wynik)])
                save(tofile)

        except (ValueError, TypeError) as error:
            logger.error('method: input_enter(): {}'.format(error))


def end():
    ''' The function closes the program '''
    while True:
        print("Game over")
        sys.exit(0)


if __name__ == '__main__':
    print(f'\n\texit wpisane zamiast wyniku kończy działanie programu !.')
    LIST = []
    RANDOM = ()
    R = regenerate()
    choices(R)
