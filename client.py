from bge import logic, events
from mathutils import Vector
from threading import Thread
import socket
import pickle

def keyDown(key_code,status=logic.KX_INPUT_ACTIVE):
    if logic.keyboard.events[key_code] == status:
        return True
    return False

def keyHit(key_code):
    return keyDown(key_code, status = logic.KX_INPUT_JUST_ACTIVATED)
    
        
class Client:
    
    def __init__(self, server_ip="", server_port=9999):
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setblocking(False)
        #self.socket.bind((host,port))
        
        self.serv_addr = (server_ip,server_port)
        
        self.entities = {}
        
        self.main = self.state_sendName
    
    def state_sendName(self):
        
        scene = logic.getCurrentScene()
        text = scene.objects["Name"]
        
        if keyHit(events.ENTERKEY):
            self.socket.sendto(bytes(text["Text"], 'utf-8'), self.serv_addr)
            text.endObject()
            self.main = self.state_loop
            
    def state_loop(self):
        self.send()
        self.receive()
        
    def send(self):        
        list_key_stat = []
        
        kevts = logic.keyboard.events
        for k in kevts:
            s = kevts[k]
            if s in (logic.KX_INPUT_JUST_ACTIVATED,logic.KX_INPUT_JUST_RELEASED):
                list_key_stat.append((k,s))
        
        if len(list_key_stat):
            self.socket.sendto(pickle.dumps(list_key_stat), self.serv_addr)
        
    def receive(self):
        
        while True:
            
            try:
                data,addr = self.socket.recvfrom(1024)
                
                state = pickle.loads(data)                                
                                
                for k in state:
                    if not k in self.entities:
                        scene = logic.getCurrentScene()
                        position = Vector((201.55084,64.08196,6.42015))
                        #playerCamPosition = scene.objects['Camera'].worldPosition
                        spawner = scene.objects["Spawner"]
                        entity = scene.addObject("character", spawner)
                        playerCam = scene.objects['Camera']
                        #print(playerCam.name)
                        #entity.parent(playerCam)
                        playerCam.setParent(entity,False,False)
                        playerCam.worldPosition = position
                        #entity.children[0]["Text"] = k[1]
                        self.entities[k] = entity         
                    else:
                        entity = self.entities[k]
                     
                    #print(entity.children[2])    
                    entity.worldPosition = Vector(state[k][0])
                    entity.worldOrientation.col[0] = Vector(state[k][1])
                    entity.worldOrientation.col[1] = Vector(state[k][2])
                    #print(state[k][2])
                                
            except socket.error:
                break
            

client = Client()
            
def main():
    threadMain = Thread(target=client.main)
    threadMain.start()
    