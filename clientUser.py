from remoteKeyboard import RemoteKeyboard

class User:
    
    def __init__(self, name):
        
        self.name = name
        self.keyboard = RemoteKeyboard()