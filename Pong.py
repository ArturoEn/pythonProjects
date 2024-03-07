import pygame
import random

pygame.init()

# colores
black = (0, 0, 0)
white = (255, 255, 255)

# jugador 1
player_width = 10
player_height = 90
player_1 = 20
mov_1 = 0
coo_1 = 250
# jugador 2
player_2 = 770
mov_2 = 0
coo_2 = 250

timer = 200 #indica los fps deljuego

# pelota
ball_x = 395
ball_y = 250

# la pelota sale solo en diagonal
while True:
    rand_x = random.randint(-1, 1)
    rand_y = random.randint(-1, 1)
    if rand_x != 0 and rand_y != 0:
        break

# tamaño ventana
size = (800, 600)

screen = pygame.display.set_mode(size)
arial = pygame.font.SysFont("arial", 20)
puntos1 = 0
puntos2 = 0
score = arial.render(str(puntos1), True, white)
clock = pygame.time.Clock()

dificultad = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # jugador 1 teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mov_1 += 2
            if event.key == pygame.K_w:
                mov_1 += -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                mov_1 = 0
            if event.key == pygame.K_w:
                mov_1 = 0

        # jugador 2 teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                mov_2 += 2
            if event.key == pygame.K_o:
                mov_2 += -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                mov_2 = 0
            if event.key == pygame.K_o:
                mov_2 = 0

    # fondo pantalla
    screen.fill(black)

    # movimiento jugador 1
    coo_1 += mov_1
    # movimiento jugador 2
    coo_2 += mov_2

    # movimiento de la pelota
    ball_x += rand_x
    ball_y += rand_y

    # dificultad
    if dificultad == 3:
        if ball_x <= 300:
            rand_x += 1
        if ball_x >= 600:
            rand_x -= 1
        dificultad = 0

    # rebotes de la pelota
    if ball_x >= 795:
        rand_x *= -1
        # incremento de puntos jugador 1
        puntos1 += 1
        # restaurar velocidad
        rand_x = 1
        ball_x = 395
        ball_y = 250

        while True:
            rand_x = random.randint(-1, 1)
            rand_y = random.randint(-1, 1)
            if rand_x != 0 and rand_y != 0:
                break

    if ball_y >= 595:
        rand_y *= -1
    if ball_x <= 0:
        rand_x *= -1
        # incremento de puntos jugador 2
        puntos2 += 1
        # restaurar velocidad
        rand_x = 1
        ball_x = 395
        ball_y = 250

        while True:
            rand_x = random.randint(-1, 1)
            rand_y = random.randint(-1, 1)
            if rand_x != 0 and rand_y != 0:
                break

    if ball_y <= 0:
        rand_y *= -1


    # colision jugdor 1
    if ball_x >= 30 + rand_x:
        if ball_y >= coo_1 and ball_y <= coo_1 + 90 and ball_x <= 30:
            rand_x *= -1
            # incremento de velocidad
            dificultad += 1
    # colicion jugador 2
    if ball_x <=770 + rand_x:
        if ball_y >= coo_2 and ball_y <= coo_2 + 90 and ball_x >= 770:
            rand_x *= -1
            # incremento de velocidad
            dificultad += 1
    # perder
    #if ball_x <= 0:
        #game_over = True


    # dibujo jugador1
    pygame.draw.rect(screen, white, (player_1, coo_1, player_width, player_height))
    # dibujo jugador2
    pygame.draw.rect(screen, white, (player_2, coo_2, player_width, player_height))

    # dibujar pelota
    pygame.draw.circle(screen, white, (ball_x, ball_y), 5)

    # pantalla puntuacion jugador 1
    score = arial.render(str(puntos1), True, white)
    screen.blit(score, (199, 10))

    # pantalla puntuacion jugador 2
    score = arial.render(str(puntos2), True, white)
    screen.blit(score, (599, 10))


    # limites jugador 1
    if coo_1 <= 0:
        coo_1 = 0
    if coo_1 >= 510:
        coo_1 = 510
    # limites jugador 2
    if coo_2 <= 0:
        coo_2 = 0
    if coo_2 >= 510:
        coo_2 = 510

    pygame.display.flip()
    clock.tick(timer)
pygame.quit()