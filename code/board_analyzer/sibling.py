from .header import *

class Sibling:
    def __init__(self):
        self.family=Family()

    def add_element(self,xyT,option_p):
        self.family.add_family_element(xyT,option_p)

    def get_valid_attackS(self):
        return self.valid_attackS

    def get_invalid_attackS(self):
        return self.invalid_attackS

    def get_valid_defenseS(self):
        return self.valid_defenseS

    def get_invalid_defense(self):
        return self.invalid_defenseS

class Family:
    def __init__(self):
        self.valid_attackS=set()
        self.valid_defenseS=set()
        self.invalid_attackS=set()
        self.invalid_defenseS=set()
       
    def add_family_element(self,xyT,option_p):
        (self.add_attack_family,self.add_defense_family)[option_p.stance==DEFENSE](xyT,option_p)

    def add_attack_family(self,xyT,option_p):
        (self.valid_attackS,self.invalid_attackS)[option_p.shape_type==CLOSED].add(xyT)

    def add_defense_family(self,xyT,option_p):
        (self.valid_defenseS,self.invalid_defenseS)[option_p.shape_type==DEFENSE5].add(xyT)
