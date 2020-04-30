# Science Comic Strip
# An game about a money - hungry helicopter
# By Simón Botero, for the science teacher Jill Holmes
# A project using Pygame 2.0.0.dev6, with the Python 3.7.7 interpreter, and the PyCharm IDE

# Import the modules we will be using for this project.
import pygame 
from time import sleep
from sys import exit
import os 

# Initialize (or enable) all of the pygame functionality!
pygame.mixer.init()
pygame.font.init()

# Define some of the variables we will be using
HEIGHT, WIDTH = (800, 800) # Creates a variable that stores our screen width and height
score = 0
FONT = pygame.font.SysFont('arial', 75, True, False, None)
score_label = FONT.render(f"Score: {score}", 1, (250, 250, 250))

# Creating the screen and setting it up (or Suface object, in technical terms)
WIN = pygame.display.set_mode((HEIGHT, WIDTH))  # Creates the screen object and stores
pygame.display.set_caption("The helicopter Game by SB")  # Sets the screen caption

# Creating a clock object, which lets us schedule the screen refresh
clock = pygame.time.Clock()

# Create a loop that makes sure our code is repeated until the end
while True:
    for event in pygame.event.get():  # For every type of event python can register, do the following code
        if event.type == pygame.QUIT:  # See if the event type is equal to the type of event that makes you quit (
            # pygame.quit())
            pygame.quit()  # Quit the screen
            exit()  # Exits any current python project, from the sys module we imported earlier
    pygame.display.update()  # Update the display