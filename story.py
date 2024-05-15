import random
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.tix import Tk
from threading import Thread

import pygame

pygame.init()


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5

    def is_alive(self):
        return self.health > 0

    def print_status(self):
        messagebox.showinfo("Outcome",
                            "\n" + "-" * 20 + "\n" + f"{self.name}: Health = {self.health}, Attacking = {self.attack}, Defense = {self.defense}")


class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attacking = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def print_status(self):
        messagebox.showinfo("Outcome",
                            "\n" + "-" * 20 + "\n" + f"{self.name}: Health = {self.health}, Attacking = {self.attacking}, Defense = {self.defense}")


def battle(player, enemy):
    messagebox.showinfo("Outcome", "A fierce " + enemy.name + " attacks!")
    while player.is_alive() and enemy.is_alive():
        player.print_status()
        enemy.print_status()

        player_damage = max(0, player.attack - enemy.defense)
        enemy.take_damage(player_damage)
        messagebox.showinfo("Outcome", f"You hit the {enemy.name} for {player_damage} damage.")

        if enemy.is_alive():
            enemy_damage = max(0, enemy.attacking - player.defense)
            player.health -= enemy_damage
            messagebox.showinfo("Outcome", f"The {enemy.name} strikes you for {enemy_damage} damage.")
        time.sleep(1)  # Add a small delay for combat actions

    if player.is_alive():
        messagebox.showinfo("Outcome", "\nVictory! You have defeated the " + enemy.name + "!")

    else:
        messagebox.showinfo("Outcome", "\nYou have been slain by the " + enemy.name + "!" + "YOU DIED")


def nickname():
    global name, player
    name = simpledialog.askstring("Player Name", "Please enter your name:")
    player = Player(name)


def introduction():
    messagebox.showinfo("Welcome", f"Welcome to the Haunted Mansion, {name}!\n"
                                   f"You are a distant family member of the Van der Meer family, who built Ravenwood Manor.\n"
                                   f"Generations of Van der Meers resided within its walls, their opulent lifestyle overshadowed by rumors of corruption and scandal.\n"
                                   "Are you prepared to uncover the dark secrets that lie within Ravenwood Manor?\n"
                                   "As the newfound owner, you decide to pay a visit to the mansion.\n"
                                   "The house is dated, creaky, and falling apart. You walk in the front door.\n"
                                   "Do you want to enter the living room, kitchen room, explore the basement, attic, or explore the garden?")


def living_room():
    messagebox.showinfo("Living Room", """
               ________
              |        |
              |  Living|   ___
              |  Room  |  |___|_______
              |________|             |
                                      |
                              ________|________
                             |                  |
                             |    Pitbull       |
                             |    (sleeping)    |
                             |__________________|
    """"As you step into the room, your eyes lock onto Bulbuc, the manor's loyal pitbull, guarding a pile of gleaming gold jewelry.")
    choice = messagebox.askquestion("Decision", "Do you want to steal the jewelry from the pitbull?")
    if choice == "yes":
        rand = random.randint(0, 2)
        if rand == 0:
            messagebox.showinfo("Outcome",
                                "You attempt to steal the jewelry, but it wakes up and rips you to shreds.\n"
                                "You are now dead.")
        elif rand == 1:
            messagebox.showinfo("Outcome",
                                "With careful and silent movements, you manage to acquire the jewelry without disturbing Bulbuc's slumber.\n"
                                "Each delicate maneuver is executed with precision, your heart pounding with every breath, relieved yet wary of the potential consequences lurking in the shadows.")
        else:
            messagebox.showinfo("Outcome", "Bulbuc bites your crotch.")
            Bulbuc = Enemy("Bulbuc", 15, 8, 2)
            battle_thread = Thread(target=battle, args=(player, Bulbuc))
            battle_thread.start()
            battle_thread.join()
    else:
        rand = random.randint(0, 2)
        if rand == 0:
            messagebox.showinfo("Outcome",
                                "Feeling the weight of Bulbuc's presence and the discomfort of the situation, you choose to abandon the idea of stealing the jewelry and quietly exit the living room.\n"
                                "The relief of escaping unscathed mixes with a lingering sense of unease, reminding you of the dangers that lurk within the manor's walls.")
        elif rand == 1:
            messagebox.showinfo("Outcome", "Bulbuc wakes up and bites you by the bottom")
        else:
            messagebox.showinfo("Outcome",
                                "Despite the ominous creaking of the floorboards that rouse Bulbuc from his slumber, luck remains on your side as he fails to detect your presence.\n"
                                "With cautious steps and bated breath, you slip away unnoticed, relieved to have escaped unscathed from the sleeping beast's domain.")


def kitchen():
    messagebox.showinfo("Kitchen", """
               ________
              |         |
              | Kitchen |   
              |         |  
              |________ |  
    """"As you walk in, you see a fresh human corpse that has had its organs harvested recently")
    choice = messagebox.askquestion("Decision", "Do you want to check on the body?")

    if choice == "yes":
        rand = random.randint(0, 2)
        if rand == 0:
            messagebox.showinfo("Outcome", 'nothing out of the ordinary... for a harvested corpse that is')
            messagebox.showinfo("Outcome", "You return to the main hall")
        elif rand == 1:
            messagebox.showinfo("Outcome", 'A bunch of burning coals instead of the harvested organs')
            messagebox.showinfo("Outcome",
                                "As your fingers brush against the scorching coals, a fleeting thought of a barbecue crosses your mind, momentarily distracting you from the looming threat")
        elif rand == 2:
            messagebox.showinfo("Outcome", 'A crumpled, blood-soaked paper with indiscernible writing')
            messagebox.showinfo("Outcome",
                                "You attempt to read the blood-soaked note, but can't make out many words other than 'Your calculations were not correct, Mr. Student")
    elif choice == "no":
        rand = random.randint(0, 2)
        if rand == 0:
            messagebox.showinfo("Outcome", 'You back away in utter shock')
        elif rand == 1:
            messagebox.showinfo("Outcome", 'You look somewhere else in the kitchen room')
        choice = messagebox.askquestion("Decision", "Do you want to further explore the kitchen ?")
        if choice == "yes":
            messagebox.showinfo("Outcome", "You see an oven, a cupboard and a fridge")
    choice = custom_choice_dialog(root)
    if choice == 'Oven':
        handle_oven()
    elif choice == 'Cupboard':
        handle_cupboard()
    elif choice == 'Fridge':
        handle_fridge()
    else:
        messagebox.showinfo("Outcome", "You decided to do nothing.")


def custom_choice_dialog(parent):
    dialog = tk.Toplevel(parent)
    dialog.title("Decision")

    tk.Label(dialog, text="What do you want to open?").pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    choice = tk.StringVar()
    choice.set(None)

    tk.Button(button_frame, text="Oven", command=lambda: set_choice(dialog, choice, "Oven")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Cupboard", command=lambda: set_choice(dialog, choice, "Cupboard")).pack(side="left",
                                                                                                          padx=5)
    tk.Button(button_frame, text="Fridge", command=lambda: set_choice(dialog, choice, "Fridge")).pack(side="left",
                                                                                                      padx=5)

    dialog.wait_window(dialog)
    return choice.get()


def set_choice(dialog, choice, value):
    choice.set(value)
    dialog.destroy()


def handle_oven():
    rand = random.randint(0, 2)
    if rand == 0:
        messagebox.showinfo("Outcome",
                            "Your gaze falls upon a talking pie, its crusty surface contorted into a sneer as it spews venomous words at you. 'You are nothing but a pathetic, worthless imbecile' it jeers, its voice dripping with malice. Stunned by the unexpected insult, you find yourself at a loss for words, grappling with the surrealism of being verbally assaulted by a dessert.")
    elif rand == 1:
        messagebox.showinfo("Outcome",
                            "As you cautiously open the stove's door, your gaze falls upon a grotesque sight: a forgotten, moldy steak lies upon a blood-stained tray, accompanied by the decaying head of a deer, its vacant eyes staring into the abyss. The putrid stench fills the air, assaulting your senses and sending a shiver down your spine, as you realize you are not alone in this macabre chamber and you puke a little into your own mouth.")
    elif rand == 2:
        messagebox.showinfo("Outcome",
                            "As you cautiously approach the oven, anticipation tinged with apprehension fills the air. With a hesitant hand, you swing open the stove's door, only to find it empty, devoid of any warmth or remnants of cooking.")
kitchen()


def handle_cupboard():
    messagebox.showinfo("Outcome",
                        "The second you open the cupboard a loot midget jumps out of it and yells")
    rand = random.randint(0, 4)
    if rand == 0:
        messagebox.showinfo("Outcome", "Mine, mine, mine, mine, mine, mine, mine, mine, mine!!!!!!!!")
    elif rand == 1:
        messagebox.showinfo("Outcome", "MY PRECIOUSSSSSSSSS............")
    elif rand == 2:
        messagebox.showinfo("Outcome", "Punch me in the face!!!")
    elif rand == 3:
        messagebox.showinfo("Outcome", "So what if I'm a short king?")
    elif rand == 4:
        messagebox.showinfo("Outcome", "Delight your eyes with the sight of a true ⚡ code wizard ⚡ ")

    messagebox.showinfo("Outcome", "Then, the midget starts...")
    rand = random.randint(0, 3)
    if rand == 0:
        messagebox.showinfo("Outcome", "...delivering blows with the strength of a kitten's whimper.")
        Midget = Enemy("Loot Midget", 1, 8, 2)
        battle_thread = Thread(target=battle, args=(player, Midget))
        battle_thread.start()
        battle_thread.join()
    elif rand == 1:
        messagebox.showinfo("Outcome",
                            "...darting around the room in a crazed frenzy, his high-pitched screams echoing off the walls like the wails of a deranged soul.")
    elif rand == 2:
        messagebox.showinfo("Outcome", "...jumping in place like a crazy rabbit")
    elif rand == 3:
        messagebox.showinfo("Outcome",
                            "...throwing a hissy fit, hurling objects around the room with reckless abandon.")
        Midget = Enemy("Loot Midget", 1, 8, 2)
        battle_thread = Thread(target=battle, args=(player, Midget))
        battle_thread.start()
        battle_thread.join()
kitchen()


def handle_fridge():
    messagebox.showinfo("Outcome", "You open the fridge and inside, you find ")
    rand = random.randint(0, 2)
    if rand == 0:
        messagebox.showinfo("Outcome",
                            "a bunch of jars filled with eyeballs which start watching you and following the movement of your hands")
    elif rand == 1:
        messagebox.showinfo("Outcome",
                            "rows of neatly organised human and animal brains, pulsating with an eerie energy")
    elif rand == 2:
        messagebox.showinfo("Outcome", "a bottle of Jack Daniel's Old No. 4")
        choice = messagebox.askquestion("Decision", "Do you drink some whiskey?")
        if choice == "yes":
            messagebox.showinfo("Outcome", "You take a few sips of cold whiskey")
        else:
            messagebox.showinfo("Outcome", "You close the fridge")
kitchen()


def explore_basement():
    messagebox.showinfo("Basement", """
               __________
              |          |
              | Basement |
              |__________| 
    """"As you descend the stairs, you feel a chill in the air."
                                    "You reach the bottom and see an old rickety wooden door, barely held together by a couple i rusty nails.")
    choice = messagebox.askquestion("Decision", "Do you want to try to force the door open or search for a key?")

    if choice == "force":
        messagebox.showinfo("Outcome",
                            "You try to force the door open, and it breaks down instantly, granting you acess to the basement.")
        broken_door()

    elif choice == "search for a key":
        messagebox.showinfo("Outcome", "You search for the key but find nothing\n")
        choice = messagebox.askquestion("Decision", "Do you want to force open the door?")

        if choice == "yes":
            messagebox.showinfo("Outcome", "You force the rickety door open with ease and enter the basement")
            broken_door()

        elif choice == "no":
            messagebox.showinfo("Outcome", "You return to the main hall")


def broken_door():
    messagebox.showinfo("Inside Basement", "You broke the door and you are now in the basement")
    choice = messagebox.askquestion("Inside basement", "Do you want to explore the basement?")

    if choice == "yes":
        messagebox.showinfo("Outcome", "You see mountain of cardboard boxes in the corner of the basement,"
                                       " a really ancient old lady rocking on her chair (she seems to be hundreds of years old), staring at the wall"
                                       " and a small table with a severed horse head")
        choice = custom_choice_basement_dialog(root)
    if choice == 'boxes':
        handle_boxes()
    elif choice == 'old':
        handle_creepyGrandma()
    elif choice == 'head':
        handle_head()

    elif choice == "no":
        messagebox.showinfo("Outcome", "You return to the main hall")


def custom_choice_basement_dialog(parent):
    dialog = tk.Toplevel(parent)
    dialog.title("Decision")

    tk.Label(dialog, text="What do you want to do?").pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    choice = tk.StringVar()
    choice.set(None)

    tk.Button(button_frame, text="Look inside the cardboard boxes",
              command=lambda: set_choice(dialog, choice, "boxes")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Try to see if the old lady is still alive",
              command=lambda: set_choice(dialog, choice, "old")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Go the the horse head", command=lambda: set_choice(dialog, choice, "head")).pack(
        side="left", padx=5)

    dialog.wait_window(dialog)
    return choice.get()


def handle_boxes():
    messagebox.showinfo("Outcome", "You start searching inside the cardboard boxes, and... ")
    rand = random.randint(0, 2)
    if rand == 0:
        messagebox.showinfo("Outcome",
                            "the mountain of boxes falls down on you. Fortunately, all of them were empty!")
    elif rand == 1:
        messagebox.showinfo("Outcome",
                            "the first few boxes are empty, but one of them has a bunch of bones of unknown origin (most of them don't look human nor animal)\n, "
                            "another box has a 'collection' of bloodied skin patches of various shapes and sizes,\n"
                            "the next box you open has a raunchy love letter inside - you refuse to read it,\n"
                            "a different box has a loot midget inside who scream 'I AAAAAAM DEEEEEEEELICIOOOOOOOOOUSSSSSSSSS!!!!!!!!!' - you quickly close the box, leaving the loot midget to his own devices")
        choice = messagebox.askquestion("Choice", "Do you want to open more boxes?")

        if choice == "yes":
            messagebox.showinfo("Outcome",
                                "The next few boxes you open all have relatively fresh human and animal intestines, eyeballs and other nasty viscera")
        elif choice == "no":
            messagebox.showinfo("Outcome", "You look somewhere else in the basement")

            choice = custom_choice_basement_dialog(root)

    elif rand == 2:
        messagebox.showinfo("Outcome", " you find that the boxes contain some mechanical parts and a blueprint for something called 'N's laser'")
        choice = messagebox.askquestion("Decision", "Do you want to try and assemble the contraption?")
        if choice == "yes":
            messagebox.showinfo("Outcome", "You try to assemble the laser but when you finish following the instructions on the blueprint, it only displays the following message:\n"
                                "Your calculations were not correct, Mr. student! Now, DO AGAIN!!!")
            choice = messagebox.askquestion("Choice", "Do you want to try and assemble the contraption again?")
            if choice == "yes":
                bool = 1;
                while (bool):
                    choice = messagebox.askquestion("Choice", "Do you want to try and assemble the contraption again?")
                    if choice == "yes":
                        messagebox.showinfo("Your calculations were not correct, Mr. student! Now, DO AGAIN!!!")
                    elif choice == "no":
                        messagebox.showinfo("Outcome", "You give up, knowing that you will never wield the power of N's laser")
                        bool = 0
            elif choice == "no":
                messagebox.showinfo("Outcome", "You give up, knowing that you will never wield the power of N's laser")
        elif choice == "no":
            messagebox.showinfo("Outcome", "You give up without even attempting to assemble the device, knowing that you will never wield the power of N's laser")
    explore_basement()

def handle_creepyGrandma():
    messagebox.showinfo("Outcome", "You go near the almost fossilised old grandma")
    messagebox.showinfo("Outcome", "The old creepy grandma follows your movements with her sight and nothing more,\n"
                                   "giving you the impression that inside the old shriveled and calcified carcass, the mind is still very very VERY functional")
    messagebox.showinfo("Outcome", "You back away from the creepy grandma, filled with fear and extreme unease as she keeps scanning your every movement")
    messagebox.showinfo("Outcome", "You try exploring other parts of the basement, not wanting to interact with the creepy grandma ever again.")
    explore_basement()

def secret_passage():
    messagebox.showinfo("Secret Passage", """
                ________________
               /                \ 
              /   Secret       /
              \  Passage      /
               \_____________/ 
    """
                                          "You discover a secret passage behind a bookshelf.\n"
                                          "As you explore further, you find yourself in a dark corridor.\n"
                                          "Suddenly, the passage collapses behind you, blocking your way back.\n")
    root.withdraw()
    messagebox.showinfo("Decision", "Do you want to continue forward or try to find another way back?")
    choice = custom_choice_dialog2(root)

    if choice == 'Continue Forward':
        handle_continue_forward()
    elif choice == 'Find Another Way':
        handle_find_another_way()
    else:
        messagebox.showinfo("Outcome", "You decided to do nothing.")


def custom_choice_dialog2(parent):
    dialog = tk.Toplevel(parent)
    dialog.title("Decision")

    tk.Label(dialog, text="Do you want to continue forward or try to find another way back?").pack(padx=20, pady=10)

    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    choice = tk.StringVar()
    choice.set(None)

    tk.Button(button_frame, text="Continue Forward",
              command=lambda: set_choice2(dialog, choice, "Continue Forward")).pack(side="left", padx=5)
    tk.Button(button_frame, text="Find Another Way",
              command=lambda: set_choice2(dialog, choice, "Find Another Way")).pack(side="left", padx=5)

    dialog.wait_window(dialog)
    return choice.get()


def set_choice2(dialog, choice, value):
    choice.set(value)
    dialog.destroy()


def handle_continue_forward():
    messagebox.showinfo("Outcome", (
        "You press on through the darkness, feeling your way along the walls. "
        "After what feels like hours, you emerge into a hidden chamber. "
        "Inside, you find the lost family heirlooms and riches beyond your wildest dreams. "
        "Congratulations, you have successfully navigated the secret passage and claimed your inheritance."
    ))


def handle_find_another_way():
    messagebox.showinfo("Outcome", (
        "You search for another way back, but the passage is blocked. "
        "In the darkness, you stumble and fall, hitting your head. "
        "You lose consciousness and never wake up. "
        "Game over."
    ))


# Define the attic function
def attic():
    messagebox.showinfo("Attic", """
                ____________
               /            \ 
              /    Attic    /
              \____________/ 
    """
                                 "You climb up to the attic, dust and cobwebs greeting your every step."
                                 "In the dim light, you spot an old chest.")
    choice = messagebox.askquestion("Decision", "Do you want to open the chest?")
    if choice == "yes":
        messagebox.showinfo("Outcome", "You open the chest and find a collection of cursed artifacts."
                                       "As you touch one, a dark energy surges through you, consuming your soul."
                                       "You are now bound to the mansion for eternity.")
    elif choice == "no":
        messagebox.showinfo("Outcome", "You decide not to open the chest."
                                       "As you turn to leave, you hear a faint whisper echoing in the attic."
                                       "It beckons you to stay, but you resist and quickly descend back down to safety.")


# Define the explore garden function
def explore_garden():
    messagebox.showinfo("Garden", """
                ___________
               /           \ 
              /   Garden    /
              \____________/ 
    """
                                  "You step out into the overgrown garden, nature having reclaimed much of it."
                                  "In the distance, you see a mausoleum.")
    choice = messagebox.askquestion("Decision", "Do you want to approach the mausoleum?")

    if choice == "yes":
        messagebox.showinfo("Outcome", "As you approach the mausoleum, the door creaks open on its own."
                                       "Inside, you find the resting place of your ancestors and a hidden passage.")
        secret_passage()
    elif choice == "no":
        messagebox.showinfo("Outcome", "You decide to avoid the mausoleum and explore the garden further."
                                       "Amidst the foliage, you find a forgotten fountain with coins scattered at the bottom."
                                       "You collect the coins and return to the mansion, feeling a strange sense of unease.")


# Define process_input function
def process_input(input_str):
    if "living" in input_str:
        living_room()
    elif "kitchen" in input_str:
        kitchen()
    elif "basement" in input_str:
        explore_basement()
    elif "attic" in input_str:
        attic()
    elif "garden" in input_str:
        explore_garden()


def ghost_encounter():
    messagebox.showinfo("Outcome", "A ghostly figure appears before you, moaning with despair."
                                   "You feel a chill down your spine.")


def treasure_found():
    messagebox.showinfo("Outcome", "You stumble upon a hidden compartment filled with ancient treasures."
                                   "The glint of gold and jewels dazzles your eyes.")


def trigger_random_event():
    # Generate a random number to determine the event
    event = random.randint(1, 3)
    if event == 1:
        ghost_encounter()
    elif event == 2:
        treasure_found()
    # Add more random events as needed


# Create the main GUI window
root = Tk()
root.title("Haunted Mansion")


def show_main_menu():
    nickname()
    introduction()
    # Create buttons for each room
    living_room_button = tk.Button(root, text="Living Room", command=living_room)
    living_room_button.pack()

    kitchen_button = tk.Button(root, text="Kitchen", command=kitchen)
    kitchen_button.pack()

    basement_button = tk.Button(root, text="Basement", command=explore_basement)
    basement_button.pack()

    secret_passage_button = tk.Button(root, text="Secret Passage", command=secret_passage)
    secret_passage_button.pack()

    attic_button = tk.Button(root, text="Attic", command=attic)
    attic_button.pack()

    garden_button = tk.Button(root, text="Garden", command=explore_garden)
    garden_button.pack()

    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack()

    # Show the main menu


show_main_menu()

# Display the main menu
root.mainloop()
