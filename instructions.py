import bge

#bge.render.showMouse(1)

def instructions():
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    
    mouseOver = cont.sensors["mouseOver"]
    click = cont.sensors["click"]
    
    
    #startGame = cont.actuators["Game"]
    
    if mouseOver.positive:
        own.color = [1,0,0,True]
        textStory = scene.objects["Story.001"]
        text = scene.objects["Instructions.001"]
        if click.positive:
            #show = False
            textStory.setVisible(False)               
            text.setVisible(True)
            
            #else:
                #text.setVisible(True)
                #show = True
                
            #pass
            #cont.activate(startGame)
    else:
        #pass
        own.color = [0,0,1,True]

if __name__ == "__main__":
    instructions()