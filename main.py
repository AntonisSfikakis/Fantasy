from euroleague_api.shot_data import ShotData

# Welcome message
def WelcomeMessage(): 
    print("Hallo! Welcome to euroluege Fantasy winner!")
    print("Select one of 2\n A)Best lineup with my point\n B)I choose some players")

# Points message 
def PointsMessage(points: int):
    print("You currently have: ",points," left")


WelcomeMessage()
choice = input()
print("How many available points do you have?")
points = input()


season = 2025 
game_code = 1
competition_code = "E"

shotdata = ShotData(competition_code)
df = shotdata.get_game_shot_data(season, game_code)
print(df)


