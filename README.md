# Code_in_Place-Brick_Breaker_Game

This repository is for my Stanford Code in Place course project.

## Overview

I have decided to create a simplified version of the Brick Breaker game, which was popular in the late 90s. The project utilizes Tkinter instead of the canvas since it wasn't available for me to use. The coding was done in the PyCharm IDE. I have set several milestones initially to complete the project in an orderly and organized fashion.

## Milestones

### Milestone 1: Game Window Creation

The first milestone was to create the game window itself. I decided to include a startup screen for the game after the file is run. I created a canvas window with a size of 800x600, displaying the message "Game Startup Screen". Below is an example of how it would look:

![Milestone_1](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/9f7f1e20-b149-44d8-a45a-f9dfd3e5d832)

### Milestone 2: Implementing Mouse Click Functionality

In Milestone 2, I added the functionality to initiate the game upon a mouse click. This prevents the game from starting immediately upon running the file, allowing players/users to prepare. The message displayed in the game window now prompts the player/user to click anywhere on the screen to start the game.

![Milestone_2](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/9eaae645-e4f6-498b-928a-0b61265622da)

### Milestone 3: Creating the Main Game Window

To simulate the start of the game after clicking, I closed the previous game window and created a completely new game window to house the game.

### Milestone 4: Adding a Paddle to the Game

To fulfill the game's requirement of having a paddle, I introduced a blue rectangular block at the bottom with the following dimensions:
- Paddle Width: 100
- Paddle Height: 10
- Paddle Y Offset: 30

Below is an illustration of the paddle in the game:

![Milestone_4](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/0ad5e803-856c-4c4b-a7b8-685e7c7930bd)

### Milestone 5: Adding Multi-Colored Bricks to the Game Window

For Milestone 5, I incorporated the essential feature of bricks into the game. I created a function that adds multiple rows of bricks of different colors. The configuration for the bricks is as follows:
- Number of Brick Rows: 5
- Number of Brick Columns: 10
- Brick Width: Width of the game window divided by the number of brick columns
- Brick Height: 20 pixels
- Brick Colors: 
  - ${\color{red}Red}$
  - ${\color{orange}Orange}$
  - ${\color{yellow}Yellow}$
  - ${\color{green}Green}$
  - ${\color{cyan}Cyan}$

Below is an illustration of the multi-colored bricks integrated into the game window:

![Milestone_5](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/066fb173-445e-4cc5-85fb-4fd477232942)

### Milestone 6: Implementing Ball Spawning Functionality

In Milestone 6, I implemented the functionality to spawn the game ball at the center of the screen. The ball has a radius of 20 units.

Below is an illustration of the spawned ball:

![Milestone_6](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/9e512d7d-e5ce-41e9-8cba-37d8ed5dbe59)

### Milestone 7: Adding Paddle Movement Functionality

For Milestone 7, I added functionality to control the paddle movement using the mouse pointer location. The paddle's position is determined by the movement of the mouse pointer within the game window. Below is a GIF demonstrating how the paddle movement works based on the mouse movement:

![Milestone_7](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/76a72323-2aa3-4db4-8179-ab27fa60a604)

