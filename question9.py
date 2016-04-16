for a in range(1,333):
  done = False
  for b in range(1,500):
    for c in range(335,998):
      if a + b + c == 1000 and a<b<c:
        if a**2 + b**2 == c**2:
          print(a*b*c)
          done = True
      if done:
        break
    if done:
      break
  if done:
    break

#OR

for i in range(335,998):
    done = False
    y = 1000 - i
    x = y//2
    if x == y-1:
        x-=1
    for j in range(x,-1,-1):
        z = y-j
        if z > i:
            break
        else:
            if z**2 + j**2 == i**2:
                print(z*j*i)
                done = True
                break
    if done:
        break
