from bge import logic,types,events,render
from command import Command

#base fighter class
class Hope(types.KX_GameObject):
    def __init__(self,own):
        self.cont = self.controllers[0]

        self.speed = 0.2
        self.health = 100.0
        self.weapon = None
        self.fireCommand = Command() 
        self.aimCommand = Command()                  
        
    def movement(self):
        pass
      
    def rotation(self):
        pass
    
    def aimAt(self,vec):
        delta = vec - self.worldPosition
        self.alignAxisToVect(delta, 1)
    
    def shooting(self):
        pass
    
    def hurting(self):
        pass
    
    def main(self):
        self.movement()
        self.rotation()
        self.shooting()