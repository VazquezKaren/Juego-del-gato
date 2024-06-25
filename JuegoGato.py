import turtle
import os

screen = turtle.Screen()
draw = turtle.Turtle()
screen.bgcolor("lightblue")
jugadas_o = []
jugadas_x = []
jugadas_ambos = ['', '', '', '', '', '', '', '', '']

posicion = []
terminar = False
reiniciar = True

def tituloPrincipal(texto, px, py, tam):
    draw.penup()
    draw.goto(px, py)
    draw.color("orange")
    draw.write(texto, align="center", font=("Baloo Bhaijaan", tam, "bold"))
    draw.pendown()

# Título
ventanaan = screen.window_width()
ventanaA = screen.window_height()
tituloPrincipal("TicTacToc", 0, ventanaA // 2 - 150, 100)

def tituloganaste(texto, px, py, tam):
    draw.penup()
    draw.goto(px, py)
    draw.color("red")
    draw.write(texto, align="center", font=("arial", tam, "bold"))
    draw.pendown()

def punto(px, py):
    draw.speed(100)
    draw.speed(60)
    draw.penup()
    draw.goto(px, py)  
    draw.color("blue")
    draw.pendown()
    draw.dot(8)

punto(-100, 100)
punto(0, 100)
punto(100, 100)
punto(-100, 0)
punto(0, 0)
punto(100, 0)
punto(-100, -100)
punto(0, -100)
punto(100, -100)

def cuadrado(px, py, cuadrados, tam):
    draw.penup()
    draw.goto(px, py)
    draw.color("green")
    draw.pendown()
    draw.speed(60)
    draw.pensize(6)

    for x in range(cuadrados):
        for y in range(4):
            draw.forward(tam)
            draw.right(90)
        draw.penup()
        draw.goto(px, py + (x + 1) * tam)
        draw.pendown()

cuadrado(50, -50, 3, 100)
cuadrado(-50, -50, 3, 100)
cuadrado(-150, -50, 3, 100)

def Circulo(px, py, radio=35):
    draw.penup()
    draw.goto(px, py - radio)  
    draw.color("blue")
    draw.pendown()
    draw.circle(radio)

def cruz(px, py, tam=25):
    draw.penup()
    draw.goto(px - tam, py + tam)  
    draw.pendown()
    draw.color("red")
    draw.goto(px + tam, py - tam)  
    draw.penup()
    draw.goto(px - tam, py - tam)  
    draw.pendown()
    draw.goto(px + tam, py + tam)  

def boton(px, py, tam, tam2):
    draw.penup()
    draw.goto(px, py)
    draw.color("black")
    draw.pendown()
    draw.speed(60)
    draw.pensize(6)
    
    for o in range(2):  
        draw.forward(tam)
        draw.right(90)
        draw.forward(tam2)
        draw.right(90)

boton(-250, -250, 150, 70)

turno = 0
contador_juegos = 1  

def guardar_jugadas(jugadas, juego_num):
    nombre_archivo = f'jugada{juego_num}.txt'
    while os.path.exists(nombre_archivo):
        juego_num += 1
        nombre_archivo = f'jugada{juego_num}.txt'
    with open(nombre_archivo, 'w') as file:
        file.write(str(jugadas))

def click(x, y):
    global turno, terminar, contador_juegos
    if terminar:
        return
    for index, (px, py) in enumerate(positions):
        if abs(x - px) < 20 and abs(y - py) < 20:
            if jugadas_ambos[index] != '':
                print("Este cuadro ya está ocupado")
                return
            if turno < 9:
                if turno % 2 == 0:
                    Circulo(px, py)
                    jugadas_o.append((px, py))
                    jugadas_ambos[index] = 'o'
                    print('Jugada de jugador O:', jugadas_o)
                    print("Posiciones ocupadas:", jugadas_ambos)
                    
                    ganador, combinacion = verificar(jugadas_o)
                    if ganador:
                        print('¡Círculo Gana!')
                        tituloganaste("¡Círculo Gana!", 0, screen.window_height() // 2 - 600, 50)
                        terminar = True
                        guardar_jugadas(jugadas_ambos, contador_juegos)
                        contador_juegos += 1
                        print("¿Desea reiniciar el juego?")
                        return
                else:
                    cruz(px, py)
                    jugadas_x.append((px, py))
                    jugadas_ambos[index] = 'x'
                    print('Jugada de jugador X:', jugadas_x)
                    print("Posiciones ocupadas:", jugadas_ambos)
                    
                    ganador, combinacion = verificar(jugadas_x)
                    if ganador:
                        print("¡X Gana!")
                        tituloganaste("¡X Gana!", 0, screen.window_height() // 2 - 600, 50)
                        terminar = True
                        guardar_jugadas(jugadas_ambos, contador_juegos)
                        contador_juegos += 1
                        return
                
                turno += 1
                return

positions = [
    (-100, 100), (0, 100), (100, 100),
    (-100, 0), (0, 0), (100, 0),
    (-100, -100), (0, -100), (100, -100)
]

jugadas_ganadoras = [
    [(-100, 100), (0, 100), (100, 100)],
    [(-100, 0), (0, 0), (100, 0)],
    [(-100, -100), (0, -100), (100, -100)],
    [(-100, 100), (-100, 0), (-100, -100)],
    [(0, 100), (0, 0), (0, -100)],
    [(100, 100), (100, 0), (100, -100)],
    [(-100, 100), (0, 0), (100, -100)],
    [(100, 100), (0, 0), (-100, -100)]
]

def verificar(jugadas):
    for combinacion in jugadas_ganadoras:
        if all(pos in jugadas for pos in combinacion):
            return True, combinacion
    return False, []

screen.onclick(click)
turtle.done()
