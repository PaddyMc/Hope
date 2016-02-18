from bge import logic, events
import bge
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
        
        self.enemies = {}
        
        self.players = {}
        
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
                                               
                #print(state)
                                
                for k in state:
                    if not k in self.entities:
                        #print(k)
                        
                        if k == "character":
                            scene = logic.getCurrentScene()
                            position = Vector((201.55084,64.08196,6.42015))

                            spawner = scene.objects["Spawner"]
                            entity = scene.addObject("character", spawner)
                            playerCam = scene.objects['Camera']

                            playerCam.setParent(entity,False,False)
                            playerCam.worldPosition = position

                            self.entities[k] = entity
                            
                        #elif       
                                   
                    elif k in self.entities:
                        entity = self.entities[k]
                            #print(entity)
                            #
                            #entity.worldPosition = Vector(state[k][0])
                            #entity.worldOrientation.col[0] = Vector(state[k][1])
                            #entity.worldOrientation.col[1] = Vector(state[k][2])
                        
                        entity.worldPosition = Vector(state[k][0])
                        entity.worldOrientation.col[0] = Vector(state[k][1])
                        entity.worldOrientation.col[1] = Vector(state[k][2])
                                
                        
                    if not k[0] in self.enemies:
                        
                        if k[0] == "enemy_mesh_basic":
                            #print(k)
                            scene = logic.getCurrentScene()
                           
                            spawner = scene.objects["SpawnerEnemy"]
                            enemy = scene.addObject("enemy_nav.003", spawner)
                            self.enemies[k[0]] = enemy
                             
                        elif k[0] == "enemy_mesh_basic.002":
                            #print(k)
                            scene = logic.getCurrentScene()
                           
                            spawner = scene.objects["SpawnerEnemy1"]
                            enemy = scene.addObject("enemy_nav.000", spawner)
                            self.enemies[k[0]] = enemy 
                        
                        elif k[0] == "enemy_mesh_basic.003":
                            #print(k)
                            scene = logic.getCurrentScene()
                           
                            spawner = scene.objects["SpawnerEnemy2"]
                            enemy = scene.addObject("enemy_nav.000", spawner)
                            self.enemies[k[0]] = enemy
                            
                        elif k[0] == "enemy_mesh_basic.001":
                            #print(k)
                            scene = logic.getCurrentScene()
                           
                            spawner = scene.objects["SpawnerEnemy3"]
                            enemy = scene.addObject("enemy_nav.000", spawner)
                            self.enemies[k[0]] = enemy    
                        
                    elif k[0] in self.enemies:
                        enemy = self.enemies[k[0]]
                        #print(state[k][0])
                        #print(k[1])
                        if k[1] < 0 :
                            enemy.endObject()                        
                        else:
                            enemy.worldPosition = Vector(state[k][0])
                            enemy.worldOrientation.col[0] = Vector(state[k][1])
                            enemy.worldOrientation.col[1] = Vector(state[k][2])
                                               
                    
                    if not k in self.players:
                        #print(k)
                        if k == "player_mesh_basic.001":
                            scene = logic.getCurrentScene()
                           
                            spawner = scene.objects["SpawnerPlayer1"]
                            player = scene.addObject("player1", spawner)
                            self.players[k] = player 
                            
                    
                        
                    elif k in self.players:
                        player = self.players[k]
                        #print(state[k][0])
                        player.worldPosition = Vector(state[k][0])
                        player.worldOrientation.col[0] = Vector(state[k][1])
                        player.worldOrientation.col[1] = Vector(state[k][2])
                        
                    
                    if k == "WinningCone":
                        #print(state[k])
                        if state[k] == 0:
                            cont = bge.logic.getCurrentController()
                            fin = cont.actuators["Game"]
                            cont.activate(fin)
                            #spawner = scene.objects["SpawnerPlayer1"]
                            print("End of Game Client")
                              
            except socket.error:
                break
            

client = Client(server_ip="172.17.9.243", server_port=9957)
           
def main():
    #threadMain = Thread(target=client.main)
    #threadMain.start()
    client.main()
    