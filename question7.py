count = 2
prime = 3
while count < 10001:
    prime += 2
    broke = False
    for i in range(2,int(prime**0.5)+1):
        if prime % i == 0:
            broke = True
            break
    if not broke:
        count += 1
    
print(prime)
