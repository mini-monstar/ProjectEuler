fibonacci = [0,1]
count = 0
length = len(fibonacci)-1

while fibonacci[length] < 4000000:
    length = len(fibonacci)-1
    fibonacci.append(fibonacci[length] + fibonacci[length-1])
    
for i in fibonacci:
    if i%2 == 0:
        count += i
print(count)
