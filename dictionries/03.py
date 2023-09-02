user = {
    'id':4170,
    'uid':"asjdbasidboasd",
    'password' : "asdasdasd",
    "first name" : "asdasd",
    "last_name" : "asdasd"

}

print(user)

user["secret"] = user.pop("password")
user["surename"] = user.pop("last_name")
print(user)

