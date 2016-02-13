from bge import types, logic
from mathutils import Vector

class Bullet(types.KX_GameObject):
    
    def __init__(self, own):
        self.cont = self.controllers[0]
        
        self.vel = self["direction"]
        self.range = self["range"]
        
        speed = 0.3
        self.vel.magnitude = speed
        
        self.vel_accum = Vector((0, 0, 0))
    
        
    def main(self):
        
        self.worldPosition += self.vel
        
        sound = self.cont.actuators["Sound"]
        self.cont.activate(sound)        
        
        self.vel_accum += self.vel
        if self.vel_accum.magnitude > self.range:
            self.endObject()


def main(cont):    
    own = cont.owner
    
    if not "init" in own:
        
        own["init"] = True
        own = Bullet(own)        
        
    own.main()