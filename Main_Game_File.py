import tkinter as tk

# Constants
WIDTH = 800
HEIGHT = 600

# MILESTONE_1
# Function to create the initial Tkinter Game window
def create_tkinter_window():
    root = tk.Tk()  # Create the main application window
    root.title("Breakout Game")  # Set the title of the window
    root.geometry(f"{WIDTH}x{HEIGHT}")  # Position the window

    # Add an instruction label to the center of the window
    instruction_label = tk.Label(root, text="Game Startup Screen", font=("Helvetica", 16))
    instruction_label.place(relx=0.5, rely=0.5, anchor="center")

    # Run the Tkinter event loop
    root.mainloop()

# Main function to start the game setup
def main():
    create_tkinter_window()  # MILESTONE 1

# Entry point of the program
if __name__ == "__main__":
    main()