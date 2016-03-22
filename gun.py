from bge import logic,types,events
from mathutils import Vector,Matrix
import random
from threading import Timer
import time
import math

class Gun(types.KX_GameObject):
    def __init__(self, own):
        self.cont = self.controllers[0]
        self.sen = self.cont.sensors
        self.own = self.cont.owner        
                        
        self.tip = self.children[0]
        
        self.bullet_name = "Bullet"
        
        self.range = 30
        self.accuracy = .99
        self.ammo = 50
        self.visible = True
        
    def fire(self):
        if(self.ammo):
            self.ammo -= 1           
            scene = logic.getCurrentScene()
            bullet = scene.addObject(self.bullet_name, self.tip)
            
            angle_range = math.pi/2 * (1 - self.accuracy)
            angle_range *= random.choice((-1, 1))
            
            mat_rot = Matrix.Rotation(random.uniform(0, angle_range), 3, 'Z')            
            
            bullet["direction"] = mat_rot * self.worldOrientation.col[1].copy()
            bullet["range"] = self.range
        else:
            timer = Timer(2, self.reload)
            #print("Reloading")
            timer.start()
            #play reloading animation + sound  
        
    
    def reload(self):
        self.ammo = 50
    
    def aim(self,vec):
        delta = vec - self.worldPosition
        self.alignAxisToVect(delta, 1)
    
        
def main(cont):
    Gun(cont.owner)