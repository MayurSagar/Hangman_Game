import pygame

pygame.init()

# Defining Width and Height of our Game Window
WIDTH, HEIGHT = 800, 500
# Display width and height in Tuple.Because pygame Display width and height as Tuple.
pygame.display.set_mode((WIDTH, HEIGHT))

# Define and Display Game name
pygame.display.set_caption("Hangman Game!")

# Frame Per Second
FPS = 60

# Clock Object
clock = pygame.time.Clock()

run = True
# while Loop
while run:
    # clock.tick while make the game run at a Constant speed like 60
    clock.tick(FPS)

    # looping through pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()






