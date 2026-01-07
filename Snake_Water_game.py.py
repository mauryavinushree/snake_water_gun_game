import random
''' Snake = 1
    Water = 0
    Gun = -1
'''

computer = random.choice([1, 0, -1])

'''
      Select one number:
      Snake = 1
      Water = -1
      Gun = 0
'''

youstr = (input("Enter your choice: "))
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "Snake", -1: "Water", 0: "Gun"}

you = yourDict[youstr]

print(f'You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}')



if (computer==you):
    print("You Draw!")
else:
    if (computer== -1 and you==1 ):
        print("You Win!")

    elif (computer==-1 and you==0):
        print("You Lose.")

    elif (computer==1 and you==-1):
        print("You lose!")

    elif (computer==1 and you== 0):
        print("You Win!")

    elif (computer==0 and you==-1):
        print("You Win!")

    elif (computer==0 and you==1):
        print("You Lose!")

    else:
        print("Something went Wrong!")




