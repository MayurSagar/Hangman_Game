import pygame
import math
import random

# ***** Setup Display ****
pygame.init()

# Defining Width and Height of our Game Window
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# ***** fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 65)

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

A = 65

for i in range(26):
    # x and y position of buttons
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + (i // 13) * (GAP + RADIUS * 2)
    letters.append([x, y, chr(A + i), True])

# ***** Game Variable *****
hangman_status = 0
words = ["NARUTO", "KAKASHI", "SAITAMA", "KENKANAKI", "EREN", "ITACHI", "MADARA"]

word = random.choice(words)
guessed = []

# ***** Colors *****
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ***** Game Loop *****
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    #draw title
    text = TITLE_FONT.render("ANIME HANGMAN", 1 , BLACK )
    win.blit(text, (WIDTH/2 - text.get_width()/2 , 10 ))

    # draw word
    display_word = ""
    for letter in word:
        # checking if the letter in word is there in guessed.
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

# Render text
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons on x, y position and letter which we want to draw
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            # render text means what text you want to get displayed
            text = LETTER_FONT.render(ltr, 1, BLACK)
            # draw text on x, y position
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


# while Loop
while run:
    # clock.tick while make the game run at a Constant speed like 60
    clock.tick(FPS)

    # looping through pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    # distance between x, y cordinate and mourse x, y coordinate m_x, m_y)
                    distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()
    won = True
    for letter in word:
            if letter not in guessed:
                won = False
                break
    if won :
        display_message("You Won!")

        break

    if hangman_status == 6:
        display_message("You Lost!")
        break
pygame.quit()
