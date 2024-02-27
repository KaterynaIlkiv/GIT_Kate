import random
number=random.randint(1,100)
while True:
    print('Guess the number: ')
    guess=input()
    i=int(guess)
    if i==number:
        print('You''re right!')
        break
    elif i<number:
        print('Take the bigger one')
    elif i>number:
        print('Take the smaller one')
