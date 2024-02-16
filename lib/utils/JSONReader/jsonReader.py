import json
import os

class JSONReader():
    def __init__(self):
        
        with open("ui/auto_offline/offline_names.json") as names:
            self.nameVar = json.load(names)

        
        #for name in self.nameVar["names"]:
            #print(name[0])
        
        
    

