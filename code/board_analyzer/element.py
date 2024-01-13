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
        self.abs_val=self.get_abs_val(self.shape_N,self.stance,self.shape_type)

    def set_targetL(self,targetL):
        self.targetL=targetL
        self.valueL=[]

    def get_abs_val(self,shape_N,stance,shape_type):
        r=1

        if shape_N==5 and stance==ATTACK:
            r=13
        elif shape_N==5 and stance==DEFENSE:
            r=11
        elif shape_N==4 and stance==ATTACK:
            r=9
        elif shape_N==4 and stance==DEFENSE:
            r=7
        elif shape_N==3 and stance==ATTACK and shape_type==OPENED:
            r=5
        elif shape_N==3 and stance==DEFENSE and shape_type in (DEFENSE1,DEFENSE3):
            r=3

        return r

    def get_vars(self):
        return self.parents,self.lineT,self.shape_N,self.stance,self.shape_type,self.element_type

    def set_matrix(self,array):
        if self.element_type in (NORMAL,TARGET):
            array[1+self.stance*10+(self.shape_N-1)*(2,5)[self.stance]+self.shape_type]+=1

    @property
    def abs_material(self):
        return self.shape_N,self.stance,self.shape_type

    @property
    def init_args(self):
        option_p=ParameterSet(OPTION,self.shape_N,self.stance,self.shape_type,self.element_type)

        return self.xyT,self.parents,option_p,self.lineT
