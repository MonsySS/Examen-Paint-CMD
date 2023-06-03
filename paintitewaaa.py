import pygame

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255, 23, 100)
surface.fill(background_color)

# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
color = (255, 120, 10)

colores_disponibles = {
    'blanco': (255, 255, 255),
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'negro': (0, 0, 0)
}

color_predeterminado = colores_disponibles["blanco"]
linea_grosor = 2
shapes = []

# Cambio de color de fondo
def help():
    print("comandos: color_lineas, color_fondo, pixeles, tam_pix, linea, cuadrado, rectangulo, circulo, borrar, equilatero, escaleno, isoceles.")
    pygame.display.flip()

def color_fondo(color):
    if color in colores_disponibles:
        background_color = colores_disponibles[color]
        surface.fill(background_color)
        pygame.display.flip()
    else:
        print("Color no válido.")

def color_lineas(colorsite):
    global color
    if colorsite == "blanco":
        color = (255, 255, 255)
    elif colorsite == "rojo":
        color = (255, 0, 0)
    elif colorsite == "verde":
        color = (0, 255, 0)
    elif colorsite == "azul":
        color = (0, 0, 255)
    elif colorsite == "negro":
        color = (0, 0, 0)
    else:
        print("El color no se encuentra disponible en la gama de colores")
    pygame.display.flip()

def grosor_lineas(pix_tam):
    global linea_grosor
    linea_grosor = max(1, pix_tam)
    pygame.display.flip()

def draw_linea(surface, color, linea_grosor, x, y):
    start_pos = (x, y)
    end_pos = (x + 100, y + 100)  # Example end position
    pygame.draw.line(surface, color, start_pos, end_pos, linea_grosor)
    shapes.append(('linea', x, y))
    pygame.display.flip()

def draw_cuadrado(x, y, lado):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, lado, lado))
    shapes.append(('cuadrado', x, y, lado))
    pygame.display.flip()

def draw_rectangulo(x, y, ancho, alto):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, ancho, alto))
    shapes.append(('rectangulo', x, y, ancho, alto))
    pygame.display.flip()

def draw_circulo(x, y, radius):
    pygame.draw.circle(surface, color, (x, y), radius)
    shapes.append(('circulo', x, y, radius))
    pygame.display.flip()

def borrar_ultimo_trazo():
    if shapes:
        last_shape = shapes.pop()
        if last_shape[0] == 'linea':
            pygame.draw.line(surface, background_color, last_shape[1], last_shape[2], linea_grosor)
        elif last_shape[0] == 'cuadrado':
            pygame.draw.rect(surface, background_color, pygame.Rect(last_shape[1], last_shape[2], last_shape[3], last_shape[3]))
        elif last_shape[0] == 'rectangulo':
            pygame.draw.rect(surface, background_color, pygame.Rect(last_shape[1], last_shape[2], last_shape[3], last_shape[4]))
        pygame.display.flip()

class triangulites:
    @staticmethod
    def equilatero(surface, color, linea_grosor, x, y, size):
        x1 = x
        y1 = y - size // 2
        x2 = x - size // 2
        y2 = y + size // 2
        x3 = x + size // 2
        y3 = y + size // 2
        pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], linea_grosor)
        pygame.display.flip()

    @staticmethod
    def escaleno(x1, y1, x2, y2, x3, y3):
        l1 = (x1, y1)
        l2 = (x2, y2)
        l3 = (x3, y3)
        pygame.draw.polygon(surface, color, [l1, l2, l3], linea_grosor)
        pygame.display.flip()

    @staticmethod
    def isoceles(x1, y1, x2, y2, x3, y3):
        l1 = (x1, y1)
        l2 = (x2, y2)
        l3 = (x3, y3)
        pygame.draw.polygon(surface, color, [l1, l2, l3], linea_grosor)
        pygame.display.flip()


while True:
    cmd = input("cmd> ")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if cmd == "help":
        help()
    elif cmd == "color_lineas":
        print("Colores disponibles para las lineas: blanco, rojo, verde, azul, negro")
        colorsite = input("Ingrese el color que deseas utilizar en las lineas: ")
        color_lineas(colorsite)
    elif cmd == "color_fondo":
        print("Colores disponibles para el fondo: blanco, rojo, verde, azul, negro")
        colorsite1 = input("Ingrese el color de fondo que deseas utilizar: ")
        color_fondo(colorsite1)
    elif cmd == "pixeles":
        grosor = int(input("Ingrese el grosor que quiere utilizar para las lineas: "))
        grosor_lineas(grosor)
    elif cmd == "tam_pix":
        print("Ingrese el tamaño de pixeles por linea: ")
        pix_tam = int(input("Ingrese el grosor de las lineas: "))
        grosor_lineas(pix_tam)
    elif cmd == "linea":
        x = int(input("Ingrese la coordenada x de su linea: "))
        y = int(input("Ingrese la coordenada y de su linea: "))
        draw_linea(surface, color, linea_grosor, x, y)
    elif cmd == "cuadrado":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        lado = int(input("Ingrese el lado: "))
        draw_cuadrado(x, y, lado)
    elif cmd == "rectangulo":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        ancho = int(input("Ingrese el ancho: "))
        alto = int(input("Ingrese el alto: "))
        draw_rectangulo(x, y, ancho, alto)
    elif cmd == "circulo":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        radius = int(input("Ingrese el radio: "))
        draw_circulo(x, y, radius)
    elif cmd == "borrarT":
        borrar_ultimo_trazo()
    elif cmd == "equilatero":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        size = int(input("Ingrese el tamaño: "))
        triangulites.equilatero(surface, color, linea_grosor, x, y, size)
    elif cmd == "escaleno":
        x1 = int(input("Ingrese la coordenada x1: "))
        y1 = int(input("Ingrese la coordenada y1: "))
        x2 = int(input("Ingrese la coordenada x2: "))
        y2 = int(input("Ingrese la coordenada y2: "))
        x3 = int(input("Ingrese la coordenada x3: "))
        y3 = int(input("Ingrese la coordenada y3: "))
        triangulites.escaleno(x1, y1, x2, y2, x3, y3)
    elif cmd == "isoceles":
        x1 = int(input("Ingrese la coordenada x1: "))
        y1 = int(input("Ingrese la coordenada y1: "))
        x2 = int(input("Ingrese la coordenada x2: "))
        y2 = int(input("Ingrese la coordenada y2: "))
        x3 = int(input("Ingrese la coordenada x3: "))
        y3 = int(input("Ingrese la coordenada y3: "))
        triangulites.isoceles(x1, y1, x2, y2, x3, y3)