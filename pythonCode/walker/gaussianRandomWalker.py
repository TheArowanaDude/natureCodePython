import turtle
import random


class gaussDistribution: 
    x = 0
    y = 0 
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
        xPosition = self.probabilityGenerate()
        self.t.setpos(xPosition,200)
        self.t.circle(30,30)

    def probabilityGenerate(self): 
        sd = 60
        mean = 400
        num = random.gauss(mean,sd)
        return num




def main(): 
    distribution = gaussDistribution()
    distribution.setupBoard(800,800)
    while True: 
        distribution.draw()



if __name__ == "__main__":
    main()