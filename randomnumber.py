import random

number = random.randint(1, 10)

guess = 0
chances = 0
while guess!= number:
    if chances == 5:
        print('you got enough changes to guess. terminating')
        break
    guess = int(input('Guess any number bw 1 and 10. Enter 0 to quit : '))
    
    if guess == 0:
        print('bye')
        break;
    if 1<=guess<=10:
        if guess == number:
            print('you guess it correct')
            break
        elif guess > number:
            print('guess lower')
        else:
            print('guess higher')
    chances = chances+1
