pencil = 3
pens = pencil + 2
markers = pens + 7

a, b, c = map(int, input("enter the amount of stuff bought: ").split())

sum_a = pencil * a
sum_b = pens * b
sum_c = markers * c

total_cost = sum_a + sum_b + sum_c

print(f" the total cost was: {total_cost}")