# hardness.py

import turtle as t
import time

HARDNESS = {
    "Low": 1, 
    "Mid": 0.5, 
    "Hard": 0.1
}
HARDNESS_KEYS = ["Low", "Mid", "Hard"]

ALIGNMENT = "center"
FONT = ("Times New Roman", 10, "normal")

def select_hardness(screen):
    selected = {"level": None}

    display = t.Turtle()
    display.color("red")
    display.hideturtle()
    display.penup()
    display.goto(0, 0)

    def choose_hardness(index):
        selected["level"] = HARDNESS_KEYS[index]
        display.clear()
        display.write(f"Hardness set to: {selected['level']}", align=ALIGNMENT, font=FONT)
        screen.clearscreen()
        time(1)

    screen.listen()
    display.write("Choose hardness: 1 for Low, 2 for Mid, 3 for Hard", align=ALIGNMENT, font=FONT)

    screen.onkeyrelease(lambda: choose_hardness(0), "1")
    screen.onkeyrelease(lambda: choose_hardness(1), "2")
    screen.onkeyrelease(lambda: choose_hardness(2), "3")

    # Wait until a level is selected
    while selected["level"] is None:
        screen.update()

    return selected["level"]
