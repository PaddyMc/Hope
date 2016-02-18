from bge import logic,types,events,render
from mathutils import Vector,Matrix


#import weapon

class Barrier(types.KX_GameObject):
    def __init__(self, own):
        self.cont = self.controllers[0]
        
    def moveBarrier(self):
        count = 0
        for gobj in self.scene.objects:
            if "enemy_nav" in gobj.name:
                #pass
                count += 1                
                #print(count)
          
        if not count:#not count:
            movement = Vector((0,0,1))
            
            self.applyMovement(movement, True)
            #print("allDead")  
                
    def main(self):
        self.moveBarrier()
                
        
def main(cont):
    own = cont.owner
    
    if not "init" in own:
        own["init"] = True
        own = Barrier(own)
    
    own.main()