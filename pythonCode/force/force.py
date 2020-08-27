import numpy as np
import turtle


class Force: 
    accelerationVector = np.array([0.00,0.00])
    locationVector = np.array([0.00,0.00])
    velocityVector = np.array([0.00,0.00])

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

    def drawCircle(self): 
        self.t.clear()        
        self.t.goto(self.locationVector[0], self.locationVector[1])
        self.t.dot(30)
        self.screen.update()
        self.update

    def applyForce(self,forceVector): 
        self.accelerationVector += forceVector; 


    def update(self): 
        self.velocityVector += self.accelerationVector
        self.locationVector += self.velocityVector
        self.accelerationVector *= 0

    def animate(self): 
        while True: 
            self.drawCircle()



def main(): 
    force = Force()
    force.setupBoard()

    while True: 
        windVector = np.array([0.001,0.001])
        force.applyForce(windVector)
        force.drawCircle()
        force.update()
    
    



if __name__ == "__main__":
    main()