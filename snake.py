import turtle as t
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        #set shape and move to correct positions 
        for i in range(3):
            segment = t.Turtle()
            segment.penup()
            segment.shape("circle")
            segment.color("white")
            segment.goto(x = -20.1*i, y = 0 )
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.segments[seg_num].goto(self.segments[seg_num-1].position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self,position):
        new_segment = t.Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)



    def extend(self):
        self.add_segment(self.segments[-1].position())
    