import copy
from constants import PLAYERS, TEAMS
import random
#The program imports the copy, PLAYERS, and TEAMS modules, and the random module.

if __name__ == "__main__":
    #The info_clean function is defined, which extracts and cleans data from the PLAYERS list. It creates lists of player heights, experience status, guardians, and names.
    def info_clean():
        players_copy = copy.deepcopy(PLAYERS)

        cleaned_heights = []
        cleaned_heights = [int(item['height'].split()[0]) for item in players_copy]

        cleaned_experience = []
        cleaned_experience = [True if item['experience'].lower() == "yes" else False for item in players_copy]

        guardians = [item['guardians'] for item in players_copy]
            
        names = [item['name'] for item in players_copy]

        return cleaned_heights, cleaned_experience, guardians, names

    cleaned_heights, cleaned_experience, guardians, names = info_clean()

    #A list of player dictionaries is created from the cleaned data and stored in the players list.

    players = []
    for i in range(len(cleaned_heights)):
        player = {
            'name': names[i],
            'guardian': guardians[i],
            'experience': cleaned_experience[i],
            'height': cleaned_heights[i]
        }
        players.append(player)

    #The balance_team function is defined to create three teams: Panthers, Bandits, and Warriors, while ensuring a balanced distribution of experienced and inexperienced players.

    def balance_team():
        
        experienced = []
        inexperienced = []
        Panthers = []
        Bandits = []
        Warriors = []
    
        experienced = [player['name'] for player in players if player['experience'] == True]

        inexperienced = [player['name'] for player in players if player['experience'] == False]
        
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
    
print("Welcome to the Basketball Stats Tool\n")

print("----------MENU-----------\n")

#The program then calls the balance_team function to create the teams, Panthers, Bandits, and Warriors.

balance_team()

#The program displays a menu for the user to choose options. The user can either display team stats or quit.

while True:
    print("Here are your choices:\n")
    print("A) Display Team Stats\n")
    print("B) Quit\n")

    #The user enters their choice, and if they choose to display team stats, they are prompted to select a team (Panthers, Bandits, or Warriors).

    choice_1 = input("Enter an option: \n")

    if choice_1 == "A":
        print_teams()

        choice_2 = input("Enter an option from above!: ")
        
        #Depending on the selected team, the program displays the team's stats, including the number of players on the team and the names of the players. The user is then given the option to see stats for another team or exit.
        #The program continues to loop, allowing the user to see stats for other teams or exit the program.

        if choice_2 == "A" or choice_2 == "B" or choice_2 == "C":
            break
        
        else:
            print("\nThat is not a valid option please pick from A B C: ")
            print_teams()
            choice_2 = input("Enter an option from above!: ")
            break


    elif choice_1 =="B":
        exit()

    else:
        print("\nThat is not a valid answer please try again!\n")

while True:
    if choice_2 == ("A"):
        print("-------------------------------------\n")
        print("Panthers Stats\n")
        print("-------------------------------------\n")
        print(f"There are {len(Panthers)} players on the team!\n")
        print(f"The players are: {(', '.join(Panthers))}")
        choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")
        

    elif choice_2 == ("B"):
        print("-------------------------------------\n")
        print("Bandits Stats\n")
        print("-------------------------------------\n")
        print(f"There are {len(Bandits)} players on the team!\n")
        print(f"The players are: {(', '.join(Bandits))}")
        choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")
        

    elif choice_2 == ("C"):
        print("-------------------------------------\n")
        print("Warriors Stats\n")
        print("-------------------------------------\n")
        print(f"There are {len(Warriors)} players on the team!\n")
        print(f"The players are: {(', '.join(Warriors))}")
        choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")
        

    elif choice_2 == ("E"):
        print("\nThank you for using our stats service!")
        break
        
    else:
        print("\nThat is not a valid option please pick from A B C: ")
        print_teams()
        choice_2 = input("\nIf you would like to see another teams stats please enter their letter here! Otherwise type 'E' to exit: ")

#Once the user chooses to exit, a thank-you message is displayed, and the program terminates.

print("\nThank you for using our stat generator! If you ever require our service again dont hesitate to use our application!")