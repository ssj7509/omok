from .updated_dict import Dict
from .turn_group import TurnGroup
from .dimension_group import DimensionGroup

class SpaceGroup(TurnGroup):
    def __init__(self,ban_dict,option):
        self.black=DimensionGroup(option)
        self.white=DimensionGroup(option)
        
        self.sibling_dict=Dict()
        self.ban_dict=ban_dict

