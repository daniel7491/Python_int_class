s = input("enter at least 6 char: ")
a = len(s)


temp1 = s[0:3].upper()
temp2 = s[-3:].upper()
temp3 = s[3:-3]
print(f"{temp1}{temp3}{temp2}")