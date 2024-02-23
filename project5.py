import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the treasure at the end of the forest.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def make_choice(choices):
    print("Choose an option:")
    for i, option in enumerate(choices, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You start walking through the forest.")
    time.sleep(1)
    print("You come across a fork in the path.")

    choices = ["Take the left path.", "Take the right path."]
    choice = make_choice(choices)

    if choice == 1:
        print("You chose the left path.")
        time.sleep(1)
        print("You encounter a friendly creature.")
        time.sleep(1)
        print("The creature gives you a map to the treasure!")
        return True
    else:
        print("You chose the right path.")
        time.sleep(1)
        print("You encounter a swarm of angry bees!")
        time.sleep(1)
        print("You run away and find a hidden shortcut.")
        return False

def treasure_hunt():
    print("You continue your journey with the map.")
    time.sleep(1)
    print("After a while, you arrive at the treasure location.")
    time.sleep(1)
    print("Congratulations! You found the treasure and won the game.")

def main():
    intro()
    if forest_path():
        treasure_hunt()

if __name__ == "__main__":
    main()
