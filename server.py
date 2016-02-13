from bge import logic
from threading import Thread
import socket
import pickle
from remoteKeyboard import RemoteKeyboard
from clientUser import User
        
class Server:
    
    def __init__(self, host="", port=9999):
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setblocking(False)
        self.socket.bind((host,port))
        
        self.addr_user = {}
        
        
    def receive(self):
        
        while True:
            
            try:
                data,addr = self.socket.recvfrom(1024)
                
                if not addr in self.addr_user:
                    user = User(data.decode())
                    
                    scene = logic.getCurrentScene()
                    spawner = scene.objects["Spawner"]
                    avatar = scene.addObject("character", spawner)
                    #avatar.children[0]["Text"] = user.name
                    avatar["user"] = user
                    
                    self.addr_user[addr] = user                
                    
                else:
                    user = self.addr_user[addr]
                    user.keyboard.updateState(pickle.loads(data))
                
            except socket.error:
                break
    
    def send(self):
        
        scene = logic.getCurrentScene()
        
        #state = {(gobj.name, gobj["user"].name): list(gobj.worldPosition) \
         #         for gobj in scene.objects \
         #         if gobj.name == "Avatar"}
         
        for gobj in scene.objects:
            if gobj.name == "character":
                state = {(gobj.name, gobj["user"].name): (list(gobj.worldPosition), list(gobj.worldOrientation.col[0].copy()), list(gobj.worldOrientation.col[1].copy()))}
                #self.worldOrientation.col[1].copy()
                  
        for addr in self.addr_user:
            self.socket.sendto(pickle.dumps(state), addr)
            
server = Server()
            
def receive():
    threadReceive = Thread(target=server.receive)
    threadReceive.start()
    
def send():
    threadSend = Thread(target=server.send)
    threadSend.start()