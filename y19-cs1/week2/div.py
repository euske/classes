x=int(input("X"))
y=int(input("y"))
q=0
while y<=x:
  x -= y
  q+=1
print(q)
print(x)
