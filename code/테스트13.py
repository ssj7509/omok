import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
cellsize,stonesize=30,13 #ps, cs에서 이름 변경
boardx,boardy=-270,250
set_boardx,set_boardy=0,0
turtlepos_x=-290
turtlepos_y=-260

def draw_board():
    t.up(); t.speed(0)
    t.goto(boardx+set_boardx,boardy+set_boardy-cellsize)
    for i in range(15):                    
        t.write(15-i); t.down(); t.fd(cellsize*16)
        t.write(15-i); t.up(); t.backward(cellsize*16)
        t.right(90); t.fd(cellsize); t.left(90)
    t.goto(boardx+set_boardx+cellsize,boardy+set_boardy); t.right(90)
    for i in range(15):
        t.write(chr(i+65)); t.down(); t.fd(cellsize*16)
        t.write(chr(i+65)); t.up(); t.backward(cellsize*16)
        t.left(90); t.fd(cellsize); t.right(90)
    t.goto(turtlepos_x,turtlepos_y); t.left(90)
def set_stone(x,y,turn):
    if turn=="Black":
        t.color("black")
    else:
        t.color("yellow")
    t.goto(boardx+set_boardx+cellsize*x,boardy+set_boardy-cellsize*(16-y)-stonesize)
    t.down(); t.begin_fill()
    t.circle(stonesize)
    t.up(); t.end_fill()
    t.goto(turtlepos_x,turtlepos_y)
draw_board()

def min_line(T):
    if T[2]==1:return (T[0],1,1)
    elif T[2]==2:return (1,T[1],2)
    elif T[2]==3:return (T[0]-min(T[0],T[1])+1,T[1]-min(T[0],T[1])+1,3)
    else:return (T[0]-min(T[0],16-T[1])+1,T[1]+min(T[0],16-T[1])-1,4)


print(min_line((3,4,1)))

def inlist(check_line,num_list,find_list):
    return all(map(lambda x:check_line[x] in find_list,num_list))

def inlist(check_line,num_list,find_list):
    for x in num_list:
        if check_line[x] not in find_list:
            return False
    return True

def notlist(check_line,num_list,find_list):
    for x in num_list:
        if check_line[x] in find_list:
            return False
    return True

def notlist(check_line,num_list,find_list):
    return all(map(lambda x:check_line[x] not in find_list,num_list))
def r_turn(turn):
    if turn=="Black":
        return "White"
    else:
        return "Black"
'''
for i in range(16):
    set_stone(i-1,-1,"Black")
    set_stone(i,15,"Black")
    set_stone(-1,i,"Black")
    set_stone(15,i-1,"Black")
'''   

Entire_stones={"Entire":[],"Black":[],"White":[]} #now_list, now_list_user, now_list_turtle에서 이름 변경
edge=[((1-y)*(x*16+((-1)**x)*z)+(1-x)*y*16,x*16+((-1)**x)*y*z) for x in range(2) for y in range(2) for z in range(16)]
Entire_stones["Entire"]+=edge

Black_mode="ai"
White_mode="user"

def play(Black_mode,White_mode):
    turn="Black"
    while True:
        globals()[globals()[turn+"_mode"]+"_turn"](turn)
        #if 5점검함수==True:
        #   print(turn+"의 승리입니다")
        #   break
        turn=r_turn(turn)
def user_turn(turn):
    #ban_L=ban_check(Entire_stones)
    while True:
        UserInput=input("좌표를 입력하세요:")
        userx=ord(UserInput[0])-64
        usery=int(UserInput[1:])
        if any(map(lambda x:x not in range(1,16),[userx,usery])):
            print("범위를 벗어난 자리입니다.")
        elif (userx,usery) in Entire_stones["Black"]+Entire_stones["White"]:
            print("이미 돌이 있는 자리입니다.")
        elif (userx,usery) in ban_L:
            print("금수 자리입니다.")
        else:
            set_stone(userx,usery,turn)
            Entire_stones[turn].append((userx,usery))
            Entire_stones["Entire"].append((userx,usery))
            break
def ai_turn(turn):
    #Dimension_3(turn)
    pass
class space():
    def __init__(self,stance,xy,Line_N,form_N,form_L,target,family):
        self.xy=xy
        self.Line_N=min_Line(Line_N)
        self.form_N=form_N
        self.form_L=form_L
        self.target=target
        self.family=family
        self.stance=stance
class space_pos():
    def __init__(self,stance,xy,Line_N,form_N,form_L,target,family):
        self.stoneN=0
        self.space_L=[]
        self.attack_L=[]
        self.xy=xy
        self.score=[]
    def add_space(self,stance,xy,Line_N,form_N,form_L,target,family):
        self.space_L.append(space(xy,stance,Line_N,form_N,form_L,target,family))
def Dimension_3(turn):
    pass
def Dimension_2(turn,check_E,check_type):
    D1_Result_Attack,D1_Result_Defense=[],[]
    D2_Score=[0,0] #공격,방어상황 수치
    if check_type=="ban_check":
        D1_Result_Attack=Dimension_1(check_E,check_type,check_E["Black"],"Black","Attack") #ban_check함수 첫부분으로 이동
    else:
        D1_Result_Attack=Dimension_1(check_E,check_type,check_E[turn],turn,"Attack")
        D1_Result_Defense=Dimension_1(check_E,check_type,check_E[r_turn(turn)],r_turn(turn),"Defense")
        #1차 제련 함수
        D2_E=check_E.copy()
        #공격space xy튜플들 Entire와 현재 turn에 추가
        #공격space instance들 "instance"항목 만들어서 추가
def ban_check():
    pass
def Dimension_1(check_E,check_type,read_L,read_color,stance):
    D1_Result={"xy":[],"Instance":{}}
    for i in range(len(read_L)):
        check_Line=[[],[],[],[]]
        check_x,check_y=read_L[i]
        for j in range(4):
            check_Line[j].append((check_x,check_y))
        for j in range(1,6):
            for k in range(2):
                check_Line[0].append((check_x-((-1)**k)*j,check_y))
                check_Line[1].append((check_x,check_y-((-1)**k)*j))
                check_Line[2].append((check_x-((-1)**k)*j,check_y-((-1)**k)*j))
                check_Line[3].append((check_x-((-1)**k)*j,check_y+((-1)**k)*j))   
        for j in range(4):
            Analyze_D1(read_color,check_Line[j],check_E,check_type,stance,(check_x,check_y,j+1),D1_Result)
    return D1_Result
def Analyze_D1(read_color,CL,check_E,check_type,stance,Line_N,D1_Result):
    Entire=check_E["Entire"]
    ally=check_E[read_color]
    enemy=check_E[r_turn(read_color)]
    parameter_set=(stance,Line_N,check_type,D1_Result)
    
    if check_type=="zero":
        if notlist(CL,[1,2],Entire):
            if CL[3] in enemy and notlist(CL,[4,6,8],Entire):
                Classify(CL[0],0,["trigger"],[],[],*parameter_set)
def Classify(xy,form_N,form_L,target,family,stance,Line_N,check_type,D1_Result):
    pos_name=f"xy_{xy[0]}_{xy[1]}"
    tmp_Instance=space_pos(xy,stance,Line_N,form_N,form_L,target,family)
    if xy not in D1_Result["xy"]:
        D1_Result["xy"].append(xy)
        D1_Result["Instance"][pos_name]=tmp_Instance
    else:
        D1_Result["Instance"][pos_name].add_space(tmp_Instance)
