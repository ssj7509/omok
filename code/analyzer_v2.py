from header import *
import numpy as np
#sys.setrecursionlimit(100000000)

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

    def get_parents_key(self):
        return self.parents,self.lineT
    
    def get_parameter_set(self):
        option_p=Parameter_set(self.shape_N,self.stance,self.shape_type,self.element_type)

        return self.xyT,self.parents,option_p,self.lineT

    def set_matrix(self,array):
        if self.element_type in (NORMAL,TARGET):
            array[1+self.stance*10+(self.shape_N-1)*(2,5)[self.stance]+self.shape_type]+=1

class Space:
    def __init__(self,xyT,turn,turn_group):
        self.xyT=xyT
        self.turn_group=turn_group
        self.turn=turn
        self.objL=[]
        self.elementL=[]
        self.triggerL=[]
        self.trigger_valueL=[]
        self.target_set=set()
        self.max_abs=0

    def set_element(self):
        for obj in self.objL:
            self.add_element(obj)

        self.objL.clear()

    def add_element(self,new_e):
        if new_e.element_type!=TARGET:
            self.max_abs=max(self.max_abs,new_e.abs_val)
        
        deleteL=[]
        
        for old_e in self.elementL:
            if self.nest_element(old_e,new_e,deleteL):
                return
            
        for de in deleteL:
            del self.elementL[self.elementL.index(de)]
        
        self.elementL.append(new_e)

    def add_obj(self,new_e):    
        self.objL.append(new_e)
    
    def add_trigger(self,e):
        if e.element_type==TRIGGER:
            self.triggerL.append(e)
            self.target_set.update(e.targetL)

    def nest_element(self,e1,e2,deleteL):
        delete_val=self.parents_nest(e1,e2,deleteL)
            
        if delete_val:
            return delete_val-1
        
        if self.turn==WHITE and self.linear_nest(e1,e2):
            return

        if e1.lineT==e2.lineT:
            return

        self.normal_nest(e1,e2)

        self.normal_trigger_nest(e1,e2)

    def normal_nest(self,e1,e2):
        if double_check(e1,e2,lambda x:x.element_type==NORMAL and x.stance==ATTACK):
            self.adjust_abs(e1,e2)

    def normal_trigger_nest(self,e1,e2):
        if not ((e1.element_type,e2.element_type) in ((NORMAL,TRIGGER),(TRIGGER,NORMAL)) and \
                double_check(e1,e2,lambda x:x.stance==ATTACK)):
            return

        normal,trigger=((e1,e2),(e2,e1))[e1.element_type==TRIGGER]

        if self.get_predict_abs(normal)<self.get_predict_abs(trigger):
            return

        if self.turn==BLACK and tuple(map(lambda e:(e.shape_N,e.shape_type),(normal,trigger))) \
                                in (((2,0),(1,0)),((3,1),(2,1))):
            return

        self.activate_trigger(normal,trigger)
    
    def get_predict_abs(self,e):
        return Element.get_abs_val(None,e.shape_N+1,e.stance,e.shape_type)
    
    def adjust_abs(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_val,e.shape_N,-e.shape_type))
        
        t=((e1.shape_N,e1.shape_type),(e2.shape_N,e2.shape_type))
        
        if e1.shape_N==2 and e1.shape_type==0 and e2.shape_N==3:
            self.max_abs=max(self.max_abs,5)
            self.defense_nest(4)

        elif double_check(e1,e2,lambda x:x.shape_N==3 and x.shape_type==CLOSED):
            self.max_abs=max(self.max_abs,5*self.turn)
            self.defense_nest(4*(self.turn))

        elif double_check(e1,e2,lambda x:x.shape_N==4):
            self.defense_nest(8*(self.turn))

        elif double_check(e1,e2,lambda x:x.shape_N==2 and x.shape_type==OPENED):
            self.max_abs=max(self.max_abs,2*self.turn)
            self.defense_nest(1.5*(self.turn))

    def defense_nest(self,absN):
        defense_space=self.get_space(self.xyT,1)
        defense_space.max_abs=max(defense_space.max_abs,absN)

    def parents_nest(self,e1,e2,deleteL):
        if compare_parents(e1.parents,e2.parents) or \
           not compare_contents(e1,e2,lambda x:(x.element_type,x.stance)):
            return

        if e1.element_type==TRIGGER:
            return self.trigger_parents_nest(e1,e2)

        te1,te2=self.get_sorted_element(e1,e2)

        if e1 is te1:
            deleteL.append(e1)
            return 1

        return 2

    def trigger_parents_nest(self,e1,e2):
        e1,e2=self.get_sorted_element(e1,e2)

        e1.targetL=[*(set(e1.targetL)-set(e2.targetL))]

    def linear_nest(self,e1,e2):
        if not (double_check(e1,e2,lambda x:x.shape_type==CLOSED and x.element_type==TRIGGER) \
           and compare_lineT(e1,e2)):
            return
        
        e1_targetS,e2_targetS=map(lambda e:set(e.targetL),(e1,e2))

        diff_set1,diff_set2=e1_targetS-e2_targetS,e2_targetS-e1_targetS
        inter_set=e1_targetS&e2_targetS

        if not (bool(diff_set1) and bool(diff_set2)):
            return
        
        if double_check(e1,e2,lambda x:x.shape_N==3):
            return self.linear_44(e1,e2,diff_set1,diff_set2)

        else:
            return self.linear_build_3(e1,e2,diff_set1,diff_set2,inter_set)

    def linear_44(self,e1,e2,diff_set1,diff_set2):
        if self.turn==BLACK:
            return

        self.adjust_abs(e1,e2)
        return 1
        
    def linear_build_3(self,e1,e2,diff_set1,diff_set2,inter_set):
        v1,v2=map(lambda e,ds:len(ds)-1+len(inter_set)>=3-e.shape_N,(e1,e2),(diff_set1,diff_set2))

        if not (v1 and v2):
            return

        S1,S2=map(lambda ds:(set(),ds)[len(ds)>=2],(diff_set1,diff_set2))
        targetS=inter_set|S1|S2

        for target in targetS:
            self.activate_target(e1,target)
            self.activate_target(e2,target)

        return 1

    def activate_trigger(self,transfer_obj,trigger):
        for target in trigger.targetL:
            self.activate_target(transfer_obj,target)

    def activate_target(self,transfer_obj,target_xyT):
        target_space=self.get_space(target_xyT,0)
        target_p=transfer_obj.get_parameter_set()

        target_element=Element(*target_p)
        target_element.element_type=TARGET

        target_space.add_element(target_element)
    
    def get_space(self,xyT,option):
        turn=option^self.turn
        space_dict=self.turn_group[turn].D1
        if not space_dict.get(xyT):
            space_dict[xyT]=Space(xyT,turn,self.turn_group)

        return space_dict[xyT]

    def get_sorted_element(self,e1,e2):
        return sorted((e1,e2),key=lambda e:(e.shape_N,-e.shape_type))

    def get_space_matrix(self):
        array=np.zeros(36)
        array[0]=self.max_abs

        for element in self.elementL:
            element.set_matrix(array)

        return array

class Bancheck_space(Space):
    def __init__(self,*p):
        super().__init__(*p)
        self.ban_name=None

    def add_element(self,new_e):
        
        if self.six_check(new_e):
            return
        
        check=0
        for old_e in self.elementL:
            
            if self.nest_element(old_e,new_e):
                return
        
        self.elementL.append(new_e)

    def six_check(self,e):
        if e.shape_N==-1:
            self.set_ban_space(self.xyT,6)
    
    def nest_element(self,e1,e2):
        if self.linear_nest(e1,e2):
            return

        if e1.lineT==e2.lineT:
            return

        self.normal_nest(e1,e2)
    
    def linear_44(self,e1,e2,diff_set1,diff_set2):
        self.set_ban_space(self.xyT,44)

        return 1
            
    def get_bancheck_space(self,xyT):
        check_dict=self.turn_group[BLACK].check_dict

        if not check_dict.get(xyT):
            check_dict[xyT]=Bancheck_space(xyT,self.turn,self.turn_group)

        return check_dict[xyT]

    def linear_build_3(self,e1,e2,diff_set1,diff_set2,inter_set):
        return 1

    def activate_trigger(self,transfer_obj,trigger):
        return

    def activate_target(self,transfer_obj,target_xyT):
        return

    def set_ban_space(self,xyT,ban_name):
        ban_space=self.get_bancheck_space(self.xyT)
        ban_space.ban_name=ban_name

    def adjust_abs(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_val,e.shape_N,-e.shape_type))
        
        t=((e1.shape_N,e1.shape_type),(e2.shape_N,e2.shape_type))

        if t==((2,0),(2,0)):
            self.set_ban_space(self.xyT,33)
        elif double_check(e1,e2,lambda x:x.shape_N==3 and x.shape_type in (0,1)):
            self.set_ban_space(self.xyT,44)

class Parents:
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

class Stone_group:
    def __init__(self):
        self.black={}
        self.white={}
        self.edge={}
        self.entire={}

    def turn_dict(self,turn):
        return (self.black,self.white)[turn]

class Space_group:
    def __init__(self,parents_dict,ban_dict):
        self.D1={}
        self.D2={}
        self.D3={}
        self.parents_dict=parents_dict
        self.ban_dict=ban_dict

    def set_check_dict(self):
        self.check_dict={}

class Parameter_set:
    def __init__(self,*p):
        if len(p)==7:
            self.set_scan_value(*p)

        elif len(p)==4:
            self.set_option_value(*p)
    
    def set_scan_value(self,run_mode,check_line,stone,turn,turn_group,result_target,lineT):
        self.update_parameter(locals())

    def set_option_value(self,shape_N,stance,shape_type,element_type):
        self.update_parameter(locals())

    def update_parameter(self,local_dict):
        self.__dict__.update(local_dict)

    def get_parameters(self):
        return tuple(self.__dict__.values())

def get_turn_group(ban_dict,option):
    parents_dict={}
    
    turn_group=[Space_group(parents_dict,ban_dict),Space_group(parents_dict,ban_dict)]

    if option:
        turn_group[BLACK].set_check_dict()
        turn_group[WHITE].set_check_dict()
        
    return turn_group

def set_stone(record_List):
    stone=Stone_group()

    for i in range(16):
        stone.edge[(i-1,-1)]=1
        stone.edge[(i,15)]=1
        stone.edge[(-1,i)]=1
        stone.edge[(15,i-1)]=1

    for i,(x,y) in enumerate(record_List):
        stone.turn_dict(i%2)[(x-1,y-1)]=1
        stone.entire[(x-1,y-1)]=1
        
    return stone

def main_play(record_List):
    stone=set_stone(record_List)
    turn=len(stone.entire)%2

    turn_group=Dimension_2(stone,turn)
    
    return turn_group,turn

def get_result(space_dict):
    spaceL=space_dict.values()
    max_abs=max(space.max_abs for space in spaceL)

    candidate_spaceL=[space for space in spaceL if space.max_abs==max_abs]

    return ([space.xyT for space in candidate_spaceL],
            tuple([space.get_space_matrix()for space in candidate_spaceL]))
    
def Dimension_2(stone,turn):
    ban_dict=ban_check(stone)
 
    turn_group=get_turn_group(ban_dict,False)
    
    Dimension_1(turn_group,stone.turn_dict(turn).keys(),stone,D1,turn,D1_NORMAL)
    Dimension_1(turn_group,stone.turn_dict(1-turn).keys(),stone,D1,1-turn,D1_NORMAL)

    set_D1_space(turn_group)

    return turn_group

def set_D1_space(turn_group):
    for space in turn_group[BLACK].D1.values():
        space.set_element()

    for space in turn_group[WHITE].D1.values():
        space.set_element()

def update_D1_trigger(space_dict):
    search_set=set()

    for trigger_xyT,obj in space_dict.items():
        search_set.update((trigger_xyT,target)for target in obj.target_set if space_dict.get(target))

    while search_set:
        trigger,target=next(iter(search_set))
        valueL=space_dict[trigger].trigger_valueL
        
        trigger_DFS(search_set,space_dict,trigger,target,valueL)

def trigger_DFS(search_set,space_dict,trigger,target,valueL):
    search_set.discard((trigger,target))
    
    trigger,obj=target,space_dict[target]
    targetL=[*obj.target_set]
    
    if update_valueL(valueL):
        search_set.update((trigger,target)for target in targetL)

    if (trigger,target) not in search_set:
        return

    for target in targetL:
        trigger_DFS(search_set,space_dict,trigger,target,valueL)

def update_valueL(valueL):
    pass

def end_check(record_List):
    stone=set_stone(record_List)
    turn=len(stone.entire)%2

    end_turn_group=get_turn_group({},True)
    
    Dimension_1(end_turn_group,stone.turn_dict(turn).keys(),stone,D1,turn,END_CHECK)
    Dimension_1(end_turn_group,stone.turn_dict(1-turn).keys(),stone,D1,1-turn,END_CHECK)

    return list(map(lambda turn:end_turn_group[turn].check_dict,(BLACK,WHITE)))

def ban_check(stone):
    ban_turn_group=get_turn_group({},True)

    Dimension_1(ban_turn_group,stone.turn_dict(BLACK).keys(),stone,D1,BLACK,BAN_CHECK)

    set_D1_space(ban_turn_group)
    
    return ban_turn_group[BLACK].check_dict

def get_checkline(xyT):
    x,y=xyT
    check_line=[[],[],[],[]]

    for i in range(11):
        check_line[0].append((x+i-5,y))
        check_line[1].append((x,y+i-5))
        check_line[2].append((x+i-5,y+i-5))
        check_line[3].append((x+i-5,y-i+5))

    return check_line

def Dimension_1(turn_group,check_list,stone,result_target,turn,run_mode):
    for xyT in check_list:
        check_line=get_checkline(xyT)

        for i in range(4):
            scan_p=Parameter_set(run_mode,check_line[i],stone,turn,
                                 turn_group,result_target,min_line((*xyT,i)))
            scan_stone(scan_p)

def scan_stone(scan_p):
    allyL,last=get_ally(scan_p)
    shape_N=len(allyL)

    run_mode=scan_p.run_mode

    if run_mode in (D1_0,D2_0) and shape_N!=1:
        return

    if run_mode==BAN_CHECK and shape_N==1:
        return

    if run_mode==END_CHECK:
        end_game(allyL,shape_N,scan_p)
        return

    for i in range(len(allyL)):
        scan_space(allyL[:i+1],allyL[i]-5,i+1,scan_p)
    
def scan_space(allyL,last,shape_N,scan_p):
    exceptL=allyL.copy()

    e_left,e_right,r_left,r_right, \
    de_left,de_right,dr_left,dr_right=measure_space(exceptL,last,scan_p)

    if (e_right-e_left<4) or (scan_p.run_mode!=BAN_CHECK and r_right-r_left<4):
        return

    stanceL,shape_N=get_valid_stanceL(r_left,r_right,dr_left,dr_right,allyL,exceptL,shape_N,scan_p)

    parents=get_parents(allyL,scan_p.check_line)

    distribute_stanceL(stanceL,parents,shape_N,scan_p)

def measure_space(exceptL,last,scan_p):
    e_left,de_left=map(lambda opt:-exclude_check(opt,exceptL,-1,4-last,4,scan_p)+5,(True,False))
    e_right,de_right=map(lambda opt:exclude_check(opt,exceptL,1,4-last,6+last,scan_p)+last+5,(True,False))

    r_left,dr_left=map(lambda x:x+sixpoint(x-1,scan_p),(e_left,de_left))
    r_right,dr_right=map(lambda x:x-sixpoint(x+1,scan_p),(e_right,de_right))

    return e_left,e_right,r_left,r_right,de_left,de_right,dr_left,dr_right

def get_valid_stanceL(r_left,r_right,dr_left,dr_right,allyL,exceptL,shape_N,scan_p):
    run_mode=scan_p.run_mode
    
    opened_rangeL=[*range(r_left+1,r_right)]
    closed_rangeL=[*range(r_left,r_right+1)]
    drangeL=[*range(dr_left,dr_right+1)]

    banL=get_banlist(opened_rangeL,scan_p)
    checked_banL=check_banlist(banL,shape_N,scan_p)

    if run_mode==BAN_CHECK and shape_N==4 and sixpoint(10,scan_p): #shape_N 3
        closed_rangeL=[*range(5,10)]
        shape_N=-1

    if run_mode in (D1_0,D2_0):
        allyL.clear()
        shape_N=0

    attackL=scan_attack(opened_rangeL,closed_rangeL,exceptL+banL,checked_banL,scan_p)
    defenseL=scan_defense(drangeL,exceptL+banL,attackL[0],scan_p)

    return [attackL,defenseL],shape_N

def scan_attack(opened_rangeL,closed_rangeL,exceptL,checkL,scan_p):
    OA_L=multiple_filter(opened_rangeL,exceptL,checkL,1)
    CA_L=index_filter(closed_rangeL,OA_L+exceptL)
    
    OT_L,CT_L=trigger_filter(OA_L,CA_L,exceptL)

    return OA_L,CA_L,OT_L,CT_L

def scan_defense(drangeL,exceptL,OA_L,scan_p):
    dlen=len(drangeL)
    
    DF1_rangeL=drangeL[dlen-5:5]
    DF3_rangeL=(lambda start,end:drangeL[start:end])(*((dlen-6,6),(0,5))[dlen==5])

    DF1_L,DF2_L=index_filter(DF1_rangeL,exceptL),[]
    if not OA_L:DF1_L,DF2_L=DF2_L,DF1_L

    exceptL+=DF1_L+DF2_L

    DF4_L=index_filter(DF3_rangeL,exceptL+multiple_filter(drangeL,exceptL,OA_L,0))
    DF3_L=index_filter(DF3_rangeL,exceptL+DF4_L)
    
    DF5_L=index_filter(drangeL,exceptL+DF3_L+DF4_L)

    return DF1_L,DF2_L,DF3_L,DF4_L,DF5_L

def distribute_stanceL(stanceL,parents,shape_N,scan_p):
    attackL,defenseL=stanceL
    
    turn=scan_p.turn

    unpack_indexL(attackL[0],parents,turn,Parameter_set(shape_N,ATTACK,OPENED,NORMAL),scan_p)
    unpack_indexL(attackL[1],parents,turn,Parameter_set(shape_N,ATTACK,CLOSED,NORMAL),scan_p)

    unpack_indexL(attackL[2],parents,turn,Parameter_set(shape_N,ATTACK,OPENED,TRIGGER),scan_p)
    unpack_indexL(attackL[3],parents,turn,Parameter_set(shape_N,ATTACK,CLOSED,TRIGGER),scan_p)
    
    if scan_p.run_mode in (BAN_CHECK,D2_0):
        return

    for i in range(5):
        unpack_indexL(defenseL[i],parents,1-turn,Parameter_set(shape_N,DEFENSE,i,NORMAL),scan_p)

def unpack_indexL(indexL,parents,option_turn,option_p,scan_p):
    if scan_p.run_mode in (D1_NORMAL,BAN_CHECK):
        set_element=set_D1_element
    
    for index in indexL:
        set_element(index,parents,option_turn,option_p,scan_p)

def set_D1_element(index,parents,option_turn,option_p,scan_p):
    element_obj=(get_normal_obj,get_trigger_obj)[option_p.element_type==TRIGGER](index,parents,option_p,scan_p)
    xyT=element_obj.xyT

    space_dict=scan_p.turn_group[option_turn].D1
    parents_dict=scan_p.turn_group[option_turn].parents_dict

    if not space_dict.get(xyT):
        space_dict[xyT]=(Space,Bancheck_space)[scan_p.run_mode==BAN_CHECK](xyT,option_turn,scan_p.turn_group)

    parents_key=(parents,scan_p.lineT)

    if not parents_dict.get(parents_key):
        parents_dict[parents_key]=Parents()

    space_dict[xyT].add_obj(element_obj)
    parents_dict[parents_key].add_element(xyT,option_p)

def get_normal_obj(index,parents,option_p,scan_p):
    xyT=scan_p.check_line[index]

    return Element(xyT,parents,option_p,scan_p.lineT)

def get_trigger_obj(index,parents,option_p,scan_p):
    index,targetL=index
    xyT=scan_p.check_line[index]
    targetL=[scan_p.check_line[x]for x in targetL]
    
    element_obj=Element(xyT,parents,option_p,scan_p.lineT)
    element_obj.set_targetL(targetL)

    return element_obj

def get_ally(scan_p):
    allyL=[5]
    last=0
    for i in range(4):
        if include(i+6,ALLY,scan_p):
            allyL.append(6+i)
            last=i+1
        elif include(i+6,ENEMY,scan_p):
            break
    return allyL,last

def include(index,option,scan_p):
    xyT=scan_p.check_line[index]
    stone=scan_p.stone
    return ((option and xyT in stone.entire) or xyT in stone.turn_dict(option^scan_p.turn))

def exclude(index,option,exceptL,scan_p):
    xyT=scan_p.check_line[index]
    result=not ((xyT in scan_p.stone.entire)+(xyT in scan_p.stone.edge))
    if not option and xyT in scan_p.stone.turn_dict(scan_p.turn):
        exceptL.append(index)
        result=1
    return result

def sixpoint(index,scan_p):
    xyT=scan_p.check_line[index]
    if scan_p.turn==WHITE:
        return False
    return xyT in scan_p.stone.turn_dict(scan_p.turn)

def exclude_check(option,exceptL,direction,iterate,start,scan_p):
    result=0
    for i in range(iterate):
        if exclude(direction*i+start,option,exceptL,scan_p):
            result+=1
        else:
            break
    return result

def multiple_filter(rangeL,exceptL,checkL,check_val):
    result=[]
    for i in range(len(rangeL)-3):
        tL=rangeL[i:i+4]
        check=check_val
        for c in checkL:
            if c in tL:
                check=1-check
                break
        if check:
            result+=index_filter(tL,exceptL+result)
    return result

def trigger_filter(OA_L,CA_L,exceptL):
    OT_L,CT_L=[],[]
    OACA=OA_L+CA_L
    for trigger in OA_L:
        op_targetL=index_filter(get_validlist(OA_L,4,trigger),exceptL+[trigger])
        cl_targetL=index_filter(get_validlist(OACA,5,trigger),exceptL+op_targetL+[trigger])
        
        if op_targetL:
            OT_L.append((trigger,op_targetL))
        if cl_targetL:
            CT_L.append((trigger,cl_targetL))

    for trigger in CA_L:
        targetL=index_filter(get_validlist(OACA,5,trigger),exceptL+[trigger])

        if targetL:
            CT_L.append((trigger,targetL))

    return OT_L,CT_L

def get_parents(allyL,check_line):
    return tuple(check_line[x]for x in allyL)

def end_game(allyL,shape_N,scan_p):
    if shape_N!=5:
        return

    check_dict=scan_p.turn_group[scan_p.turn].check_dict

    for xyT in get_parents(allyL,scan_p.check_line):
        check_dict[xyT]=1
    
def get_validlist(indexL,rangeN,head):
    return [x for x in indexL if abs(head-x)<rangeN]

def index_filter(indexL,targetL):
    return list(filter(lambda index:index not in targetL,indexL))

def get_banlist(opened_rangeL,scan_p):
    ban_dict=scan_p.turn_group[0].ban_dict
    return [i for i,xy in enumerate(scan_p.check_line) if xy in ban_dict]

def check_banlist(banL,shape_N,*_): #check
    #return banL
    return []

def compare_parents(P1,P2):
    U=P1+P2
    return len(U)==len(set(U))

def compare_lineT(element1,element2):
        lineT1,lineT2=map(lambda e:e.lineT,(element1,element2))
        return lineT1==lineT2

        #compare_contents(element1,element2,lambda e:e.lineT)

def compare_contents(C1,C2,func):
    return (lambda x,y:x==y)(*map(lambda c:func(c),(C1,C2)))

def double_check(C1,C2,func):
    return (lambda x,y:all((x,y)))(*map(lambda c:func(c),(C1,C2)))

def min_line(T):
    if T[2]==0:
        return (0,T[1],T[2])
    elif T[2]==1:
        return (T[0],0,T[2])
    elif T[2]==2:
        return (T[0]-min(T[0],T[1]),T[1]-min(T[0],T[1]),T[2])
    else:
        return (T[0]-min(T[0],14-T[1]),T[1]+min(T[0],14-T[1]),T[2])

#편의성 임시 함수
def get_record(fname):
    with open(f"기보/{fname}.txt","r") as f:
        return [tuple(map(int,xy.split(',')))for xy in f.read().split("\n")]

def print_check(attackL,defenseL,allyL,scan_p):
    OA_L,CA_L,OT_L,CT_L=attackL
    DF1_L,DF2_L,DF3_L,DF4_L,DF5_L=defenseL
    print(f"xy : {scan_p.check_line[5]} {scan_p.lineT[2]}")
    print(f"allyL : {allyL}")
    print(f"OA_L : {OA_L}")
    print(f"CA_L : {CA_L}")
    print(f"OT_L : {OT_L}")
    print(f"CT_L : {CT_L}")
    print(f"DF1_L : {DF1_L}")
    print(f"DF2_L : {DF2_L}")
    print(f"DF3_L : {DF3_L}")
    print(f"DF4_L : {DF4_L}")
    print(f"DF5_L : {DF5_L}")

'''
main_play(get_record("설계보조2"))

#print(end_check(get_record("end_check"),False))
'''
