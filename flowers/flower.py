import turtle

# Membuat fungsi untuk menggambar pola lingkaran kecil
def small_circle(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Membuat fungsi untuk menggambar pola lingkaran besar
def big_circle(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

# Membuat objek Turtle
t = turtle.Turtle()

# Mengatur kecepatan objek Turtle
t.speed(0)

# Menggambar bunga dengan 6 kelopak
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    t.penup()
    t.goto(0,0)
    t.pendown()
    big_circle(colors[i])
    t.penup()
    t.goto(0, 60)
    t.pendown()
    small_circle("white")
    t.right(60)

# Menggambar tangkai bunga
t.penup()
t.goto(0, -70)
t.pendown()
t.pensize(5)
t.right(90)
t.forward(100)

# Menghentikan Turtle Graphics
turtle.done()
