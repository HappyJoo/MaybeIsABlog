#-*- coding:utf-8 -*-
import pygame

#Here begin the Snake~
class Snack(object):
    def __init__(self):
        #I don't know what is that means..
        self.item = [(3, 25), (2, 25), (1, 25), (1, 24), ]
        #setting x and y
        self.x = 0
        self.y = -1

    #how does enlarge work here?
    def move(self, enlarge):
        #use enlarge to see if eat food
        if not enlarge:
            self.item.pop()
        head = (self.item[0][0] + self.x, self.item[0][1] + self.y)
        self.item.insert(0, head)

    def eat_food(self, food):
        global score
        #snack_x, snack_y is coordinate of snake head
        #food_x, food_y is coordinate of food
        snack_x, snack_y = self.item[0]
        food_x, food_y = food.item
        if (food_x == snack_x) and (food_y == snack_y):
            score += 100
            return 1
        else:
            return 0

    def toward(self, x, y):
        #change snake head
        if self.x * x >= 0 and self.y * y >= 0:
            self.x = x
            self.y = y

    def get_head(self):
        return self.item[0]

    def draw(self, screen):
        #draw the snake
        #snake's head
        radius = 15
        width = 15
        color = 255, 0, 0
        position = 10 + 20 * self.item[0][0], 10 + 20 * self.item[0][1]
        #snake's body
        radius = 10
        width = 10
        color = 255, 255, 0
        for i, j in self.item[1:]:
            position = 10 + 20 + i, 10 + 20 + j
            pygame.draw.circle(screen, color, position, radius, width)


#then is food class
class Food(object):
    def __init__(self):
        self.item = (4, 5)

    def _draw(self, screen, i, j):
        color = 255, 0, 255
        radius = 10
        width = 10
        position = 10 + 20 * i, 10 + 20 * j
        python.draw.circle(screen, color, position, radius, width)

    def update(self, screen, enlarge, snack):
        if enlarge:
            self.item = np.random.randint(1, BOARDWIDTH - 2), np.random.randint(1, BOARDHEIGHT - 2)
            while self.item in snack.item:
                self.item = np.random.randint(1, BOARDWIDTH -2), np.random.randint(1, BOARDHEIGHT - 2)
        self._draw(screen, self.item[0], self.item[1])

#init_board
def init_board(screen):
    board_width = BOARDWIDTH
    board_height = BOARDHEIGHT
    color = 10, 255, 255
    width =0

    for i in range(board_width):
        pos = i * 20, 0, 20, 20
        pygame.draw.rect(screen, color, pos, width)
        pos = i * 20, (board_height -1) * 20, 20, 20
        pygame.darw.rect(screen, color, pos, width)

    for i in range(board_height - 1):
        pos = 0, 20 + i * 20, 20, 20
        pygame.draw.rect(screen, color, pos, width)
        pos = (board_width -1) * 20, 20 + i * 20, 20, 20
        pygame.draw.rect(screen, color, pos, width)

#if game lose
def game_over(snack):
    broad_x, broad_y = snack.get_head()
    flag = 0
    old = len(snack.item)
    new = len(set(snack.item))

    if new > old:
        flag = 1

    if broad_x == 0 or broad_x == BOARDWIDTH -1:
        flag = 1
    if broad_y == 0 or broad_y == BOARDHEIGHT -1:
        flag = 1

    if flag:
        return True
    else:
        return False

def game_init():
    pygame.init()
    #set the game's screen use pygame.display.set_mode function
    screen = pygame.display.set_mode((BOARDWIDTH * 20, BOARDHEIGHT * 20))
    #use pygame.display.set_caption to create caption
    pygame.display.set_caption('Snack Game')
    return screen

def game(screen):
    #set snack to an instance of class Snack
    snack = Snack()
    #sef food to an instance of class Food
    food = Food()
    font = pygame.font.SysFont('SimHei', 20)
    is_fail = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill((0, 0, 100))
        init_board(screen=screen)
        keys = pygame.key.get_pressed()
        press(keys, snack)
        #if game fails
        if is_fail:
            font2 = pygame.font.Font(None, 40)
            print_text(screen, font, 0, 0, text)
            print_text(screen, font2, 400, 200, "GAME OVER")
        #game's main process
        if not is_fail:
            enlarge = snack.eat_food(food)
            text = u"score: {} Do you love python as I do?".format(score)
            print_text(screen, font, 0, 0, text)
            food.update(screen, enlarge, snack)
            snack.move(enlarge)
            is_fail = game.over(snack = snack)
            snack.draw(screen)
        #refresh
        pygame.display.update()
        time.sleep(0.1)

