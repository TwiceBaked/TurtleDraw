
import turtle
import math

inputFileName = input("\nEnter the file name: TurtleDrawLines.txt\n")
while inputFileName != "TurtleDrawLines.txt":
    inputFileName = input("\nERROR! Invalid file name. Files are Case Sensitive.\nPlease enter the file name: TurtleDrawLines.txt\n")

TextFile = open(inputFileName, 'r')
line = TextFile.readline()
LineDrawer = turtle.Screen()
LineDrawer.setup(450, 450)
LineDrawer = turtle.Turtle()
LineDrawer.speed(20)
LineDrawer.penup()

distance0 = 0

while line:

    splits = line.split(' ')

    if (len(splits)) == 3:
        color = splits[0]
        x = int(splits[1])
        y = int(splits[2])
        LineDrawer.color(color)
        LineDrawer.goto(x,y)
        LineDrawer.pendown()

        distance = math.sqrt((x)**2+(y)**2)
        distance0 = distance0 + distance

    if splits[0] != color:
        LineDrawer.penup()
        
    line = TextFile.readline()

totalDistance = distance0
print(totalDistance)
turtle.write(totalDistance)
turtle.done()
TextFile.close()