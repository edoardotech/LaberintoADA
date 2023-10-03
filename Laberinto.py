import turtle

usuario = "jaimedoardo"
contraseña = "1438"

while usuario == str(input("Ingrese su usuario: ")):
    if contraseña == str(input("Ingrese su contraseña: ")):
        print("Bienvenido jaimedoardo")
            
    else:
        print("Error de contraseña")
        
break
        
print("Error de usuario")

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Laberinto ADA")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.direction = "stop"
        
niveles =[]

nivel_1 = [
    "  XXXXXXXXXXXXXXXXXXXXXXX",
    "  P  X                  X",
    "X X XXXXX XXXXXXXXXXXXX X",
    "X X               X X X X",
    "X XXXXX X XXX X X X X X X",
    "X   X X X XX        X   X",
    "X X X XXXXXXXXXXX X XXXXX",
    "X X   XX       XX X   X X",
    "XXXXX XXXXX X X  XXXXX  X",
    "X X X X         XX   XX X",
    "X X X XXXXXXXX  XXXXXXX X",
    "X   X   X   X  XX  XX   X",
    "XXX X XXXXX X X  X XXXX X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

niveles.append(nivel_1)

def iniciar_lab(nivel):
    for file in range(len(nivel)):
        for column in range(len(nivel[file])):
            
            letra_x = nivel[file][column]
            screen_x = -288 + (column * 23)
            screen_y = 288 - (file * 23)
            
            if letra_x == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
            if letra_x == "P":
                player.goto(screen_x, screen_y)
      

            
pen = Pen()
player = Player()

iniciar_lab(niveles[0])

