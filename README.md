# Code_in_Place-Brick_Breaker_Game

This repository is for my Stanford Code in Place course project.

## Overview

I have decided to create a simplified version of the Brick Breaker game, which was popular in the late 90s. The project utilizes Tkinter instead of the canvas since it wasn't available for me to use. The coding was done in the PyCharm IDE. I have set several milestones initially to complete the project in an orderly and organized fashion.

## Milestones

### Milestone 1: Game Window Creation

The first milestone was to create the game window itself. I decided to include a startup screen for the game after the file is run. I created a canvas window with a size of 800x600, displaying the message "Game Startup Screen". Below is an example of how it would look:

![Milestone_1](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/e3f0da00-f859-4684-9475-61b171fb5402)

### Milestone 2: Implementing Mouse Click Functionality

In Milestone 2, I added the functionality to initiate the game upon a mouse click. This prevents the game from starting immediately upon running the file, allowing players/users to prepare. The message displayed in the game window now prompts the player/user to click anywhere on the screen to start the game.

![Milestone_2](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/b649b72a-52cd-453d-9d87-4c31c826f0aa)

### Milestone 3: Creating the Main Game Window

To simulate the start of the game after clicking, I closed the previous game window and created a completely new game window to house the game.

### Milestone 4: Adding a Paddle to the Game

To fulfill the game's requirement of having a paddle, I introduced a blue rectangular block at the bottom with the following dimensions:
- Paddle Width: 100
- Paddle Height: 10
- Paddle Y Offset: 30

Below is an illustration of the paddle in the game:

![Milestone_4](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/806e4921-891d-4906-9907-f9385a6eaa09)

### Milestone 5: Adding Multi-Colored Bricks to the Game Window

For Milestone 5, I incorporated the essential feature of bricks into the game. I created a function that adds multiple rows of bricks of different colors. The configuration for the bricks is as follows:
- Number of Brick Rows: 5
- Number of Brick Columns: 10
- Brick Width: Width of the game window divided by the number of brick columns
- Brick Height: 20 pixels
- Brick Colors: 
  - ${\color{red}Red}$
  - ${\color{orange}Orange}$
  - ${\color{gold}Yellow}$
  - ${\color{green}Green}$
  - ${\color{cyan}Cyan}$

Below is an illustration of the multi-colored bricks integrated into the game window:

![Milestone_5](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/d840d948-60d3-4ced-9bc4-01326a82c3e5)

### Milestone 6: Implementing Ball Spawning Functionality

In Milestone 6, I implemented the functionality to spawn the game ball at the center of the screen. The ball has a radius of 20 units.

Below is an illustration of the spawned ball:

![Milestone_6](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/cac81858-1b42-4929-afce-76daafe5072d)

### Milestone 7: Adding Paddle Movement Functionality

For Milestone 7, I added functionality to control the paddle movement using the mouse pointer location. The paddle's position is determined by the movement of the mouse pointer within the game window. Below is a GIF demonstrating how the paddle movement works based on the mouse movement:

![Milestone_7](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/76a72323-2aa3-4db4-8179-ab27fa60a604)

### Milestone 8: Adding Ball Movement Dynamics

In Milestone 8, I implemented the ball dynamics for bouncing off walls. If the ball hits the bottom edge of the screen, the message "Game Over" is displayed.

Below is an illustration of the ball movement dynamics:

![Milestone_8](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/4e314263-9158-47e2-ac81-63d3e3b154ef)

### Milestone 9: Fine-tuning Ball Movement Dynamics

For Milestone 9, I further refined the ball movement dynamics, including bouncing off the paddle, walls, and triggering game over when the ball hits the lower edge.

Below is a demonstration of the refined ball movement dynamics:

![Milestone_9](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/ea8ccdfc-27fa-4bc8-a16b-c5e23a882f63)

### Milestone 10.1: Implementing Collision Detection with Bricks

In this milestone, I created a function to handle collision detection between the bricks and the ball. The function determines the overlap between the individual canvas functions of the bricks and initiates a bounce.

Below is an illustration of the collision detection with bricks:

![Milestone_10_1](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/51421aed-da5b-4c41-90b2-4ae474999e8f)

### Milestone 10.2: Nesting Collision Detection Functions

Milestone 10.2 involved nesting the collision detection functions for bricks and the paddle into one main collision function, enhancing code modularity.

### Milestone 11: Implementing Score Tracking Functionality

For Milestone 11, I created a function to track the player's score. Points are awarded based on the color of the broken bricks, and a bubble displaying the points appears on the bottom right of the screen.

Below is a visualization of the score tracking feature:

![Milestone_11](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/bb731fb7-5160-4759-a1de-3653d9af268a)

The points associated with each brick color are displayed in the table below:

| **Brick Color** | **Points** |
|-------------|--------|
| ${\color{red}Red}$        | 5      |
| ${\color{orange}Orange}$  | 4      |
| ${\color{gold}Yellow}$    | 3      |
| ${\color{green}Green}$    | 2      |
| ${\color{cyan}Cyan}$      | 1      |

### Milestone 12: Implementing Win Condition

In Milestone 12, I added code to determine if the player has won the game by destroying all the bricks. Upon destroying all bricks, a win message is displayed on the screen along with the player's score.

Below are illustrations of the win condition with the score displayed:

![Milestone_12_1_Win_Message](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/ee79b39d-7bac-4742-88c6-f9b8fde5a694)

Please note that the score tracking continues even if the player loses the game. Below is an illustration of the lose condition with the score displayed:

![Milestone_12_2_Lose_Message](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/6c45adc7-aee5-4e15-91c8-6284f262456c)

You can watch the gameplay video demonstrating the win condition of the complete game through the following embedded video:

[Gameplay Video - Win Condition](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/dbf47fe0-3c50-4055-b8ff-4565d7dc4a5b)

### Milestone 13: Game Icon Implementation

I created a game icon for the startup screen to enhance its appearance. Using Python's PIL library, I processed the image and positioned it correctly in the canvas window.

Below is an illustration of the current game window:

![Milestone_13](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/f6e730e7-e958-41ce-b5eb-fb7f183ea01f)

You can watch a gameplay video demonstrating the win condition of the complete game, including the startup game icon, through the following embedded video:

[![Gameplay Video - Game Icon Milestone Demo]](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/47de15c5-9c8d-47f2-b7bd-48a6f6bd6d34)

## Game Demo

Watch the complete gameplay video below, which demonstrates various scenarios, including wins, losses, and score tracking:

[![Gameplay Video - Game Demo]](https://github.com/Prithivvj2406/Code_in_Place-Brick_Breaker_Game/assets/159470988/08fceb56-2390-47f2-8d4a-b65627337f7c)

[Watch on YouTube](https://youtu.be/EbqWmH6yqHI)
