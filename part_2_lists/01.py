x = []
y = int(input("enter the list size: "))
i = 0
z = 0
avg = 0
summ = 0
while i < y:

    print("enter numbers:")
    z = int(input("enter a number"))
    x.append(z)
    i += 1

for num in range(0,y):
    summ += x[num]
avg = summ / y
print(f"the avarge of the numbers we input is: {avg}")