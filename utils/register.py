import hashlib

def register(usernameGiven,passwordGiven): #returns True if successfully registered, False if the username exists already
    #imports file
    csv = open("data/users.csv","r+")
    users = csv.read().split("\n")

    #checks if any of the users are the same as the username given
    for combo in users:
        username = combo.split(",")[0]
        if usernameGiven == username:
            return False

    #otherwise, hashes the password and puts it into the file
    hashObj = hashlib.sha1()
    hashObj.update(passwordGiven)
        
    csv.write(csv.read()+usernameGiven+","+hashObj.hexdigest()+"\n")
    
    return True
