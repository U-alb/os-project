# Haunted Mansion

## Description

Haunted Mansion is an interactive text-based adventure game that uses a GUI interface built with `tkinter`. Players explore different rooms of a haunted mansion, uncovering secrets, encountering random events, and making choices that affect their fate. The game features randomized outcomes to enhance replayability and includes sound effects for an immersive experience.

## Features

- Explore various rooms: living room, kitchen, basement, attic, and garden.
- Random events that occur during exploration.
- GUI-based interface with `tkinter`.
- Player input for decisions.
- Sound effects using `pygame`.
- Customizable player name.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/haunted-mansion.git
    cd haunted-mansion
    ```

2. Install the required dependencies:
    ```sh
    pip install pygame
    ```

3. Ensure you have `tkinter` installed (it comes pre-installed with standard Python distributions).

## How to Play

1. Run the game:
    ```sh
    python main.py
    ```

2. A window will appear prompting you to enter your name.

3. Navigate through the mansion by making choices presented in dialog boxes.

4. Encounter random events and make decisions to uncover secrets and survive the haunted mansion.

5. Enjoy the immersive experience with sound effects.

## Code Structure

- `main.py`: Main game logic and GUI implementation.
- `assets/`: Directory containing sound files used in the game.

## Example Code

Here is a snippet of how the game initializes and introduces the player:

```python
import random
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

def introduction():
    messagebox.showinfo("Welcome", f"Welcome to the Haunted Mansion, {name}!\n"
                                   f"You are a distant family member of the Van der Meer family, who built Ravenwood Manor.\n"
                                   f"Generations of Van der Meers resided within its walls, their opulent lifestyle overshadowed by rumors of corruption and scandal.\n"
                                   "Are you prepared to uncover the dark secrets that lie within Ravenwood Manor?\n"
                                   "As the newfound owner, you decide to pay a visit to the mansion.\n"
                                   "The house is dated, creaky, and falling apart. You walk in the front door.\n"
                                   "Do you want to enter the living room, kitchen room, explore the basement, attic, or explore the garden?")
