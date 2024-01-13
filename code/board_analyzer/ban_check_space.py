from .header import *
from .space import Space

class BanCheckSpace(Space):
    def __init__(self,*p):
        super().__init__(*p)
        self.ban_name=None
        self.release_val=False

    def add_element(self,new_e):
        if self.check_parents_nest(new_e) or self.six_check(new_e):
            return
        
        self.elementL.append(new_e)

    def six_check(self,e):
        if e.shape_N==-1:
            self.set_ban_space(self.xyT,6)
    
    def nest_element(self,e1,e2):
        if self.line_check(e1,e2):
            return

        if e1.lineT==e2.lineT:
            return

        self.ban_nest(e1,e2)

    def line_nest(self,e1,e2):
        if not self.line_check(e1,e2):
            return False
        
        if self.double_check(e1,e2,shape_N=3):
            self.set_ban_space(self.xyT,44)
            return True

        return False
    
    def linear_44(self,e1,e2,diff_set1,diff_set2):
        self.set_ban_space(self.xyT,44)

        return 1
            
    def get_bancheck_space(self,xyT):
        check_dict=self.space_group.black.check_dict
        check_dict.update_key(xyT,BanCheckSpace,p=(xyT,self.turn,self.space_group))

        return check_dict[xyT]

    def set_ban_space(self,xyT,ban_name):
        ban_space=self.get_bancheck_space(self.xyT)
        ban_space.ban_name=ban_name

    def ban_nest(self,e1,e2):
        if not self.normal_nest_check(e1,e2) and self.double_check(e1,e2,stance=ATTACK):
            return

        if self.double_check(e1,e2,shape_N=2,shape_type=OPENED):
            self.set_ban_space(self.xyT,33)

        elif self.double_check(e1,e2,shape_N=3):
            self.set_ban_space(self.xyT,44)
