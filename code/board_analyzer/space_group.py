from .updated_dict import Dict
from .turn_group import TurnGroup
from .dimension_group import DimensionGroup
from .sibling import Sibling
from .space import Space

class SpaceGroup(TurnGroup):
    def __init__(self,ban_dict,option):
        self.black=DimensionGroup(option)
        self.white=DimensionGroup(option)
        
        self.sibling_dict=Dict()
        self.ban_dict=ban_dict

    def update_sibling(self,e):
        sibling_key=e.parents,e.lineT

        self.sibling_dict.update_key(sibling_key,Sibling)
        sibling=self.sibling_dict[sibling_key]
        
        sibling.add_sibling(e)
        e.set_sibling(sibling)

    def update_element(self,xyT,turn,e):
        space=self.get_space(xyT,turn)
        space.add_element(e)

    def update_space(self,xyT,turn,cls):
        dimension1_dict=self.get_dimension1_turn(turn)
        dimension1_dict.update_key(xyT,cls,p=(xyT,turn,self))

    def update_check_dict(self,xyT,turn,cls):
        check_dict=self.get_check_dict(turn)
        check_dict.update_key(xyT,cls,p=(xyT,turn,self))

    def get_space(self,xyT,turn):
        dimension1_dict=self.get_dimension1_turn(turn)

        return dimension1_dict[xyT]

    def get_check_space(self,xyT,turn):
        check_dict=self.get_check_dict(turn)

        return check_dict[xyT]

    def update_ban(self,key,cls,p):
        self.family_dict.update_key(key,cls,p=p)

    def get_dimension1_turn(self,turn):
        return self.turn_member(turn).get_dimension1_dict()

    def get_check_dict(self,turn):
        return self.turn_member(turn).get_check_dict()

