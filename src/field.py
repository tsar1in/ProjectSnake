import src.config as con
import pygame as pg


class Field:
    def __init__(self, square_size, width, height):
        self.square_size = square_size
        self.width = width
        self.height = height

    def Draw(self, i, j, dis, color):
        pg.draw.rect(dis, color, [(2 + i) * self.square_size,
                                  (2 + j) * self.square_size,
                                  self.square_size, self.square_size])

    def PrintField(self, dis):
        dis.fill(con.brown)
        for i in range((self.width - 4 * self.square_size) // self.square_size):
            for j in range((self.height - 4 * self.square_size) // self.square_size):
                if (i + j) % 2 == 0:
                    self.Draw(i, j, dis, con.white)
                else:
                    self.Draw(i, j, dis, con.grey)