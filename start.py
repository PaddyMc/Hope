import bge

bge.render.showMouse(1)

def start():
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    
    mouseOver = cont.sensors["mouseOver"]
    click = cont.sensors["click"]
    
    startGame = cont.actuators["Game"]
    
    if mouseOver.positive:
        own.color = [1,0,0,True]
        if click.positive:
            cont.activate(startGame)
    else:
        #pass
        own.color = [0,0,1,True]

if __name__ == "__main__":
    start()