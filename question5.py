import math
multiples = 1

def prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                return False
        return True
    
for i in range(1,21):
    if prime(i):
        multiples *= i

answer = multiples

while True:
    divisible = True
    for i in range(3,21):
        if answer % i != 0:
            divisible = False
            break
    if divisible:
        print(answer)
        break
    else:
        answer += multiples
