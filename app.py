import copy
from constants import PLAYERS, TEAMS

# def balance_teams():

#  def clean_data():
players_copy = copy.deepcopy(PLAYERS)
heights = [item['height'] for item in players_copy]
for item in heights:
    height_int = (int(item.split()[0]))
    cleaned_height = (f"{height_int} inches")
    print(cleaned_height)

names = [item['name'] for item in players_copy]
guardian = [item['guardians'] for item in players_copy]
experience = [item['experience'] for item in players_copy]



# if __name__ == "__main__":