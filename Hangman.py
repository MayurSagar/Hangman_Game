import pygame

# ***** Setup Display ****
pygame.init()

# Defining Width and Height of our Game Window
WIDTH, HEIGHT = 800, 500

# Display width and height in Tuple.Because pygame Display width and height as Tuple.
# Storing the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Define and Display Game name
pygame.display.set_caption("Hangman Game!")

# ***** Load Images *****
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# button variables
RADIUS = 20
GAP = 15
letters = []

startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)  # horizontal
starty = 400  # vertical stating
for i in range(26):
    # x and y position of buttons
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + (i // 13) * (GAP + RADIUS * 2)
    letters.append([x, y])

# ***** Game Variable *****
# for knowing the status of hangman images which we are using.
hangman_status = 0

# ***** Colors *****
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# ***** Game Loop *****
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    # draw buttons
    for letter in letters:
        x, y = letter
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# while Loop
while run:
    # clock.tick while make the game run at a Constant speed like 60
    clock.tick(FPS)

    draw()

    # looping through pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
