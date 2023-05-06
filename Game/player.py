import json

class Player:
    def __init__(self):
        self.player_id = ''
        self.level = 1
        self.current_xp = 0
        self.needed_xp = self.level ** 2 + 50
        self.base_hp = self.level*200
        self.base_resource = self.level*20
        self.equipment = {}
        self.abilities = {}
        self.inventory = {}
        self.inventory['materials'] = {}
        self.inventory['weapons'] = {}
        self.inventory['materials']['xallarock'] = 0
        self.inventory['materials']['gold_ore'] = 0

    def level_up(self):
        overflow_xp = self.current_xp - self.needed_xp
        if overflow_xp >= 0:
            self.level += 1
            self.current_xp = overflow_xp
            self.needed_xp = self.level ** 2 + 50
            print(f"Congratulations, you have leveled up to level {self.level}!")
        else:
            print("You do not have enough XP to level up yet.")

    def import_player(self, id):
        self.player_id = f'Game/Saves/{id}.json'
        with open(self.player_id, "r") as file:
            player_json = file.read()

        player_data = json.loads(player_json)
        self.__dict__.update(player_data)

    def export_player(self):
        self.player.player_id = input("Export player as:")
        player_json = json.dumps(self.player.__dict__)
        player_id = f'Game/Saves/{self.player_id}.json'
        with open(player_id, "w") as file:
            file.write(player_json)



