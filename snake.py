import pygame
import random

# Initializing the pygame
pygame.init()

# Dimension of window
width = 600
height = 400

# Creating the game window
screen = pygame.display.set_mode((width, height))

# Setting the Title and icon
pygame.display.set_caption('Snake Game')

# Frames per second controller
c = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Font style
font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)


# Function to display the score
def your_score(score):
    value = score_font.render(f"Your Score: {score}", True, (0, 0, 0))
    screen.blit(value, [0, 0])


# Function to draw snakes
def snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x, y, snake_block, snake_block])


# Function to print the message
def message(msg, color, **kwargs):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [kwargs.get('x', width / 6), kwargs.get('y', height / 3)])


# Function for game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Defining food parameters
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Game Loop
    running = True
    while running:
        while game_close:
            screen.fill((0, 0, 0))
            message("You Lost!", (255, 0, 0), x=width / 3)
            pygame.display.update()

        # Loop for events
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                running = False
            # Keyboard arrow event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Setting the boundaries
        if not (0 <= x1 < width and 0 <= y1 < height):
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill((255, 255, 255))

        # Drawing the food
        pygame.draw.rect(screen, (0, 0, 0), [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # For snake to not hit its own body
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Checking same coordinates
        if x1 == food_x and y1 == food_y:
            # Making food appear at random position
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            # Increasing the length of snake
            length_of_snake += 1

        # Setting the frames per second
        c.tick(snake_speed)
    # Quit event
    pygame.quit()
    quit()


game_loop()