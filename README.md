
# Snake Game

This is a classic Snake Game implemented using the Pygame library in Python. The objective of the game is to control the snake and eat the food while avoiding collision with the boundaries and the snake's own body.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Make sure you have Python 3.x installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Install the Pygame library by running the following command in your terminal or command prompt:

   ```
   pip install pygame
   ```

## How to Play

1. Run the `snake_game.py` file using Python.

2. The game window will open, and you will see the snake and the food on the screen.

3. Use the arrow keys to control the movement of the snake:
   - Press the left arrow key to move the snake to the left.
   - Press the right arrow key to move the snake to the right.
   - Press the up arrow key to move the snake upwards.
   - Press the down arrow key to move the snake downwards.

4. The objective is to eat the food by guiding the snake towards it. Each time the snake eats the food, its length increases by one unit, and your score increases by one.

5. Be careful not to collide with the boundaries of the game window or the snake's own body. If the snake collides with either, the game will end, and you will see a "You Lost!" message.

6. To quit the game, simply close the game window or press the 'X' button.

## Game Features

- The game window has a dimensions of 600 pixels wide and 400 pixels high.
- The snake is represented by green rectangles, and the food is represented by a black rectangle.
- The snake moves at a speed of 15 units per second.
- The score is displayed at the top-left corner of the game window.
- The game ends if the snake collides with the boundaries or its own body.
- The food appears at random positions on the screen after each successful eat.

## Code Structure

The code is structured as follows:

- The necessary modules, `pygame` and `random`, are imported.
- The Pygame library is initialized.
- The game window is created with the specified dimensions.
- The game title and icon are set.
- The font styles for displaying the score and messages are defined.
- Functions are defined for displaying the score, drawing the snake, and printing messages.
- The main game loop function, `game_loop()`, is defined, which handles the game logic and events.
- Inside the game loop:
  - The game window is filled with a white background.
  - The snake and food are drawn on the screen.
  - The snake's movement is controlled based on user input from the arrow keys.
  - Collision detection with boundaries and the snake's own body is performed.
  - The snake's length and score are updated when the snake eats the food.
  - The game window is updated with the latest changes.
- The game loop continues until the game is over or the user quits the game.
