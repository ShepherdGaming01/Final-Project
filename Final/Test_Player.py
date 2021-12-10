import Player_Character

#type python3 -m pytest

def test_Player_init():
    #create player
    pc = Player_Character.player_character()
    #print player
    print(f"{pc}")

def test_Player_attacking():
    #create player
    pc = Player_Character.player_character()
    #print player
    print(f"pc.Player_attacking(): {pc.Player_attacking(None)}")
