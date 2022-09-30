import time
import pygame
import random
pygame.init()# инициализирует все модули pygame
white = (255,255,255) #цветовые переменные
yellow=(255,255,102)
black = (0,0,0)
red = (213,50,80)
green=(0,255,0)
blue=(50,153,213)
dis_width=600#переменные для размера экрана
dis_height=400#
dis = pygame.display.set_mode((dis_width,dis_height))# создания экрана
pygame.display.set_caption('Snake')# заголовок в рамке
clock=pygame.time.Clock()#отслеживание времени
snake_block=10#размер змейки
snake_speed=15#скорость змейки

front_style=pygame.font.SysFont('bahnschrift',25)# задает шрифт
score_font= pygame.font.SysFont('comicsansms',35)# задает шрифт

def You_score(score):# счет игрока= длине змейки -1(исходный размер)
    value=score_font.render('Your Score:'+str(score),True, yellow)#
    dis.blit(value,[0,0])

def our_snake(snake_block,snake_list):# метод рисования змейки
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])#функция для
        # рисования прямоугольника-змейки

def message(msg,color):# функция для вывода сообщений
    mesg=front_style.render(msg,True, color)
    dis.blit(mesg,[dis_width/6, dis_height/3])

def gameLoop():# функция для игры
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1=dis_height/2

    x2=0#переменные для сохранения изменений при движении змейки
    y2=0
    snake_List=[]#список для хранения длины змейки
    Length_of_snake=1#

    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0# место на экране
    # где будет еда для змейки на  за минусом самой змейки
    foody=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0#

    while not game_over:#цикл для того чтобы экран не пропадал
        while game_close==True:
            dis.fill(white)# меняем цвет экрана на белый
            message("You lost! Press Q-quit or C-Play again",red)#сообщение при проигрыше
            pygame.display.update()#обновляет экран, принимает изменения

            for event in pygame.event.get():#отображаетвсе действия игры
                if event.type == pygame.KEYDOWN:#
                    if event.key == pygame.K_q:#если игрок выбрал Q, то выход
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:#если игрок выбрал C, то заново играем
                        gameLoop()#

        for event in pygame.event.get():# выводит список всех событий
            if event.type==pygame.QUIT:#условие для закрытия окна игры
                game_over=True
            if event.type==pygame.KEYDOWN:# движение змейки из класса KEYDOWN
              if event.key==pygame.K_LEFT:
                x2=-snake_block#сдвинулась по горизонтали назад на размер змейки
                y2=0
              elif  event.key==pygame.K_RIGHT:
                x2=snake_block
                y2=0
              elif event.key == pygame.K_UP:
                y2 = -snake_block
                x2 = 0
              elif event.key == pygame.K_DOWN:
                y2 = snake_block
                x2 = 0
        if x1 >=dis_width or x1 <0 or y1>=dis_height or y1<0:#проверяет не ушла ли
            # змейка за границы экрана
           game_close=True
        x1+=x2#новое положение змейки
        y1+=y2
        dis.fill(blue)# меняем экран на голубой
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])# рисуем
        # прямоугольник с переданными параметрами
        snake_Head=[]#еда змейки
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)# добавляем к длине змейки, то что съела
        if len(snake_List)> Length_of_snake:#проверяем не столкнулась ли змейка со своим хвостом
            del  snake_List[0]
        for x in snake_List[:-1]:
            if x==snake_Head:# элемент, который пересекла змейка ее последний элемент, то проигрыш
                game_close=True
        our_snake(snake_block,snake_List)#
        You_score(Length_of_snake-1)#

        pygame.display.update()# обновляет экран, принимает изменения
        if x1==foodx and y1==foody:#если змейка пересекла прямоугольник едой,
            # то увеличиваем змейку
           foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0#
           foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0#
           Length_of_snake+=1# увеличиваем длину змейки
        clock.tick(snake_speed)#

    pygame.quit()# закрытие всех модулей
    quit()
gameLoop()

