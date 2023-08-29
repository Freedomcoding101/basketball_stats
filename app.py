import copy
from constants import PLAYERS, TEAMS

# def balance_teams():

# Read the existing player data from the PLAYERS constants provided in constants.py
def info_clean():
    players_copy = copy.deepcopy(PLAYERS)
    cleaned_data=[]
    cleaned_heights = []
    cleaned_heights = [int(item['height'].split()[0]) for item in players_copy]

    cleaned_experience = []
    cleaned_experience = [True if item['experience'].lower() == "yes" else False for item in players_copy]

    return cleaned_heights, cleaned_experience

cleaned_heights, cleaned_experience = info_clean()

print(cleaned_heights)
print(cleaned_experience)


    