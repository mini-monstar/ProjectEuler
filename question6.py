sumsquare = 0
squaresum = 0

for i in range(1,101):
    sumsquare += i**2
    squaresum += i
    
print(squaresum**2 - sumsquare)
