import random
import string
import qrcode
import time
    
def rand(u):

    return int(random.random() * u)

def passgenV1(l=9):
    character = (
        list(string.ascii_lowercase) + 
        list(string.ascii_uppercase) + 
        [str(i) for i in range(10)] + 
        ["*","$","#","@","&"]
    )

    password = ""
    for i in range(l):

        password += character[rand(len(character))]

    return password

def passgenV2(l = 10):

    character = [list(string.ascii_lowercase),
                list(string.ascii_uppercase),
                [str(i) for i in range(10)],
                ["*","$","#","@","&"]
    ]
    

    password = ""

    for i in range(l):
        r1 = rand(4) #2
        r2 = rand(len(character[r1]))
        password += character[r1][r2] #2 5


    return password


n = 0
while n< 100:
    image = qrcode.make(passgenV2())
    image.save("PASSWORD.jpg")
    time.sleep(3)
    n += 1




















