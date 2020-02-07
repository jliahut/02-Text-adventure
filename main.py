import sys, os, json
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'zork.json'
item_file = 'items.json'


def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)

# The main function for the game
def main():
    current = 'PIZZ1'  # The starting location
    end_game = ['GAME1']  # Any of the end-game locations

    (game,items) = load_files()

    # Add your code here

# run the main function
if __name__ == '__main__':
	main()
