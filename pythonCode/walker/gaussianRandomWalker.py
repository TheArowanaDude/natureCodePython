import turtle
import random


class gaussDistribution: 

    t = None
    screen = None

    def setupBoard(self, width = 500, height = 500): 
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.t.fillcolor((100,1,1))
        self.t.ht()
        self.screen.setup(width, height)
        
    def draw(self): 
        xPosition = self.probabilityGenerate(0, 20)
        yPosition = self.probabilityGenerate(0,20)
        self.t.goto(xPosition,yPosition)

    def probabilityGenerate(self,mean,sd): 
        num = random.gauss(mean,sd)
        print(num)
        return num




def main(): 
    distribution = gaussDistribution()
    distribution.setupBoard(800,800)
    while True: 
        distribution.draw()



if __name__ == "__main__":
    main()