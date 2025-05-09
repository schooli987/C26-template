import pygame
import pymunk
import pymunk.pygame_util
import sys
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("balloon game")

clock = pygame.time.Clock()
FPS = 60

space = pymunk.Space()
space.gravity = (0, -50)
balloons=[]

score = 0
target_score = 1500  # 20 balloons * 100
balloons = []

frame_count = 0
max_frames = 900  # 30 seconds at 60 fps
game_over = False
won = False
draw_options = pymunk.pygame_util.DrawOptions(screen)
frame_count = 0
running = True

balloon_image = pygame.image.load("balloon.png")
balloon_image = pygame.transform.scale(balloon_image, (150, 150))
background=pygame.image.load("balloonbg.jpg")
background = pygame.transform.scale(background, (800, 600))

def create_balloon():
    x = random.randint(75, 725)
    y = 500
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 25))
    body.position = x, y
    shape = pymunk.Circle(body, 25)
    shape.elasticity = 0
    shape.friction = 0.5
    space.add(body, shape)
    return body, shape

# Timer Logic
frame_count = 0
max_frames = 900  # 30 seconds at 60 FPS



while running:
    screen.blit(background, (0, 0))
    if random.randint(1,30)==1:
        balloons.append(create_balloon())

   
    time_left = max(0, (max_frames - frame_count) // 60)
    
    # Display time left on screen
      # HUD
    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Time Left: {time_left}s", True, (0, 0, 0)), (600, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

            for body, shape in balloons:
                x, y = body.position
                balloon_rect = pygame.Rect(x - 75, y - 75, 150, 150)
                if balloon_rect.colliderect(mouse_rect):
                    balloons.remove((body, shape))
                    space.remove(body, shape)
                    score+=100
                    
    for body, shape in balloons:
        x, y = body.position
        screen.blit(balloon_image, (x - 75, y - 75))

   
    space.step(1 / FPS)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
