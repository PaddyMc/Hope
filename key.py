from bge import logic,types

class StrategyKey():
        
    def Down(self, code, events, status):
        
        if events[code] == status:
            return True
        else:
            return False
            
    def keyDown(self, key_code, status=logic.KX_INPUT_ACTIVE):
        
        return self.Down(key_code, logic.keyboard.events, status)

    def mouseEvent(self, mouse_event, status=logic.KX_INPUT_ACTIVE):
        
        return self.Down(mouse_event, logic.mouse.events, status)

    def keyTouch(self, key_code):
        
        return self.keyDown(key_code, logic.KX_INPUT_ACTIVE)