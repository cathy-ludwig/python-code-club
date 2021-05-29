# going to 7 wonders of the world
# get eaten by a shark at the great barrier reef
import sys

first_stop = None
first_items = ["nerf gun", "makeup bag", "pick axe", "snorkel"]
first_item = None
second_items = ["fishing pole", "wetsuit", "boots", "cheetos"]
second_item = None


def check_input(choice):
    if choice in ["1","2","3","4"]:
        return choice
    else:
        print("Invalid choice. Pick again.")
        return None 

def check_place(choice):
    if choice in ["a","b"]:
        return choice
    else:
        print("Invalid choice. Pick again.")
        return None 


print("Welcome to the 7 Natural Wonders of the World Adventure Game")

# choose our first stop
while first_stop is None:
    first_stop = check_place(input("Where would you like to go first? (a) Great Barrier Reef or (b) Mount Everest "))
    

# choose your items to bring
print("You can bring two things.")
while first_item is None:
    print("")
    print("Pick one of these first options: ")
    first_choice = check_input(input("(1) nerf gun, (2) makeup bag, (3) pick axe, (4) snorkel "))
    if first_choice:
        first_item = first_items[int(first_choice) - 1]

while second_item is None:
    print("")
    print("Pick one of these second options: ")
    second_choice = check_input(input("(1) fishing pole, (2) wetsuit, (3) boots, (4) cheetos "))
    if second_choice:
        second_item = second_items[int(second_choice) - 1]


print("As a reminder, you chose to bring: " + first_item +  " and " + second_item)
print("")

def great_reef():
    print("We're outside of Australia")
    print("")
    # fishing pole to fish
    activity = input("Do you want to go to the ocean or a mall? ")
    if activity == "ocean":
        if second_item == "fishing pole":
            fish_choice = input("It looks like you brought your fishing pole, would you like to fish? (true, false) ")
            if fish_choice:
                if first_item == "pick axe":
                    print("A shark swam up to get you, but you had your pick axe. You were able to fight it off.")
                elif first_item == "makeup bag":
                    print("Your makeup bag saved you from the shark.")
                else:
                    print("Unfortunately, a shark came along and got you. Game over.")
                    return
        elif first_item == "snorkel" and second_item == "wetsuit":
            print("Awesome. Since you brought your snorkel and wetsuit. You went snorkeling.")



def mount_everest():
    print("We're in Nepal")

# start adventure
if first_stop is "a":
    print("Cool, we're going to the Great Barrier Reef")
    great_reef()
elif first_stop == "b":
    print("Cool, we're going to Mount Everest")
    mount_everest()
else:
    print("Sorry, that's not an option")