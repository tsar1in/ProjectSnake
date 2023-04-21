import pygame as pg
import numpy as np


class Food:
    def __init__(self, square_size, width, height):
        self.square_size = square_size
        self.width = width
        self.height = height
        self.GetFood()
        self.LoadImage()

    def GetFood(self):
        self.x_food = round(np.random.randint(2 * self.square_size,
                                              self.width - 3 * self.square_size) // self.square_size) * self.square_size
        self.y_food = round(np.random.randint(2 * self.square_size,
                                              self.height - 3 * self.square_size) // self.square_size) * self.square_size

    def LoadImage(self):
        self.image = pg.image.load('Graph/apple.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.square_size, self.square_size))

    def PrintFood(self, dis):
        dis.blit(self.image, (self.x_food, self.y_food))