# Импорт нужных модулей
import pygame
import random

# initializing the game
pygame.init()  # Инициализация игры (момент её создания)

# creating the start screen
display1 = pygame.display.set_mode((1280, 720))  # Установка разрешения экрана

# Title and Icon
pygame.display.set_caption("Roulette")  # Смена названия игры
icon = pygame.image.load('roulette.png')  # Присвоение файла иконки
pygame.display.set_icon(icon)  # Смена иконки игры

# running process
running = True

# money & bets
bet = 0
money = 15000
temp_money = None

# bets
dealer_number = random.randrange(0, 37)  # рандомит число, которое выпадет на рулетке *сменить на (0, 37)
print(dealer_number)
bet_number = None


# Проверка выиграша
confirm = False
def check_match():
    global bet_number, dealer_number, temp_money, confirm
    if bet_number == dealer_number:
        print(bet_number, dealer_number)
        temp_money = money + bet * 2
        confirm = False

    else:
        confirm = False

# Операции с деньгами во время ставок и выиграша
def money_operations():
    global bet, money
    money = money - bet
    check_match()


# Функция рендера текста
def print_text(var, x, y, font_color, custom_font, font_type, font_size):
    if custom_font:
        font = pygame.font.Font(font_type, font_size)
    else:
        font = pygame.font.SysFont(font_type, font_size)

    text = font.render(var, True, font_color)  # параметр True отвечает за сглаживание текста
    display1.blit(text, (x, y))


# game process
while running:

    #Ограничения переменных
    if money <= 0:
        money = 0
    if bet <= 0:
        bet = 0

    # Задержка выполнения цикла для уменьшения нагрузки на систему и стабильного FPS
    pygame.time.delay(6)

    # Важна иерархия слоёв отображения. Последний слой будет самым верхним
    # Заполняем бэкграунд цветом в RGB
    display1.fill((0, 80, 0))

    # Вывод текста. print_text(переменка типа str, x-позиция, y-позиция, (цвет в RGB),кастомный шрифт (True\False),
    # 'название шрифта', размер шрифта)
    print_text(('Your money: ' + str(money)), 1050, 15, (255, 255, 255), True, 'Fulbo Argenta.otf', 22)
    print_text(('Your bet: ' + str(bet)), 1050, 50, (255, 255, 255), True, 'Fulbo Argenta.otf', 22)
    print_text(('dealer: ' + str(dealer_number)), 10, 50, (255, 255, 255), True, 'Facon Bold Italic.otf', 22)
    print_text('♥  ♦ ', 587, 20, (155, 0, 0), False, 'Arial', 40)
    print_text('♠  ♣', 610, 20, (0, 0, 0), False, 'Arial', 40)


    # Цикл, отвечающий за отклик кнопок. for позволяет ограничить пропускную способность сигнала с кнопки,
    # в то время, как while спамит значениями в большом количестве
    for event in pygame.event.get():
        # Даёт возможность закрывать программу на "крестик"
        if event.type == pygame.QUIT:
            running = False

        # При НАЖАТИИ клавиши происходит действие
        if event.type == pygame.KEYDOWN:
            # Конкретная клавиша указывается как показано ниже ---> K_*, где * любая кнопка из предложенных клавиш
            if event.key == pygame.K_w:
                bet += 50

            if event.key == pygame.K_s:
                bet -= 50

            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass

            if event.key == pygame.K_SPACE:
                confirm = True

                if confirm:
                    check_match()
                    money_operations()

        # При ОТПУСКАНИИ клавиши происходит действие
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pass

    # display updating
    pygame.display.update()
