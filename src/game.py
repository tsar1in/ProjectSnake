import pygame as pg
import pygame_menu
import numpy as np
import src.config as con
import src.bonus as bon
import src.snake_c as sn
import src.food as fo
import src.field as fi


class Game:
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 600
        self.dis = pg.display.set_mode((self.width, self.height))
        self.game_over = True
        self.game_close = False
        self.square_size = 30
        self.name = ''
        self.flag = False
        self.str_dict = {}
        self.food = fo.Food(self.square_size, self.width, self.height)
        self.bonus = bon.Bonus(self.square_size, self.width, self.height)
        self.snake = sn.Snake(self.square_size, self.width, self.height)
        self.field = fi.Field(self.square_size, self.width, self.height)
        pg.display.set_caption('Snake')
        pg.display.update()

    def message1(self):
        mes1 = pg.font.SysFont('times new roman', 40).render(f"YOU LOST, Your score {self.snake.snake_size - 1}", True, con.red)
        mes2 = pg.font.SysFont('times new roman', 40).render(f"Press any button", True, con.grey)
        self.dis.blit(mes1, [(self.width - mes1.get_width()) / 2, (self.height - mes1.get_height()) / 2])
        self.dis.blit(mes2, [(self.width - mes2.get_width()) / 2, (self.height - mes1.get_height() + 2 * mes2.get_height()) / 2])

    def message(self, str, color, size=20):
        mesg = pg.font.SysFont('times new roman', size).render(str, True, color)
        self.dis.blit(mesg, [0, 0])

    def Directions(self, event):
        if event.key == pg.K_UP and self.snake.where != "up":
            self.snake.delta_x = 0
            self.snake.delta_y = -self.square_size
            self.snake.where = "down"
        if event.key == pg.K_DOWN and self.snake.where != "down":
            self.snake.delta_x = 0
            self.snake.delta_y = self.square_size
            self.snake.where = "up"
        if event.key == pg.K_LEFT and self.snake.where != "right":
            self.snake.delta_x = -self.square_size
            self.snake.delta_y = 0
            self.snake.where = "left"
        if event.key == pg.K_RIGHT and self.snake.where != "left":
            self.snake.delta_x = self.square_size
            self.snake.delta_y = 0
            self.snake.where = "right"

    def set_diff(self, value, dif):
        if value[0][1] == 1:
            self.snake.snake_speed = 11
        if value[0][1] == 2:
            self.snake.snake_speed = 8
        if value[0][1] == 3:
            self.snake.snake_speed = 5

    def set_color(self, value, dif):
        if value[0][1] == 1:
            self.snake.snake_color = "blue"
        if value[0][1] == 2:
            self.snake.snake_color = "red"
        if value[0][1] == 3:
            self.snake.snake_color = "brown"

    def read_table_record(self):
        with open('Table/table.txt') as f:
            while True:
                s = f.readline()
                if s == '':
                    break
                else:
                    str_arr = s.split()
                    self.str_dict[str_arr[0]] = int(str_arr[1])

    def table_records(self):
        self.read_table_record()
        sorted_str = dict(sorted(self.str_dict.items(), key=lambda it: -it[1]))
        self.dis.fill(con.field)
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    self.__init__()
                    self.Start()
            x = self.width
            ms = pg.font.SysFont('times new roman', 60).render('Table of records', True, con.text_col)
            ms2 = pg.font.SysFont('times new roman', 40).render(f"Press any button", True, con.black)
            self.dis.blit(ms, [(x - ms.get_width()) / 2, 0])
            self.dis.blit(ms2, [(x - ms2.get_width()) / 2, self.height - ms2.get_height()])
            y = 0 + ms.get_height()
            count = 0
            for item in sorted_str.items():
                if count == 5:
                    break
                ms = pg.font.SysFont('times new roman', 40).render(item[0], True, con.text_col)
                ch = pg.font.SysFont('times new roman', 40).render(str(item[1]), True, con.text_col)
                y += 2 * ms.get_height()
                self.dis.blit(ms, [(x - 360) / 2, y / 2])
                self.dis.blit(ch, [(x + 300) / 2, y / 2])
                count += 1
            pg.display.update()

    def GetName(self, name):
        self.name = name

    def Start(self):
        menu = pygame_menu.Menu('Snake', self.width, self.height, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.text_input('Name:', default='Pavel', onchange=self.GetName)
        menu.add.selector('Difficulty :', [('Hard', 1), ('Middle', 2), ('Easy', 3)], onchange=self.set_diff)
        menu.add.selector('Snake color :', [('Blue', 1), ('Red', 2), ('Brown', 3)], onchange=self.set_color)
        menu.add.button('Table of records', self.table_records)
        menu.add.button('Play', self.Event)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        image = pg.image.load('Graph/snake.jpeg').convert_alpha()
        image = pg.transform.scale(image, (self.square_size, self.square_size))
        self.dis.blit(image, (0, 0))
        pg.display.update()
        menu.mainloop(self.dis)

    def GameClose(self):
        self.dis.fill(con.white)
        self.message1()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if self.name == '':
                    self.name = 'Pavel'
                with open('Table/table.txt') as f:
                    data = f.read()
                with open('Table/table.txt', 'w') as w:
                    w.write(data + self.name)
                    w.write(f' {self.snake.snake_size - 1}\n')
                self.__init__()
                self.Start()

    def TakeFood(self):
        if self.snake.x == self.food.x_food and self.snake.y == self.food.y_food:
            self.food.GetFood()
            if np.random.randint(0, 4) == 3:
                self.bonus.GetBonus()
                self.flag = True
            else:
                self.flag = False
            self.snake.snake_size += 1
            self.snake.snake_speed += 0.2

    def TakeBonus(self):
        if self.snake.x == self.bonus.x_bonus and self.snake.y == self.bonus.y_bonus:
            self.snake.snake_speed = max(6, self.snake.snake_speed - 0.8)
            self.flag = False

    def Intersection(self):
        for i in self.snake.snake_list[:-1]:
            if i[0] == self.snake.x and i[1] == self.snake.y:
                self.game_close = True

    def BeyondBorders(self):
        if self.snake.x > self.width - 3 * self.square_size or self.snake.x < 2 * self.square_size \
                or self.snake.y >= self.height - 2 * self.square_size or self.snake.y < 2 * self.square_size:
            self.game_close = True

    def Event(self):
        clock = pg.time.Clock()
        while self.game_over:
            while self.game_close:
                self.GameClose()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                if event.type == pg.KEYDOWN:
                    self.Directions(event)
            self.snake.x += self.snake.delta_x
            self.snake.y += self.snake.delta_y
            self.field.PrintField(self.dis)
            self.food.PrintFood(self.dis)
            if self.flag:
                self.bonus.PrintBonus(self.dis)
            self.snake.snake_list.append([self.snake.x, self.snake.y])
            if len(self.snake.snake_list) > self.snake.snake_size:
                del self.snake.snake_list[0]
            self.BeyondBorders()
            self.Intersection()
            self.snake.PrintSnake(self.dis)
            self.message(f'Your score {self.snake.snake_size - 1}', con.white, 30)
            pg.display.update()
            self.TakeFood()
            self.TakeBonus()
            clock.tick(self.snake.snake_speed)
        pg.quit()
        quit()
