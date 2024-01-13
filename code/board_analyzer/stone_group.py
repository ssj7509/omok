from .updated_dict import Dict
from .turn_group import TurnGroup

class StoneGroup(TurnGroup):
    def __init__(self,recordL):
        self.black=Dict()
        self.white=Dict()
        self.edge=Dict()
        self.entire=Dict()

        self.set_stone(recordL)

    def set_stone(self,recordL):
        for i in range(16):
            self.edge[(i-1,-1)]=1
            self.edge[(i,15)]=1
            self.edge[(-1,i)]=1
            self.edge[(15,i-1)]=1

        for i,(x,y) in enumerate(recordL):
            self.turn_member(i%2)[(x-1,y-1)]=1
            self.entire[(x-1,y-1)]=1
            
