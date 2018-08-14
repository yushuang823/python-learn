"""
功能：五角星的绘制
"""
import turtle
def main():
    count = 1
    while count <= 5:

        turtle.forward(100)   #向前走50
        turtle.right(144)    #向右转144度
        count = count + 1
    turtle.exitonclick()

if __name__ == '__main__':
    main()