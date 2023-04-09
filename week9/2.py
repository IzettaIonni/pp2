from functools import total_ordering
import random
from datetime import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("comicsans", 30) #created font for lvl and score


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 5  # Right.
        self.dy = 0
        self.is_add = False
        self.speed = 30
        self.xwall = 0
        self.ywall = 0
        self.eatbox = 15 #added eatbox variable

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, foodcords):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodcords[0] - self.eatbox <= x <= foodcords[0] + self.eatbox and foodcords[1] - self.eatbox <= y <= foodcords[1] + self.eatbox:   #fixed and raised eatboxes also for big food 
            return True
        return False
    def wall(self):     #wall check
        self.xwall, self.ywall = 0, 0
        if self.elements[0][0] < 10:
            self.xwall = -1
        if self.elements[0][1] < 10:
            self.ywall = -1
        if self.elements[0][0] > 790:
            self.xwall = 1
        if self.elements[0][1] > 790:
            self.ywall = 1
        return self.xwall, self.ywall


class Food:
    def __init__(self):
        self.x = random.randint(30, 770)
        self.y = random.randint(30, 770)
        self.big_food = False

    def gen(self):
        self.x = random.randint(30, 770)
        self.y = random.randint(30, 770)
        if random.randint(-3, 1):
            self.big_food = True
            snake1.eatbox = 25
        else:
            self.big_food = False
            snake1.eatbox = 13
    
    def center(self):                   #eatbox fix
        if self.big_food:
            return (self.x+15, self.y+15)
        else:
            return (self.x+5, self.y+5)

    def draw(self):
        if self.big_food:                                                         #size difference in food
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 30, 30))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))


class level_score:         #added level and score class 
    def __init__(self):
        self.score = 0
        self.lvl = 1
        self.lvl_counter = 0
        self.food_cost = 1      #added level difference between big and normal food

    def scoreup(self):     #at levels 1-3 level up gives 5 speed, at levels 3+ gives 2
        if food.big_food:           #food difference realisation
            self.food_cost = 2  
        else:
            self.food_cost = 1
        self.score += self.food_cost            
        self.lvl_counter += self.food_cost
        if self.lvl_counter >= 3:            
            if self.lvl < 4:
                snake1.speed += 5
            else:
                snake1.speed += 2
            self.lvl += 1
            self.lvl_counter -= 3

    def draw(self):
        self.score_txt = font.render('score: ' + str(self.score), True, (255, 255, 255))    
        self.lvl_txt = font.render('level: ' + str(self.lvl), True, (255, 255, 255))
        screen.blit(self.score_txt, (670,0))
        screen.blit(self.lvl_txt, (20,0))


snake1 = Snake(100, 100)    #removed second snake
food = Food()
lvl_score = level_score()

running = True

FPS = 30
d = 5
lvl_counter = 0
food_timer = datetime.now().replace(microsecond=0)      #10 seconds timer for food respawn

clock = pygame.time.Clock()

while running:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key == pygame.K_SPACE:
            #     snake1.is_add = True
            #     snake2.is_add = True
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_a and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_w and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_s and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

    if snake1.eat(food.center()):
        snake1.is_add = True
        lvl_score.scoreup()     #score and lvl up update
        food.gen()
        food_timer = datetime.now().replace(microsecond=0)

    if snake1.wall() != [0, 0]:     #check wall and move in opposite direction if touch the wall
        wallxy = snake1.wall()
        if wallxy[0] == -1 or wallxy[0] == 1:
            if snake1.elements[0][0] > 400:
                snake1.dx = -d
                snake1.dy = 0
            else:
                snake1.dx = d
                snake1.dy = 0
        if wallxy[1] == -1 or wallxy[1] == 1:   
            if snake1.elements[0][1] > 400:
                snake1.dx = 0
                snake1.dy = -d
            else:
                snake1.dx = 0
                snake1.dy = d
        if (datetime.now().replace(microsecond=0) - food_timer).total_seconds() >= 10:       #if food didn't peeked up 10 seconds it's respawned
            food_timer = datetime.now().replace(microsecond=0)
            food.gen()

    snake1.move()
    screen.fill((0, 0, 0))
    snake1.draw()
    food.draw()
    lvl_score.draw()                    #showing level and score
    pygame.display.flip()

pygame.quit()