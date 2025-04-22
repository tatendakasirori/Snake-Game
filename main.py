from turtle import Screen
from snake import Snake  
from food import Food
from scoreboard import Scoreboard
import time
import hardness  # your file

# Create ONE screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Get difficulty using the same screen
selected_level = hardness.select_hardness(screen)
sleep_time = {
    "Low": 0.5, 
    "Mid": 0.25, 
    "Hard": 0.1
}[selected_level]

# Now reuse the screen after selection
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
