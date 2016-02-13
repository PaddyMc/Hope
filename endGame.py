from bge import logic,types,events,render

class EndGame(types.KX_GameObject):
    def __init__(self, own):
        self.cont = self.controllers[0]
        self.winner = 0        
                
        print(self.cont.actuators)
        print(self.cont.sensors)
        
    def endGame(self):
        self.winner = self["healt"]
        
        endGame = self.cont.actuators["endGame"]
        #print(self["healt"])
        #if(collision): 
        #self.winner = 0           
        if(self.winner<=0):
            print("WINNER")
            self.cont.activate(endGame)
            #pass
                               
                
    def main(self):
        self.endGame()
                
        
def main(cont):
    own = cont.owner
    
    if not "init" in own:
        own["init"] = True
        own = EndGame(own)
    
    own.main()