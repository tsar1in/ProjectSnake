import pygame as pg
import numpy as np


class Bonus:
    def __init__(self, square_size, width, height):
        self.square_size = square_size
        self.width = width
        self.height = height
        self.GetBonus()
        self.LoadImage()

    def GetBonus(self):
        self.x_bonus = round(np.random.randint(2 * self.square_size,
                                               self.width - 3 * self.square_size) // self.square_size) * self.square_size
        self.y_bonus = round(np.random.randint(2 * self.square_size,
                                               self.height - 3 * self.square_size) // self.square_size) * self.square_size

    def LoadImage(self):
        self.image = pg.image.load('Graph/watch.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.square_size, self.square_size))

    def PrintBonus(self, dis):
        dis.blit(self.image, (self.x_bonus, self.y_bonus))