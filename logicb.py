import random

def gen_passnow(pass_lengthnow):
    elementsi = "+-/*!&$#?=@<>123456789"
    passwordnow = ""
    for i in range(pass_lengthnow):
        passwordnow += random.choice(elementsi)
    return passwordnow