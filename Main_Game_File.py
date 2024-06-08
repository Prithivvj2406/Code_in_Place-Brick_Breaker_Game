import tkinter as tk
import random

# Constants
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_Y_OFFSET = 30
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 20
BRICK_COLORS = ["red", "orange", "yellow", "green", "cyan"]
# New Constants
BALL_SIZE = 20


# Milestone 1: Create the Start Screen
def create_tkinter_window():
    root = tk.Tk()  # Create the main application window
    root.title("Brick Breaker Game")  # Set the title of the window
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position the window

    # Add an instruction label to the center of the window
    instruction_label = tk.Label(root, text="CLICK ANYWHERE ON THE SCREEN TO START THE GAME", font=("Helvetica", 16))
    instruction_label.place(relx=0.5, rely=0.5, anchor="center")

    # Milestone 2: Add click event for closing the screen and opening the game window
    root.bind("<Button-1>", lambda event: root.destroy())

    # Run the Tkinter event loop
    root.mainloop()


# Milestone 3: Create the Game Window
def create_game_window():
    global game_canvas  # Declare canvas as a global variable
    root = tk.Tk()  # Create the main game window
    root.title("Brick Breaker Game")
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position window

    game_canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    game_canvas.pack()

    create_paddle(game_canvas)
    create_bricks(game_canvas)
    spawn_ball(game_canvas)

    # Run the Tkinter event loop for the game window
    root.mainloop()


# Milestone_4: Create the Paddle
def create_paddle(canvas_element):
    global paddle  # Declare paddle as a global variable
    paddle = canvas_element.create_rectangle(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT - PADDLE_Y_OFFSET,
                                             WIDTH / 2 + PADDLE_WIDTH / 2, HEIGHT - PADDLE_Y_OFFSET, fill='blue')


# Milestone_5 :  Create the multicolored Bricks
def create_bricks(canvas_element):
    global bricks
    bricks = []
    for i in range(BRICK_ROWS):
        for j in range(BRICK_COLS):
            x1 = j * BRICK_WIDTH
            y1 = i * BRICK_HEIGHT
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            color = BRICK_COLORS[i // (BRICK_ROWS // len(BRICK_COLORS))]

            # Create brick on canvas
            brick = canvas_element.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
            bricks.append((brick, color))  # Store brick and its color


# Milestone_6 : Create the ball
def spawn_ball(canvas_element):
    ball = canvas_element.create_oval(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2,
                                      WIDTH / 2 + BALL_SIZE / 2, HEIGHT / 2 + BALL_SIZE / 2,
                                      fill='red')  # Create the ball


# Main function to start the game setup
def main():
    create_tkinter_window()  # Milestone 1 & 2
    create_game_window()  # Milestone 3 to 6


# Entry point of the program
if __name__ == "__main__":
    main()
    