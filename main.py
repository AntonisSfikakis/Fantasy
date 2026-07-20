def WelcomeMessage(): 
    print("Hallo! Welcome to euroluege Fantasy winner!")
    print("Select one of 2\n A)Best lineup with my point\n B)I choose some players\n")

# read points
def PointsMessage(points):
    print("You currently have: ",points," left")


WelcomeMessage()
choice = input()
print("How many available points do you have?")
points = input()
