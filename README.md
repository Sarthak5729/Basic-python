# Import required libraries
import datetime

# Define a dictionary to store player data
players = {}

# Define a dictionary to store team data
teams = {}

# Function to register a new player
def register_player(name, email, phone, skills):
    player_id = len(players) + 1  # Generate a new player ID
    # Store the player data in the players dictionary
    players[player_id] = {"name": name, "email": email, "phone": phone, "skills": skills}
    print(f"Player {name} registered successfully with ID {player_id}!")
    # Print out details for confirmation
    print(f"Details - Email: {email}, Phone: {phone}, Skills: {skills}")
    
# Function to create a new team
def create_team(team_name, team_type):
    team_id = len(teams) + 1  # Generate a new team ID
    # Store the team data in the teams dictionary
    teams[team_id] = {"name": team_name, "type": team_type, "players": []}
    print(f"Team {team_name} created successfully with ID {team_id}!")
    # Print out the team type for confirmation
    print(f"Team Type: {team_type}")

# Function to assign a player to a team
def assign_player(team_id, player_id):
    # Check if both team and player IDs are valid
    if team_id in teams and player_id in players:
        # Assign the player to the team
        teams[team_id]["players"].append(player_id)
        print(f"Player {players[player_id]['name']} assigned to team {teams[team_id]['name']} successfully!")
    else:
        print("Invalid team or player ID!")
        
# Function to display player details
def display_players():
    if players:
        print("\nRegistered Players:")
        for player_id, details in players.items():
            print(f"ID: {player_id} | Name: {details['name']} | Skills: {details['skills']}")
    else:
        print("No players registered yet!")

# Function to display team details
def display_teams():
    if teams:
        print("\nRegistered Teams:")
        for team_id, details in teams.items():
            print(f"ID: {team_id} | Name: {details['name']} | Type: {details['type']} | Players: {len(details['players'])}")
    else:
        print("No teams created yet!")
        
# Main program loop
def main():
    while True:
        print("\nWelcome to the Cricket Team Registration System!")
        print("1. Register Player")
        print("2. Create Team")
        print("3. Assign Player to Team")
        print("4. Display Registered Players")
        print("5. Display Registered Teams")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice (1-6): ")

        # Perform action based on choice
        if choice == "1":
            name = input("Enter player name: ")
            email = input("Enter player email: ")
            phone = input("Enter player phone: ")
            skills = input("Enter player skills (e.g. batting, bowling, all-rounder): ")
            register_player(name, email, phone, skills)

        elif choice == "2":
            team_name = input("Enter team name: ")
            team_type = input("Enter team type (e.g. men, women, junior): ")
            create_team(team_name, team_type)

        elif choice == "3":
            if not teams:
                print("No teams available! Create a team first.")
            elif not players:
                print("No players available! Register a player first.")
            else:
                team_id = int(input("Enter team ID: "))
                player_id = int(input("Enter player ID: "))
                assign_player(team_id, player_id)

        elif choice == "4":
            display_players()

        elif choice == "5":
            display_teams()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()


Well as we all know that SOLID play very important role in software development. SOLID is an acronym that stands for five design principles of object-oriented which i have elaborated below with brief Description.


S - Single Responsibility Principle (SRP)

In general, the main function controls the big program flow and is another important task. However, it might be divided into smaller ones, where each performs something particular, such as testing input, registering players, forming teams, and so on.
The functions register_player, create_team, assign_player, display_players and display_teams - each do one thing. Good.

O - Open-Closed Rule (OCP)

The code is difficult to modify. Adding new features implies modification of the existing code. For example, if we need to introduce a new type of team or player, we will want to modify the create_team and register_player functions.
To make this even better, we can use abstract classes or interfaces to explain how teams and players should behave, then create real examples for each type.

L - Liskov Substitution Principle (LSP)

In the code, inheritance and polymorphism do not apply, so it is out of the scope of this principle. However, if we are adding inheritance, it should guarantee that subclasses can replace their base classes.
I - Interface Segregation Principle (ISP)

The code is not using interfaces, thus this rule does not directly apply. But should we refactor the code to use interfaces, we should ensure that clients should not depend upon interfaces they do not use.

D - Dependency Inversion Principle, DIP

The code shows the tight coupling between functions. That is, it is hard to modify any function without impacting other functions. For example, the assign_player function depends on the teams and players dictionaries.
To make this better, we could use dependency injection. This means that functions get the things they need as arguments instead of using global variables.

Here is a brief explanation of each principle and its possible use in the code:

SRP: Break the main function into smaller functions, each for a specific task.
OCP: Employ abstract classes or interfaces to indicate how teams and players shall behave, while creating concrete implementations for each type. LSP: Ensure that whenever inheritance is used, subclasses can be used in place of their base classes. 
ISP: Make interfaces that spell out how teams and players shall behave and ensure that clients shall not depend upon an interface that they will never use. 
DIP: Dependency injection can be used to reduce the connectivity between functions and to make changes easier. The application of these can, in general, make the code modular, flexible, and maintainable.

    
