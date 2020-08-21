import numpy as np

class Force: 
    accelerationVector = np.array([0.00,0.00])
    locationVector = np.array([0.00,0.00])
    velocityVector = np.array([0.00,0.00])

    def update(self): 
        self.velocityVector += self.accelerationVector
        self.locationVector += self.velocityVector
        self.accelerationVector *= 0



