
from constants import PLAYERS
from constants import TEAMS


player_names = []
player_guardians = []

player_experience = []

PanthersHeight = []
BanditsHeight = []
WarriorsHeight = []

player_height = []

PanthersHeight = []
BanditssHeight = []
WarriorsHeight = []

Panthers = []
Bandits = []
Warriors = []


def balance_teams():

    for player in PLAYERS:
        player_names.append(player['name'])

    while len(player_names) > 0 :

        Panthers.append(player_names.pop())
        Bandits.append(player_names.pop())
        Warriors.append(player_names.pop())
    return clean_data() 



def clean_data():
    for player in PLAYERS:
        player_height.append(int(player['height'].split()[0]))

    while len(player_height) > 0:
        PanthersHeight.append(player_height.pop())
        BanditsHeight.append(player_height.pop())
        WarriorsHeight.append(player_height.pop())

    return start_app()
    #player_experience.append(player['experience'])
    #if player_experience == 'YES':
       # return True
    #else:
        #return False
    
    

def start_app():
    print('BASKETBALL STATS TOOL\n\nHere are your choices:\n\nA) Display Team Stats\nB) Quit')
    answer = input('\n Enter an option: ').lower()
    return which_team(answer)


def which_team(answer):
    if answer == 'a':
        print('A) Panthers\nB) Bandits\nC) Warriors')
        which_team = input('\nEnter and option: ').lower()
        
        if which_team == 'a':
            print(len(Panthers))
            PantherString = ', '.join(Panthers)
            PHeightAvg = sum(PanthersHeight) / len(Panthers)
            print(f'Average Height: {PHeightAvg}')
            print(f"Total players: {len(Panthers)}")
            print(f'\n Players on Team: {PantherString}')

        elif which_team == 'b':
            BHeightAvg = sum(BanditsHeight) / len(Bandits)
            BanditsString = ', '.join(Bandits)
            print(f'Average Height: {BHeightAvg}')
            print(f"Total players: {len(Bandits)}")
            print(f'\n Players on team: {BanditsString}')
            
        elif which_team == 'c':
            WHeightAvg = sum(WarriorsHeight) / len(Warriors)
            WarriorsString = ', '.join(Warriors)
            print(f'Average Height: {WHeightAvg}')
            print(f"Total players: {len(Warriors)}")
            print(f'\n Players on Team: {WarriorsString}')
        else:
            print('Please select a listed option.')
            return which_team(answer)
    else:
        exit()



balance_teams()