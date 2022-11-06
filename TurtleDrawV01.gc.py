
import turtle

inputFileName = input("Enter the file name: TurtleDrawLines.txt\n")
while inputFileName != "TurtleDrawLines.txt":
    inputFileName = input("ERROR! Invalid file name. Please enter the file name: TurtleDrawLines.txt\n")

TextFile = open(inputFileName, 'r')

line = TextFile.readline()

LineDrawer = turtle.Screen()
LineDrawer.setup(450, 450)

LineDrawer = turtle.Turtle()
LineDrawer.speed(20)

LineDrawer.penup()

while line:

    splits = line.split(' ')

    if (len(splits)) == 3:
        color = splits[0]
        x = int(splits[1])
        y = int(splits[2])
        LineDrawer.color(color)
        LineDrawer.goto(x,y)
        LineDrawer.pendown()
        
        while LineDrawer == LineDrawer.pendown():
            LineDrawer = turtle.distance(x,y)
            totalDistance = turtle.distance(x,y) + turtle.distance(x,y)

    if splits[0] != color:
        LineDrawer.penup()
        LineDrawer != turtle.distance(x,y)
        
    line = TextFile.readline()

totalDistance = turtle.distance(x,y) + turtle.distance(x,y)
turtle.write(totalDistance)
turtle.done()
TextFile.close()