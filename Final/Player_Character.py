#Represents the player

# print(f"player_character.__name__: {__name__}")
import random
import Enemy_Characters

class player_character:
    def __init__(self, new_name="Empty Value", new_class="class", new_health=10, new_attack=10, new_defense=10, new_dodge=10, new_level=1, new_experience=0, new_gold = 0):
        self.name = new_name
        self.classes = new_class
        self.health = new_health
        self.attack = new_attack
        self.defense = new_defense
        self.dodge = new_dodge

        self.level = new_level
        self.experience = new_experience

        self.gold = new_gold
    
    def __str__(self):
        character_sheet = f"Name: {self.name}\n" + \
            f"Class: {self.classes}\n" + \
            f"Level: {self.level}\n" + \
            f"Experence: {self.experience}\n" + \
            f"Gold: {self.gold}\n" + \
            f"\n" + \
            f"Health: {self.health}\n" + \
            f"Attack: {self.attack}\n" + \
            f"Defense: {self.defense}\n" + \
            f"Dodge: {self.dodge}\n"
        return character_sheet

    #Player attacks Enemy and updates Enemy health
    def Player_attacking(self, enemy):
        result = 0
        if random.randint(1,100) >= enemy.dodge:
            result = self.attack + random.randint(0,5) - enemy.defense
            if result < 0:
                result = 0
                print(f"{self.name} attack missed")
            else:
                enemy.health -= result
                if enemy.health < 0:
                    enemy.health = 0

        return result
def main():
    pass

if __name__ == "__main__":
    main()