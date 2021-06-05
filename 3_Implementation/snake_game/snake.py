import tkinter as tk
from tkinter import messagebox
import random
import pygame


class Cube:
    """
    This class forms objects for snake body
    and snack
    """

    rows = 20   # Must be divisible by w
    w = 500

    def __init__(self, start, dir_x=1, dir_y=0, color=(255, 0, 0)):
        """
        This is parameterized constructor
        :param start: tuple
        :param dir_x: int
        :param dir_y: int
        :param color: tuple
        """
        self.pos = start
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.color = color

    def move(self, dir_x, dir_y):
        """
        This function is responsible for snack and snake movement
        :param dir_x: int
        :param dir_y: int
        :return: int
        """
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)
        return self.pos[0]  # Unit Testing

    def draw(self, surface, eyes=False):
        """
        This function is responsible for generating GUI
        :param surface: GUI element
        :param eyes: bool
        :return: int
        """
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


class Snake:
    """
    This class used Cube class to create snake object
    """
    body = []
    turns = {}

    def __init__(self, color, pos):
        """
        Constructor
        :param color tuple
        :param pos: tuple
        """
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1

    def __del__(self):
        """
        Destructor
        :return: None
        """
        SNAKE.reset((10, 10))

    def move(self):  # Manual Testing
        """
        This function is responsible to move the snake object
        :return: int
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

            keys = pygame.key.get_pressed()

            for _ in keys:
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

        for i, cube in enumerate(self.body):
            position = cube.pos[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(position)
            else:
                if cube.dir_x == -1 and cube.pos[0] <= 0:
                    cube.pos = (cube.rows - 1, cube.pos[1])
                elif cube.dir_x == 1 and cube.pos[0] >= cube.rows - 1:
                    cube.pos = (0, cube.pos[1])
                elif cube.dir_y == 1 and cube.pos[1] >= cube.rows - 1:
                    cube.pos = (cube.pos[0], 0)
                elif cube.dir_y == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], cube.rows - 1)
                else:
                    cube.move(cube.dir_x, cube.dir_y)

    def reset(self, pos):  # Tested
        """
        Resets the game frame on start up
        :param pos: tuple
        :return: int
        """
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
        return 0

    def add_cube(self):  # Tested
        """
        Adds a new cube object everytime it snake overlaps snack
        :return: int
        """
        tail = self.body[-1]
        direction_x, direction_y = tail.dir_x, tail.dir_y

        if direction_x == 1 and direction_y == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif direction_x == -1 and direction_y == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif direction_x == 0 and direction_y == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif direction_x == 0 and direction_y == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dir_x = direction_x
        self.body[-1].dir_y = direction_y
        return 0

    def draw(self, surface):    # Tested
        """
        Draws GUI surface
        :param surface: Gui element
        :return:
        """
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)
        return 0


def draw_grid(width, rows, surface):  # Tested
    """
    Draws grids
    :param width: int
    :param rows: int
    :param surface: GUI elements
    :return:
    """
    size_between = width // rows

    position_x = 0
    position_y = 0
    for _ in range(rows):
        position_x = position_x + size_between
        position_y = position_y + size_between

        pygame.draw.line(surface, (255, 255, 255), (position_x, 0), (position_x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, position_y), (width, position_y))

    return 0


def redraw_window(surface):     # Tested
    """
    Resets game window after restart
    :param surface: GUI element
    :return: int
    """
    surface.fill((0, 0, 0))
    SNAKE.draw(surface)
    SNACK.draw(surface)
    draw_grid(WIDTH, R, surface)
    pygame.display.update()
    return 0


def random_snack(rows, item, test_flag):    # Tested
    """
    Generates Snack at random grid
    :param rows: int
    :param item: int
    :param test_flag: int
    :return: tuple
    """
    positions = item.body

    while True:
        position_x = random.randrange(rows)
        position_y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (position_x, position_y), positions))) > 0:
            continue
        break
    if test_flag == 1:
        return 0
    return position_x, position_y


def message_box(subject, content, test_flag):  # Tested
    """
    Generates window on loss or win
    :param subject: String
    :param content: String
    :param test_flag: int
    :return: int
    """
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    if test_flag == 1:
        return 0
    messagebox.showinfo(subject, content)
    root.after(2, lambda: root.quit())

    # try:
    #     root.quit()
    # except:
    #     pass
    return 0


def run(test_flag):     # Tested
    """
    Responsible to execute the feature
    :param test_flag: int
    :return: int
    """
    pygame.init()
    testing_flag = test_flag
    global R, WIDTH, SNAKE, SNACK
    R = 20
    WIDTH = 500
    height = 500
    windows = pygame.display.set_mode((WIDTH, height))

    SNAKE = Snake((255, 0, 0), (10, 10))

    SNACK = Cube(random_snack(R, SNAKE, 0), color=(0, 255, 0))
    flag = True

    if test_flag == 1:
        for _ in range(400):
            # snake.body.append(Cube((20, 20)))
            SNAKE.add_cube()

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        ret = SNAKE.move()
        if ret == 0:
            break
        if SNAKE.body[0].pos == SNACK.pos:
            SNAKE.add_cube()
            SNACK = Cube(random_snack(R, SNAKE, 0), color=(0, 255, 0))

        for i in range(len(SNAKE.body)):
            if len(SNAKE.body) > 399:
                if testing_flag == 0:
                    message_box("You Won", "Play Again...", 0)
                return 0
            if SNAKE.body[i].pos in list(map(lambda z: z.pos, SNAKE.body[i + 1:])):
                print("Score is: ", len(SNAKE.body))
                if testing_flag == 0:
                    message_box("You Lost!", "Play again...", 0)
                    SNAKE.reset((10, 10))
                    break
                return 0

        redraw_window(windows)

    return 0
