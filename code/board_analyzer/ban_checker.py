from .header import *
from .ban_check_space import BanCheckSpace
from .space_group import SpaceGroup
from .space_checker import SpaceChecker

class BanChecker(SpaceChecker):
    def __init__(self):
        self.space_obj=BanCheckSpace
    
    def check_space(self,stone,ban_dict):
        space_group=SpaceGroup(ban_dict,True)

        self.analyze(space_group,stone.black.keys(),stone,BLACK)

        self.set_dimension1_space(space_group)

        return space_group.black.check_dict

    def check_stone(self,allyL,scan_p):
        if len(allyL)==1:
            return
        
        self.scan_space(allyL,scan_p)

    def scan_sliced_space(self,allyL,last,shape_N,scan_p):
        exceptL,measure_p=self.measure_space(allyL,last,scan_p)

        if measure_p.e_right-measure_p.e_left<4:
            return

        self.distribute_space(exceptL,allyL,shape_N,measure_p,scan_p)

    def distribute_space(self,exceptL,allyL,shape_N,measure_p,scan_p):
        attackL,shape_N=self.get_stanceL(measure_p,allyL,exceptL,shape_N,scan_p)
        parents=self.get_parents(allyL,scan_p)

        self.distribute_attackL(attackL,parents,shape_N,scan_p)

    def get_stanceL(self,measure_p,allyL,exceptL,shape_N,scan_p):
        opened_rangeL,closed_rangeL=self.get_attack_rangeL(measure_p)

        if shape_N==4 and self.sixpoint(10,scan_p):
            closed_rangeL=[*range(5,10)]
            shape_N=-1
        
        attack_banL,defense_banL=self.get_banlist(shape_N,scan_p)

        attackL=self.scan_attack(opened_rangeL,closed_rangeL,exceptL,attack_banL,shape_N,scan_p)

        return attackL,shape_N
