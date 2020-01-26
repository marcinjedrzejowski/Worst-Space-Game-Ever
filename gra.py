import pygame
import numpy as np

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setting up score
score = 0

# Some colors for UI
lightgrey = (211,211,211)
grey = (105,105,105)
white = (255,255,255)
black = (0,0,0)


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Player.png").convert()
        self.surf.set_colorkey(black, RLEACCEL)
        self.rect = self.surf.get_rect(center=(0, SCREEN_HEIGHT/2))

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("enemy.png").convert()
        self.surf.set_colorkey(black, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                np.random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                np.random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = np.random.randint(5, 25)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the planet1 object by extending pygame.sprite.Sprite
class Planet1(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet1, self).__init__()
        self.surf = pygame.image.load("Planet1.png").convert()
        self.surf.set_colorkey(black, RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                np.random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                np.random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the planet1 based on a constant speed
    # Remove the planet1 when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Define the planet2 object by extending pygame.sprite.Sprite
class Planet2(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet2, self).__init__()
        self.surf = pygame.image.load("Planet2.png").convert()
        self.surf.set_colorkey(black, RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                np.random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                np.random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the planet2 based on a constant speed
    # Remove the planet2 when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Define the star object by extending pygame.sprite.Sprite
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.surf = pygame.image.load("Star.png").convert()
        self.surf.set_colorkey(black, RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                np.random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                np.random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the star based on a constant speed
    # Remove the star when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def game_intro():
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        textSurf, textRect = text_objects("Worst Space Game Ever", largeText)
        textRect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
        screen.blit(textSurf, textRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Play", smallText)
        textRect.center = ((150+(100/2)), (450+(50/2)))
        screen.blit(textSurf, textRect)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, lightgrey, (150, 450, 100, 50))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(screen, grey, (150, 450, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        screen.blit(textSurf, textRect)

        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen,lightgrey, (550, 450, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, grey, (550, 450, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("QUIT!", smallText)
        textRect.center = ((550+(100/2)), (450+(50/2)))
        screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Set font size and type
myfont = pygame.font.SysFont("monospace", 20)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 4
pygame.time.set_timer(ADDENEMY, 300)
ADDPLANET1 = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPLANET1, 2000)
ADDPLANET2 = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPLANET2, 2000)
ADDSTAR = pygame.USEREVENT + 3
pygame.time.set_timer(ADDSTAR, 500)

player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
planets1 = pygame.sprite.Group()
planets2 = pygame.sprite.Group()
stars = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

intro = True

# Starting Game Intro
game_intro()

# Variable to keep the main loop running
running = True
# Setup the clock for decent framerate
clock = pygame.time.Clock()

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new planet?
        elif event.type == ADDPLANET1:
            # Create the new planet1 and add it to sprite groups
            new_planet1 = Planet1()
            planets1.add(new_planet1)
            all_sprites.add(new_planet1)

        elif event.type == ADDPLANET2:
            # Create the new planet2 and add it to sprite groups
            new_planet2 = Planet2()
            planets2.add(new_planet2)
            all_sprites.add(new_planet2)

        elif event.type == ADDSTAR:
            # Create the new star and add it to sprite groups
            new_star = Star()
            stars.add(new_star)
            all_sprites.add(new_star)

    # Update enemy position
    enemies.update()
    planets1.update()
    planets2.update()
    stars.update()

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill(black)

    # Show score on screen
    scoretext = myfont.render("Score {0}".format(score), 1, white)
    screen.blit(scoretext, (5, 10))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Check if any stars have collided with the player, if so add 1 to score and remove star
    gets_hit = pygame.sprite.spritecollide(player, stars, True)
    if gets_hit:
        score += 1

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(60)