from header import *
import numpy as np
#sys.setrecursionlimit(100000000)

class Element:
    def __init__(self,xyT,parents,lineT,prior_val,stance,shape,element_type):
        self.xyT=xyT
        self.parents=parents
        self.prior_val=prior_val
        self.stance=stance
        self.shape=shape
        self.element_type=element_type
        self.lineT=lineT
        self.abs_score=self.get_abs_score(prior_val,stance,shape)
        self.D1_score=self.get_D1_score(prior_val,stance,shape,element_type)

    def get_abs_score(self,prior_val,stance,shape):
        r=1

        if prior_val==5 and stance==ATTACk:
            r=13
        elif prior_val==4 and stance==ATTACK:
            r=9
        elif prior_val==4 and stance==DEFENSE:
            r=7
        elif prior_val==3 and stance==ATTACK and shape==OPENED:
            r=5
        elif prior_val==3 and stance==DEFENSE and shape in (DEFENSE1,DEFENSE3):
            r=3

        return r
    
    def get_D1_score(self,prior_val,stance,shape,element_type):
        return

    def get_vars(self):
        return self.parents,self.lineT,self.prior_val,self.stance,self.shape,self.element_type

    def set_matrix(self,array):
        if self.element_type in (NORMAL,TARGET):
            array[1+self.stance*10+(self.prior_val-1)*(2,5)[self.stance]+self.shape]+=1

class Trigger_element(Element):
    def __init__(self,targetL,*p):
        super().__init__(*p)
        self.targetL=targetL
        self.valueL=[]



class Space:
    def __init__(self,xyT,D2_spaces,turn):
        self.xyT=xyT
        self.D2_spaces=D2_spaces
        self.turn=turn
        self.line_score=[[0,0]for _ in range(4)]
        self.elementL=[]
        self.triggerL=[]
        self.trigger_valueL=[]
        self.target_set=set()
        self.max_abs=0
        self.max_D1=0
        self.D2_score=0

    def add_element(self,new_e):
        if new_e.element_type!=TARGET:
            self.max_abs=max(self.max_abs,new_e.abs_score)
            
        deleteL=[]
        check=0
        
        for old_e in self.elementL:
            if self.nest_element(old_e,new_e,deleteL):
                return
            
        for de in deleteL:
            del self.elementL[self.elementL.index(de)]
        
        self.elementL.append(new_e)
        
        #self.add_trigger(new_e)
        

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

        if self.turn==BLACK and tuple(map(lambda e:(e.prior_val,e.shape),(normal,trigger))) \
                                in (((2,0),(1,0)),((3,1),(2,1))):
            return

        self.activate_trigger(normal,trigger)
    
    def get_predict_abs(self,e):
        return Element.get_abs_score(None,e.prior_val+1,e.stance,e.shape)
        
    '''
    def adjust_abs(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_score,e.prior_val,-e.shape))
        
        t=((e1.prior_val,e1.shape),(e2.prior_val,e2.shape))
        
        if self.turn==0 and t==((2,0),(3,1)):
            self.max_abs=max(self.max_abs,5)
        elif self.turn==1 and t in (((2,0),(3,1)),((2,2),(3,1))):
            self.max_abs=max(self.max_abs,3)
        elif self.turn==1 and double_check(e1,e2,lambda x:x.prior_val==3 and x.shape in (0,2)):
            self.max_abs=max(self.max_abs,6)
        elif self.turn==1 and double_check(e1,e2,lambda x:x.prior_val==4 and x.shape in (1,4)):
            self.max_abs=max(self.max_abs,8)
        elif self.turn==1 and double_check(e1,e2,lambda x:x.prior_val==2 and x.shape in (0,2)):
            self.max_abs=max(self.max_abs,4)
            self.adjust_33(e1,e2)
    
    '''
    
    def adjust_abs(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_score,e.prior_val,-e.shape))
        
        t=((e1.prior_val,e1.shape),(e2.prior_val,e2.shape))
        
        if e1.prior_val==2 and e1.shape==0 and e2.prior_val==3:
            #print(self.turn,e1.stance,e1.element_type,self.xyT) 
            self.max_abs=max(self.max_abs,5)
            self.defense_nest(4)

        elif double_check(e1,e2,lambda x:x.prior_val==3 and x.shape==CLOSED):
            self.max_abs=max(self.max_abs,5*self.turn)
            self.defense_nest(4*(self.turn))

        elif double_check(e1,e2,lambda x:x.prior_val==4):
            self.defense_nest(8*(self.turn))

        elif double_check(e1,e2,lambda x:x.prior_val==2 and x.shape==OPENED):
            self.max_abs=max(self.max_abs,2*self.turn)
            self.defense_nest(1.5*(self.turn))
            #self.adjust_33(e1,e2)

    def defense_nest(self,absN):
        #print("check",self.xyT,self.turn,absN)
        defense_space=self.get_space(self.xyT,1)
        defense_space.max_abs=max(defense_space.max_abs,absN)
        #print(defense_space.max_abs)
    
    def adjust_33(self,e1,e2):
        self.D2_spaces[TEST2].append((self.turn,self.xyT,e1,e2))
        #임시

    def parents_nest(self,e1,e2,deleteL):
        if compare_parents(e1.parents,e2.parents) or \
           not compare_contents(e1,e2,lambda x:(x.element_type,x.stance)):
            return

        if e1.element_type==TRIGGER:
            return self.trigger_parents_nest(e1,e2)

        te1,te2=sorted((e1,e2),key=lambda e:(e.prior_val,-e.shape))

        if e1 is te1:
            deleteL.append(e1)
            return 1

        return 2

    def trigger_parents_nest(self,e1,e2):
        e1,e2=sorted((e1,e2),key=lambda e:(e.prior_val,-e.shape))

        e1.targetL=[*(set(e1.targetL)-set(e2.targetL))]

    def linear_nest(self,e1,e2):
        if not (double_check(e1,e2,lambda x:x.shape==CLOSED and x.element_type==TRIGGER) \
           and compare_lineT(e1,e2)):
            return
        
        e1_targetS,e2_targetS=map(lambda e:set(e.targetL),(e1,e2))

        diff_set1,diff_set2=e1_targetS-e2_targetS,e2_targetS-e1_targetS
        inter_set=e1_targetS&e2_targetS

        if not (bool(diff_set1) and bool(diff_set2)):
            return
        
        if double_check(e1,e2,lambda x:x.prior_val==3):
            return self.linear_44(e1,e2,diff_set1,diff_set2)

        else:
            return self.linear_build_3(e1,e2,diff_set1,diff_set2,inter_set)

    def linear_44(self,e1,e2,diff_set1,diff_set2):
        if self.turn==BLACK:
            return

        self.adjust_abs(e1,e2)
        return 1
        
    def linear_build_3(self,e1,e2,diff_set1,diff_set2,inter_set):
        v1,v2=map(lambda e,ds:len(ds)-1+len(inter_set)>=3-e.prior_val,(e1,e2),(diff_set1,diff_set2))

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
        transfer_p=transfer_obj.get_vars()[:-1]

        target_element=Element(target_xyT,*transfer_p,TARGET)
        target_space.add_element(target_element)
    
    def get_space(self,xyT,option):
        turn=option^self.turn
        space_dict=self.D2_spaces[D1][turn]
        if not space_dict.get(xyT):
            space_dict[xyT]=Space(xyT,self.D2_spaces,turn)

        return space_dict[xyT]

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
        if e.prior_val==-1:
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
        space_dict=self.D2_spaces[TEST]
        if not space_dict.get(xyT):
            space_dict[xyT]=Bancheck_space(xyT,self.D2_spaces,self.turn)

        return space_dict[xyT]

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
        e1,e2=sorted((e1,e2),key=lambda e:(e.abs_score,e.prior_val,-e.shape))
        
        t=((e1.prior_val,e1.shape),(e2.prior_val,e2.shape))

        if t==((2,0),(2,0)):
            self.set_ban_space(self.xyT,33)
        elif double_check(e1,e2,lambda x:x.prior_val==3 and x.shape in (0,1)):
            self.set_ban_space(self.xyT,44)
    

class Ban_space:
    pass


class Parents:
    def __init__(self):
        self.attackS=set()
        self.defenseS=set()

    def add_space(self,xyT,option_turn,shape):
        (self.attackS,self.defenseS)[option_turn].add((xyT,shape))

def get_target_obj(xy,trigger_obj):
    target_obj=copy.deepcopy(trigger_obj)
    target_obj.xy=xy

def activate_trigger(D2_spaces,obj):
    if obj.element_type!=TRIGGER:
        return
    for tobj in get_target_objL:
        if not self.D2_spaces[D1][self.turn]:
            self.D2_spaces[D1][self.turn]=space(self.xy,self.D2_spaces,self.turn)

def get_entire():
    return {BLACK:{},WHITE:{},EDGE:{},ENTIRE:{},END:0}

def get_D2_spaces():
    return {D1:{BLACK:{},WHITE:{}},D2:{BLACK:{},WHITE:{}},BAN:{},
            PARENTS:{ATTACK:{},DEFENSE:{}}}

def get_D2_spaces():
    return {D1:{BLACK:{},WHITE:{}},D2:{BLACK:{},WHITE:{}},BAN:{},PARENTS:{},TEST:{},TEST2:[]}

def set_entire(record_List):
    entire_stone=get_entire()

    for i in range(16):
        entire_stone[EDGE][(i-1,-1)]=1
        entire_stone[EDGE][(i,15)]=1
        entire_stone[EDGE][(-1,i)]=1
        entire_stone[EDGE][(15,i-1)]=1

    for i,(x,y) in enumerate(record_List):
        entire_stone[i%2][(x-1,y-1)]=1
        entire_stone[ENTIRE][(x-1,y-1)]=1
        
    return entire_stone

def main_play(record_List,mode):#ban은 임시
    entire=set_entire(record_List)
    #print(entire[0])
    #print(entire[1])
    turn=len(entire[ENTIRE])%2

    #
    '''
    for xy in ban_List:
        entire[BAN][xy]=1
    '''
    #

    D2_spaces=Dimension_2(entire,turn)
    
    if mode==0:
        return D2_spaces,turn

    elif mode==1:
        return get_result(D2_spaces[D1][turn])

def get_result(space_dict):
    spaces=space_dict.values()
    max_abs=max(space.max_abs for space in spaces)

    candidate_spaces=[space for space in spaces if space.max_abs==max_abs]

    return ([space.xyT for space in candidate_spaces],
            tuple([space.get_space_matrix()for space in candidate_spaces]))
    
def Dimension_2(entire,turn):
    D2_spaces=get_D2_spaces()
    
    D2_spaces[BAN]=ban_check(entire)

    Dimension_1(D2_spaces,entire[turn].keys(),entire,D1,turn,D1_NORMAL)
    Dimension_1(D2_spaces,entire[1-turn].keys(),entire,D1,1-turn,D1_NORMAL)

    #tmp_33(D2_spaces)

    #print(D2_spaces[D1][turn])

    #update_D1_trigger(D2_spaces[D1][turn])
    #update_D1_trigger(D2_spaces[D1][1-turn])

    #D1_space_check(D2_spaces,turn)
    #D1_space_check(D2_spaces,1-turn)

    #t_func_D1(D2_spaces) #1차원 자리 종합

    #2차원 탐색 추가 부분
    #2차원 자리 종합

    return D2_spaces

def tmp_33(D2_spaces):
    for turn,xyT,e1,e2 in D2_spaces[TEST2]:
        ds1,ds2=map(lambda e:D2_spaces[PARENTS][(e.parents,e.lineT)].attackS,(e1,e2))
        print(ds1,ds2)
        dL=[xyT for xyT,shape in ds1|ds2 if shape<3]

        for xyT in dL:
            space=D2_spaces[D1][turn][xyT]
            space.max_abs=max(space.max_abs,4)

        

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
    entire=set_entire(record_List)
    
    if not entire:
        entire=set_entire(record_List)
    turn=len(entire[ENTIRE])%2

    end_spaces=get_D2_spaces()
    
    Dimension_1(end_spaces,entire[turn].keys(),entire,D1,turn,END_CHECK)
    Dimension_1(end_spaces,entire[1-turn].keys(),entire,D1,1-turn,END_CHECK)

    return entire[END]

def ban_check(entire):
    bancheck_spaces=get_D2_spaces()

    Dimension_1(bancheck_spaces,entire[BLACK].keys(),entire,D1,BLACK,BAN_CHECK)

    return bancheck_spaces[TEST]

def get_checkline(xyT):
    x,y=xyT
    check_line=[[],[],[],[]]

    for i in range(11):
        check_line[0].append((x+i-5,y))
        check_line[1].append((x,y+i-5))
        check_line[2].append((x+i-5,y+i-5))
        check_line[3].append((x+i-5,y-i+5))

    return check_line

def Dimension_1(D2_spaces,check_list,entire,result_target,turn,run_mode):
    for xyT in check_list:
        check_line=get_checkline(xyT)

        for i in range(4):
            scan_stone(run_mode,check_line[i],entire,turn,D2_spaces,result_target,min_line((*xyT,i)))

def scan_stone(run_mode,*p):
    allyL,last=get_ally(p)
    prior_val=len(allyL)

    if run_mode in (D1_0,D2_0) and prior_val!=1:
        return

    if run_mode==BAN_CHECK and prior_val==1:
        return

    if run_mode==END_CHECK:
        end_game(allyL,prior_val,*p)
        return

    for i in range(len(allyL)):
        scan_space(allyL[:i+1],allyL[i]-5,i+1,run_mode,*p)
    
def scan_space(allyL,last,prior_val,run_mode,*p):
    exceptL=allyL.copy()

    e_left,de_left=map(lambda opt:-exclude_check(opt,exceptL,-1,4-last,4,p)+5,(True,False))
    e_right,de_right=map(lambda opt:exclude_check(opt,exceptL,1,4-last,6+last,p)+last+5,(True,False))

    if e_right-e_left<4:
        return

    r_left,dr_left=map(lambda x:x+sixpoint(x-1,*p),(e_left,de_left))
    r_right,dr_right=map(lambda x:x-sixpoint(x+1,*p),(e_right,de_right))


    if run_mode!=BAN_CHECK and r_right-r_left<4:
        return

    opened_rangeL=[*range(r_left+1,r_right)]
    closed_rangeL=[*range(r_left,r_right+1)]

    drangeL=[*range(dr_left,dr_right+1)]

    banL=get_banlist(opened_rangeL,*p)
    checked_banL=check_banlist(banL,prior_val,*p)

    '''
    if run_mode==BAN_CHECK and prior_val in (3,4) and sixpoint(10,*p):
        closed_rangeL=[*range(5,11)]
        prior_val=-1
    '''
    if run_mode==BAN_CHECK and prior_val==4 and sixpoint(10,*p):
        closed_rangeL=[*range(5,10)]
        prior_val=-1

    if run_mode in (D1_0,D2_0):
        allyL=[]
        prior_val=0

    attackL=scan_attack(opened_rangeL,closed_rangeL,exceptL+banL,checked_banL,p)
    defenseL=scan_defense(drangeL,exceptL+banL,attackL[0],p)

    #print_check(attackL,defenseL,allyL,p)

    parents=get_parents(allyL,*p)

    distribute_space(attackL,defenseL,parents,prior_val,run_mode,p)

def scan_attack(opened_rangeL,closed_rangeL,exceptL,checkL,p):
    OA_L=multiple_filter(opened_rangeL,exceptL,checkL,1)
    CA_L=index_filter(closed_rangeL,OA_L+exceptL)
    
    OT_L,CT_L=trigger_filter(OA_L,CA_L,exceptL)

    return OA_L,CA_L,OT_L,CT_L

def scan_defense(drangeL,exceptL,OA_L,p):
    dlen=len(drangeL)
    
    #DF1_rangeL=(lambda start,end:closed_rangeL[start:end])(*((clen-5,5),(0,4))[clen==4])
    DF1_rangeL=drangeL[dlen-5:5]
    DF3_rangeL=(lambda start,end:drangeL[start:end])(*((dlen-6,6),(0,5))[dlen==5])

    DF1_L,DF2_L=index_filter(DF1_rangeL,exceptL),[]
    if not OA_L:DF1_L,DF2_L=DF2_L,DF1_L

    exceptL+=DF1_L+DF2_L

    DF4_L=index_filter(DF3_rangeL,exceptL+multiple_filter(drangeL,exceptL,OA_L,0))
    DF3_L=index_filter(DF3_rangeL,exceptL+DF4_L)
    
    DF5_L=index_filter(drangeL,exceptL+DF3_L+DF4_L)

    return DF1_L,DF2_L,DF3_L,DF4_L,DF5_L

def print_check(attackL,defenseL,allyL,p):
    OA_L,CA_L,OT_L,CT_L=attackL
    DF1_L,DF2_L,DF3_L,DF4_L,DF5_L=defenseL
    print(f"xy : {p[0][5]} {p[5][2]}")
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

def distribute_space(attackL,defenseL,parents,prior_val,run_mode,p):
    turn=p[2]

    p=parents,run_mode,*p

    unpack_indexL(attackL[0],(turn,prior_val,ATTACK,OPENED,NORMAL),*p)
    unpack_indexL(attackL[1],(turn,prior_val,ATTACK,CLOSED,NORMAL),*p)

    unpack_indexL(attackL[2],(turn,prior_val,ATTACK,OPENED,TRIGGER),*p)
    unpack_indexL(attackL[3],(turn,prior_val,ATTACK,CLOSED,TRIGGER),*p)

    if run_mode in (BAN_CHECK,D2_0):
        return

    for i in range(5):
        unpack_indexL(defenseL[i],(1-turn,prior_val,DEFENSE,i,NORMAL),*p)

    #if D2_0 -> activate_parents()

def unpack_indexL(indexL,dp,parents,run_mode,check_line,*p):
    if run_mode in (D1_NORMAL,BAN_CHECK):
        set_element=set_D1_normal
    
    for index in indexL:
        set_element(index,parents,run_mode,check_line,p,*dp)


def set_D1_normal(index,parents,run_mode,check_line,p,option_turn,*dp):
    entire,turn,D2_spaces,RT,lineT,element_type=*p,dp[-1]
    
    if element_type==TRIGGER:
        index,targetL=index
        xyT=check_line[index]
        targetL=[check_line[x]for x in targetL]
        sobj=Trigger_element(targetL,xyT,parents,lineT,*dp)
    else:
        xyT=check_line[index]
        sobj=Element(xyT,parents,lineT,*dp)
        
    space_dict=D2_spaces[D1][option_turn]
    parents_dict=D2_spaces[PARENTS]

    if not space_dict.get(xyT):
        space_dict[xyT]=(Space,Bancheck_space)[run_mode==BAN_CHECK](xyT,D2_spaces,option_turn)

    if not parents_dict.get(parents):
        parents_dict[(parents,lineT)]=Parents()

    space_dict[xyT].add_element(sobj)
    parents_dict[(parents,lineT)].add_space(xyT,option_turn,dp[2])

def get_ally(p):
    allyL=[5]
    last=0
    for i in range(4):
        if include(i+6,ALLY,*p):
            allyL.append(6+i)
            last=i+1
        elif include(i+6,ENEMY,*p):
            break
    return allyL,last

def include(index,option,check_line,entire,turn,*_):
    xyT=check_line[index]
    return ((option and xyT in entire[EDGE]) or xyT in entire[option^turn])

def exclude(index,option,exceptL,check_line,entire,turn,*_):
    xyT=check_line[index]
    result=not ((xyT in entire[ENTIRE])+(xyT in entire[EDGE]))
    if not option and xyT in entire[turn]:
        exceptL.append(index)
        result=1
    return result

def sixpoint(index,check_line,entire,turn,*_):
    xyT=check_line[index]
    if turn==WHITE:
        return False
    return xyT in entire[turn]

def exclude_check(option,exceptL,direction,iterate,start,p):
    result=0
    for i in range(iterate):
        if exclude(direction*i+start,option,exceptL,*p):
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

def get_parents(allyL,check_line,*_):
    return tuple(check_line[x]for x in allyL)

def end_game(allyL,prior_val,check_line,entire,*_):
    if prior_val==5:
        entire[END]=get_parents(allyL,check_line,0)

def get_validlist(indexL,rangeN,head):
    return [x for x in indexL if abs(head-x)<rangeN]

def index_filter(indexL,targetL):
    return list(filter(lambda index:index not in targetL,indexL))

def get_banlist(opened_rangeL,check_line,*p):
    D2_spaces=p[2]
    return [i for i,xy in enumerate(check_line) if xy in D2_spaces[BAN]]

def check_banlist(banL,prior_val,*_):
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

'''
main_play(get_record("설계보조2"))

#print(end_check(get_record("end_check"),False))
'''
