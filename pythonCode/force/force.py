import numpy as np
import turtle


class Force: 
    accelerationVector = np.array([0.00,0.00])
    locationVector = np.array([150.00,150.00])
    velocityVector = np.array([0.00,0.00])
    ballMass = 3000

    def setupBoard(self, width = 500, height = 500): 
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.t.fillcolor((100,1,1))
        self.t.ht()
        self.screen.setup(width, height)
        self.screen.tracer(0)
        self.t.speed(0)
        #self.screen.setworldcoordinates(0,0,width,height)

    def bounce(self): 
        if self.locationVector[0] > self.screen.screensize()[0] or self.locationVector[0] < 0: 
            print("width   " + str(self.screen.screensize()[0]))
            self.velocityVector[0] *= -1

        if self.locationVector[1] > self.screen.screensize()[1] or self.locationVector[1] < 0: 
            print("height   " + str(self.screen.screensize()[0]))
            self.velocityVector[1] *= -1     
        

    def drawCircle(self): 
        self.t.clear()        
        self.t.goto(self.locationVector[0], self.locationVector[1])
        self.t.dot(30)
        self.screen.update()
        #self.update

    def applyForce(self,forceVector): 
        print(forceVector)
        self.accelerationVector += (forceVector/self.ballMass); 


    def update(self): 
        self.velocityVector += self.accelerationVector
        self.locationVector += self.velocityVector
        self.accelerationVector *= 0

    def animate(self): 
        while True: 
            self.drawCircle()



def main(): 
    force = Force()
    force.setupBoard(800, 800)

    while True: 
        windVector = np.array([0.0001,0.00])
        gravityVector = np.array([0.000,-0.09])
        force.applyForce(windVector)
        force.applyForce(gravityVector)
        force.bounce()
        force.drawCircle()
        force.update()
    
    



if __name__ == "__main__":
    main()