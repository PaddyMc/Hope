import bge
from command import Command
from gun import Gun

class FireCommand(Command):
    #gun = Gun()    
    def __init__(self,gun):
        self.gun = gun
        
    def execute(self):
        self.gun.fire()