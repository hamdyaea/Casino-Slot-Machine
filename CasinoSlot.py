# Developer : Hamdy Abou El Anein

from easygui import *
import random
import sys

bar_tk = "./images/bar.gif"
cherry_tk = "./images/cherry.gif"
seven_tk = "./images/lucky-seven.gif"
slot_machine = "./images/slot.gif"

user_money = 100
slot1 = 1
slot2 = 2
slot3 = 3
B1 = 0
B2 = 0
B3 = 0
B4 = 0
bet= 0

def game():

    global user_score, slot1, slot2, slot3, bet
    bet = bet + 100
    slot1 = random.randint(1,3)
    if slot1 == 1:
        slot1 = bar_tk
    elif slot1 == 2:
        slot1 = cherry_tk
    else:
        slot1 = seven_tk

    slot2 = random.randint(1,3)
    if slot2 == 1:
        slot2 = bar_tk
    elif slot2 == 2:
        slot2 = cherry_tk
    else:
        slot2 = seven_tk
    slot3 = random.randint(1,3)
    if slot3 == 1:
        slot3 = bar_tk
    elif slot3 == 2:
        slot3 = cherry_tk
    else:
        slot3 = seven_tk
def result():
    global user_money
    if slot1 == slot2 == slot3:
        user_money = user_money + 300
    elif slot1 == slot2:
        user_money = user_money + 200
    elif slot1 == slot3:
        user_money = user_money + 200
    elif slot2 == slot3:
        user_money = user_money + 200
    else:
        user_money= user_money*0


def begin():
    result()
    image = slot1,slot2,slot3
    msg = "Do you want to replay ? \n\nYou have win "+str(user_money)+str(" $ ")+str("\n\nYou have spend ")+str(bet)+str(" of your money")
    choices = ["Yes","No"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Yes":
        #print(user_money)
        if user_money < 100:
            user_money == 100
        game()
        begin()
    else:
        sys.exit(0)

def enter():
    msg = "                        Casino Slot Machine\n\n Rules of the game :\n\n1) You Begin with 100$\n\n2) You always have the choice to leave or replay. \n\n  If You leave you can keep the money you have got\n\n3) Everytime you replay, you bet 100$\n\n4) 2 x the same = your money + 200$, 3 x the same = your money +300$\n\n  all different = you loose everything"
    choices = ["Begin and bet the first 100$"]
    reply = buttonbox(msg, image=slot_machine, choices=choices)
    if reply == "Begin and bet the first 100$":
        #print(user_money)
        begin()
    else:
        sys.exit(0)
game()
enter()