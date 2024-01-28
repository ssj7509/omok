from .header import *
from .dimension1 import OneDimensionalAnalyzer
from .space_group import SpaceGroup

class EndChecker(OneDimensionalAnalyzer):
    def check_space(self,stone,ban_dict):
        space_group=SpaceGroup(ban_dict,True)

        self.analyze(space_group,stone.turn_member(BLACK).keys(),stone,BLACK)
        self.analyze(space_group,stone.turn_member(WHITE).keys(),stone,WHITE)

        return list(map(lambda turn:space_group.turn_member(turn).check_dict,(BLACK,WHITE)))
    
    def check_stone(self,allyL,scan_p):
        if len(allyL)!=5:
           return

        check_dict=scan_p.space_group.turn_member(scan_p.turn).check_dict
        parents=self.get_parents(allyL,scan_p)

        for xyT in parents:
            check_dict[xyT]=1
        

