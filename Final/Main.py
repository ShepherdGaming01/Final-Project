#Resident Evil Text Based Campaign
#by @ShepherdGaming

import Player_Character
import Enemy_Characters
import random
import Read_In
import Room

# print(f"Story.__name__: {__name__}")

def Beginning():
    intro = Read_In.read_in()

def Menu(Current_Room):
    game_over = False
    while game_over == False:
        wrong_input = True
        while wrong_input == True:
        
            print(f"{Current_Room.name}")
            print(f"A: Examine ({Current_Room.name})\n" + \
                f"B: Loot Items: ({Current_Room.item})\n" + \
                f"C: Fight Enemy: ({Current_Room.enemy})\n" + \
                f"D: Move from Room: {Current_Room.exit}\n" + \
                f"Q: Quit the Game")
            User_input = input(f"\nChoice an option:\n").lower().strip()

            if User_input in "abcdq":
                wrong_input = False

            if  User_input == "a": #discription
                print(f"\n{Current_Room}")
            
            elif User_input == "b": #items
                pass
            elif User_input == "c": #fight
                pass
                #If player dies set game_over to True
            elif User_input == "d": #exit
                pass
            elif User_input == "q": #quit
                exit()
            else:
                print(f"\nInvalid Input {User_input}, please try again!\n")

def Character_Creation():
    
    #Players Name
    name = input("What was your name again?:")
    
    #player picks job with verification
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
        Character_Creation()

        #player roll for health with verification
    player_health = int(input("Roll a D20 for Health:"))
    if player_health >= 21:
        print("Invalid roll, please try again.")
        Character_Creation()
    else:
        pass
         #player roll for attack with verification
    player_attack = int(input("Roll a D6 for Attack:"))
    if player_attack >= 7:
        print("Invalid roll, please try again.")
        Character_Creation()
    else:
        pass

        #player roll for defense with verification
    player_defense = int(input("Roll a D6 for Defense:"))
    if player_defense >= 7:
        print("Invalid roll, please try again.")
        Character_Creation()
    else:
        pass

        #player roll for dodge with verification
    player_dodge = int(input("roll a D4 for Dodge:"))
    if player_dodge >= 5:
        print("Invalid roll, please try again.")
        Character_Creation()
    else:
        pass

        #Doctor skill modifiers
    if class_pick == "doctor":
        player_health = player_health + 4
        player_attack = player_attack + 2
        player_defense = player_defense + 2
        player_dodge = player_dodge + 2
    else:
        pass

        #Soldier skill modifiers
    if class_pick == "soldier":
        player_health = player_health + 2
        player_attack = player_attack + 4
        player_defense = player_defense + 3
        player_dodge = player_dodge + 2
    else:
        pass

        #Accountant skill modifiers
    if class_pick == "accountant":
        player_health = player_health + 2
        player_attack = player_attack + 2
        player_defense = player_defense + 2
        player_dodge = player_dodge + 2
    else:
        pass

        #Police Officer skill modifiers
    if class_pick == "police officer":
        player_health = player_health + 2
        player_attack = player_attack + 3
        player_defense = player_defense + 3
        player_dodge = player_dodge + 2
    else:
        pass

        #Gun Runner skill modifiers
    if class_pick == "gun runner":
        player_health = player_health + 1
        player_attack = player_attack + 1
        player_defense = player_defense + 1
        player_dodge = player_dodge + 5
    else:
        pass
    player = Player_Character.player_character(name, class_pick, player_health, player_attack, player_defense, player_dodge, 1, 0, 100 )
    print(f"\n \nPlayer: {player}")

def Fight(player, enemy): 
    enemy = Enemy_Characters.Enemy("Zombie","Undead", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 1, 0, 10)
    print(f"Enemy: {enemy}")

    while enemy.health > 0 and player.health > 0:
        Player_attacking_result = player.Player_attacking(enemy)
        print(f"{player.name} attacks {enemy.name} for {Player_attacking_result} damage!")
        if enemy.health <= 0:
            exp_gained = enemy.level * 10
            player.experience += exp_gained
            player.gold += exp_gained
            print(f"{player.name} has defeated {enemy.name}, you have gained {exp_gained} experience!")
        else:
            enemy_attacking_result = enemy.Enemy_attacking(player)
            print(f"{enemy.name} attacks {player.name} for {enemy_attacking_result} damage!")

        #player death
    else:
        pass
        print(f"{player.name} or {enemy.name} has died.")
        print(f"player: {player}")
        print(f"enemy: {enemy}")



def main():
    Current_Room = Room.room("Room 16", "You are currently in your room, they place is tossed and the dresser is in front of the door.", None, None, None)
    print(f"Welcome to Resident Evil Raccoon City")
    start = input("Start the Game? (yes/no)").lower().strip()
    print(start)
    if start == "yes":
        #Beginning()
        Character_Creation()
        Menu(Current_Room)
    else:
        quit()








if __name__ == "__main__":
    main()

