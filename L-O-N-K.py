from player import Player
import world


def play():
    player = Player()
    action_input = get_player_command()
    user_name = input("What is your name? ")

    print("Hello, " + user_name)
    print("You find yourself lying in a small meadow.\n")
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            player.move_north()
        elif action_input in ['s', 'S']:
            player.move_south()
        elif action_input in ['e', 'E']:
            player.move_east()
        elif action_input in ['w', 'W']:
            player.move_west()
        elif action_input in ['i', 'I']:
            player.print_inventory()
        else:
            print("Invalid action!")

def get_player_command():
    return input('>> ')

play()