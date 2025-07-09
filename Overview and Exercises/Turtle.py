import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Turtle Art")
screen.bgcolor("black")  # Dark background for better visibility

# Constants
num_turtles = 12  # Using more turtles for interesting patterns
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan',
          'lime', 'magenta', 'white', 'gold']

# Create turtles with random starting positions
turtles = []
for i in range(num_turtles):
    t = turtle.Turtle()
    t.speed(100)
    t.penup()
    # Random starting position within screen bounds
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.color(colors[i])
    t.pensize(2)
    t.pendown()
    # Random starting angle
    t.setheading(random.randint(0, 360))
    turtles.append(t)


# Function to make random movements
def random_move(t):
    # Random curve angle between -30 and 30 degrees
    t.right(random.randint(-30, 30))
    # Random forward movement
    t.forward(random.randint(5, 20))
    # Random pen size changes
    if random.random() < 0.1:  # 10% chance to change pen size
        t.pensize(random.randint(1, 4))


# Main animation loop
for _ in range(10000):  # Number of movements
    for t in turtles:
        # Random chance to lift pen
        if random.random() < 0.1:  # 10% chance to lift pen
            t.penup()
        elif t.isdown() == False:
            t.pendown()

        random_move(t)

        # Bounce off screen edges
        x, y = t.pos()
        if abs(x) > 300 or abs(y) > 300:
            t.setheading(t.heading() + 180)  # Turn around

        # Random color changes
        if random.random() < 0.05:  # 5% chance to change color
            t.color(random.choice(colors))

# Hide turtles at the end
for t in turtles:
    t.hideturtle()

# Keep the window open
screen.mainloop()