from .header import *
from .parameter_set import ParameterSet

class Element:
    def __init__(self,xyT,parents,option_p,lineT):
        self.xyT=xyT
        self.parents=parents
        self.shape_N=option_p.shape_N
        self.stance=option_p.stance
        self.shape_type=option_p.shape_type
        self.element_type=option_p.element_type
        self.lineT=lineT

    def set_targetL(self,targetL):
        self.targetL=targetL
        self.valueL=[]

    def get_vars(self):
        return self.parents,self.lineT,self.shape_N,self.stance,self.shape_type,self.element_type

    def set_sibling(self,sibling):
        self.sibling=sibling

    def set_matrix(self,array):
        if self.element_type in (NORMAL,TARGET):
            array[1+self.stance*10+(self.shape_N-1)*(2,5)[self.stance]+self.shape_type]+=1

    def compare_parents(self,e):
        union=self.parents+e.parents
        
        return len(union)==len(set(union))

    def get_opened_attack_sibling(self):
        return self.sibling.opened_attack

    def get_closed_attack_sibling(self):
        return self.sibling.closed_attack

    def get_complete_defense_sibling(self):
        return self.sibling.complete_defense

    def get_incomplete_defense_sibling(self):
        return self.sibling.incomplete_defense

    def get_entire_defense_sibling(self):
        return self.sibling.entire_defense

    @property
    def abs_material(self):
        return self.shape_N,self.stance,self.shape_type

    @property
    def init_args(self):
        option_p=ParameterSet(OPTION,self.shape_N,self.stance,self.shape_type,self.element_type)

        return self.xyT,self.parents,option_p,self.lineT

