triangle = 0
count = 1
found = False
divisors = 0

while not found:
    divisors = 0
    triangle += count
    print(triangle)
    for i in range(1,int(triangle**0.5)+1):
        if triangle % i == 0:
            divisors += 1
            if triangle // i != i:
                divisors += 1
    if divisors > 500:
        found = True
    else:
        count+=1

print(triangle)
