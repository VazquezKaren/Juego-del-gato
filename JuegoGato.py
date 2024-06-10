import turtle 
import sys

screen = turtle.Screen()
draw = turtle.Turtle()
screen.bgcolor("lightblue")
jugadas_o = []
jugadas_x = []
jugadas_ambos = ['', '', '', '', '', '', '', '', '']

posicion = []
terminar = False
reiniciar = True

def maintitulo(texto, px, py, tam):
    draw.penup()
    draw.goto(px, py)
    draw.color("orange")
    draw.write(texto, align="center", font=("Baloo Bhaijaan", tam, "bold"))
    draw.pendown()

# título
ventanaan = screen.window_width()
ventanaA = screen.window_height()
maintitulo("TicTacToc", 0, ventanaA // 2 - 150, 100)

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

def click(x, y):
    global turno, terminar
    if terminar:
        return
    for index, (px, py) in enumerate(positions):
        if abs(x - px) < 20 and abs(y - py) < 20:
            if jugadas_ambos[index] != '':
                print("Este cuadro ya está ocupado")
                return
            while turno < 9:
                if turno % 2 == 0:
                    Circulo(px, py)
                    jugadas_o.append((px, py))
                    jugadas_ambos[index] = 'o'
                    posicion.append((px, py))
                    print('jugada de jugador O:', jugadas_o)
                    print("posiciones ocupadas", jugadas_ambos)
                    
                    if verificar(jugadas_o):
                        print('¡Circulo Gana!')
                        tituloganaste("¡Circulo Gana!", 0, screen.window_height() // 2 - 600, 50)
                        terminar = True
                        print("¿Desea reiniciar el juego?")
                        return
                else:
                    cruz(px, py)
                    jugadas_x.append((px, py))
                    jugadas_ambos[index] = 'x'
                    posicion.append((px, py))

                    print('jugada de jugador X:', jugadas_x)
                    print("posiciones ocupadas", jugadas_ambos)
                    
                    if verificar(jugadas_x):
                        print("¡X Gana!")
                        tituloganaste("¡X Gana!", 0, screen.window_height() // 2 - 600, 50)
                        terminar = True
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
            return True
    return False

def no_duplicados(ambos):
    for i in positions:
        if all(linea in ambos for linea in i):
            return True
    return False

screen.onclick(click)
turtle.done()

