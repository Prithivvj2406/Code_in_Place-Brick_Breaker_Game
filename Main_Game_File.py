import tkinter as tk

# Constants
WIDTH = 800
HEIGHT = 600


# MILESTONE_1
# Function to create the initial Tkinter window
def create_tkinter_window():
    root = tk.Tk()  # Create the main application window
    root.title("Breakout Game")  # Set the title of the window
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position the window

    # Add an instruction label to the center of the window
    instruction_label = tk.Label(root, text="CLICK ANYWHERE ON THE SCREEN TO START THE GAME", font=("Helvetica", 16))
    instruction_label.place(relx=0.5, rely=0.5, anchor="center")

    # MILESTONE_2
    # Add click for closing the screen
    root.bind("<Button-1>", lambda event: root.destroy())

    # Run the Tkinter event loop
    root.mainloop()


# Main function to start the game setup
def main():
    create_tkinter_window()  # MILESTONE 1 & 2


# Entry point of the program
if __name__ == "__main__":
    main()
