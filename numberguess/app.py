import random
from random import randint

guesstaken = 0
ran = random.randint(1,20)
maxn =4

while guesstaken < 5:
    guess = int(input('what is the number(1,20): '))

    if guess > ran:
        guesstaken +=1
        print('Number is too large, Try Again')
        continue

    elif guesstaken == maxn:
        print(f'Game Over, The Correct Answer is {ran}')
        break

    elif guess < ran:
        guesstaken +=1
        print('Number is too small, Try Again') 
        continue

    else:
        print('Correct Answer!')
        break 

  
    