import random

def sleeping(one):
    vibor = "zzzzzzzzzzzzzzzzzzzzzzzz"
    choto = ""
    for i in range(one):
        choto += random.choice(vibor)
    return choto