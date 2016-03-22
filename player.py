from bge import logic,types,events,render
from mathutils import Vector
from key import StrategyKey
import base
from gun import Gun
from threading import Timer
from fireCommand import FireCommand
from aimCommand import AimCommand
from shootFurther import ShootFurther

strategyKey = StrategyKey()

class Player(base.Hope):
    def __init__(self, own):
        
        super().__init__(own)        
        self.sen = self.cont.sensors
        self.action = self.cont.actuators
        
        self.sense_range = 25
        self.enemy = None
        
        self.weapon = self.children[1]
        
        self.fireCommand = FireCommand(self.weapon)
        self.aimCommand = AimCommand(self.weapon)
        
        for child in self.children:
            if "player_armature" in child.name:
                self.arm = child
        
        #animation = self.arm.actuators["Action"]        
        #print(self.arm.children[0]["healt"])
        
        
        #self.hud()
        #self.weapon.range = 25
        #self.user = self["user"]
        
    def movement(self):
        keyPressed = strategyKey.keyDown                               
            
        if keyPressed(events.WKEY):
            speed = 0.4
            movement = Vector((0,speed,0))
            #self.arm.controller[0].activate(animation)
            self.applyMovement(movement, True)
            
        elif keyPressed(events.SKEY):            
            movement = Vector((0,-self.speed,0))
            self.applyMovement(movement, True)                                                       
        else:
            pass
        
    def straif(self):
        keyPressed = strategyKey.keyDown
        if keyPressed(events.QKEY):            
            rotation = Vector((-self.speed,0,0))           
            self.applyMovement(rotation, True)    
            
        elif keyPressed(events.EKEY):
            rotation = Vector((self.speed,0,0))
            self.applyMovement(rotation, True) 
        
    def rotation(self):
        keyPressed = strategyKey.keyDown                
        #playerCam = logic.getCurrentScene().objects['Camera']
    
        if keyPressed(events.AKEY):
            rotation = Vector((0,0,0.1))
            self.applyRotation(rotation, True)
                        
        elif keyPressed(events.DKEY):
            rotation = Vector((0,0,-0.1))
            self.applyRotation(rotation, True)
                                  
    
    def shooting(self):
        keyPressed = strategyKey.keyDown
        
        if keyPressed(events.SPACEKEY):
            self.fireCommand.execute()
    
    def reload(self):
        keyPressed = strategyKey.keyDown
        if keyPressed(events.RKEY):
            timer = Timer(2, self.weapon.reload)
            #print("Reloading")
            timer.start()
            
        #pass
        #keyPressed = strategyKey.keyDown
        # impliment weapon switch                        
                
    def hurting(self):
        keyPressed = strategyKey.keyTouch
        self.health = self.arm.children[0]["healt"] 
        #self.health = self["healt"]
        
        if keyPressed(events.HKEY):
            #self.health = self.health - 50.0
            print(self.health)  
            
        if(self.health<0):
            #passp
            logic.restartGame()
            #pass
            #print("DEAD")   
            
    def hud(self):
        sceneList = logic.getSceneList()
        #displayAmmo = None
        #print(sceneList[1])
        try:
            if(sceneList):#.objects["Ammo.001"]
                displayAmmo = sceneList[1].objects["Ammo.001"]
                displayHealth = sceneList[1].objects["Health.001"]
                displayAmmo.text = str(self.weapon.ammo)
                displayHealth.text = str(self.health)            
        except:
            pass#print("No")        
        #print(displayAmmo)
        #pass
        
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


def createPlayer(own):
    return ShootFurther(Player(own))
    
def main(cont):
    own = cont.owner
    
    if not "init" in own:
        own["init"] = True
        own = createPlayer(own)
  
    own.main()
    own.hurting()
    own.aimAtEnemy()
    own.straif()
    own.reload()
    own.hud()


