#Represents the enemies
import random
# print(f"enemy_characters.__name__: {__name__}")

class Enemy:
    def __init__(self, new_name="Enemy", new_class="class", new_health=10, new_attack=10, new_defense=10, new_dodge=10, new_level=1, new_experience=0, new_gold = 0):
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
        Enemy = f"Name: {self.name}\n" + \
            f"Level: {self.level}\n" + \
            f"\n" + \
            f"Health: {self.health}\n" + \
            f"Attack: {self.attack}\n" + \
            f"Defense: {self.defense}\n" + \
            f"Dodge: {self.dodge}\n"
        return Enemy

    #Enemy attacks Player and changes Player health
    def Enemy_attacking(self, player):
        result = 0
        if random.randint(1,100) >= player.dodge:
            result = self.attack + random.randint(0,5) - player.defense
            if result < 0:
                result = 0
                print(f"{self.name} attack missed")
            else:
                player.health -= result
                if player.health < 0:
                    player.health = 0

        return result

def main():
    pass

if __name__ == "__main__":
    main()