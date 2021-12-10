#Resident Evil Text Based Campaign
#by @ShepherdGaming

import Player_Character
import Enemy_Characters
import random
import Read_In

# print(f"Story.__name__: {__name__}")

def main():
    intro = Read_In.read_in()
    name = input("What was your name again?:")
    class_pick = input("What was your job prior? a doctor, a soldier, an accountant, a police officer, or gun runner:").lower().strip()
    if class_pick == "doctor":
        pass
    elif class_pick == "soldier":
        pass
    elif class_pick == "accountant":
        pass
    elif class_pick == "police officer":
        pass
    elif class_pick == "gun runner":
        pass
    else:
        print("Invalid job title, please try again.")
    player_health = int(input("Roll a D20 for Health:"))
    if player_health >= 21:
        print("Invalid roll, please try again.")
        main()
    else:
        pass
    player_attack = int(input("Roll a D6 for Attack:"))
    if player_attack >= 7:
        print("Invalid roll, please try again.")
        main()
    else:
        pass
    player_defense = int(input("Roll a D6 for Defense:"))
    if player_defense >= 7:
        print("Invalid roll, please try again.")
        main()
    else:
        pass
    player_dodge = int(input("roll a D4 for Dodge:"))
    if player_dodge >= 5:
        print("Invalid roll, please try again.")
        main()
    else:
        pass

    if class_pick == "doctor":
        player_health = player_health + 4
        player_attack = player_attack + 2
        player_defense = player_defense + 2
        player_dodge = player_dodge + 2
    else:
        pass

    if class_pick == "soldier":
        player_health = player_health + 2
        player_attack = player_attack + 4
        player_defense = player_defense + 3
        player_dodge = player_dodge + 2
    else:
        pass

    if class_pick == "accountant":
        player_health = player_health + 2
        player_attack = player_attack + 2
        player_defense = player_defense + 2
        player_dodge = player_dodge + 2
    else:
        pass

    if class_pick == "police officer":
        player_health = player_health + 2
        player_attack = player_attack + 3
        player_defense = player_defense + 3
        player_dodge = player_dodge + 2
    else:
        pass

    if class_pick == "gun runner":
        player_health = player_health + 1
        player_attack = player_attack + 1
        player_defense = player_defense + 1
        player_dodge = player_dodge + 5
    else:
        pass

    player = Player_Character.player_character(name, class_pick, player_health, player_attack, player_defense, player_dodge, 1, 0, 100 )
    enemy = Enemy_Characters.Enemy("Zombie","Undead", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 1, 0, 10)
    
    print(f"Player: {player}")
    print(f"Enemy: {enemy}")

    while enemy.health > 0 and player.health > 0:
        Player_attacking_result = player.Player_attacking(enemy)
        print(f"{player.name} attacks {enemy.name} for {Player_attacking_result} damage!")
        if enemy.health <= 0:
            exp_gained = enemy.level * 10
            player.experience += exp_gained
            print(f"{player.name} has defeated {enemy.name}, you have gained {exp_gained} experience!")
        else:
            enemy_attacking_result = enemy.Enemy_attacking(player)
            print(f"{enemy.name} attacks {player.name} for {enemy_attacking_result} damage!")

    #player death
    else:
        pass
        #print(f"{player.name} or {enemy.name} has died.")
        #print(f"player: {player}")
        #print(f"enemy: {enemy}")
















if __name__ == "__main__":
    main()
