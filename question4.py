largest = 0
palindromes = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if str(i*j)[:3] == str(i*j)[-3:][::-1] and len(str(i*j)) == 6:
            palindromes.append(i*j)
            break

for i in palindromes:
    if i > largest:
        largest = i
        
print(largest)
