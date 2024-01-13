from .header import *
from .normal_space import NormalSpace
from .space_group import SpaceGroup
from .space_checker import SpaceChecker

class NormalChecker(SpaceChecker):
    def __init__(self):
        self.space_obj=NormalSpace
    
    def check_space(self,stone,ban_dict):
        space_group=SpaceGroup(ban_dict,False)

        self.analyze(space_group,stone.turn_member(BLACK).keys(),stone,BLACK)
        self.analyze(space_group,stone.turn_member(WHITE).keys(),stone,WHITE)

        self.set_dimension1_space(space_group)

        return space_group

    def check_stone(self,allyL,scan_p):
        self.scan_space(allyL,scan_p)

    def scan_sliced_space(self,allyL,last,shape_N,scan_p):
        exceptL,measure_p=self.measure_space(allyL,last,scan_p)

        if measure_p.r_right-measure_p.r_left<4:
            return

        self.distribute_space(exceptL,allyL,shape_N,measure_p,scan_p)

    def distribute_space(self,exceptL,allyL,shape_N,measure_p,scan_p):
        attackL,defenseL=self.get_stanceL(measure_p,allyL,exceptL,shape_N,scan_p)
        parents=self.get_parents(allyL,scan_p)

        self.distribute_attackL(attackL,parents,shape_N,scan_p)
        self.distribute_defenseL(defenseL,parents,shape_N,scan_p)

    def get_stanceL(self,measure_p,allyL,exceptL,shape_N,scan_p):
        opened_rangeL,closed_rangeL=self.get_attack_rangeL(measure_p)
        defense_rangeL=self.get_defense_rangeL(measure_p)

        attack_banL,defense_banL=self.get_banlist(shape_N,scan_p)

        attackL=self.scan_attack(opened_rangeL,closed_rangeL,exceptL,attack_banL,shape_N,scan_p)
        defenseL=self.scan_defense(defense_rangeL,exceptL+defense_banL,attackL[0],scan_p)

        return attackL,defenseL
        

