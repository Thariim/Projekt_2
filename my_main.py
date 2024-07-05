"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

import string
from random import sample

spacer='-'*47


def user_input() -> str:
          """
          Funkce veme vstup od uzivatele.
          """
          return input(f'{spacer}\nEnter a 4-digit number without duplicate digits:\n{spacer}\n')



def correction(number) -> str:
     """
     Funkce proveri uzivatelsky vstup a upozorni jej pokud nesplnuje pozadavky
     """
     while True:
          if not number.isdigit():
               print('Your input is not a number')
               number = user_input()
          elif len(number) != 4:
               print('Your input is not 4 digits long')
               number = user_input()
          elif len(list(number)) != len(set(number)):
               print('Your input contains duplicates')
               number = user_input()
          else:
               return number
          
def number_generator() -> str:
    """
    Funkce vygeneruje skryte 4 mistne cislo
    """
    chars = string.digits
    while True:
        random_number = sample(chars, k=4)
        if random_number[0] != '0':
            return ''.join(random_number)    


def cows(input_number,checked_number) -> int:
     """
     Funkce veme uzitalske cislo a proveri zda se hodnoty shoduji se skrytym cislem ale ne na stejnych pozicich 
     """
     cows_count = 0
     for i in range(len(input_number)):
        if input_number[i] != checked_number[i] and input_number[i] in checked_number:
            cows_count += 1
     return cows_count




def bulls(input_number, checked_number) -> int:
    """
    Function to calculate the number of bulls (correct digits in correct positions).
    """
    bulls_count = 0
    for i in range(len(input_number)):
        if input_number[i] == checked_number[i]:
            print(input_number[i],checked_number[i])
            bulls_count += 1
    return bulls_count
     
               
print(f'Hi there!\n'
    f'{spacer}\nI\'ve generated a random 4 digit number for you.\n'
    'Let\'s play a bulls and cows game.'
    )

hidden_number=str(number_generator())

while True:
     user_guess=str(correction(user_input()))
     bulls_count=bulls(user_guess,hidden_number)
     cows_count=cows(user_guess,hidden_number)

     print(f'Bulls: {bulls_count} and Cows: {cows_count}')
     if bulls_count==4:
          print('cg')
          break
     else:
          print('try again')








