import pygame as pg


class Snake:
    def __init__(self, square_size, width, height):
        self.square_size = square_size
        self.x = ((width / 2) // self.square_size) * self.square_size
        self.y = ((height / 2) // self.square_size) * self.square_size
        self.delta_x = 0
        self.delta_y = 0
        self.snake_list = []
        self.snake_size = 1
        self.snake_speed = 10
        self.snake_color = "blue"
        self.where = ""

    def LoadImage(self):
        color = self.snake_color
        self.head_up = pg.image.load(f'Graph/head_down_{color}.png')
        self.head_down = pg.image.load(f'Graph/head_up_{color}.png')
        self.head_left = pg.image.load(f'Graph/head_left_{color}.png')
        self.head_right = pg.image.load(f'Graph/head_right_{color}.png')
        self.tail_up = pg.image.load(f'Graph/tail_down_{color}.png')
        self.tail_down = pg.image.load(f'Graph/tail_up_{color}.png')
        self.tail_left = pg.image.load(f'Graph/tail_left_{color}.png')
        self.tail_right = pg.image.load(f'Graph/tail_right_{color}.png')
        self.body_horizontal = pg.image.load(f'Graph/body_horizontal_{color}.png')
        self.body_vertical = pg.image.load(f'Graph/body_vertical_{color}.png')
        self.body_tr = pg.image.load(f'Graph/body_tr_{color}.png')
        self.body_tl = pg.image.load(f'Graph/body_tl_{color}.png')
        self.body_br = pg.image.load(f'Graph/body_br_{color}.png')
        self.body_bl = pg.image.load(f'Graph/body_bl_{color}.png')

    def TransformImage(self):
        size = (self.square_size, self.square_size)
        self.head_right = pg.transform.scale(self.head_right, size)
        self.head_down = pg.transform.scale(self.head_down, size)
        self.head_up = pg.transform.scale(self.head_up, size)
        self.head_left = pg.transform.scale(self.head_left, size)
        self.tail_down = pg.transform.scale(self.tail_down, size)
        self.tail_up = pg.transform.scale(self.tail_up, size)
        self.tail_left = pg.transform.scale(self.tail_left, size)
        self.tail_right = pg.transform.scale(self.tail_right, size)
        self.body_horizontal = pg.transform.scale(self.body_horizontal, size)
        self.body_vertical = pg.transform.scale(self.body_vertical, size)
        self.body_br = pg.transform.scale(self.body_br, size)
        self.body_bl = pg.transform.scale(self.body_bl, size)
        self.body_tr = pg.transform.scale(self.body_tr, size)
        self.body_tl = pg.transform.scale(self.body_tl, size)

    def PrintHead(self, i, dis):
        if self.where == 'down':
            dis.blit(self.head_down, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.where == 'up':
            dis.blit(self.head_up, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.where == 'left':
            dis.blit(self.head_left, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.where == 'right':
            dis.blit(self.head_right, (self.snake_list[i][0], self.snake_list[i][1]))

    def PrintTail(self, i, dis):
        if self.snake_list[i + 1][1] == self.snake_list[i][1] + self.square_size:
            dis.blit(self.tail_down, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.snake_list[i + 1][1] == self.snake_list[i][1] - self.square_size:
            dis.blit(self.tail_up, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.snake_list[i + 1][0] == self.snake_list[i][0] + self.square_size:
            dis.blit(self.tail_left, (self.snake_list[i][0], self.snake_list[i][1]))
        if self.snake_list[i + 1][0] == self.snake_list[i][0] - self.square_size:
            dis.blit(self.tail_right, (self.snake_list[i][0], self.snake_list[i][1]))

    def PrintBody(self, i, dis):
        if (self.snake_list[i + 1][1] == self.snake_list[i][1] and self.snake_list[i - 1][1] == self.snake_list[i][1] or
                self.snake_list[i - 1][1] == self.snake_list[i][1] and self.snake_list[i + 1][1] == self.snake_list[i][1]):
            dis.blit(self.body_horizontal, (self.snake_list[i][0], self.snake_list[i][1]))
        if (self.snake_list[i + 1][0] == self.snake_list[i][0] and self.snake_list[i - 1][0] == self.snake_list[i][0] or
                self.snake_list[i - 1][0] == self.snake_list[i][0] and self.snake_list[i + 1][0] == self.snake_list[i][0]):
            dis.blit(self.body_vertical, (self.snake_list[i][0], self.snake_list[i][1]))
        if (self.snake_list[i + 1][1] == self.snake_list[i][1] + self.square_size and self.snake_list[i - 1][0] == self.snake_list[i][0] + self.square_size or
                self.snake_list[i - 1][1] == self.snake_list[i][1] + self.square_size and self.snake_list[i + 1][0] == self.snake_list[i][0] + self.square_size):
            dis.blit(self.body_br, (self.snake_list[i][0], self.snake_list[i][1]))
        if (self.snake_list[i + 1][1] == self.snake_list[i][1] + self.square_size and self.snake_list[i - 1][0] == self.snake_list[i][0] - self.square_size or
                self.snake_list[i - 1][1] == self.snake_list[i][1] + self.square_size and self.snake_list[i + 1][0] == self.snake_list[i][0] - self.square_size):
            dis.blit(self.body_bl, (self.snake_list[i][0], self.snake_list[i][1]))
        if (self.snake_list[i + 1][1] == self.snake_list[i][1] - self.square_size and self.snake_list[i - 1][0] == self.snake_list[i][0] + self.square_size or
                self.snake_list[i - 1][1] == self.snake_list[i][1] - self.square_size and self.snake_list[i + 1][0] == self.snake_list[i][0] + self.square_size):
            dis.blit(self.body_tr, (self.snake_list[i][0], self.snake_list[i][1]))
        if (self.snake_list[i + 1][1] == self.snake_list[i][1] - self.square_size and self.snake_list[i - 1][0] == self.snake_list[i][0] - self.square_size or
                self.snake_list[i - 1][1] == self.snake_list[i][1] - self.square_size and self.snake_list[i + 1][0] == self.snake_list[i][0] - self.square_size):
            dis.blit(self.body_tl, (self.snake_list[i][0], self.snake_list[i][1]))

    def PrintSnake(self, dis):
        self.LoadImage()
        self.TransformImage()
        dis.blit(self.head_right, (self.snake_list[-1][0], self.snake_list[-1][1]))
        for i in range(len(self.snake_list)):
            if i == len(self.snake_list) - 1:  # Отрисовка положения головы змейки
                self.PrintHead(i, dis)
            elif i == 0:  # Отрисовка положения хвоста змейки
                self.PrintTail(i, dis)
            else:  # Положение угловых(поворотных) элементов змейки
                self.PrintBody(i, dis)
