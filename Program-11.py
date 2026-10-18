import turtle
import math

screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.setup(width=800, height=700)

print("Choose Background Color:")
print("1. Black")
print("2. White")
print("3. Blue")

bg_choice = int(input("Enter choice: "))

if bg_choice == 1:
    screen.bgcolor("black")
elif bg_choice == 2:
    screen.bgcolor("white")
else:
    screen.bgcolor("blue")

pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)

pen.color("cyan" if bg_choice == 1 else "red")

def draw_spiral():
    for i in range(100):
        pen.forward(i * 2)
        pen.right(91)

def koch_curve(length, level):
    if level == 0:
        pen.forward(length)
    else:
        length /= 3
        koch_curve(length, level - 1)
        pen.left(60)
        koch_curve(length, level - 1)
        pen.right(120)
        koch_curve(length, level - 1)
        pen.left(60)
        koch_curve(length, level - 1)

def koch_snowflake(length, level):
    for _ in range(3):
        koch_curve(length, level)
        pen.right(120)

def draw_pattern():
    colors = ["red", "orange", "yellow", "green", "cyan", "magenta"]

    for i in range(36):
        pen.color(colors[i % len(colors)])
        for _ in range(4):
            pen.forward(100)
            pen.right(90)
        pen.right(10)

print("\nChoose Pattern:")
print("1. Geometric Spiral")
print("2. Koch Snowflake")
print("3. Colorful Geometric Pattern")

choice = int(input("Enter choice: "))

pen.penup()
pen.goto(-200, 100)
pen.pendown()

if choice == 1:
    draw_spiral()
elif choice == 2:
    pen.penup()
    pen.goto(-150, 100)
    pen.pendown()
    koch_snowflake(300, 3)
elif choice == 3:
    draw_pattern()
else:
    print("Invalid choice!")

pen.hideturtle()
screen.mainloop()