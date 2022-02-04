import random

randomVar = 0
container = []

for i in range(1000000):
    randomVar = random.randint(0, 100)
    container.append(randomVar)

for i in range(100):
    repeat = int(container.count(i)/100)
    print(str(i) + ' : ', end='')
    for y in range(repeat):
        print("*",end='')
    print('')
    
