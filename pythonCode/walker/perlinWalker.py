import turtle
import random
import perlin


class perlinWalker: 

    t = None
    screen = None
    perlinGenerator = perlin.PerlinNoiseFactory(1) #1 dimension argument passed
    def setupBoard(self, width = 500, height = 500): 
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.t.fillcolor((100,1,1))
        self.t.ht()
        self.screen.setup(width, height)
        self.screen.tracer(0)
        
    def map_range(self, value, start1, stop1, start2, stop2):
        return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2

    def perlinGenerate(self,x): 
        num = self.perlinGenerator(x)
        print(num)
        return num

    def drawCircle(self): 
        t = 0
        while True: 
            self.t.penup()
            self.t.clear()
            xPosition = self.perlinGenerate(t)
            yPosition = self.perlinGenerate(t)
            self.t.goto(xPosition,yPosition)
            self.t.pendown()
            self.t.circle(30)
            self.t._update()
            t+=0.01
            

    




def main(): 
    distribution = perlinWalker()
    distribution.setupBoard(800,800)
    distribution.drawCircle()



if __name__ == "__main__":
    main()