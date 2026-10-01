import pygame
import random 

# pygame setup
pygame.init()

# width height, screen size, game name 
WIDTH, HEIGHT = 1080,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FraSnake")

# backgroun color,defining snake color black, food color and score white color 
background_color = (0, 255, 255)
black = (0,0,0)
food = (200,0,0)
white = (255, 255, 255)

# scoreboard
score_font = pygame.font.Font(None,50)

# counting score and snake length 
score = 0 

# snake setting 
snake_size = 30 
player_speed = 10

# Create a rectangle (x_position, y_position, width, height)
player_rect = pygame.Rect(375, 275, 50, 50)

# clock frame rate 
clock =  pygame.optimizations = pygame.time.Clock()

# direction of the snake 
direction = "Right"



# snake head | and body which is a dict and copy of the head
snake_head = pygame.Rect(390, 270, snake_size, snake_size)
snake_body = [
    snake_head.copy()
]

#circle food radius  
circle_radius = 15

# function of the food and random geneate the food 
def get_random_food_pos():
    x = random.randint(circle_radius,WIDTH-circle_radius)
    y = random.randint(circle_radius,HEIGHT-circle_radius)
    return x,y


circle_x , circle_y = get_random_food_pos()


# game over variable
game_over = False 



# -----------------------------game loop----------------------------------
running = True
while running:

    # control the keyboard 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

            elif event.key == pygame.K_UP:
                direction = "UP"

            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

    # check if not game over give the left right up down 
    if not game_over:
        if direction == "LEFT":
            snake_head.x -= player_speed

        elif direction == "RIGHT":
            snake_head.x += player_speed

        elif direction == "UP":
            snake_head.y -= player_speed

        elif direction == "DOWN":
            snake_head.y += player_speed


    # wall detection 
    if (
        snake_head.left < 0
        or snake_head.right>WIDTH
        or snake_head.top < 0 
        or snake_head.bottom > HEIGHT
    ): 
        game_over =  True
    # wall detection 


    # snake self collide detection
    snake_body.insert(0,snake_head.copy())

    for segment in snake_body[100:]:
        if snake_head.colliderect(segment):
            game_over= True
            break
    # snake self collide detection

    # food and score count 
    food_rect = pygame.Rect(circle_x - circle_radius
                            , circle_y - circle_radius
                            , circle_radius * 2
                            , circle_radius * 2)

    if snake_head.colliderect(food_rect):
        circle_x, circle_y = get_random_food_pos()
        score += 1
    else:
        snake_body.pop()

    # render 
    screen.fill(background_color)
    score_text = score_font.render(f"Score: {score}", True, black)
    screen.blit(score_text,(500,0))

    for segment in snake_body:
        pygame.draw.rect(screen, black, segment)
        
    pygame.draw.circle(screen, food, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(screen,food,(circle_x,circle_y),circle_radius)

    # game over text
    if game_over:
            game_over_text = score_font.render(
                "GAME OVER", True,white
            )
    
            screen.blit(
                game_over_text,
                (WIDTH//2-100,HEIGHT//2)
            )

    pygame.display.flip()
    clock.tick(20)
pygame.quit()
