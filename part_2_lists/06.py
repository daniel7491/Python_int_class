numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16]
num = 0
num = numbers[-1]
numbers.pop(-1)
print(f"removed in the last position: ",numbers)
num += numbers[0]
numbers.pop(0)
print(f"removed in the 0 position: ",numbers)
num += numbers[12]
numbers.pop(12)
print(f"removed in the 12 position: ",numbers)
num += numbers[7]
numbers.pop(7)
print(f"removed in the 7 position: ",numbers)

print(f"the sum is: ",num )

