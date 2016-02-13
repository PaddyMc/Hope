import bge
from command import Command
from gun import Gun

class AimCommand(Command):
    #gun = Gun()    
    def __init__(self,gun):
        self.gun = gun
        
    def execute(self,vec):
        self.gun.aim(vec)