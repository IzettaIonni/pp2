import pygame
import math
import datetime


def draw_arrow(val, num_units, arrow_len, thickness=2):
    alpha = val * math.pi * 2 / num_units
    length = int(arrow_len * min(size)) // 2
    end_coord = (
        center[0] + int(length * math.sin(alpha)),
        center[1] - int(length * math.cos(alpha))
    )
    pygame.draw.line(screen, (0, 0, 0), center, end_coord, thickness)


pygame.init()
pygame.display.set_caption("clock")
size = (958, 958)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
dial = pygame.image.load('week7\dial.png')
center = screen.get_rect().center

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 10, 40))
    screen.blit(dial, (0, 0))
    now = datetime.datetime.now()
    draw_arrow(now.hour + now.minute/60, 12, 0.5, thickness=20)
    draw_arrow(now.minute, 60, 0.7, thickness=10)
    draw_arrow(now.second, 60, 0.8, thickness=5)
    fps.tick(60)
    pygame.display.flip()

pygame.quit()
