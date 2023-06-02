import pygame

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255,23,100)
surface.fill(background_color)

# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
color = (255,120, 10)

colores_disponibles={
    'blanco': (255, 255, 255),
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'negro': (0, 0, 0)
}

color_predeterminado = colores_disponibles["blanco"]
linea_grosor = 2
shapes=[]

#cambio de color fondo
def help (): 
    print("comandos: color_lineas, color_fondo, pixeles, tam_pix, linea, cuadrado, rectangulo, circulo, borrar, equilatero, escaleno, isoseles.")

def color_fondo (colorsite1): 
    global colores_disponibles
    if colorsite1 == "blanco": 
        background_color = (255, 255, 255)
    elif colorsite1 == "rojo":
        background_color =  (255, 0, 0)
    elif colorsite1 == "verde":
        background_color = (0, 255, 0)
    elif colorsite1 == "azul":
        background_color = (0, 0, 255)
    elif colorsite1 == "negro":
        background_color = (0, 0, 0)
    else: 
        print("El color no se encuentra disponible en la gama de colores")

def color_lineas (colorsite): 
    global colores_disponibles
    if colorsite == "blanco": 
        background_color = (255, 255, 255)
    elif colorsite == "rojo":
        background_color =  (255, 0, 0)
    elif colorsite == "verde":
        background_color = (0, 255, 0)
    elif colorsite == "azul":
        background_color = (0, 0, 255)
    elif colorsite == "negro":
        background_color = (0, 0, 0)
    else: 
        print("El color no se encuentra disponible en la gama de colores")

def grosor_lineas(pix_tam):
    global pixel_tamaño
    pixel_tamaño = max(10, pix_tam)

def draw_linea(x, y):
    pygame.draw.line(surface, color, x, y, linea_grosor)
    shapes.append(('linea', x, y))

def draw_cuadrado(x, y, lado):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, lado, lado))
    shapes.append(('cuadrado', x, y, lado))

def draw_rectangulo(x, y, ancho, alto):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, ancho, alto))
    shapes.append(('rectangulo', x, y, ancho, alto))

def draw_circulo(x, y, radius):
    pygame.draw.circle(surface, color, (x, y), radius)
    shapes.append(('circulo', x, y, radius))

def borrar_ultimo_trazo():
    if shapes:
        last_shape = shapes.pop()
        if last_shape[0] == 'linea':
            pygame.draw.line(surface, background_color, last_shape[1], last_shape[2], linea_grosor)
        elif last_shape[0] == 'cuadrado':
            pygame.draw.rect(surface, background_color, pygame.Rect(last_shape[1], last_shape[2], last_shape[3], last_shape[3]))
        elif last_shape[0] == 'rectangulo':
            pygame.draw.rect(surface, background_color, pygame.Rect(last_shape[1]))

class triangulites: 
    def equilatero (x1, x2, y1, y2, size): 
        y1 = y - size // 2
        x2 = x - size // 2
        y2 = y + size // 2
        x3 = x + size // 2
        y3 = y + size // 2
        pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], linea_grosor)

    def escaleno(x1,y1,x2,y2,x3,y3):
        l1 = (x1, y2)
        l2 = (x2, y2)
        l3 = (x3, y3)
        pygame.draw.polygon(surface, color, [l1, l2, l3], linea_grosor)

    def isoceles(x1,y1,x2,y2,x3,y3):
        l1 = (x1, y2)
        l2 = (x2, y2)
        l3 = (x3, y3)
        pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], linea_grosor)

 
while True:
    cmd= input("cmd> ")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
        if cmd == "help":
            help()
        if cmd == "color_lineas":
            print("Colores disponible para las lineas: blanco, rojo, verde, azul, negro")
            colorsite = input("ingresa el color que deseas utilizar en las lineas:")
            color_lineas (colorsite)
        
        elif cmd == "color_fondo":
            print("Colores disponibles para el fondo: Blanco, Rojo, Verde, Azul, Negro: ")
            colorsite1=int(input("Ingrese el color de"))
            color_fondo (colorsite1)

        elif cmd == "pixeles":
            grosor = int(input("Ingrese el grosor que quiere utilizar para las lineas: "))
            grosor_pixel = linea_grosor
        else:
            print("seleccione un numero")

        if cmd== "tam_pix":
            print("escriba el tamaño de pixeles por linea: ")
            pix_tam = int(input("Ingrese el grosor de las lineas: "))
            grosor_lineas(pix_tam)
        
        if cmd == "linea": 
            x= int(input("Ingrese la coordenada x de su linea: "))
            y= int(input("Ingrese la coordenada y de su linea: "))
            draw_linea(x, y)

        if cmd == "cuadrado": 
            x= int(input("Ingrese la coordenada x: "))
            y= int(input("Ingrese la coordenada y: "))
            lado= int(input("Ingrese el lado: "))        
            draw_cuadrado(x, y, lado)
        
        if cmd == "rectangulo": 
            x= int(input("Ingrese la coordenada x: "))
            y= int(input("Ingrese la coordenada y: "))
            ancho= int(input("Ingrese el alto: "))
            alto= int(input("Ingrese el ancho: "))
            draw_rectangulo(x, y, ancho, alto)
        
        if cmd=="circulo": 
            x= int(input("Ingrese la coordenada x: "))
            y= int(input("Ingrese la coordenada y: "))
            radius= int(input("Ingrese el radio: "))     
            draw_circulo(x, y, radius)
        
        if cmd == "borrarT":
            last_shape=  int(input("Que linea quieres borrar: "))
            borrar_ultimo_trazo()

        if cmd == "equilatero": 
            x1=  int(input("Ingrese la coordenada x1: "))
            x2 =  int(input("Ingrese la coordenada x2: "))
            y1 = int(input("Ingrese la coordenada y1: "))
            y2 = int(input("Ingrese la coordenada y2: "))
            size = int(input("Ingrese size: "))
            triangulites.equilatero (x1, x2, y1, y2, size)

        if cmd == "escaleno": 
            x1=  int(input("Ingrese la coordenada x1: "))
            x2 =  int(input("Ingrese la coordenada x2: "))
            x3 =  int(input("Ingrese la coordenada x3: "))
            y1 = int(input("Ingrese la coordenada y1: "))
            y2 = int(input("Ingrese la coordenada y2: "))
            y3 = int(input("Ingrese la coordenada y3: "))
            triangulites.escaleno(x1,y1,x2,y2,x3,y3)

        if cmd == "isoceles": 
            x1=  int(input("Ingrese la coordenada x1: "))
            x2 =  int(input("Ingrese la coordenada x2: "))
            x3 =  int(input("Ingrese la coordenada x3: "))
            y1 = int(input("Ingrese la coordenada y1: "))
            y2 = int(input("Ingrese la coordenada y2: "))
            y3 = int(input("Ingrese la coordenada y3: "))       
            triangulites.isoceles(x1,y1,x2,y2,x3,y3)
