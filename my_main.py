"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Viktor Krchňavý
email: krchnavy.viktor@gmail.com
discord: thariim
"""
import string
from random import sample

spacer='-'*47

def user_input() -> str:
    '''
    Funkce čistě pro sběr vstupu od uživatele.
    '''
    return input(f'{spacer}\nEnter a 4-digit number without duplicate digits:\n{spacer}\n>>> ')

def input_correction(number) -> str:
    '''
    Funkce prověřuje zda uživatel vložil číslo, ne kratší, ne delší než 4 znaky a bez duplikací.
    '''
    while True:
        if not number.isnumeric():
            print('Your input is not a number. Please try again.')
            number=user_input()
        elif len(number) != 4:
            print('Your input is not 4-digit long. Please try again')
            number=user_input()
        elif len(number) != len(set(number)):
            print('Your input contains duplicates. Please try again')
            number=user_input()
        else:
            return str(number)
        
def hidden_generator() -> str:
    '''
    Funkce skrytě vygeneruje číslo dlouhé 4 znaky bez duplikací, které nezačíná 0
    '''
    roster=string.digits
    while True:
        hidden_number=''.join(sample(roster,4))
        if hidden_number[0] != '0':
            return str(hidden_number)

def numOfBullsCows(num:str,guess:str) -> list[int]: 
    '''
    Funkce vyhodnocuje kolik číslic z uživatelem zadané hodnoty se shoduje 
    s vygenerovaným číslem a kolik jich také sdílí i stejnou pozici.
    '''
    bull_cow = [0,0] 
    for i,j in zip(num,guess): 
        if i in guess: 
            if i == j: 
                bull_cow[0] += 1
            else: 
                bull_cow[1] += 1
    return bull_cow 

def plural_singular(bull_cows:list) -> None:
    '''
    Funkce vypíše jednotné číslo bull/cow v případě, že se uživatel trefil jenom jedním číslem.
    '''
    if bull_cows[0] == 1:
        bulls_str=' bull'
    else:
        bulls_str=' bulls'
    if bull_cows[1] == 1:
        cows_str=' cow'
    else:
        cows_str=' cows'
    print(f'{bull_cows[0]} {bulls_str}, {bull_cows[1]} {cows_str}')

def attempt(attempts) -> str:
    '''
    Funkce zabezpečí aby počet pokusů byl zapsán ve správném tvaru.
    '''
    result=''
    if attempts == 1:
        result=f'in {attempts} guess!'
    else:
        result=f'in {attempts} guesses!'
    return result


print(f'Hi there!\n'
    f'{spacer}\nI\'ve generated a random 4 digit number for you.\n'
    'Let\'s play a bulls and cows game.'
    )

hidden_number=hidden_generator()
print(hidden_number)
attempts=1

while True:
    input_str=input_correction(user_input())
    bull_cow=numOfBullsCows(input_str,hidden_number)
    
    if bull_cow[0] == 4:
        print(f'Correct, you\'ve guessed the right number {attempt(attempts)}')
        break
    else:
        plural_singular(bull_cow)
        attempts+=1








