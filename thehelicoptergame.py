# Science Comic Strip
# An game about a money - hungry helicopter
# By Simón Botero, for the science teacher Jill Holmes
# A project using Pygame 2.0.0.dev6, with the Python 3.7.7 interpreter, and the PyCharm IDE

# Import the modules we will be using for this project.
import pygame
from time import sleep
from sys import exit
from os import path

# Initialize (or enable) all of the pygame functionality!
pygame.mixer.init()
pygame.font.init()

# Define some of the variables we will be using
HEIGHT, WIDTH = (800, 800)  # Creates a variable that stores our screen width and height
score = 0
FONT = pygame.font.SysFont('arial', 50)
score_label = FONT.render(f"Score: {score}", 1, (250, 250, 250))

# While setting up our variables, let's set the names of our images. Also, lets load them up.
FILE_FORMAT = ".png"
HELICOPTER_NAME = "helicopterHelicopter"
COIN_NAME = "helicopterCoin" + FILE_FORMAT
CLOUD_NAME = "helicoptercloud" + FILE_FORMAT
BG_NAME = "backgroundHelicopter" + FILE_FORMAT

COIN = pygame.image.load(COIN_NAME)
CLOUD = pygame.image.load(CLOUD_NAME)
BG = pygame.image.load(BG_NAME)
HELICOPTER = HELICOPTER_NAME + FILE_FORMAT

# Creating the screen and setting it up (or Surface object, in technical terms)
WIN = pygame.display.set_mode((HEIGHT, WIDTH))  # Creates the screen object and stores
pygame.display.set_caption("The helicopter Game by SB")  # Sets the screen caption


# I will now create functions to display and do various things
class Game:
    def __init__(self):
        self.WIN = WIN
        self.COIN = COIN
        self.score = score
        self.coins_list = []
        self.coins = 50


    def score_label_on_screen(self):
        WIN.blit(score_label, (WIDTH - score_label.get_width() - 10, 0 + score_label.get_width() / 8 - 20))


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIN = WIN
        self.clouds_list = []
        self.number_of_clouds = 500

    def create_clouds(self):
        for cloud in self.clouds_list:
            WIN.blit(CLOUD, (self.x, self.y))

    def out_of_screen(self):
        for cloud in self.clouds_list:
            if cloud.x + cloud.get_width() == 0:
                self.clouds_list.remove(cloud)


class Player:
    def __init__(self, x, y):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.HELICOPTER = HELICOPTER

    def check_for_keypress(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP] + 5 > 0:
            pass
        if keypress[pygame.K_DOWN]:
            pass
        if keypress[pygame.K_RIGHT]:
            pass
        if keypress[pygame.K_LEFT]:
            pass

# Let's create some objects that belong to our previously created classes
controller = Game()
sbPlayer = Player(30 + CLOUD.get_width(), 400)

# Creating a clock object, which lets us schedule the screen refresh
clock = pygame.time.Clock()

# Create a loop that makes sure our code is repeated until the end
while True:
    WIN.blit(BG, (0, 0))

    for clouds in controller.number_of_clouds:
        controller.clouds_list.append(clouds)

    if len(controller.clouds_list) == 0:
        controller.number_of_clouds += 25

    for event in pygame.event.get():  # For every type of event python can register, do the following code
        if event.type == pygame.QUIT:  # See if the event type is equal to the type of event that makes you quit (
            # pygame.quit())
            pygame.quit()  # Quit the screen
            exit()  # Exits any current python project, from the sys module we imported earlier
    controller.score_label_on_screen()

    pygame.display.update()  # Update the display
