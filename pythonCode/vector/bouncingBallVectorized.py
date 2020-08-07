import turtle
import random
import numpy as np

class bouncingBall: 

    loc_Vector = None
    velocity_Vector = None
    screen = None

    def setupBoard(self, width = 500, height = 500): 
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.t.fillcolor((100,1,1))
        self.t.ht()
        self.screen.setup(width, height)
        self.screen.tracer(0)
        self.t.speed(0)
        self.screen.setworldcoordinates(0,0,width,height)
        self.loc_Vector = np.array([float(random.randrange(width)),float(random.randrange(height))])
        self.velocity_Vector = np.array([0.55,0.13])

    def bounce(self): 
        if self.loc_Vector[0] > self.screen.screensize()[0] or self.loc_Vector[0] < 0: 
            print("width   " + str(self.screen.screensize()[0]))
            self.velocity_Vector[0] *= -1

        if self.loc_Vector[1] > self.screen.screensize()[1] or self.loc_Vector[1] < 0: 
            print("height   " + str(self.screen.screensize()[0]))
            self.velocity_Vector[1] *= -1     
    
    
    def drawCircle(self): 
        self.t.clear()
        self.loc_Vector+=self.velocity_Vector
        self.bounce()
        #print("xPosition: " + str(self.loc_Vector[0]) + " yPosition" + str(self.loc_Vector[1]))
        self.t.goto(self.loc_Vector[0], self.loc_Vector[1])
        self.t.dot(30)
        self.screen.update()
            
    def animate(self): 
        while True: 
            self.drawCircle()

def main(): 
    distribution = bouncingBall()
    distribution.setupBoard(800,800)
    distribution.animate()



if __name__ == "__main__":
    main()