from abc import abstractmethod

from .header import *
from .dimension1 import OneDimensionalAnalyzer
from .parameter_set import ParameterSet
from .element import Element
from .parents import Parents
from .sibling import Sibling

class SpaceChecker(OneDimensionalAnalyzer):
    def scan_space(self,allyL,scan_p):
        for i in range(len(allyL)):
            self.scan_sliced_space(allyL[:i+1],allyL[i]-5,i+1,scan_p)

    def measure_space(self,allyL,last,scan_p):
        exceptL=allyL.copy()
        
        e_left,de_left=map(lambda opt:-self.exclude_check(opt,exceptL,-1,4-last,4,scan_p)+5,(True,False))
        e_right,de_right=map(lambda opt:self.exclude_check(opt,exceptL,1,4-last,6+last,scan_p)+last+5,(True,False))

        r_left,dr_left=map(lambda x:x+self.sixpoint(x-1,scan_p),(e_left,de_left))
        r_right,dr_right=map(lambda x:x-self.sixpoint(x+1,scan_p),(e_right,de_right))

        return exceptL,ParameterSet(MEASURE,e_left,e_right,r_left,r_right,dr_left,dr_right)

    def get_attack_rangeL(self,measure_p):
        opened_rangeL=[*range(measure_p.r_left+1,measure_p.r_right)]
        closed_rangeL=[*range(measure_p.r_left,measure_p.r_right+1)]
        
        return opened_rangeL,closed_rangeL
        
    def get_defense_rangeL(self,measure_p):
        return [*range(measure_p.dr_left,measure_p.dr_right+1)]

    def get_banlist(self,shape_N,scan_p):
        if shape_N==4:
            return [],[]
        
        banL=[i for i,xy in enumerate(scan_p.check_line) if xy in scan_p.space_group.ban_dict]
        
        return ((banL,[]),([],banL))[scan_p.turn]

    def check_banlist(self,banL,shape_N,scan_p):
        return []

    def scan_attack(self,opened_rangeL,closed_rangeL,exceptL,banL,shape_N,scan_p):
        checked_banL=self.check_banlist(banL,shape_N,scan_p)
        checkL=self.index_filter(banL,checked_banL)

        trigger_exceptL=exceptL+checkL
        exceptL=exceptL+banL
        
        OA_L=self.multiple_filter(opened_rangeL,exceptL+banL,checkL,1)
        CA_L=self.index_filter(closed_rangeL,OA_L+exceptL+banL)
        OACA=OA_L+CA_L
        
        OT_L,CT_L=[],[]
        
        for trigger in self.index_filter(opened_rangeL,trigger_exceptL):
            op_targetL=self.index_filter(self.get_validlist(OA_L,4,trigger),exceptL+[trigger])
            cl_targetL=self.index_filter(self.get_validlist(OACA,5,trigger),exceptL+op_targetL+[trigger])
            
            if op_targetL:
                OT_L.append((trigger,op_targetL))
            if cl_targetL:
                CT_L.append((trigger,cl_targetL))

        for trigger in self.index_filter(closed_rangeL,trigger_exceptL):
            targetL=self.index_filter(self.get_validlist(OACA,5,trigger),exceptL+[trigger])

            if targetL:
                CT_L.append((trigger,targetL))

        return OA_L,CA_L,OT_L,CT_L

    def scan_defense(self,defense_rangeL,exceptL,OA_L,scan_p):
        dlen=len(defense_rangeL)
        
        DF1_rangeL=defense_rangeL[dlen-5:5]
        DF3_rangeL=(lambda start,end:defense_rangeL[start:end])(*((dlen-6,6),(0,5))[dlen==5])

        DF1_L,DF2_L=self.index_filter(DF1_rangeL,exceptL),[]
        if not OA_L:DF1_L,DF2_L=DF2_L,DF1_L

        exceptL+=DF1_L+DF2_L

        DF4_L=self.index_filter(DF3_rangeL,exceptL+self.multiple_filter(defense_rangeL,exceptL,OA_L,0))
        DF3_L=self.index_filter(DF3_rangeL,exceptL+DF4_L)
        
        DF5_L=self.index_filter(defense_rangeL,exceptL+DF3_L+DF4_L)

        return DF1_L,DF2_L,DF3_L,DF4_L,DF5_L

    def distribute_attackL(self,attackL,parents,shape_N,scan_p):
        turn=scan_p.turn
        
        self.unpack_indexL(attackL[0],parents,turn,ParameterSet(OPTION,shape_N,ATTACK,OPENED,NORMAL),scan_p)
        self.unpack_indexL(attackL[1],parents,turn,ParameterSet(OPTION,shape_N,ATTACK,CLOSED,NORMAL),scan_p)

        self.unpack_indexL(attackL[2],parents,turn,ParameterSet(OPTION,shape_N,ATTACK,OPENED,TRIGGER),scan_p)
        self.unpack_indexL(attackL[3],parents,turn,ParameterSet(OPTION,shape_N,ATTACK,CLOSED,TRIGGER),scan_p)
        
    def distribute_defenseL(self,defenseL,parents,shape_N,scan_p):
        turn=1-scan_p.turn

        for i in range(5):
            self.unpack_indexL(defenseL[i],parents,turn,ParameterSet(OPTION,shape_N,DEFENSE,i,NORMAL),scan_p)

    def unpack_indexL(self,indexL,parents,option_turn,option_p,scan_p):
        for index in indexL:
            self.set_dimension1_element(index,parents,option_turn,option_p,scan_p)

    def set_dimension1_element(self,index,parents,option_turn,option_p,scan_p):
        xyT,element_obj=self.get_element_obj(index,parents,option_p,scan_p)

        space_dict=scan_p.space_group.turn_member(option_turn).D1
        space_dict.update_key(xyT,self.space_obj,p=(xyT,option_turn,scan_p.space_group))

        sibling_key=parents.sibling_key
        sibling_dict=scan_p.space_group.sibling_dict
        sibling_dict.update_key(sibling_key,Sibling)

        space_dict[xyT].add_element(element_obj)
        sibling_dict[sibling_key].add_element(xyT,option_p)

    def get_element_obj(self,index,parents,option_p,scan_p):
        if option_p.element_type==NORMAL:
            return self.get_normal_obj(index,parents,option_p,scan_p)

        elif option_p.element_type==TRIGGER:
            return self.get_trigger_obj(index,parents,option_p,scan_p)

    def get_normal_obj(self,index,parents,option_p,scan_p):
        xyT=scan_p.check_line[index]

        element=Element(xyT,parents,option_p,scan_p.lineT)

        return xyT,element

    def get_trigger_obj(self,index,parents,option_p,scan_p):
        index,targetL=index
        xyT=scan_p.check_line[index]
        targetL=[scan_p.check_line[x]for x in targetL]

        element=Element(xyT,parents,option_p,scan_p.lineT)
        element.set_targetL(targetL)

        return xyT,element

    def exclude_check(self,option,exceptL,direction,iterate,start,scan_p):
        result=0
        for i in range(iterate):
            if self.exclude(direction*i+start,option,exceptL,scan_p):
                result+=1
            else:
                break
        return result

    def exclude(self,index,option,exceptL,scan_p):
        xyT=scan_p.check_line[index]
        result=not ((xyT in scan_p.stone.entire)+(xyT in scan_p.stone.edge))
        if not option and xyT in scan_p.stone.turn_member(scan_p.turn):
            exceptL.append(index)
            result=1
        return result

    def sixpoint(self,index,scan_p):
        xyT=scan_p.check_line[index]
        if scan_p.turn==WHITE:
            return False
        return xyT in scan_p.stone.turn_member(scan_p.turn)

    def multiple_filter(self,rangeL,exceptL,checkL,check_val):
        result=[]
        for i in range(len(rangeL)-3):
            tL=rangeL[i:i+4]
            check=check_val
            for c in checkL:
                if c in tL:
                    check=1-check
                    break
            if check:
                result+=self.index_filter(tL,exceptL+result)
        return result

    def trigger_filter(self,opened_rangeL,closed_rangeL,banL,checkL,exceptL):
        OT_L,CT_L=[],[]
        
        for trigger in opened_indexL:
            op_targetL=self.index_filter(self.get_validlist(OA_L,4,trigger),exceptL+[trigger])
            cl_targetL=self.index_filter(self.get_validlist(OACA,5,trigger),exceptL+op_targetL+[trigger])
            
            if op_targetL:
                OT_L.append((trigger,op_targetL))
            if cl_targetL:
                CT_L.append((trigger,cl_targetL))

        for trigger in CA_L:
            targetL=self.index_filter(self.get_validlist(OACA,5,trigger),exceptL+[trigger])

            if targetL:
                CT_L.append((trigger,targetL))

        return OT_L,CT_L

    def index_filter(self,indexL,targetL):
        return list(filter(lambda index:index not in targetL,indexL))

    def get_validlist(self,indexL,rangeN,head):
        return [x for x in indexL if abs(head-x)<rangeN]

    @abstractmethod
    def check_stone(self,allyL,scan_p):
        pass

    @abstractmethod
    def distribute_space(self,exceptL,allyL,shape_N,measure_p,scan_p):
        pass

    @abstractmethod
    def get_stanceL(self,measure_p,allyL,exceptL,shape_N,scan_p):
        pass

    
    

    
