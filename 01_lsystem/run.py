import turtle
import config
from lsystem import LSystem

class TurtleExecutor():
  def __init__(self, turtle):
    self.turtle = turtle
    self.stack = []

  def left(self, angle):
    self.turtle.lt(angle)

  def right(self, angle):
    self.turtle.rt(angle)

  def draw(self, steps):
    self.turtle.fd(steps)

  def move(self, steps):
    self.turtle.penup()
    self.turtle.fd(steps)
    self.turtle.pendown()

  def store(self):
    x, y = self.turtle.pos()
    angle = self.turtle.heading()
    self.stack.append((x, y, angle))

  def restore(self):
    x, y, angle = self.stack.pop()
    self.turtle.penup()
    self.turtle.setheading(angle)
    self.turtle.setpos(x, y)
    self.turtle.pendown()

class TurtleBoundsLoggerExecutor(TurtleExecutor):
  def __init__(self, turtle, bounds):
    super().__init__(turtle)
    self.x, self.y, self.width, self.height = bounds
    self.log()

  def draw(self, steps):
    super().draw(steps)
    self.log()

  def log(self):
    x, y = self.turtle.pos()
    inbound = self.isinbound(x, y)
    if inbound:
      self.turtle.pencolor('green')
    else:
      self.turtle.pencolor('red')
    print(round(x), round(y), inbound)

  def isinbound(self, x, y):
    if x < self.x or x > self.x + self.width:
      return False
    if y > self.y or y < self.y - self.height:
      return False
    return True

def draw_rect(rect, turtle):
  x_current, y_current = turtle.pos()
  angle_current = turtle.heading()
  x, y, width, height = rect

  turtle.penup()
  turtle.setpos(x, y)
  turtle.setheading(0)
  turtle.pendown()

  turtle.fd(width)
  turtle.rt(90)
  turtle.fd(height)
  turtle.rt(90)
  turtle.fd(width)
  turtle.rt(90)
  turtle.fd(height)

  turtle.penup()
  turtle.setpos(x_current, y_current)
  turtle.setheading(0)
  turtle.pendown()

if __name__ == '__main__':
  turtle.speed(100)

  turtle.pencolor('blue')
  bounds = (0, 0, 150, 150)
  draw_rect(bounds, turtle)

  turtle.pencolor('green')
  lsystem = LSystem(config.dragon_curve)
  lsystem.run(TurtleBoundsLoggerExecutor(turtle, bounds))
  turtle.mainloop()
