import bge

#bge.render.showMouse(1)

def story():
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    
    mouseOver = cont.sensors["mouseOver"]
    click = cont.sensors["click"]
    
    #startGame = cont.actuators["Game"]
    
    if mouseOver.positive:
        own.color = [1,0,0,True]
        text = scene.objects["Story.001"]
        textInstructions = scene.objects["Instructions.001"]
        if click.positive:
            text.setVisible(True)
            textInstructions.setVisible(False)
            #cont.activate(startGame)
    else:
        #pass
        own.color = [0,0,1,True]

if __name__ == "__main__":
    story()