import random
y = random.randint(1, 10)
x = int(input('Please enter a number from 1 to 10:'))
attempt = 1
while attempt <= 3:
    if x != y:
        print('You lose :c')
        attempt += 1
        x = int(input('New attempt:'))
    else:
        print('You won!')
        break
print('Game over')
