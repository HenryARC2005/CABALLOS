import pygame


# Configuración de pantalla

ANCHO, ALTO = 1280, 720
FPS = 60

pygame.init()
screen=pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Carrera de Caballos')


#Assets

fondo_carrera = pygame.image.load("sprites/background.png").convert()
fondo_carrera = pygame.transform.scale_by(fondo_carrera, (2))
caballo_sprite = pygame.image.load("sprites/player.png").convert_alpha()


# Colores

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)


# Fuente global para textos

pygame.init()
FUENTE = pygame.font.Font(None, 36)


#Meta

META = ANCHO-80
