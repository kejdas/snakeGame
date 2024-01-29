from tkinter import *
import random

# Constants defining the game properties
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 2
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# Snake class to manage the snake's properties and behavior
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize snake coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 700])

        # Create snake squares on the canvas
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

# Food class to manage the food's properties and placement
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Create food square on the canvas
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

# Function to handle the next turn of the snake
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    # Update coordinates based on the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert the new head coordinates at the beginning
    snake.coordinates.insert(0, (x, y))

    # Create a new snake square at the new head position
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
    snake.squares.insert(0, square)

    # Delete the tail of the snake
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])

    # Call the next turn after a delay
    window.after(SPEED, next_turn, snake, food)

# Placeholder function for changing the direction of the snake
def change_direction():
    pass

# Placeholder function for checking collisions
def check_collisions():
    pass

# Placeholder function for handling game over
def game_over():
    pass

# Set up the Tkinter window
window = Tk()
window.title("Kejdi's Snake GAME")
window.resizable(False, False)

# Initialize game-related variables
score = 0
direction = "down"

# Create a label to display the score
label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

# Create a canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Update the window to get accurate width and height
window.update()

# Set window position on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create instances of Snake and Food classes
snake = Snake()
food = Food()

# Start the game by calling the next_turn function
next_turn(snake, food)

# Start the Tkinter main loop
window.mainloop()
