from bge import logic

class RemoteKeyboard:
    
    def __init__(self):
        
        self.key_stat = {}
        
    def updateState(self, list_key_stat):
        
        for key, stat in list_key_stat:
            self.key_stat[key] = stat
            
    def keyDown(self,key_code, status = logic.KX_INPUT_JUST_ACTIVATED):
        
        if key_code in self.key_stat:
            if self.key_stat[key_code] == status:
                return True
            
        return False