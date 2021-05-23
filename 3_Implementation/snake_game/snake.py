import pygame
import random
import tkinter as tk
from tkinter import messagebox
import time


class Cube(object):
    rows = 20   # Must be divisible by w
    w = 500

    def __init__(self, start, dir_x=1, dir_y=0, color=(255, 0, 0)):
        self.pos = start
        self.dir_x = 1
        self.dir_y = 0
        self.color = color

    def move(self, dir_x, dir_y):  # Tested
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)
        return self.pos[0]  # Unit Testing

    def draw(self, surface, eyes=False):  # Tested
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circle_middle = (i * dis + centre - radius, j * dis + 8)
            circle_middle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)

        return 0


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):

        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1

    def move(self):  # Manual Testing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dir_x = -1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_RIGHT]:
                    self.dir_x = 1
                    self.dir_y = 0
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_UP]:
                    self.dir_x = 0
                    self.dir_y = -1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

                elif keys[pygame.K_DOWN]:
                    self.dir_x = 0
                    self.dir_y = 1
                    self.turns[self.head.pos[:]] = [self.dir_x, self.dir_y]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    print("Popping")
                    self.turns.pop(p)
            else:
                if c.dir_x == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dir_x == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dir_y == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dir_y == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dir_x, c.dir_y)

    def reset(self, pos):  # Tested
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
        return 0

    def add_cube(self):  # Tested
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy
        return 0

    def draw(self, surface):    # Tested
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
        return 0


def draw_grid(w, rows, surface):  # Tested

    size_btwn = w // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

    return 0


def redraw_window(surface):     # Tested

    global r, width, snake, snack

    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, r, surface)
    pygame.display.update()
    return 0


def random_snack(rows, item, test_flag):    # Tested

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    if test_flag == 1:
        return 0
    else:
        return x, y


def message_box(subject, content):  # Tested
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.after(2, lambda: root.quit())
    # try:
    #     root.quit()
    #
    # except:
    #
    #     pass
    return


def run(test_flag):     # Tested

    testing_flag = test_flag

    print("In main")
    global r, width, snake, snack
    r = 20
    width = 500
    height = 500
    windows = pygame.display.set_mode((width, height))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(r, snake, 0), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()
    print("Here_1")
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        ret = snake.move()
        if ret == 0:
            break
        if snake.body[0].pos == snack.pos:
            snake.add_cube()
            snack = Cube(random_snack(r, snake, 0), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if len(snake.body) > 399:
                if testing_flag == 0:
                    message_box("You Won", "Play Again...")
                return 0
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print("Score is: ", len(snake.body))
                if testing_flag == 0:
                    message_box("You Lost!", "Play again...")
                    snake.reset((10, 10))
                    break
                return 0

        redraw_window(windows)

    return 0

