import combat
from player import Player


def show_player_stats(player):
    print(f'''
Player:{player.player_id}
    Level:{player.level}
    Base HP:{player.base_hp}
    Base Resource:{player.base_resource}
    XP:{player.current_xp}/{player.needed_xp}''')

def select_character():
    id = input("Play as:")
    player = Player()
    player.import_player(id)
    show_player_stats(player)
    return player

def forge():
    i = input("Do you want item?")
    if i == 'y':
        player.inventory['weapons']['sword'] = {
            'damage' : 10
        }

def world_map():
    level = input("Level:")
    if level == '0':
        combat.main(level)
    pass

def merchant():
    pass

def inventory():
    print("INVENTORY:")
    for item in player.inventory:
        print(f'{item}/{player.inventory[item]}')
        

def equipment():
    pass

options = {
    '1': forge,
    '2': world_map,
    '3': merchant,
    '4': inventory,
    '5': equipment
}

if __name__ == '__main__':

    player = select_character()
    while True:
        print(f'''
{player.player_id} is currently at town.
    1. Go to Forge
    2. Go to World Map
    3. Go to Merchant
    4. Access Inventory
    5. Access Equipment''')

        option = input("Where to go (1-5):")

        if option in options:
            options[option]()