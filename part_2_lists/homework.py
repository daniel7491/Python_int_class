users = []
users.append("kevin")
users.append("bob")
users.append("alice")
print(users)
del users[1:2]
print(users)
revers_users = list(reversed(users))
print(revers_users)
users.insert(1,"melody")
print(users)
users = users + ['andy', 'wanda', 'jim']
print(users)
sliced_users= users[2:-2]
print(sliced_users)