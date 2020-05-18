# Science Comic Strip
# An game about a money - hungry helicopter
# By Simón Botero, for the science teacher Jill Holmes
# A project using Pygame 2.0.0.dev6, with the Python 3.7.7 interpreter, and the PyCharm IDE

# Import the modules we will be using for this project.
import pygame
from sys import exit
import random

# Initialize (or enable) all of the pygame functionality!
pygame.mixer.init()
pygame.mixer.init()
pygame.font.init()

# Define some of the variables we will be using
HEIGHT, WIDTH = (800, 800)  # Creates a variable that stores our screen width and height
score = 0
BLACK_RGB = (0, 0, 0)
PI = 3.1419
level = 1
out_of_screen = False
arial = pygame.font.SysFont('arial', 50)
starting_or_menu = True

# While setting up our variables, let's set the names of our images. Also, lets load them up.
FILE_FORMAT = ".png"
HELICOPTER_NAME = "helicopterHelicopter"
COIN_NAME = "helicopterCoin" + FILE_FORMAT
CLOUD_NAME = "helicoptercloud" + FILE_FORMAT
BG_NAME = "backgroundHelicopter" + FILE_FORMAT

COIN = pygame.image.load(COIN_NAME)
CLOUD = pygame.image.load(CLOUD_NAME)
BG = pygame.image.load(BG_NAME)
HELICOPTER = pygame.image.load(HELICOPTER_NAME + FILE_FORMAT)

clouds_list = []
coins_list = []
wave_length = 100
number_of_clouds = len(clouds_list)
number_of_coins = len(coins_list)

# Creating the screen and setting it up (or Surface object, in technical terms)
WIN = pygame.display.set_mode((HEIGHT, WIDTH))  # Creates the screen object and stores
pygame.display.set_caption("The helicopter Game by SB")  # Sets the screen caption
pygame.display.set_icon(HELICOPTER)


# I will now create functions to display and do various things
class Game:
    def __init__(self):
        self.WIN = WIN
        self.COIN = COIN
        self.score = 0
        self.coins_list = []
        self.coins = 50
        self.level = 0

    def score_label_on_screen(self):
        score_tag = arial.render(f"Score: {self.score}", 1, BLACK_RGB)
        WIN.blit(score_tag, (WIDTH - score_tag.get_width() - 10, 0 + score_tag.get_width() / 8 - 20))

    def level_label_on_screen(self):
        level_tag = arial.render(f"Level: {self.level}", 1, BLACK_RGB)
        WIN.blit(level_tag, (level_tag.get_width() - 165, level_tag.get_height() - 112 / 2))


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIN = WIN
        self.clouds_list = []
        self.number_of_clouds = 500


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        WIN.blit(COIN, (self.x, self.y))


class Player:
    def __init__(self, x, y):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.HELICOPTER = HELICOPTER
        self.mask = pygame.mask.from_surface(HELICOPTER)

    def check_for_keypress(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP] and sbPlayer.y - 7 > 0:
            self.y -= 7
        if keypress[pygame.K_DOWN] and sbPlayer.y + 7 + HELICOPTER.get_height() < HEIGHT:
            self.y += 7
        if keypress[pygame.K_RIGHT] and sbPlayer.x + 7 + HELICOPTER.get_width() < 800:
            self.x += 7
        if keypress[pygame.K_LEFT] and sbPlayer.x - 7 > 0:
            self.x -= 7


# Let's create some objects that belong to our previously created classes
controller = Game()
sbPlayer = Player(30 + HELICOPTER.get_width(), 400)

# Creating a clock object, which lets us schedule the screen refresh
clock = pygame.time.Clock()


# Create a loop that makes sure our code is repeated until the end
def mainloop(wave_length=wave_length):
    running = True

    while running:

        WIN.blit(BG, (0, 0))

        def draw_clouds():
            for cloud in range(wave_length):
                cloud = Cloud(random.randint(200, 15000), random.randint(0, HEIGHT - CLOUD.get_width()))
                clouds_list.append(cloud)

        for cloud in clouds_list:
            if cloud.x <= -CLOUD.get_width() + 10:
                clouds_list.remove(cloud)
            else:
                WIN.blit(CLOUD, (cloud.x, cloud.y))
                cloud.x -= 3.1419 + PI / PI

        for coin in range(wave_length):
            coin = Coin(random.randint(WIDTH * 2, 30000), random.randint(0, HEIGHT - COIN.get_height()))
            coins_list.append(coin)

        if len(clouds_list) == 0:
            wave_length += 25
            controller.level += 1
            draw_clouds()

        WIN.blit(HELICOPTER, (sbPlayer.x, sbPlayer.y))

        for event in pygame.event.get():  # For every type of event python can register, do the following code
            if event.type == pygame.QUIT:  # See if the event type is equal to the type of event that makes you quit
                running = False
                pygame.quit()  # Quit the screen
                exit()  # Exits any current python project, from the sys module we imported earlier
        controller.score_label_on_screen()
        controller.level_label_on_screen()
        sbPlayer.check_for_keypress()

        pygame.display.update()  # Update the display


def pre_game_screen():
    while not starting_or_menu:
        WIN.blit()


#  pre_game_screen()
mainloop()
