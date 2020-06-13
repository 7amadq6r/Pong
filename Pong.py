import pygame
import random
pygame.font.init()
pygame.init()

WIN_H = 650
WIN_W = 650
SIZE = (WIN_W, WIN_H)
win = pygame.display.set_mode(SIZE)
run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
p1score = 0
p2score = 0
myfont = pygame.font.SysFont('Comic Sans MS', 50)

class Paddle():
    HEIGHT = 80
    WIDTH = 15
    VELOCITY = 0.8
    def __init__(self, x, y):
        self.pos = [x, y]
        self.hitbox = (self.pos[1], self.pos[1], 16, 81)
    
    def draw_paddle(self):
        self.player = pygame.draw.rect(win, WHITE, (self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT))


    def move_paddle_up(self):
        if self.pos[1] >= 5:
            self.pos[1] -= self.VELOCITY

    def move_paddle_down(self):
        if self.pos[1] <= WIN_H - self.HEIGHT - 5:
            self.pos[1] += self.VELOCITY




class ball():
    RAD = 30
    VEL = [random.uniform(0.1, 0.4), random.uniform(0.1, 0.4)]

    def __init__(self, x, y):
        self.pos = [x, y]
    
    def draw_ball(self):
        self.ball = pygame.draw.ellipse(win, WHITE, (self.pos[0], self.pos[1], self.RAD, self.RAD))

    def move_ball(self):
        global ballx, bally
        self.pos[0] += self.VEL[0]
        self.pos[1] += self.VEL[1]


p1 = Paddle(WIN_W - 25, WIN_H / 2 - 40)
p2 = Paddle(25, WIN_H / 2 - 40)
Ball = ball(int(WIN_W / 2), int(WIN_H / 2))

def draw():
    Score1 = myfont.render(str(p1score), False, WHITE)
    Score2 = myfont.render(str(p2score), False, WHITE)
    win.blit(Score1, (200, 20))
    win.blit(Score2, (WIN_W /2 + 100, 20))
    Ball.draw_ball()
    p1.draw_paddle()
    p2.draw_paddle()

def reset():
    p1.pos = [WIN_W - 25, WIN_H / 2 - 40]
    p2.pos = [25, WIN_H / 2 - 40]
    Ball.pos = [int(WIN_W / 2), int(WIN_H / 2)]
    pygame.time.wait(1000)
    Ball.VEL = [random.uniform(0.1, 0.4), random.uniform(0.1, 0.4)]

while run:
    win.fill(BLACK)
    draw()
    if p1.player.colliderect(Ball.ball):
        Ball.VEL[0] = - Ball.VEL[0]
        Ball.VEL[0] *= 1.1
        Ball.VEL[1] *= 1.1


    if p2.player.colliderect(Ball.ball):
        Ball.VEL[0] = -Ball.VEL[0]
        Ball.VEL[0] *= 1.1
        Ball.VEL[1] *= 1.1

    if Ball.pos[1] + Ball.RAD >= WIN_H:
        Ball.VEL[1] = - Ball.VEL[1]

    if Ball.pos[1] <= 0:
        Ball.VEL[1] = - Ball.VEL[1]

    if Ball.pos[0] > p1.pos[0] + 5:
        reset()
        p1score += 1

    if Ball.pos[0] + Ball.RAD < p2.pos[0] - 5:
        reset()
        p2score += 1


    Ball.move_ball()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        p1.move_paddle_up()

    if keys[pygame.K_s]:
        p1.move_paddle_down()

    if p2.pos[1] < Ball.pos[1] - 10:
        p2.move_paddle_down()

    elif p2.pos[1] > Ball.pos[1] + 10:
        p2.move_paddle_up()



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





pygame.quit()
quit()
