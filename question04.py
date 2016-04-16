palindrome = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        product = str(i*j)
        if product == product[::-1] and len(str(i*j)) == 6:
            if int(product) > palindrome:
                palindrome = int(product)
            break
        
print(palindrome)
