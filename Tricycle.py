class Tricycle:
    def __init__(self,speed=1):
        self.speed = speed
    def setSpeed(self,speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed
    def pedal(self):
        self.setSpeed(self.getSpeed() + 1)
        print("Pedaling: Speed: " + str(self.getSpeed()))
    def brake(self):
        self.setSpeed(self.getSpeed() - 1)
        print("Brakes: Speed: " + str(self.getSpeed()))