print(
"WELCOME TO BASIC CALCULATOR#0602", 
"1. ADD", "2. SUBTRACT", "3. PRODUCT", "4. DIVIDE", "5. EXIT", sep="\n")

while True:
  y = int(input("Enter number 1: "))
  z = int(input("Enter number 2: "))
  x = int(input("Hello, what do you want to do today"))

if x == 1:
  print(x+y)
elif x == 2:
  print(x-y)
elif x == 3:
  print(x*y)
elif x == 4:
  print(x/y)
elif x == 5:
  break
else:
  pass


  
