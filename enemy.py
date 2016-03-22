import base
from fireCommand import FireCommand
from aimCommand import AimCommand
from bge import events

class Enemy(base.Hope):
    
    def __init__(self, own):
        super().__init__(own)
        
        self.sen = self.cont.sensors
        self.action = self.cont.actuators
        
        self.sense_range = 20
        self.target = None                               
        
        for child in self.children:
            if "AK" in child.name:
                self.weapon = child
            elif "enemy_armature" in child.name:
                self.arm = child
        
        #for child in self.children:
            #if "enemy_armature" in child.name:
                #self.arm = child
                
        self.fireCommand = FireCommand(self.weapon)
        self.aimCommand = AimCommand(self.weapon) 
        
    def getThreat(self):
        
        for gobj in self.scene.objects:
            if "player" in gobj.name:
                delta = gobj.worldPosition - self.worldPosition
                if delta.magnitude < self.sense_range:                    
                    return gobj
    
    def rotation(self):
        self.target = self.getThreat()
        AI = self.action["path"]
        
        if self.target:
            self.aimAt(self.target.worldPosition)
            self.aimCommand.execute(self.target.worldPosition)
            self.fireCommand.execute()
            AI.target = self.target.name 
            self.cont.activate(AI)
                  
        else:
            newTarget = self.getThreat()
            
    def collision(self):
        
        sound = self.action["Sound"]
        self.health = self.arm.children[0]["healt"]
        
        if(self.health <= 50):
            self.cont.activate(sound)
            
        if(self.health<0):
            print("Enemy dead")
            
            #wait time
            self.endObject()#cont.activate(death)
            

def createEnemy(own):
    return Enemy(own)
            
def main(cont):
    own = cont.owner
    
    if not "init" in own:
        own["init"] = True
        own = createEnemy(own)
        
    own.main()
    own.collision()