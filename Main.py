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

print('Welcome to the Roulette')

# running process
running = True

# money & bets
bet = 0
money = 15000
temp_money = None
# bets

dealer_number = random.randrange(0, 1)
print(dealer_number)
bet_number = None


# win checking
def check_match():
    global bet_number, dealer_number, temp_money
    if bet_number == dealer_number:
        print(bet_number, dealer_number)
        temp_money = money + bet * 2

def money_operations():
    global bet, money, temp_money
    temp_money = money - bet
    check_match()

    print(temp_money)


money_operations()

confirm = False
# game process
while running:

    # Задержка выполнения цикла для уменьшения нагрузки на систему и стабильного FPS
    pygame.time.delay(6)

    # Важна иерархия слоёв отображения. Последний слой будет самым верхним

    # Заполняем бэкграунд цветом в RGB
    display1.fill((0, 80, 0))

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
                bet += 10
            if event.key == pygame.K_s:
                bet -= 10
            if event.key == pygame.K_SPACE:
                confirm = True

        # При ОТПУСКАНИИ клавиши происходит действие
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pass
    if confirm:
        check_match()
        money_operations()

    # display updating
    pygame.display.update()
