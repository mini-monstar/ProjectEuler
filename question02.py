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

##OR

fibonacci = [0,1]
count = 0
length = len(fibonacci)-1

while fibonacci[length] + fibonacci[length-1] < 4000000:
    x = fibonacci[length] + fibonacci[length-1]
    fibonacci.append(x)
    if x%2 == 0:
        count + x
    length += 1

print(count)
