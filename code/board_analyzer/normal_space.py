import numpy as np

from .header import *
from .space import Space
from .element import Element

class NormalSpace(Space):
    def add_element(self,new_e):
        if self.check_parents_nest(new_e):
            return

        self.max_abs=max(self.max_abs,self.get_origin_abs(new_e))
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
            
        '''
        if self.double_check(e1,e2,stance=DEFENSE):
            self.defense_nest(e1,e2)
        '''

    def normal_trigger_nest(self,e1,e2):
        if not ((e1.element_type,e2.element_type) in ((NORMAL,TRIGGER),(TRIGGER,NORMAL)) and \
                self.double_check(e1,e2,stance=ATTACK)):
            return

        normal,trigger=((e1,e2),(e2,e1))[e1.element_type==TRIGGER]

        if self.get_predict_abs(normal)<self.get_predict_abs(trigger):
            return

        if self.turn==BLACK and tuple(map(lambda e:(e.shape_N,e.shape_type),(normal,trigger))) \
                                in (((2,0),(1,0)),((3,1),(2,1))):
            return

        self.activate_trigger(normal,trigger)
    
    def attack_nest(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(self.get_origin_abs(e),e.shape_N,-e.shape_type))
        
        t=((e1.shape_N,e1.shape_type),(e2.shape_N,e2.shape_type))
        
        if e1.shape_N==2 and e1.shape_type==0 and e2.shape_N==3:
            self.max_abs=max(self.max_abs,5)
            self.defense_nest(4)

        elif self.double_check(e1,e2,shape_N=3,shape_type=CLOSED):
            self.max_abs=max(self.max_abs,5*self.turn)
            self.defense_nest(4*(self.turn))

        elif self.double_check(e1,e2,shape_N=4):
            self.defense_nest(8*(self.turn))

        elif self.double_check(e1,e2,shape_N=2,shape_type=OPENED):
            self.max_abs=max(self.max_abs,2*self.turn)
            self.defense_nest(1.5*(self.turn))
    '''
    def attack_nest(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_val,e.shape_N,-e.shape_type))

        self.max_abs=max(self.max_abs,self.get_nest_abs(e1,e2))
    '''
    '''
    def defense_nest(self,e1,e2):
        nest_abs=self.get_nest_abs(e1,e2)

        if not nest_abs:
            return

        #candidate_space=
        #cal_candidate_space

        if candidate_state==CASE1:
            for xyT in candidate_space:
                #xyT space <- nest_abs

        elif candidate_state==CASE2:
            self.max_abs=max(self.max_abs,nest_abs+1)

        if CASE1 or CASE2:
            self.defense_nest_val=True
            
    '''
    def defense_nest(self,absN):
        defense_space=self.get_space(self.xyT,1)
        defense_space.max_abs=max(defense_space.max_abs,absN)

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

        self.adjust_abs(e1,e2)
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
        
        space_dict=self.space_group.turn_member(turn).D1
        space_dict.update_key(xyT,NormalSpace,p=(xyT,turn,self.space_group))

        return space_dict[xyT]

    def get_element_abs(self,shape_N,stance,shape_type):
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

    def get_origin_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N,stance,shape_type)

    def get_predict_abs(self,e):
        shape_N,stance,shape_type=e.abs_material

        return self.get_element_abs(shape_N+1,stance,shape_type)

    def get_nest_abs(self,e1,e2):
        return min(self.predict_abs(e1),self.predict_abs(e2)-VAL_DISTANCE)

    @property
    def space_matrix(self):
        array=np.zeros(MATRIX_SIZE)
        array[0]=self.max_abs

        for element in self.elementL:
            element.set_matrix(array)

        return array
