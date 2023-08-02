#a, b, c = map(int, input("enter 3 numbers: ").split())
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
option_1 = a + b * c
option_2 = a * (b+c)
option_3 = a * b * c
option_4 = (a+b) * c

print(max(option_1, option_2, option_3, option_4))
