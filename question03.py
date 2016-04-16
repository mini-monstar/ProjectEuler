number = 600851475143
primenumber = 2
while number > primenumber:
    while number % primenumber == 0:
        number //= primenumber
        
    primenumber += 1
print(primenumber)
