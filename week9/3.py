import pygame 

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pos =  screen.get_rect().center
pos = list(pos)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if not pos[1] - 20 <= 50:
                    pos[1] -= 20
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if not pos[1] + 20 >= size[1]-50:
                    pos[1] += 20                    
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if not pos[0] - 20 <= 50:
                    pos[0] -= 20
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if not pos[0] + 20 >= size[0]-50:
                    pos[0] += 20

    fps.tick(60)
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), pos, 50)
    pygame.display.flip()

pygame.quit()