import turtle

# Mengatur kecepatan gambar objek turtle
turtle.speed('fastest')

# Mendefinisikan fungsi untuk menggambar pola bunga
def draw_flower(size, angle):
    for i in range(0, 360, angle):
        turtle.color('magenta')
        turtle.circle(size)
        turtle.color('orange')
        turtle.circle(size / 2)
        turtle.left(angle)

# Menggambar pola bunga pada koordinat (0, 0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
draw_flower(100, 5)

# Menggambar pola bunga pada koordinat (200, 0)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
draw_flower(100, 10)

# Menggambar pola bunga pada koordinat (0, -200)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
draw_flower(100, 15)

# Menggambar pola bunga pada koordinat (200, -200)
turtle.penup()
turtle.goto(200, -200)
turtle.pendown()
draw_flower(100, 20)

# Menutup window
turtle.done()
