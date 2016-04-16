count = 2
x = 2000000

def prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True

for i in range(3,x,2):
    if prime(i):
        count += i
print(count)
