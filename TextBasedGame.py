# Noah Piasecki
# Professor Rae
# IT-140
# 15 August 2026
# The Bella Game.

# This shows the introduction to the game and gives instructions on how the game is played.
def show_instructions():
    print("Welcome to the Bella Text Adventure Game!")
    print("Your aunt has asked you to watch Bella for the weekend because she is going on vacation with the family.")
    print("Turns out, the dog food brand your aunt feeds Bella has been accidentally contaminated with an experimental growth hormone.")
    print("This caused Bella to grow astronomically!!")
    print("Your goal is to collect all 7 items to save Bella before your aunt comes home.")
    print("Move commands: go South, go North, go East, go West.")
    print("Add to Inventory: get 'item name'")

# This shows the room you are currently in, your inventory, and tells you what item is in the room.
def show_status(current_room, inventory, rooms):
    print(f"You are in the {current_room}.")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    print("_________")

# This is the start of my main function.
def main():

    # The dictionary that links all of my rooms together along with the items.
    rooms = {
        "Entrance": {
            "East": "Library",
            "South": "Living Room"
        },

        "Library": {
            "West": "Entrance",
            "item": "Storage Key"
        },

        "Living Room": {
            "North": "Entrance",
            "South": "Hallway",
            "East": "Kitchen",
            "West": "Storage Closet",
            "item": "Distraction Toys"
        },

        "Storage Closet": {
            "East": "Living Room",
            "item": "Distilled Water"
        },

        "Kitchen": {
            "West": "Living Room",
            "North": "Garage",
            "item": "Dog Treats"
        },

        "Garage": {
            "South": "Kitchen",
            "item": "Mixing Bowl"
        },

        "Hallway": {
            "North": "Living Room",
            "East": "Bedroom",
            "West": "Bathroom",
            "item": "Garage Key"
        },

        "Bathroom": {
            "East": "Hallway",
            "item": "Fish Oil Capsules"
        },

        "Bedroom": {
            "West": "Hallway",
            "item": "Bella"
        }
    }

    # This sets the player's starting room to the Entrance, inventory, and the number of items needed to beat the game.
    current_room = "Entrance"
    inventory = []
    required_items = 7

    show_instructions()

    while True:

        show_status(current_room, inventory, rooms)

        # This checks if you have all 7 items needed to win the game. If you enter the Bedroom without having all 7 items, you lose the game.
        if current_room == "Bedroom":
            if len(inventory) == required_items:
                print("You collected all the needed items to help Bella!")
                print("You mixed the Dog Treats, Fish Oil Capsules, and some Distilled Water together.")
                print("You threw the combined treat at Bella and she caught it.")
                print("After she eats the treats, she returns back to normal, and you hear your alarm ring.")
                print("Buzz!! Buzz!! Buzz!!")
                print("Turns out, this was all just a bad dream.")
                print("Thank you for taking the time to play the game! I hope you enjoyed it!")
            else:
                print("Bella caught you before you collected all the needed items!")
                print("GAME OVER!")
                print("Thank you for taking the time to play the game!")

            break

        command = input("Enter your move: ").strip()

        # This handles the movement commands.
        if command.lower().startswith("go "):
            direction = command[3:].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # This handles item commands.
        elif command.lower().startswith("get "):
            requested_item = command[4:].strip()

            # This checks if the item is in the room currently or not.
            if (
                "item" in rooms[current_room]
                and requested_item.lower() == rooms[current_room]["item"].lower()
            ):
                item = rooms[current_room]["item"]
                inventory.append(item)
                print(f"{item} retrieved!")

                # This gets rid of the item from the room after you type "get X item".
                del rooms[current_room]["item"]

            else:
                print(f"You cannot get {requested_item}!")

        else:
            print("Input Invalid!")


main()