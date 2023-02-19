"""Sum of one number in each row must be as close to 0 as possible
"""
import random

# Read and input file
with open('cvicenie1data.txt') as f:
    text = f.readlines()[2:]

with open('cvicenie1data.txt') as f:
    row = int(f.readlines()[0])

# The number that must be as close to 0 as possible
ret = 0
textArray = []

def createArray():
    global text
    for i in range(row):
        x = text[i].split()
        x = list(map(int, x))
        textArray.append(x)

createArray()

def fun(i):
    global ret
    min = textArray[i][0]
    for j in textArray[i]:
        if(abs(j + ret) < abs(min + ret)):
            min = j
    
    ret += min

# Global iteration (not good)
print('greedy normal: ')
for i in range(row):
    fun(i)
print("ret1: ", ret)

ret = 0

# Random row algoritm (not much better)
print()
print('greedy random: ')
r = list(range(row))
random.shuffle(r)
for i in r:
    fun(i)
print("ret2: ", ret)
print()

min_ret = ret

# Randomly change value in each row sometimes, to get better results
counter = 0
while(counter < 5000):
    for i in range(row):
        rand = random.randint(0, 3)
        min = textArray[i][rand]

        rand2 = random.randint(0, 3)
        if(rand2 != 0):
            for j in textArray[i]:
                if(abs(j + ret) < abs(min + ret)):
                    min = j

        ret += min

    counter += 1

    if(abs(ret) <= abs(min_ret)):
        min_ret = ret
        counter = 0

    ret = 0

print("sum: ", min_ret)