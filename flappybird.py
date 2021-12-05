# MADE BY ALEXANDER GEMAZASHVILI
import pygame
import random

# Screen Settings
WIDTH = 600
HEIGHT = 850
FPS = 60

# Colors
YELLOW = (255, 255, 0)
SKY = (133, 193, 233)
GREEN = (46, 204, 113)
WHITE = (255, 255, 255)
bg = pygame.image.load("background.png")
# Initialisation
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')

# Character Setting
bird = pygame.Rect(40, 250, 30, 23)
birdImg = pygame.image.load('bird.png')
points = 0


# Fonts
font = pygame.font.SysFont('comic sans ms', 30)
game_over_font = pygame.font.SysFont('comic sans ms', 50)
game_over_text = game_over_font.render('GAME OVER', 1, WHITE)

# Fall
GRAVITY = 0.3
y_change = 0

# Jump
isJump = False
jumpCount = 10

# Pipe Settings
pipes = []
pipecd = 1500

check = []

# Time Parameters
clock = pygame.time.Clock()
currentTime = 0
lastPipeTime = 0

game_over = False
running = True
while running:
    screen.blit(bg, (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                isJump = True
                hopCount = 0

    # Jump
    if isJump:
        hopCount += 1
        bird.top -= 6
        if hopCount == 5:
            y_change = 0
            isJump = False
    # falling
    else:
        y_change += GRAVITY
        bird.top += y_change

    # time
    currentTime = pygame.time.get_ticks()

    if currentTime - lastPipeTime > pipecd:
        width_pipe = 40
        # Up Pipe
        height_up_pipe = random.randint(50, 400)
        up_pipe = pygame.Rect(WIDTH, 0, width_pipe, height_up_pipe)

        # Down Pipe
        y_down_pipe = height_up_pipe + 100
        height_down_pipe = HEIGHT - y_down_pipe
        down_pipe = pygame.Rect(WIDTH, y_down_pipe, width_pipe, height_down_pipe)

        y_middle_space = height_up_pipe
        height_middle_space = HEIGHT - height_up_pipe - height_down_pipe
        middle_space = pygame.Rect(WIDTH, y_middle_space, width_pipe, height_middle_space)
        check.append(middle_space)

        # Pipe Adding
        pipes.append((up_pipe, down_pipe))

        lastPipeTime = currentTime
        pipecd = random.randint(1500, 2000)

        # PIPE
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, GREEN, pipe[1])
        pipe[0].left -= 2
        pipe[1].left -= 2

    if bird.top < 0 or bird.bottom > HEIGHT:
        game_over = True

    # Pipe Colliderect
    for pipe in pipes:
        up_pipe = pipe[0]
        down_pipe = pipe[1]

        if bird.colliderect(up_pipe):
            game_over = True
        elif bird.colliderect(down_pipe):
            game_over = True

    for flag in check:
        flag.left -= 2
        if bird.colliderect(flag):
            points += 1
            check.remove(flag)

    screen.blit(birdImg, (bird.left, bird.top))


    if game_over:
        screen.blit(SKY)
        screen.blit(game_over_text, (330, 300))

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
