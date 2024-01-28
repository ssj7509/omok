import numpy as np

from .header import *
from .space import Space
from .element import Element

class NormalSpace(Space):
    def set_max_abs(self,abs_val):
        self.max_abs=max(self.max_abs,abs_val)
    
    def add_element(self,new_e):
        if self.check_parents_nest(new_e):
            return

        if new_e.element_type==NORMAL:
            self.set_max_abs(self.origin_abs(new_e))

        self.space_group.update_sibling(new_e)
        
        self.elementL.append(new_e)
    
    def add_trigger(self,e):
        if e.element_type==TRIGGER:
            self.triggerL.append(e)
            self.target_set.update(e.targetL)

    def nest_element(self,e1,e2):
        if self.turn==WHITE and self.line_nest(e1,e2):
            return

        if e1.lineT==e2.lineT:
            return

        self.normal_nest(e1,e2)
        self.normal_trigger_nest(e1,e2)

    def normal_nest(self,e1,e2):
        if not self.double_check(e1,e2,element_type=NORMAL):
            return

        if self.double_check(e1,e2,stance=ATTACK):
            self.attack_nest(e1,e2)
        
    def normal_trigger_nest(self,e1,e2):
        if not ((e1.element_type,e2.element_type) in ((NORMAL,TRIGGER),(TRIGGER,NORMAL)) and \
                self.double_check(e1,e2,stance=ATTACK)):
            return

        normal,trigger=((e1,e2),(e2,e1))[e1.element_type==TRIGGER]

        if self.predict_attack_abs(normal)<self.predict_attack_abs(trigger):
            return

        if self.turn==BLACK and tuple(map(lambda e:(e.shape_N,e.shape_type),(normal,trigger))) \
                                in (((2,0),(1,0)),((3,1),(2,1))):
            return

        self.activate_trigger(normal,trigger)
   
    def attack_nest(self,e1,e2):
        e1_abs,e2_abs=map(self.predict_attack_abs,(e1,e2))

        nest_abs=self.predict_nest_abs(e1_abs,e2_abs)
        self.set_max_abs(nest_abs)
        
        if nest_abs>DEFAULT_ABS:
            self.defense_nest(e1,e2)

    def defense_nest(self,e1,e2):
        e1_abs,e2_abs=map(self.predict_defense_abs,(e1,e2))

        nest_abs=self.predict_nest_abs(e1_abs,e2_abs)
        
        candidates=self.get_candidates(e1,e2)
        checked_candidates=self.check_candidates(e1,e2,candidates)

        if not checked_candidates:
            return

        if len(candidates)!=len(checked_candidates):
            nest_abs+=1
        
        self.set_candidates_abs(checked_candidates,nest_abs)

    def set_candidates_abs(self,candidates,nest_abs):
        for candidate in candidates:
            candidate_space=self.get_space(candidate,1)
            candidate_space.set_max_abs(nest_abs)
      
    def get_candidates(self,e1,e2):
        e1_defense,e2_defense=map(lambda e:e.get_entire_defense_sibling(),(e1,e2))

        return e1_defense|e2_defense|{self.xyT}

    def check_candidates(self,e1,e2,candidates):
        checked=[]
        
        for candidate in candidates:
            if self.defense_predict_check(e1,e2,candidate)==DEFAULT_ABS:
                checked.append(candidate)
            
        return checked

    def defense_predict_check(self,e1,e2,candidate):
        e1_predict_abs,e1_defensed=self.predict_defense_element(e1,candidate)
        e2_predict_abs,e2_defensed=self.predict_defense_element(e2,candidate)

        nest_abs=self.predict_nest_abs(e1_predict_abs,e2_predict_abs)

        e1_abs=DEFAULT_ABS if e1_defensed else self.max_attack_abs(e1)
        e2_abs=DEFAULT_ABS if e2_defensed else self.max_attack_abs(e2)

        return max(e1_abs,e2_abs,nest_abs)

    def predict_defense_element(self,e,candidate):#attack predict abs
        predict_abs=self.predict_attack_abs(e)
        defensed=False

        if candidate in e.get_complete_defense_sibling():
            predict_abs=DEFAULT_ABS
            defensed=True

        if candidate in e.get_incomplete_defense_sibling():
            predict_abs=self.check_defense_vector(e,candidate)
            defensed=True
            
        if candidate not in e.get_entire_defense_sibling() and self.xyT==candidate:
            predict_abs=DEFAULT_ABS

        return predict_abs,defensed

    def check_defense_vector(self,e,candidate):
        parents_point=e.parents[0]
        
        standard_vector=self.get_space_vector(parents_point,self.xyT)
        candidate_vector=self.get_space_vector(parents_point,candidate)

        parents_start=e.parents[0]
        parents_end=e.parents[1]

        left_vector=self.get_space_vector(parents_start,self.xyT)
        right_vector=self.get_space_vector(parents_end,self.xyT)

        standard_vector=self.get_space_vector(parents_start,self.xyT)
        candidate_vector=self.get_space_vector(parents_start,candidate)

        if left_vector==right_vector and standard_vector==candidate_vector:
            return DEFAULT_ABS

        return self.predict_closed_abs(e)

    def get_space_vector(self,parents_xyT,space_xyT):
        x1,y1=parents_xyT
        x2,y2=space_xyT

        r1,r2=map(lambda p1,p2:(0,(-1,1)[p2-p1>0])[p2-p1!=0],(x1,y1),(x2,y2))

        return r1,r2

    def line_nest(self,e1,e2):
        if not self.line_check(e1,e2):
            return False
        
        if self.double_check(e1,e2,shape_N=3):
            return self.line_44(e1,e2)

        else:
            return self.line_build_3(e1,e2)

    def line_44(self,e1,e2):
        if self.turn==BLACK:
            return False

        self.attack_nest(e1,e2)
        
        return True
        
    def line_build_3(self,e1,e2):
        e1_targetS,e2_targetS,diff_set1,diff_set2=self.get_target_set(e1,e2)
        
        inter_set=e1_targetS&e2_targetS
        
        v1,v2=map(lambda e,ds:len(ds)-1+len(inter_set)>=3-e.shape_N,(e1,e2),(diff_set1,diff_set2))

        if not (v1 and v2):
            return False

        S1,S2=map(lambda ds:(set(),ds)[len(ds)>=2],(diff_set1,diff_set2))
        targetS=inter_set|S1|S2

        for target in targetS:
            self.activate_target(e1,target)
            self.activate_target(e2,target)

        return True

    def activate_trigger(self,transfer_obj,trigger):
        for target in trigger.targetL:
            self.activate_target(transfer_obj,target)

    def activate_target(self,transfer_obj,target_xyT):
        target_space=self.get_space(target_xyT,0)
        target_init_args=transfer_obj.init_args

        target_element=Element(*target_init_args)
        target_element.element_type=TARGET

        target_space.add_element(target_element)
    
    def get_space(self,xyT,option):
        turn=option^self.turn
        
        self.space_group.update_space(xyT,turn,NormalSpace)

        return self.space_group.get_space(xyT,turn)

    def get_element_abs(self,shape_N,stance,shape_type):
        r=DEFAULT_ABS

        if shape_N==5 and stance==ATTACK:
            r=16
        elif shape_N==5 and stance==DEFENSE:
            r=14
        elif shape_N==4 and stance==ATTACK:
            r=12
        elif shape_N==4 and stance==DEFENSE:
            r=10
        elif shape_N==3 and stance==ATTACK and shape_type==OPENED:
            r=8
        elif shape_N==3 and stance==DEFENSE and shape_type in (DEFENSE1,DEFENSE3):
            r=6

        return r    

    def origin_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N,stance,shape_type)

    def max_attack_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        if e.get_opened_attack_sibling():
            shape_type=OPENED

        return self.get_element_abs(shape_N,stance,shape_type)

    def predict_attack_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N+1,stance,shape_type)

    def predict_defense_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N+1,DEFENSE,shape_type)

    def predict_closed_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N+1,stance,CLOSED)

    def predict_nest_abs(self,abs1,abs2):
        abs1,abs2=sorted((abs1,abs2))
        
        return max(DEFAULT_ABS,min(abs1,abs2-ABS_DISTANCE))

    @property
    def space_matrix(self):
        array=np.zeros(MATRIX_SIZE)
        array[0]=self.max_abs

        for element in self.elementL:
            element.set_matrix(array)

        return array
