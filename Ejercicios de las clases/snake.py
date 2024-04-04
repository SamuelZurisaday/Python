import pygame
import time
import random

pygame.init()

# Colores
negro = (0, 0, 0)
verde = (0, 255, 0)
rojo = (213, 50, 80)

# Dimensiones de la pantalla
ancho, alto = 600, 400

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente')

clock = pygame.time.Clock()

# Tamaño de la serpiente y velocidad del juego
tamano_serpiente = 10
velocidad = 15

# Definir la fuente para el texto
fuente = pygame.font.SysFont("bahnschrift", 25)

def nuestra_serpiente(tamano_serpiente, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamano_serpiente, tamano_serpiente])

def mensaje(msg, color):
    mesg = fuente.render(msg, True, color)
    pantalla.blit(mesg, [ancho / 6, alto / 3])

def juego():
    juego_cerrado = False
    juego_terminado = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamano_serpiente) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamano_serpiente) / 10.0) * 10.0

    while not juego_cerrado:

        while juego_terminado == True:
            pantalla.fill(negro)
            mensaje("¡Has perdido! Presiona Q-Salir o C-Jugar de nuevo", rojo)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        juego_cerrado = True
                        juego_terminado = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_cerrado = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamano_serpiente
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamano_serpiente
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamano_serpiente
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamano_serpiente
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            juego_terminado = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tamano_serpiente, tamano_serpiente])
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                juego_terminado = True

        nuestra_serpiente(tamano_serpiente, lista_serpiente)
        pygame.display.update()