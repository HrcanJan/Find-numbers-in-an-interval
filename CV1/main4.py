"""Napíšte algoritmus, ktorý pre dané vstupné pole n prirodzených čísel, pričom každý prvok poľa patrí do intervalu <0;k>, 
predspracuje vstup a po predspracovaní dokáže odpovedať na otázku,  koľko prvkov poľa patrí do intervalu <a;b> pre ľubovoľné a,b také, 
že 0 ≤ a ≤ b ≤ k, s výpočtovou zložitosťou O(1). Zložitosť predspracovania môže byť Θ(n + k).
"""

import random

# Random numbers in interval <0;k>
n = []
n_length = random.randint(1, 100)
k = random.randint(0, 1000)

for i in range(0, n_length - 1):
    n.append(random.randint(0, k))

print("n: ", n)

# new interval
a = random.randint(0, k)
b = random.randint(a, k)
print("a: ", a, "\nb: ", b)
newArr = []

for i in n:
    if(i >= a and i <= b):
        newArr.append(i)

# length of a row
print("answer: ", len(newArr))