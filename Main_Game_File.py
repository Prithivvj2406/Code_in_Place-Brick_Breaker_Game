import tkinter as tk

# Constants
WIDTH = 800
HEIGHT = 600
# New Constants
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_Y_OFFSET = 30

# Milestone 1
# Function to create the initial Tkinter window
def create_tkinter_window():
    root = tk.Tk()  # Create the main application window
    root.title("Breakout Game")  # Set the title of the window
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position the window

    # Add an instruction label to the center of the window
    instruction_label = tk.Label(root, text="CLICK ANYWHERE ON THE SCREEN TO START THE GAME", font=("Helvetica", 16))
    instruction_label.place(relx=0.5, rely=0.5, anchor="center")

    # Milestone 2: Add click event for closing the screen and opening the game window
    root.bind("<Button-1>", lambda event: root.destroy())

    # Run the Tkinter event loop
    root.mainloop()

# Milestone_3
def create_game_window():
    global canvas  # Declare canvas as a global variable
    root = tk.Tk()  # Create the main game window
    root.title("Breakout Game")
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position window

    # Create the Canvas Variable
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    canvas.pack()

    # Run the Tkinter event loop for the game window
    root.mainloop()

# Main function to start the game setup
def main():
    create_tkinter_window()  # Milestone 1 & 2
    create_game_window() # Milestone 3

# Entry point of the program
if __name__ == "__main__":
    main()