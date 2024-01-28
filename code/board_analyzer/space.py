from abc import ABC,abstractmethod

from .header import *

class Space(ABC):
    def __init__(self,xyT,turn,space_group):
        self.xyT=xyT
        self.space_group=space_group
        self.turn=turn
        self.elementL=[]
        self.triggerL=[]
        self.trigger_valueL=[]
        self.target_set=set()
        self.max_abs=0

    def check_parents_nest(self,new_e):
        deleteL=[]
        
        for old_e in self.elementL:
            if self.parents_nest(old_e,new_e,deleteL):
                return True
            
        for de in deleteL:
            del self.elementL[self.elementL.index(de)]

        return False

    def parents_nest(self,e1,e2,deleteL):
        if e1.compare_parents(e2) or \
            not self.compare_attribute(e1,e2,lambda e:(e.element_type,e.stance)) \
            or e1.element_type==TRIGGER: 
            return False

        te1,te2=self.get_sorted_element(e1,e2)

        if e1 is te1:
            deleteL.append(e1)
            return False

        return True
        
    def set_element(self):
        e_len=len(self.elementL)
        
        for i in range(e_len):
            for j in range(i+1,e_len):
                self.nest_element(self.elementL[i],self.elementL[j])

    def normal_nest_check(self,e1,e2):
        if self.double_check(e1,e2,element_type=NORMAL):
            return True

        return False

    def line_check(self,e1,e2):
        if not (self.double_check(e1,e2,shape_type=CLOSED,element_type=TRIGGER) \
           and self.compare_attribute(e1,e2,lambda e:e.lineT)):
            return False

        e1_targetS,e2_targetS,diff_set1,diff_set2=self.get_target_set(e1,e2)

        if not (bool(diff_set1) and bool(diff_set2)):
            return False

        return True

    def get_target_set(self,e1,e2):
        e1_targetS,e2_targetS=map(lambda e:set(e.targetL),(e1,e2))

        diff_set1,diff_set2=e1_targetS-e2_targetS,e2_targetS-e1_targetS

        return e1_targetS,e2_targetS,diff_set1,diff_set2

    def double_check(self,e1,e2,**kwargs):
        return all(map(lambda e:all(getattr(e,k)==kwargs[k]for k in kwargs),(e1,e2)))

    def compare_attribute(self,e1,e2,func):
        return (lambda r1,r2:r1==r2)(*map(lambda e:func(e),(e1,e2)))

    def get_sorted_element(self,e1,e2):
        return sorted((e1,e2),key=lambda e:(e.shape_N,-e.shape_type))

    @abstractmethod
    def add_element(self,new_e):
        pass

    @abstractmethod
    def nest_element(self,e1,e2):
        pass

    @abstractmethod
    def line_nest(self,e1,e2):
        pass

