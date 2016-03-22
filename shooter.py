from bge import logic,types,events,render
from mathutils import Vector
from key import StrategyKey
import bge

from fireCommand import FireCommand
from aimCommand import AimCommand


def shooter():
    strategyKey = StrategyKey()
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = logic.getCurrentScene()
    gun = None
    gunPlayer = None
    #gun = scene.objects["AK.004"]
    for gobj in scene.objects:
            if gobj.name == "ClientGun":
                gun = gobj
            elif gobj.name == "Lowpoly..002":
                gunPlayer = gobj
                
            elif gobj.name == "player1":
                orientationPlayer = gobj 
                
            elif gobj.name == "character":
                orientation = gobj  
                
            elif gobj.name == "player_mesh_basic_Client":
                healthMonitor = gobj             
    
    if gun:
        keyPressed = strategyKey.keyDown
        
        fireCommand = FireCommand(gun)
        aimCommand = AimCommand(gun)
        
        target = getThreat(scene,gun)
        hud(healthMonitor["healt"],gun)
        endGame(healthMonitor["healt"])
        #print(orientation.health)
            
        if keyPressed(events.SPACEKEY):
            fireCommand.execute()   
            
        if target:            
            aimCommand.execute(target.worldPosition)
            
        else:
            gun.worldOrientation = orientation.worldOrientation
            #pass
            #fix aim
            
    if gunPlayer:
        #keyPressed = strategyKey.keyDown
        
        fireCommand = FireCommand(gunPlayer)
        aimCommand = AimCommand(gunPlayer)
        
        target = getThreat(scene,gunPlayer)
            
        if target:
            fireCommand.execute()
            aimCommand.execute(target.worldPosition)   
        else:
            gunPlayer.worldOrientation = orientationPlayer.worldOrientation
            #pass
            #fix orientation    
        #if target:            

def hud(health,weapon):
    sceneList = logic.getSceneList()
    
    try:
        if(sceneList):
            displayAmmo = sceneList[1].objects["Ammo.001"]
            displayHealth = sceneList[1].objects["Health.001"]
            displayAmmo.text = str(weapon.ammo)
            displayHealth.text = str(health)            
    except:
        pass            
            
def getThreat(scene,gun):
        for gobj in scene.objects:
            if "enemy_mesh" in gobj.name:
                delta = gobj.worldPosition - gun.worldPosition
                if delta.magnitude < 25:                    
                    return gobj

def endGame(health):
    if health<0:
        logic.restartGame()
        
shooter()    