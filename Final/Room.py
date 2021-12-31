#the rooms
import random
import Enemy_Characters


class room:
    def __init__(self,new_name = "Unnamed", new_description = "Not yet explained", new_item_list=None, new_enemy=None, new_exits=("None",None)):
        self.name = new_name
        self.description = new_description
        self.item = new_item_list
        self.enemy = new_enemy
        self.exit = new_exits

    def __str__(self):
        result = self.name + \
                 f"\n  {self.description}" + \
                 f"\n  Items: {self.item}" + \
                 f"\n  Enemy: {self.enemy}" + \
                 f"\n  Exit: {self.exit}" + \
                 f"\n\n"

        return result


    Room_List = []


    def Room_01():
        #randomly selecting room discription
        description = random.randint(1,7)
        if description == 1:
            description = "The room is very clean, it appears that no one has been staying in this room."
        elif description == 2:
            description = "The room is completely trashed, everything is thrown everywhere."
        elif description == 3:
            description = "This room is pristine. It could easily pass a white glove test. It looks mighty expensive."
        elif description == 4:
            description = "The room is morbid. Blood splatters the walls, and it looks like a bomb went off inside."
        elif description == 5:
            description = "The room makes your jaw drop. It is stunning, white and gold, with regal archways."
        elif description == 6:
            description = "The room is a disappointment. The decor is very drab, your typical rundown hotel room."
        else:
            description = "If cleanliness were godliness, this room would be fit for the gods. Clean and expensive, this room is breathtaking."
        

        #randomly selecting room items
        item = random.randint(1,50)
        if item == (1,15):
            item = None
        elif item == (16):
            item = 1
        elif item == (17,23):
            item = None
        elif item == (24):
            item = 2
        elif item == (25,30):
            item = None
        elif item == (31):
            item = 3
        else:
            item = "Health"


        #randomly selecting room enemy
        enemy = random.randint(0,50)
        if enemy == (0):
            enemy = Enemy_Characters.Enemy("Tyrant","T-Type", 250, 25, 25, 50, 100, 0, 10000)
        elif enemy == (1,4):
            enemy = None
        elif enemy == (5):
            enemy = Enemy_Characters.Enemy("Zombie","T-Type", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 2, 0, 10)
        elif enemy == (6,9):
            enemy = None
        elif enemy == (10):
            enemy = Enemy_Characters.Enemy("Cerberus","T-Type", random.randint(5,10), random.randint(3,5), random.randint(3,5), random.randint(2,5), 3, 0, 20)
        elif enemy == (11,14):
            enemy = None
        elif enemy == (15):
            enemy = Enemy_Characters.Enemy("Zombies","T-Type", random.randint(2,10), random.randint(2,6), random.randint(2,6), random.randint(2,4), 3, 0, 30)
        elif enemy == (16,19):
            enemy = None
        elif enemy == (20):
            enemy = Enemy_Characters.Enemy("Spider","T-Type", random.randint(1,3), random.randint(1,2), random.randint(1,2), random.randint(1,2), 1, 0, 10)
            enemy = None
        elif enemy == (25):
            enemy = Enemy_Characters.Enemy("Cerberus Pack","T-Type", random.randint(10,20), random.randint(6,10), random.randint(6,10), random.randint(4,10), 7, 0, 100)
        elif enemy == (26,29):
            enemy = None
        elif enemy == (30):
            enemy = Enemy_Characters.Enemy("Licker","T-Type", random.randint(15,25), random.randint(10,15), random.randint(10,15), random.randint(12,15), 8, 0, 150)
        elif enemy == (31,34):
            enemy = None
        elif enemy == (35):
            enemy = Enemy_Characters.Enemy("Spiders","T-Type", random.randint(2,6), random.randint(2,6), random.randint(2,6), random.randint(2,4), 2, 0, 10)
        elif enemy == (36,39):
            enemy = None
        elif enemy == (40):
            enemy = Enemy_Characters.Enemy("Lickers","T-Type", random.randint(30,50), random.randint(20,30), random.randint(20,30), random.randint(24,30), 16, 0, 350)
        elif enemy == (41,44):
            enemy = None
        elif enemy == (45):
            enemy = Enemy_Characters.Enemy("Devourer","G-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)
        elif enemy == (46,49):
            enemy = None
        else:
            enemy = Enemy_Characters.Enemy("Nemesis","T-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)


        room_01 = room("Room 01", description, item, enemy, ("None", None))
        room.Room_List.append(room_01)


    def Room_02():
        #randomly selecting room discription
        description = random.randint(1,7)
        if description == 1:
            description = "The room is very clean, it appears that no one has been staying in this room."
        elif description == 2:
            description = "The room is completely trashed, everything is thrown everywhere."
        elif description == 3:
            description = "This room is pristine. It could easily pass a white glove test. It looks mighty expensive."
        elif description == 4:
            description = "The room is morbid. Blood splatters the walls, and it looks like a bomb went off inside."
        elif description == 5:
            description = "The room makes your jaw drop. It is stunning, white and gold, with regal archways."
        elif description == 6:
            description = "The room is a disappointment. The decor is very drab, your typical rundown hotel room."
        else:
            description = "If cleanliness were godliness, this room would be fit for the gods. Clean and expensive, this room is breathtaking."
        

        #randomly selecting room items
        item = random.randint(1,50)
        if item == (1,15):
            item = None
        elif item == (16):
            item = 1
        elif item == (17,23):
            item = None
        elif item == (24):
            item = 2
        elif item == (25,30):
            item = None
        elif item == (31):
            item = 3
        else:
            item = "Health"


        #randomly selecting room enemy
        enemy = random.randint(0,50)
        if enemy == (0):
            enemy = Enemy_Characters.Enemy("Tyrant","T-Type", 250, 25, 25, 50, 100, 0, 10000)
        elif enemy == (1,4):
            enemy = None
        elif enemy == (5):
            enemy = Enemy_Characters.Enemy("Zombie","T-Type", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 2, 0, 10)
        elif enemy == (6,9):
            enemy = None
        elif enemy == (10):
            enemy = Enemy_Characters.Enemy("Cerberus","T-Type", random.randint(5,10), random.randint(3,5), random.randint(3,5), random.randint(2,5), 3, 0, 20)
        elif enemy == (11,14):
            enemy = None
        elif enemy == (15):
            enemy = Enemy_Characters.Enemy("Zombies","T-Type", random.randint(2,10), random.randint(2,6), random.randint(2,6), random.randint(2,4), 3, 0, 30)
        elif enemy == (16,19):
            enemy = None
        elif enemy == (20):
            enemy = Enemy_Characters.Enemy("Spider","T-Type", random.randint(1,3), random.randint(1,2), random.randint(1,2), random.randint(1,2), 1, 0, 10)
            enemy = None
        elif enemy == (25):
            enemy = Enemy_Characters.Enemy("Cerberus Pack","T-Type", random.randint(10,20), random.randint(6,10), random.randint(6,10), random.randint(4,10), 7, 0, 100)
        elif enemy == (26,29):
            enemy = None
        elif enemy == (30):
            enemy = Enemy_Characters.Enemy("Licker","T-Type", random.randint(15,25), random.randint(10,15), random.randint(10,15), random.randint(12,15), 8, 0, 150)
        elif enemy == (31,34):
            enemy = None
        elif enemy == (35):
            enemy = Enemy_Characters.Enemy("Spiders","T-Type", random.randint(2,6), random.randint(2,6), random.randint(2,6), random.randint(2,4), 2, 0, 10)
        elif enemy == (36,39):
            enemy = None
        elif enemy == (40):
            enemy = Enemy_Characters.Enemy("Lickers","T-Type", random.randint(30,50), random.randint(20,30), random.randint(20,30), random.randint(24,30), 16, 0, 350)
        elif enemy == (41,44):
            enemy = None
        elif enemy == (45):
            enemy = Enemy_Characters.Enemy("Devourer","G-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)
        elif enemy == (46,49):
            enemy = None
        else:
            enemy = Enemy_Characters.Enemy("Nemesis","T-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)


        room_02 = room("Room 02", description, item, enemy, ("None", None))
        room.Room_List.append(room_02)


    def Room_03():
        #randomly selecting room discription
        description = random.randint(1,7)
        if description == 1:
            description = "The room is very clean, it appears that no one has been staying in this room."
        elif description == 2:
            description = "The room is completely trashed, everything is thrown everywhere."
        elif description == 3:
            description = "This room is pristine. It could easily pass a white glove test. It looks mighty expensive."
        elif description == 4:
            description = "The room is morbid. Blood splatters the walls, and it looks like a bomb went off inside."
        elif description == 5:
            description = "The room makes your jaw drop. It is stunning, white and gold, with regal archways."
        elif description == 6:
            description = "The room is a disappointment. The decor is very drab, your typical rundown hotel room."
        else:
            description = "If cleanliness were godliness, this room would be fit for the gods. Clean and expensive, this room is breathtaking."
        

        #randomly selecting room items
        item = random.randint(1,50)
        if item == (1,15):
            item = None
        elif item == (16):
            item = 1
        elif item == (17,23):
            item = None
        elif item == (24):
            item = 2
        elif item == (25,30):
            item = None
        elif item == (31):
            item = 3
        else:
            item = "Health"


        #randomly selecting room enemy
        enemy = random.randint(0,50)
        if enemy == (0):
            enemy = Enemy_Characters.Enemy("Tyrant","T-Type", 250, 25, 25, 50, 100, 0, 10000)
        elif enemy == (1,4):
            enemy = None
        elif enemy == (5):
            enemy = Enemy_Characters.Enemy("Zombie","T-Type", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 2, 0, 10)
        elif enemy == (6,9):
            enemy = None
        elif enemy == (10):
            enemy = Enemy_Characters.Enemy("Cerberus","T-Type", random.randint(5,10), random.randint(3,5), random.randint(3,5), random.randint(2,5), 3, 0, 20)
        elif enemy == (11,14):
            enemy = None
        elif enemy == (15):
            enemy = Enemy_Characters.Enemy("Zombies","T-Type", random.randint(2,10), random.randint(2,6), random.randint(2,6), random.randint(2,4), 3, 0, 30)
        elif enemy == (16,19):
            enemy = None
        elif enemy == (20):
            enemy = Enemy_Characters.Enemy("Spider","T-Type", random.randint(1,3), random.randint(1,2), random.randint(1,2), random.randint(1,2), 1, 0, 10)
            enemy = None
        elif enemy == (25):
            enemy = Enemy_Characters.Enemy("Cerberus Pack","T-Type", random.randint(10,20), random.randint(6,10), random.randint(6,10), random.randint(4,10), 7, 0, 100)
        elif enemy == (26,29):
            enemy = None
        elif enemy == (30):
            enemy = Enemy_Characters.Enemy("Licker","T-Type", random.randint(15,25), random.randint(10,15), random.randint(10,15), random.randint(12,15), 8, 0, 150)
        elif enemy == (31,34):
            enemy = None
        elif enemy == (35):
            enemy = Enemy_Characters.Enemy("Spiders","T-Type", random.randint(2,6), random.randint(2,6), random.randint(2,6), random.randint(2,4), 2, 0, 10)
        elif enemy == (36,39):
            enemy = None
        elif enemy == (40):
            enemy = Enemy_Characters.Enemy("Lickers","T-Type", random.randint(30,50), random.randint(20,30), random.randint(20,30), random.randint(24,30), 16, 0, 350)
        elif enemy == (41,44):
            enemy = None
        elif enemy == (45):
            enemy = Enemy_Characters.Enemy("Devourer","G-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)
        elif enemy == (46,49):
            enemy = None
        else:
            enemy = Enemy_Characters.Enemy("Nemesis","T-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)


        room_03 = room("Room 03", description, item, enemy, ("None", None))
        room.Room_List.append(room_03)


    def Room_04():
        #randomly selecting room discription
        description = random.randint(1,7)
        if description == 1:
            description = "The room is very clean, it appears that no one has been staying in this room."
        elif description == 2:
            description = "The room is completely trashed, everything is thrown everywhere."
        elif description == 3:
            description = "This room is pristine. It could easily pass a white glove test. It looks mighty expensive."
        elif description == 4:
            description = "The room is morbid. Blood splatters the walls, and it looks like a bomb went off inside."
        elif description == 5:
            description = "The room makes your jaw drop. It is stunning, white and gold, with regal archways."
        elif description == 6:
            description = "The room is a disappointment. The decor is very drab, your typical rundown hotel room."
        else:
            description = "If cleanliness were godliness, this room would be fit for the gods. Clean and expensive, this room is breathtaking."
        

        #randomly selecting room items
        item = random.randint(1,50)
        if item == (1,15):
            item = None
        elif item == (16):
            item = 1
        elif item == (17,23):
            item = None
        elif item == (24):
            item = 2
        elif item == (25,30):
            item = None
        elif item == (31):
            item = 3
        else:
            item = "Health"


        #randomly selecting room enemy
        enemy = random.randint(0,50)
        if enemy == (0):
            enemy = Enemy_Characters.Enemy("Tyrant","T-Type", 250, 25, 25, 50, 100, 0, 10000)
        elif enemy == (1,4):
            enemy = None
        elif enemy == (5):
            enemy = Enemy_Characters.Enemy("Zombie","T-Type", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 2, 0, 10)
        elif enemy == (6,9):
            enemy = None
        elif enemy == (10):
            enemy = Enemy_Characters.Enemy("Cerberus","T-Type", random.randint(5,10), random.randint(3,5), random.randint(3,5), random.randint(2,5), 3, 0, 20)
        elif enemy == (11,14):
            enemy = None
        elif enemy == (15):
            enemy = Enemy_Characters.Enemy("Zombies","T-Type", random.randint(2,10), random.randint(2,6), random.randint(2,6), random.randint(2,4), 3, 0, 30)
        elif enemy == (16,19):
            enemy = None
        elif enemy == (20):
            enemy = Enemy_Characters.Enemy("Spider","T-Type", random.randint(1,3), random.randint(1,2), random.randint(1,2), random.randint(1,2), 1, 0, 10)
            enemy = None
        elif enemy == (25):
            enemy = Enemy_Characters.Enemy("Cerberus Pack","T-Type", random.randint(10,20), random.randint(6,10), random.randint(6,10), random.randint(4,10), 7, 0, 100)
        elif enemy == (26,29):
            enemy = None
        elif enemy == (30):
            enemy = Enemy_Characters.Enemy("Licker","T-Type", random.randint(15,25), random.randint(10,15), random.randint(10,15), random.randint(12,15), 8, 0, 150)
        elif enemy == (31,34):
            enemy = None
        elif enemy == (35):
            enemy = Enemy_Characters.Enemy("Spiders","T-Type", random.randint(2,6), random.randint(2,6), random.randint(2,6), random.randint(2,4), 2, 0, 10)
        elif enemy == (36,39):
            enemy = None
        elif enemy == (40):
            enemy = Enemy_Characters.Enemy("Lickers","T-Type", random.randint(30,50), random.randint(20,30), random.randint(20,30), random.randint(24,30), 16, 0, 350)
        elif enemy == (41,44):
            enemy = None
        elif enemy == (45):
            enemy = Enemy_Characters.Enemy("Devourer","G-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)
        elif enemy == (46,49):
            enemy = None
        else:
            enemy = Enemy_Characters.Enemy("Nemesis","T-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)


        room_04 = room("Room 04", description, item, enemy, ("None", None))
        room.Room_List.append(room_04)


    def Room_05():
        #randomly selecting room discription
        description = random.randint(1,7)
        if description == 1:
            description = "The room is very clean, it appears that no one has been staying in this room."
        elif description == 2:
            description = "The room is completely trashed, everything is thrown everywhere."
        elif description == 3:
            description = "This room is pristine. It could easily pass a white glove test. It looks mighty expensive."
        elif description == 4:
            description = "The room is morbid. Blood splatters the walls, and it looks like a bomb went off inside."
        elif description == 5:
            description = "The room makes your jaw drop. It is stunning, white and gold, with regal archways."
        elif description == 6:
            description = "The room is a disappointment. The decor is very drab, your typical rundown hotel room."
        else:
            description = "If cleanliness were godliness, this room would be fit for the gods. Clean and expensive, this room is breathtaking."
        

        #randomly selecting room items
        item = random.randint(1,50)
        if item == (1,15):
            item = None
        elif item == (16):
            item = 1
        elif item == (17,23):
            item = None
        elif item == (24):
            item = 2
        elif item == (25,30):
            item = None
        elif item == (31):
            item = 3
        else:
            item = "Health"


        #randomly selecting room enemy
        enemy = random.randint(0,50)
        if enemy == (0):
            enemy = Enemy_Characters.Enemy("Tyrant","T-Type", 250, 25, 25, 50, 100, 0, 10000)
        elif enemy == (1,4):
            enemy = None
        elif enemy == (5):
            enemy = Enemy_Characters.Enemy("Zombie","T-Type", random.randint(1,5), random.randint(1,3), random.randint(1,3), random.randint(1,2), 2, 0, 10)
        elif enemy == (6,9):
            enemy = None
        elif enemy == (10):
            enemy = Enemy_Characters.Enemy("Cerberus","T-Type", random.randint(5,10), random.randint(3,5), random.randint(3,5), random.randint(2,5), 3, 0, 20)
        elif enemy == (11,14):
            enemy = None
        elif enemy == (15):
            enemy = Enemy_Characters.Enemy("Zombies","T-Type", random.randint(2,10), random.randint(2,6), random.randint(2,6), random.randint(2,4), 3, 0, 30)
        elif enemy == (16,19):
            enemy = None
        elif enemy == (20):
            enemy = Enemy_Characters.Enemy("Spider","T-Type", random.randint(1,3), random.randint(1,2), random.randint(1,2), random.randint(1,2), 1, 0, 10)
            enemy = None
        elif enemy == (25):
            enemy = Enemy_Characters.Enemy("Cerberus Pack","T-Type", random.randint(10,20), random.randint(6,10), random.randint(6,10), random.randint(4,10), 7, 0, 100)
        elif enemy == (26,29):
            enemy = None
        elif enemy == (30):
            enemy = Enemy_Characters.Enemy("Licker","T-Type", random.randint(15,25), random.randint(10,15), random.randint(10,15), random.randint(12,15), 8, 0, 150)
        elif enemy == (31,34):
            enemy = None
        elif enemy == (35):
            enemy = Enemy_Characters.Enemy("Spiders","T-Type", random.randint(2,6), random.randint(2,6), random.randint(2,6), random.randint(2,4), 2, 0, 10)
        elif enemy == (36,39):
            enemy = None
        elif enemy == (40):
            enemy = Enemy_Characters.Enemy("Lickers","T-Type", random.randint(30,50), random.randint(20,30), random.randint(20,30), random.randint(24,30), 16, 0, 350)
        elif enemy == (41,44):
            enemy = None
        elif enemy == (45):
            enemy = Enemy_Characters.Enemy("Devourer","G-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)
        elif enemy == (46,49):
            enemy = None
        else:
            enemy = Enemy_Characters.Enemy("Nemesis","T-Type", random.randint(25,100), random.randint(25,50), random.randint(25,50), random.randint(25,50),150, 0, 1000000)


        room_05 = room("Room 05", description, item, enemy.name, ("None", None))
        room.Room_List.append(room_05)


room.Room_01()
room.Room_02()
room.Room_03()
room.Room_04()
room.Room_05()
print(room.Room_List)