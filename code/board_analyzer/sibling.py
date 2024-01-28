from .header import *

class Sibling:
    def __init__(self): 
        self.opened_attack=set()
        self.closed_attack=set()

        self.complete_defense=set()
        self.incomplete_defense=set()
        
        self.entire_defense=set()
        self.defense=[set()for _ in range(4)]

    def add_sibling(self,e):
        if e.stance==ATTACK:
            self.add_attack(e)

        elif e.stance==DEFENSE:
            self.add_defense(e)

    def add_attack(self,e):
        if e.shape_type==OPENED:
            self.opened_attack.add(e.xyT)

        elif e.shape_type==CLOSED:
            self.closed_attack.add(e.xyT)

    def add_defense(self,e):
        if e.shape_type==DEFENSE5:
            return

        if e.shape_type in (DEFENSE1,DEFENSE2):
            self.complete_defense.add(e.xyT)

        elif e.shape_type in (DEFENSE3,DEFENSE4):
            self.incomplete_defense.add(e.xyT)

        self.entire_defense.add(e.xyT)
        self.defense[e.shape_type].add(e.xyT)
    
