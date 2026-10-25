# Cyberattack_python-game
“A cybersecurity-themed Python text adventure built to practice dictionaries, loops, conditionals, and user input.”
# CyberAttack!

A cybersecurity-themed Python text adventure created for IT 140: Introduction to Scripting.

## Game Objective

Explore eight rooms and collect all six security tools before confronting the Ransomware Phantom in the Core Server Room. Entering that room without every tool ends the game in a loss.

## Security Tools

* Firewall Shield
* Packet Scanner
* Encryption Key
* Access Token
* Backup Drive
* Antivirus Tool

## How to Run

Install Python 3, download `text_based_game.py`, and run this command from the folder containing the file:

```bash
python text_based_game.py
```

## How to Play

You begin in the Security Operations Center.

Move between rooms using:

```text
go north
go south
go east
go west
```

Collect the tool in your current room using its name:

```text
get Firewall Shield
```

The game displays your current room, inventory, available exits, and any tool in the room. Commands are case-insensitive.

## Programming Skills Practiced

- Nested dictionaries for room connections and items
- Lists for inventory management
- Functions for instructions, player status, and game logic
- Loops and conditional branching
- String processing and user input validation
- Win and loss conditions

## Future Improvements

- Add help and exit commands
- Include additional cybersecurity challenges

## Acknowledgment

Created for IT 140: Introduction to Scripting.
OpenAI ChatGPT assisted with drafting and testing the code,
as acknowledged in the source file.

* ## Gameplay Screenshot

![CyberAttack gameplay](python%20text%20game.jpg)
