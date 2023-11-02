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
        cleaned_experience = [True if item['experience'].lower() == "yes" else False for item in players_copy]

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

    # print("Welcome to the Basketball Stats Tool\n")

    # print("----------MENU-----------\n")

    # # Display Menu for user to input choices

    # while True:
    #     print("Here are your choices:\n")
    #     print("A) Display Team Stats\n")
    #     print("B) Quit\n")

    # # Select a team for stats

    #     choice_1 = input("Enter an option: \n")

    #     if choice_1 == "A":
    #         print_teams()

    #         choice_2 = input("Enter an option from above!: ")

    # # Displays stats and option to continue
    # # Program Loops until broken

    #         if choice_2 == "A" or choice_2 == "B" or choice_2 == "C":
    #             break

    #         else:
    #             print("\nThat is not a valid option please pick from A B C: ")
    #             print_teams()
    #             choice_2 = input("Enter an option from above!: ")
    #             break

    #     elif choice_1 == "B":
    #         exit()

    #     else:
    #         print("\nThat is not a valid answer please try again!\n")

    # while True:
    #     if choice_2 == ("A"):
    #         print("-------------------------------------\n")
    #         print("Panthers Stats\n")
    #         print("-------------------------------------\n")
    #         print(f"There are {len(Panthers)} players on the team!\n")
    #         print(f"The players are: {(', '.join(Panthers))}")
    #         choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")

    #     elif choice_2 == ("B"):
    #         print("-------------------------------------\n")
    #         print("Bandits Stats\n")
    #         print("-------------------------------------\n")
    #         print(f"There are {len(Bandits)} players on the team!\n")
    #         print(f"The players are: {(', '.join(Bandits))}")
    #         choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")

    #     elif choice_2 == ("C"):
    #         print("-------------------------------------\n")
    #         print("Warriors Stats\n")
    #         print("-------------------------------------\n")
    #         print(f"There are {len(Warriors)} players on the team!\n")
    #         print(f"The players are: {(', '.join(Warriors))}")
    #         choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")

    #     elif choice_2 == ("E"):
    #         print("\nThank you for using our stats service!")
    #         break

    #     else:
    #         print("\nThat is not a valid option please pick from A B C: ")
    #         print_teams()
    #         choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")

    # # Display thank you message once user exits

    # print("\nThank you for using our stat generator! If you ever require our service again dont hesitate to use our application!")
