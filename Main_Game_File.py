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
BALL_SPEED = 4
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
    root = tk.Tk()  # Create the main game window
    root.title("Brick Breaker Game")
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position window

    global game_canvas  # Declare canvas as a global variable
    game_canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    game_canvas.pack()

    create_paddle(game_canvas)
    create_bricks(game_canvas)
    spawn_ball(game_canvas)
    move_paddle(game_canvas)

    ball_dynamics(game_canvas, root)

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
    global ball, change_x, change_y
    change_x = random.choice([-BALL_SPEED, BALL_SPEED])
    change_y = BALL_SPEED
    ball = canvas_element.create_oval(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2,
                                      WIDTH / 2 + BALL_SIZE / 2, HEIGHT / 2 + BALL_SIZE / 2,
                                      fill='red')  # Create the ball


# Milestone_7: Move the Paddle
def move_paddle(canvas_element):
    def on_mouse_move(event):
        paddle_x = event.x  # Get the x-coordinate of the mouse pointer
        if paddle_x < PADDLE_WIDTH / 2:
            paddle_x = PADDLE_WIDTH / 2
        elif paddle_x > WIDTH - PADDLE_WIDTH / 2:
            paddle_x = WIDTH - PADDLE_WIDTH / 2
        canvas_element.coords(paddle, paddle_x - PADDLE_WIDTH / 2, HEIGHT - PADDLE_HEIGHT - PADDLE_Y_OFFSET,
                              paddle_x + PADDLE_WIDTH / 2, HEIGHT - PADDLE_Y_OFFSET)

    # Bind the mouse movement event to the canvas
    canvas_element.bind("<Motion>", on_mouse_move)


# Milestone_8: Ball Movement Dynamics
def ball_dynamics(canvas_element, root):
    global change_x, change_y
    canvas_element.move(ball, change_x, change_y)
    ball_pos = canvas_element.coords(ball)

    # Collision detection and handling
    if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
        change_x = -change_x
    if ball_pos[1] <= 0:
        change_y = -change_y
    if ball_pos[3] >= HEIGHT:
        canvas_element.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", font=('Helvetica', 30), fill='red')
        return

    move_paddle(canvas_element)

    detect_paddle_collision(canvas_element)

    detect_brick_collision(bricks, canvas_element)

    root.after(20, ball_dynamics, canvas_element, root)


# Milestone_9: Detection Collisions with Paddle
def detect_paddle_collision(canvas_element):
    ball_pos = canvas_element.coords(ball)
    global change_y
    if canvas_element.find_overlapping(*ball_pos):
        for obj in canvas_element.find_overlapping(*ball_pos):
            if obj == paddle:
                change_y = -change_y


# Milestone_10_1: Detection Collisions with Bricks
def detect_brick_collision(bricks, canvas_element):
    global change_y
    ball_pos = canvas_element.coords(ball)
    for brick, color in bricks:
        if canvas_element.find_overlapping(*ball_pos) and brick in canvas_element.find_overlapping(*ball_pos):
            change_y = -change_y
            return


# Main function to start the game setup
def main():
    create_tkinter_window()  # Milestone 1 & 2
    create_game_window()  # Milestone 3 to 10.1


# Entry point of the program
if __name__ == "__main__":
    main()
    