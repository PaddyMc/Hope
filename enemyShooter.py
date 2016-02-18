from bge import logic,types,events,render
from mathutils import Vector
#from key import StrategyKey
import bge

from fireCommand import FireCommand
from aimCommand import AimCommand


def enemyShooter():
    #strategyKey = StrategyKey()
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = logic.getCurrentScene()
    gun = None
    #gun = scene.objects["AK.004"]
    for gobj in scene.objects:
            if gobj.name == "AK.003":
                gun = gobj 
    
    if gun:
        #keyPressed = strategyKey.keyDown
        
        fireCommand = FireCommand(gun)
        aimCommand = AimCommand(gun)
        
        target = getThreat(scene,gun)
            
        #if keyPressed(events.SPACEKEY):
              
            
        if target:            
            aimCommand.execute(target.worldPosition)
            fireCommand.execute()
            #print("pew") 


def getThreat(scene,gun):
        for gobj in scene.objects:
            if "player_mesh" in gobj.name:
                delta = gobj.worldPosition - gun.worldPosition
                if delta.magnitude < 20:                    
                    return gobj
        
enemyShooter()    