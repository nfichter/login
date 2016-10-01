import hashlib

def register(usernameGiven,passwordGiven):
    csv = open("data/users.csv","r+")
    users = csv.read().split("\n")

    for combo in users:
        username = combo.split(",")[0]
        if usernameGiven == username:
            return False
        
    hashObj = hashlib.sha1()
    hashObj.update(passwordGiven)
        
    csv.write(csv.read()+"\n"+usernameGiven+","+hashObj.hexdigest())
    
    return True
