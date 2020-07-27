import turtle
import random 

class randomWalker: 
    x = 0
    y = 0 
    t = None
    screen = None

    def setupBoard(self, width = 500, height = 500): 
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.t.ht()
        self.screen.setup(width, height)

    def nextStep(self):
        choice = random.randrange(4)
        if(choice == 0): 
            self.x+=1
        elif(choice == 1):
            self.x-=1
        elif(choice == 2): 
            self.y+=1
        else:
            self.y-=1

    def draw(self): 
        self.nextStep()
        self.t.goto(self.x,self.y)




def main(): 
    theWalker = randomWalker()
    theWalker.setupBoard(1000,900)
    while True:
        theWalker.draw()




if __name__ == "__main__":
    main()