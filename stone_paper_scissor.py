#win = [(stone over scissor), (scissor over paper), (paper over stone)]
# Draw = [A==B] 

import random

while True:
    win = [(3,1),(1,2), (2,3)]
    cpu = random.randint(1,3)

    print(" Pick respective int scissor=1 paper=2 rock=3 Enter Below")
    Player = int(input())

    if (Player,cpu) in win:
        print("WIN")
    elif (Player==cpu):
        print("DRAW")
    else:
        print("LOOS")