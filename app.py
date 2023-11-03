import copy
from constants import PLAYERS
import random
# The Program Imports Modules Used

if __name__ == "__main__":
    # Extract and Clean Data from Players List
    def info_clean():
        players_copy = copy.deepcopy(PLAYERS)

        cleaned_heights = []
        cleaned_heights = [int(item['height'].split()[0]) for item in players_copy]

        cleaned_experience = []
        cleaned_experience = [bool(True) if item['experience'].lower() == "yes" else bool(False) for item in players_copy]

        guardians = [item['guardians'].split("and") for item in players_copy]
        names = [item['name'] for item in players_copy]

        return cleaned_heights, cleaned_experience, guardians, names

    cleaned_heights, cleaned_experience, guardians, names = info_clean()

    # Create List of Player Dictionaries

    players = []
    for i in range(len(cleaned_heights)):
        player = {
            'name': names[i],
            'guardian': guardians[i],
            'experience': cleaned_experience[i],
            'height': cleaned_heights[i]
        }
        players.append(player)

    # Function Designed to make 3 Balanced Teams

    def balance_team():
        experienced = []
        inexperienced = []
        Panthers = []
        Bandits = []
        Warriors = []
        experienced = [player['name'] for player in players if bool(player['experience'])]
        inexperienced = [player['name'] for player in players if not bool(player['experience'])]
        random.shuffle(experienced)
        random.shuffle(inexperienced)

        Panthers = experienced[:3] + inexperienced[:3]
        Bandits = experienced[3:6] + inexperienced[3:6]
        Warriors = experienced[6:9] + inexperienced[6:9]

        return Panthers, Bandits, Warriors
    Panthers, Bandits, Warriors = balance_team()

    def print_teams():
        print("\nA) Panthers\n")
        print("B) Bandits\n")
        print("C) Warriors\n")

    def menu_option():
        print("Welcome to the Basketball Stats Tool:\n")
        print("A) Display Team Stats\n")
        print("B) Quit\n")

    def print_parents(team_stats):
        for player in team_stats:
            name = player["name"]
            guardian = (', ').join(player["guardian"])
            print(f"Player: {name} - Guardian: {guardian}\n")

    def experience_level(team_stats):
        experienced = 0
        inexperienced = 0
        for player in team_stats:
            if player["experience"] == True:
                experienced += 1
            elif player["experience"] == False:
                inexperienced += 1
        return experienced, inexperienced

    def average_height(team_stats):
        total_height = sum(player['height'] for player in team_stats)
        average = total_height / len(team_stats)
        return '{:.2f}'.format(average)

    bandit_stats = []
    warrior_stats = []
    panther_stats = []
    
    for player_name in Bandits:
        for player_data in players:
            if player_data["name"] == player_name:
                result = {
                    "name": player_name,
                    "height": player_data["height"],
                    "guardian": player_data["guardian"],
                    "experience": player_data["experience"],
                }
                bandit_stats.append(result)

    for player_name in Warriors:
        for player_data in players:
            if player_data["name"] == player_name:
                result = {
                    "name": player_name,
                    "height": player_data["height"],
                    "guardian": player_data["guardian"],
                    "experience": player_data["experience"],
                }
                warrior_stats.append(result)

    for player_name in Panthers:
        for player_data in players:
            if player_data["name"] == player_name:
                result = {
                    "name": player_name,
                    "height": player_data["height"],
                    "guardian": player_data["guardian"],
                    "experience": player_data["experience"],
                }
                panther_stats.append(result)

    panther_heights = average_height(panther_stats)
    warrior_heights = average_height(warrior_stats)
    bandit_heights = average_height(bandit_stats)
    experienced_panthers, inexperienced_panthers = experience_level(panther_stats)
    experienced_bandits, inexperienced_bandits = experience_level(bandit_stats)
    experienced_warriors, inexperienced_warriors = experience_level(warrior_stats)

    print("Welcome to the Basketball Stats Tool\n")

    print("----------MENU-----------\n")

    # Display Menu for user to input choices

    while True:
        menu_option()

    # Select a team for stats

        choice_1 = input("Enter an option: \n")

        if choice_1 == "A":
            print_teams()
            choice_2 = input("Enter an option from above!: ")

        elif choice_1 == "B":
            exit()

        else:
            print("\nThat is not a valid answer please try again!\n")

        if choice_2 == ("A"):
            print("-------------------------------------\n")
            print("Panthers Stats\n")
            print("-------------------------------------\n")
            print(f"There are {len(Panthers)} players on the team!\n")
            print(f"The players are: {(', '.join(Panthers))}\n")
            print_parents(panther_stats)
            experience_level(panther_stats)
            print(f"There are {experienced_panthers} experienced players, and {inexperienced_panthers} inexperienced players.\n")
            print(f"The average height is {panther_heights} inches!\n")
            continue

        elif choice_2 == ("B"):
            print("-------------------------------------\n")
            print("Bandits Stats\n")
            print("-------------------------------------\n")
            print(f"There are {len(Bandits)} players on the team!\n")
            print(f"The players are: {(', '.join(Bandits))}")
            print_parents(bandit_stats)
            print(f"There are {experienced_bandits} experienced players, and {inexperienced_bandits} inexperienced players.\n")
            print(f"The average height is {bandit_heights} inches!\n")
            continue

        elif choice_2 == ("C"):
            print("-------------------------------------\n")
            print("Warriors Stats\n")
            print("-------------------------------------\n")
            print(f"There are {len(Warriors)} players on the team!\n")
            print(f"The players are: {(', '.join(Warriors))}")
            print_parents(warrior_stats)
            print(f"There are {experienced_warriors} experienced players, and {inexperienced_warriors} inexperienced players.\n")
            print(f"The average height is {warrior_heights} inches!\n")
            continue

        else:
            print("\nThat is not a valid option please pick from A B C: ")
            print_teams()
            continue

    # Display thank you message once user exits

    print("\nThank you for using our stat generator! If you ever require our service again dont hesitate to use our application!")
