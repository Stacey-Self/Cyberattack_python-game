# Name: [Enter Your Full Name]
# Course: IT 140 - Project Two
# Game: CyberAttack!
# AI acknowledgment: OpenAI ChatGPT (2026) assisted with drafting and testing this code.


def show_instructions():
    """Display the game's goal and available commands."""
    print("Welcome to CyberAttack!")
    print("Collect all 6 security tools before confronting the Ransomware Phantom.")
    print("Move commands: go north, go south, go east, go west")
    print("Collect an item: get <item name>")
    print("Example: get Firewall Shield")


def show_status(current_room, inventory, rooms):
    """Show the current room, inventory, available exits, and room item."""
    print("\n------------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    directions = ("north", "south", "east", "west")
    available_exits = [direction for direction in directions
                       if direction in rooms[current_room]]
    print(f"Available exits: {', '.join(available_exits)}")
    print("------------------------------")


def main():
    """Run the game until the player defeats the villain or loses."""
    # These connections and items follow the CyberAttack! game map.
    rooms = {
        "Security Operations Center": {
            "west": "Firewall Station",
            "north": "Core Server Room"
        },
        "Firewall Station": {
            "east": "Security Operations Center",
            "north": "Network Monitoring Room",
            "item": "Firewall Shield"
        },
        "Network Monitoring Room": {
            "south": "Firewall Station",
            "north": "Encryption Lab",
            "item": "Packet Scanner"
        },
        "Encryption Lab": {
            "south": "Network Monitoring Room",
            "east": "Authentication Office",
            "item": "Encryption Key"
        },
        "Authentication Office": {
            "west": "Encryption Lab",
            "east": "Backup Vault",
            "item": "Access Token"
        },
        "Backup Vault": {
            "west": "Authentication Office",
            "south": "Malware Analysis Lab",
            "item": "Backup Drive"
        },
        "Malware Analysis Lab": {
            "north": "Backup Vault",
            "west": "Core Server Room",
            "item": "Antivirus Tool"
        },
        "Core Server Room": {
            "south": "Security Operations Center",
            "east": "Malware Analysis Lab",
            "villain": "Ransomware Phantom"
        }
    }

    current_room = "Security Operations Center"
    inventory = []
    villain_room = "Core Server Room"
    required_items = sum("item" in room for room in rooms.values())

    show_instructions()

    # The game ends only after entering the villain's room.
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip()
        command_parts = command.split(maxsplit=1)

        if not command_parts:
            print("Invalid command. Use 'go <direction>' or 'get <item name>'.")
            continue

        action = command_parts[0].lower()
        target = " ".join(command_parts[1].split()) if len(command_parts) > 1 else ""

        if action == "go":
            direction = target.lower()
            if direction in ("north", "south", "east", "west") and direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You moved to the {current_room}.")

                if current_room == villain_room:
                    if len(inventory) == required_items:
                        print("Congratulations! You collected all 6 tools and defeated the Ransomware Phantom!")
                    else:
                        print("The Ransomware Phantom has taken over the network. GAME OVER!")
                    break
            else:
                print("Invalid direction. You cannot go that way.")

        elif action == "get":
            room_item = rooms[current_room].get("item")
            if not target:
                print("Invalid item command. Use 'get <item name>'.")
            elif room_item is None:
                print("There is no item to collect in this room.")
            elif target.casefold() == room_item.casefold():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"You collected the {room_item}!")
            else:
                print("Invalid item. That item is not in this room.")

        else:
            print("Invalid command. Use 'go <direction>' or 'get <item name>'.")

    print("Thanks for playing the game. Hope you enjoyed it.")


if __name__ == "__main__":
    main()
