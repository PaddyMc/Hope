from bge import logic,types,events
from mathutils import Vector
import base
from fireCommand import FireCommand
from aimCommand import AimCommand

def keyDown(key_code,status=logic.KX_INPUT_ACTIVE):
    if logic.keyboard.events[key_code] == status:
        return True
    return False

class PlayerClient(base.Hope):
    def __init__(self,own):
        
        self.speed = 0.1
        self.user = self["user"]
        #self.weapon = self.children[0]
        
        for child in self.children:
            if "AK" in child.name:
                self.weapon = child
            elif "player_armature" in child.name:
                self.arm = child
        
        self.sense_range = 25
        self.enemy = None
        
        self.fireCommand = FireCommand(self.weapon)
        self.aimCommand = AimCommand(self.weapon)
        
    def movement(self):
        keyPressed = self.user.keyboard.keyDown            
        
        if keyPressed(events.EKEY):
            #speed = 0.3
            movement = Vector((0,self.speed,0))
            #self.arm.controller[0].activate(animation)
            self.applyMovement(movement, True)
            
        elif keyPressed(events.DKEY):
            movement = Vector((0,-self.speed,0))
            self.applyMovement(movement, True)                                                       
        else:
            pass
        
    def straif(self):
        keyPressed = self.user.keyboard.keyDown
        if keyPressed(events.AKEY):
            rotation = Vector((-self.speed,0,0))           
            self.applyMovement(rotation, True)    
            
        elif keyPressed(events.GKEY):
            rotation = Vector((self.speed,0,0))
            self.applyMovement(rotation, True)
            
    def rotation(self):
        keyPressed = self.user.keyboard.keyDown                
        #playerCam = logic.getCurrentScene().objects['Camera']
    
        if keyPressed(events.SKEY):
            rotation = Vector((0,0,0.1))
            self.applyRotation(rotation, True)
                        
        elif keyPressed(events.FKEY):
            rotation = Vector((0,0,-0.1))
            self.applyRotation(rotation, True)
        
    def fire(self):
        keyPressed = self.user.keyboard.keyDown
        
        if keyPressed(events.SPACEKEY):
            self.fireCommand.execute()
            #self.weapon.fire()
            
    def getThreat(self):
        #threats = list()
        
        for gobj in self.scene.objects:
            if "enemy_mesh" in gobj.name:
                delta = gobj.worldPosition - self.worldPosition
                if delta.magnitude < self.sense_range:                    
                    return gobj
                
    def aimAtEnemy(self):
        self.target = self.getThreat()
        
        if self.target:            
            self.aimCommand.execute(self.target.worldPosition)                        
        else:
            self.weapon.worldOrientation = self.worldOrientation 
            
    def hurting(self):
        self.health = self.arm.children[0]["healt"] 
            
        if(self.health<0):
            pass
            #print("DEAD")         
        
def main(cont):
    
    own = cont.owner
    
    if not "init" in own:
        own["init"] = 1
        PlayerClient(own)
    else:
        own.main()
        own.hurting()
        own.fire()
        own.straif()
        own.aimAtEnemy()
    
    #self.fire()    