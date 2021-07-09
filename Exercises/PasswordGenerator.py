import random


def generate_password():
    uppercase_letters=["A","B","C","D","E","F","G","H",
    "I","J","K","L","N","M","O","P","Q","R","S","T","U",
    "V","W","X","Y","Z"]
    lowercase_letters=["a","b","c","d","e","f","g","h",
    "i","j","k","l","n","m","o","p","q","r","s","t","u",
    "v","w","x","y","z"]
    symbols=["!","#","$","%","&","/"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    password=[]
    characteres= uppercase_letters + lowercase_letters + symbols + numbers
    

    for j in range(15):
        password.append(random.choice(characteres))
    
    password=''.join(password)

    return password


def run():
    password= generate_password()
    print(password)


if __name__ == '__main__':
    run()