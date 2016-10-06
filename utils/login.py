import hashlib

def login(usernameGiven,passwordGiven): #returns 0 if user does not exist, 1 if wrong password, 2 if correct password
    csv = open("data/users.csv","r+")
    users = csv.read().split("\n")
    del users[len(users)-1]
    print users
    usersDict = {}

    userExists = False
    
    for combo in users:
        username = combo.split(",")[0]
        password = combo.split(",")[1]
        usersDict[username] = password

        if username == usernameGiven:
            userExists = True

    if not userExists:
        return 0
            
    hashObj = hashlib.sha1()
    hashObj.update(passwordGiven)

    if hashObj.hexdigest() == usersDict[usernameGiven]:
        return 2
    else:
        return 1
