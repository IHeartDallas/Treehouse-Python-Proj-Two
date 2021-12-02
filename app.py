import constants
selected_teamS = constants.TEAMS
potential_players = constants.PLAYERS

def clean_height_data(player_roster):
    for player in player_roster:
        player['height'] = player['height'].split()
        for item in player['height']:
            if item.isdigit():
                player['height'] = int(item)
    return player_roster

def clean_guardian_data(player_roster):
    for player in player_roster:
        player.update({"guardians": player["guardians"].split(" and ")})
    return player_roster


def identify_inexp_players(player_roster):
    inexp_player_roster = []
    for player in player_roster:
        if player['experience'] == 'NO':
            inexp_player_roster.append(player)
    return inexp_player_roster

def identify_exp_players(player_roster):
    exp_player_roster = []
    for player in player_roster:
        if player['experience'] == 'YES':
            exp_player_roster.append(player)
    return exp_player_roster

def determine_team_size(player_roster):
    num_of_players = 0
    while num_of_players < len(player_roster):
        for player in player_roster:
            player['team'] = selected_teamS[num_of_players % 3]
            num_of_players += 1

def assign_players(player_roster):
    for player in player_roster:
        if player['team'] == 'Panthers':
            panthers.append(player)
        elif player['team'] == 'Bandits':
            bandits.append(player)
        elif player['team'] == 'Warriors':
            warriors.append(player)


def menu_options():
    while True:
        print('''
BASKETBALL TEAM STATS TOOL\n
---- MENU ----\n
Here are your choices:
  1) Display Team Stats
  2) Quit
        ''')
        try:
            choice = int(input("Enter an option >  "))
        except ValueError:
            input("Enter a valid number. Press Enter to continue.")
        else:
            if choice == 1:
                choose_a_team()
            elif choice == 2:
                print("App Ended, Goodbye \n")
                exit()
            else:
                print("Enter 1 or 2\n")
          
def choose_a_team():
    while True:
        print("\nChoose a team:\n  1) Panthers\n  2) Bandits\n  3) Warriors")
        try:
            choice = int(input("\nEnter an option > "))
        except ValueError:
            input("Please enter a number. Press Enter to continue.\n")
        else:
            if choice == 1:
                team_info(panthers)
                break
            elif choice == 2:
                team_info(bandits)
                break
            elif choice == 3:
                team_info(warriors)
                break
            else:
                input("Please enter 1, 2, or 3.\nEnter to continue\n")


def team_info(selected_team):
   
    num_players = len(selected_team)

    final_roster = []
    for player in selected_team:
        final_roster.append(player['name'])
    player_name = ", ".join(final_roster)
   
    num_advanced_players = 0
    num_novice_players = 0
    for player in selected_team:
        if player['experience'] == 'YES':
            num_advanced_players += 1
        elif player['experience'] == 'NO':
            num_novice_players += 1

    height_average = 0
    for player in selected_team:
        height_average += player['height']
    height_average = round((height_average / len(selected_team)), ndigits=1)

    
    guardian_roster = []
    for player in selected_team:
        guardian_roster.extend(player['guardians'])
    guardian_names = ", ".join(guardian_roster)

    # print the output prepared above
    print("\nTeam: {}:".format(selected_team[0]['team'].capitalize()))
    print('''
    --------------------
    * Total players: {}
    * Players on the team: {}
    * Number of advanced players on the team: {}
    * Number of novice players on the team: {}
    * Height average on the team: {} inches
    * Guardians on the team: {}
    '''.format(num_players, player_name, num_advanced_players, num_novice_players, height_average, guardian_names))

    input("Press Enter to continue ... ")


if __name__ == "__main__":
    clean_guardian_data(potential_players)
    clean_height_data(potential_players)
    advanced = identify_exp_players(potential_players)
    novice = identify_inexp_players(potential_players)

    determine_team_size(advanced)
    determine_team_size(novice)

    panthers = []
    bandits = []
    warriors = []

    assign_players(advanced)
    assign_players(novice)

    menu_options()