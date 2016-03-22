from playerDecorator import PlayerDecorator

def ShootFurther(PlayerDecorator):
    def __init__(self,player):
        self.decorated = player
        self.sen = player.sen
        self.action = player.action
        
        self.sense_range = player.sense_range + 15
        self.weapon = player.weapon
        
        self.fireCommand = player.fireCommand
        self.aimCommand = player.aimCommand
        
        self.arm = player.arm
        
    def main():
        self.decorated.main()