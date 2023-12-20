import numpy as np
from header import *

def get_entire():
    return {BLACK:{},WHITE:{},EDGE:{},BAN:{}}

def get_D2_spaces():
    return {D1:{BLACK:{},WHITE:{}},D2:{BLACK:{},WHITE:{}},BAN:{}}

def set_entire(record_array):
    entire_stone=get_entire()
    
    for i in range(16):
        entire_stone[EDGE][(i-1,-1)]=1
        entire_stone[EDGE][(i,15)]=1
        entire_stone[EDGE][(-1,i)]=1
        entire_stone[EDGE][(15,i-1)]=1

    for i,(x,y) in enumerate(record_array):
        entire_stone[i%2][(x-1,y-1)]=1
        
    return entire_stone

class space():
    def __init__(self):
        pass

def main_play(entire,black_mode,white_mode):
    turn=(BLACK,WHITE)[len(entire_stone[BLACK])>len(entire_stone[WHITE])]
    Dimension_3(entire,turn)

def Dimension_3(entire,turn):
    pass

def Dimension_2(entire,turn):
    D2_spaces=get_D2_spaces()
    
    D2_spaces[BAN]=ban_check(entire,turn)

    Dimension_1(D2_spaces,entire[turn].keys(),entire,D1,turn,D1_NORMAL)
    Dimension_1(D2_spaces,entire[1-turn].keys(),entire,D1,turn,D1_NORMAL)

    t_func_D1(D2_spaces)

    Dimension_1(D2_spaces,D2_spaces[D1][turn].keys()+entire[turn].keys(),entire,D2,1-turn,D2_NORMAL)
    Dimension_1(D2_spaces,D2_spaces[D1][1-turn].keys()+entire[1-turn].keys(),entire,D2,1-turn,D2_NORMAL)

    t_func_D2(D2_spaces)

    return D2_spaces

def ban_check(entire):
    bancheck_spaces=get_D2_spaces()

    Dimension_1(bancheck_spaces,entire[BLACK].keys(),entire,D1,BLACK,BAN_CHECK)

    t_func_ban(bancheck_spaces)

    return bancheck_spaces[BAN]
    

def get_checkline(xyT):
    x,y=xyT
    check_line=[[xyT]for i in range(4)]
    
    for i in range(1,6):
        for j in range(2):
            check_line[0].append((x-((-1)**j)*i,y))
            check_line[1].append((x,y-((-1)**j)*i))
            check_line[2].append((x-((-1)**j)*i,y-((-1)**j)*i))
            check_line[3].append((x-((-1)**j)*i,y+((-1)**j)*i))

    return check_line

def get_checkline(xyT):
    x,y=xyT
    check_line=[[xyT]for i in range(4)]

    for i in range(4):
        check_line[0].append((x+i-5,y))
        check_line[1].append((x,y+i-5))
        check_line[2].append((x+i-5,y+i-5))
        check_line[3].append((x+i+5,y+i-5))  


def Dimension_1(D2_spaces,check_list,entire,result_target,turn,run_mode):
    for xyT in check_list:
        check_line=get_checkline(xyT)

        for i in range(4):
            scan_space(run_mode,check_line,entire,turn,D2_spaces,result_target,(*xyT,i))
            
    return D1_result

def scan_space(run_mode,*p):
    p=*p,run_mode

    scan_form2(p)
    scan_form3(p)

    if run_mode not in (BAN_CHECK):
        scan_form1(p)

    if run_mode not in (D1_0,D2_0):
        scan_form4(p)

    if run_mode in (END_CHECK):
        scan_form5(p)
    
    if run_mode==BAN_CHECK:
        scan_form6(p)

def get_ally(p):
    allyL=[5]
    last=0
    prior_val=1
    for i in range(4):
        if include([i+6],ALLY,*p):
            allyL[i].append(6+i)
            last=i+1
            prior_val+=1
        elif include([i+6],ENEMY,*P):
            break
    return allyL,last,prior_val

def get_ally(p):
    allyL=[5]
    last=0
    prior_val=1
    D2val=isD1(*p)
    for i in range(4):
        D2val|=D2check(i+6,*p)
        if include(i+6,ALLY,D2val,*p):
            allyL[i].append(6+i)
            last=i+1
            prior_val+=1
        elif include(i+6,ENEMY,False,*P):
            break
    return allyL,last,prior_val

def include(indexL,option,check_line,entire,turn,D2_spaces,RT,*_):
    result=RT==D1
    for x in indexL:
        xyT=check_line[x]
        D2check=not option and RT and D2_spaces[D1][turn].get(xyT)
        if not ((option and entire[EDGE].get(xyT)) or \
                D2check or entire[option^turn].get(xyT)):
            return False
        result|=D2check
    return result

def D2check(index,check_line,entire,turn,D2_spaces,RT,*_):
    return RT and D2_spaces[D1][turn].get(xyT)

def include(indexL,option,D2val,check_line,entire,turn,D2_spaces,RT,*_):
    result=RT==D1
    for x in indexL:
        xyT=check_line[x]
        if not ((option and entire[EDGE].get(xyT)) or \
                D2val or entire[option^turn].get(xyT)):
            return False
        result|=D2check
    return result

def exclude_check(func,direction,iterate,start,p):
    result=0
    for i in range(iterate):
        if func([direction*i+start],*p):
            result+=1
        else:
            break
    return result

def index_filter(indexL,targetL):
    return list(filter(lambda index:index not in targetL))

def get_OAlist(opened_rangeL,exceptL,checked_banL):
    result=[]
    for range(len(opened_rangeL)-3):
        tL=opened_rangeL[i:i+4]
        check=1
        for cb in checked_banL:
            if cb in tL:
                check=0
                break
        if check:
            result+=filter_list(tL,exceptL+result)
    return result

def multiple_filter(rangeL,exceptL,checkL,iterate,start,end):
    result=[]
    for i in range(iterate):
        tL=rangeL[i+start:i+start+end]
        check=1
        for c in checkL:
            if c in tL:
                break
        if check:
            result+=index_filter(tL,exceptL+result)
    return result

def scan_space(run_mode,*p):
    p=*p,run_mode
    
    allyL,last,prior_val=get_ally(p)

    if run_mode in (D1_0,D2_0) and prior_val!=1:
        return

    e_left=-exclude_check(exclude,-1,4-last,4,p)+5
    e_right=exclude_check(exclude,1,4-last,6+last,p)+last+5
    
    if e_right-e_left<4:
        return

    r_left=e_left+exclude_check(sixpoint,1,6-e_left,e_left-1,p)
    r_right=e_right-exclude_check(sixpoint,-1,6-e_right,e_right+1,p)

    if run_mode!=BAN_CHECK and r_right-r_left<4:
        return

    opened_rangeL=[*range(r_left+1,r_right)]
    closed_rangeL=[*range(r_left,r_right+1)]
    olen,clen=len(opened_rangeL),len(closed_rangeL)

    DF1_rangeL=[*(range(clen-5,5),range(4))[clen==4]]
    DF3_rangeL=[*(range(olen-5,5),range(4))[olen==4]]

    banL=get_banlist(opened_rangeL,*p)
    checked_banL=check_banlist(banL,prior_val)

    OA_L=multiple_filter(opened_rangeL,allyL+banL,checked_banL,olen-3,0,4)
    CA_L=index_filter(closed_rangeL,OA_L+allyL+banL)
    
    DF4=multiple_filter(opened_rangeL,allyL+banL+DF1+DF2,(olen-5),)
    
def scan_form1(p):
    if include([1],ENEMY,*p) and exclude([2,4,6,8],*p) and sixpoint(10,*p):
        set_space([[2],[4],[6],[8]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
        set_space([2,4,6,8],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

        set_space([[2,4,6,8]],[0],1,DEFENSE,CLOSED,NORMAL,[0],*p)
        set_space([[2,4,6,8]],[],0,DEFENSE,CLOSED,NORMAL,[1],*p)
        
    if include([2],ENEMY,*p) and exclude([1,3,5,7],*p) and sixpoint(9,*p):
        set_space([[1],[3],[5],[7]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
        set_space([1,3,5,7],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

        set_space([[1,3,5,7]],[0],1,DEFENSE,CLOSED,NORMAL,[0],*p)
        set_space([[1,3,5,7]],[],0,DEFENSE,CLOSED,NORMAL,[1],*p)


    if include([3],ENEMY,*p) and exclude([1,2,4,6],*p):
        if include([8],ENEMY,*p) or (exclude([8],*p) and not sixpoint(10,*p)):
            set_space([[1],[2],[4],[6]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([1,2,4,6],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,2,4,6]],[0],1,DEFENSE,CLOSED,NORMAL,[0],*p)
            set_space([[1,2,4,6]],[],0,DEFENSE,CLOSED,NORMAL,[1],*p)
            
        elif exclude([8],*p) and sixpoint(10,*p):
            set_space([[2],[4],[6]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([2,4,6],[],OPENED,TRIGGER,[1,3],*p)

            set_space([[1],[8]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([1,8],[],1,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[2,4,6],[1,8]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[2,4,6],[1,8]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)

    if include([4],ENEMY,*p) and exclude([1,2,3,5],*p):
        if include([7],ENEMY,*p) or (exclude([7],*p) and not sixpoint(9,*p)):
            set_space([[1],[2],[3],[5]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([1,2,3,5],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,2,3,5]],[0],1,DEFENSE,CLOSED,NORMAL,[0],*p)
            set_space([[1,2,3,5]],[],0,DEFENSE,CLOSED,NORMAL,[1],*p)
            
        elif exclude([7],*p) and sixpoint(9,*p):
            set_space([[1],[3],[5]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([1,3,5],[],OPENED,TRIGGER,[1,3],*p)

            set_space([[2],[7]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([2,7],[],1,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,3,5],[2,7]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[1,3,5],[2,7]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)

    
    if include([5],ENEMY,*p) and exclude([1,2,3,4],*p):
        if include([6],ENEMY,*p):
            set_space([[1],[2],[3],[4]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([1,2,3,4],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,2,3,4]],[0],1,DEFENSE,NORMAL,[0],*p)
            set_space([[1,2,3,4]],[],0,DEFENSE,NORMAL,[1],*p)

        elif exclude([6],*p) and (include([8],ENEMY,*p) or exclude([8],*p) and not sixpoint(10,*p)):
            set_space([[1],[2],[4]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([1,2,4],[],0,ATTACK,OPENED,TRIGGER,[1,3],*p)

            set_space([[3],[6]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([3,6],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,2,4],[3,6]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[1,2,4],[3,6]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)

        elif exclude([6,8],*p) and sixpoint(10,*p):
            set_space([[1],[2],[4],[6]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([1,2,4,6],[],0,ATTACK,OPENED,TRIGGER,[1,3],*p)

            set_space([[3],[8]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([3,8],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[2,4],[1,6],[3,8]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[2,4],[1,6],[3,8]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)

    if include([6],ENEMY,*p) and exclude([1,2,3,4],*p):
        if exclude([5],*p) and (include([7],ENEMY,*p) or exclude([7],*p) and not sixpoint(9,*p)):
            set_space([[1],[2],[3]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([1,2,3],[],0,ATTACK,OPENED,TRIGGER,[1,3],*p)

            set_space([[4],[5]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([4,5],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,2,3],[3,6]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[1,2,3],[3,6]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)

        elif exclude([5,7],*p) and sixpoint(9,*p):
            set_space([[1],[2],[3],[5]],[0],1,ATTACK,OPENED,NORMAL,[0,2],*p)
            set_space([1,2,3,5],[],0,ATTACK,OPENED,TRIGGER,[1,3],*p)

            set_space([[4],[7]],[0],1,ATTACK,CLOSED,NORMAL,[0,2],*p)
            set_space([4,7],[],0,ATTACK,CLOSED,TRIGGER,[1,3],*p)

            set_space([[1,3],[2,5],[4,7]],[0],1,DEFENSE,OPENED,NORMAL,[0],*p)
            set_space([[1,3],[2,5],[4,7]],[],0,DEFENSE,OPENED,NORMAL,[1],*p)


        
            
def isD1(p1,p2,p3,p4,p5,p6,RT,*_):
    return RT==D1

#include((1,3,4),ALLY,*check_set)
def include(indexL,option,check_line,entire,turn,D2_spaces,RT,*_):
    result=RT==D1
    for x in indexL:
        xyT=check_line[x]
        D2check=not option and RT and D2_spaces[D1][turn].get(xyT)
        if not ((option and entire[EDGE].get(xyT)) or \
                D2check or entire[option^turn].get(xyT)):
            return False
        result|=D2check
    return result

#exclude((1,3,4),*check_set)
def exclude(index,check_line,entire,turn,*_):
    xyT=check_line[index]
    return not entire[BLACK].get(xyT) or entire[WHITE].get(xyT) or entire[EDGE].get(xyT)

def sixpoint(index,check_line,entire,turn,*_):
    xyT=check_line[index]
    if turn==WHITE:
        return False    
    return entire[turn].get(xyT)    

def get_banlist(indexL,check_line,entire,turn,D2_spaces,*_):
    if turn==WHITE:
        return []
    return list(filter(lambda index:D2_spaces[BAN].get(check_line[index]),indexL))
        

def ex_ban(indexL,space_type,*_):
    pass

def set_space(indexL,parents,prior_val,stance,shape,space_type,modeL,
              check_line,entire,turn,D2_spaces,result_target,lineT,run_mode):
    if target_mode!=run_mode:
        return


    
def min_line(T):
    if T[2]==0:
        return (T[0],0,T[2])
    elif T[2]==1:
        return (0,T[1],T[2])
    elif T[2]==2:
        return (T[0]-min(T[0],T[1]),T[1]-min(T[0],T[1]),T[2])
    else:
        return (T[0]-min(T[0],14-T[1]),T[1]+min(T[0],14-T[1]),T[2])


#파일에서 읽어서 딕셔너리로 정리
record_array=[]

entire_stone=set_entire(record_array)

black_mode="computer"
white_mode="user"


