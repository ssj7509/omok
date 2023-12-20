###전체 세팅값###
#separator1
MSP1=290
MSP2=830

###보드 세팅값###
master_BX=310
master_BY=50

#오목판
BX=0+master_BX
BY=0+master_BY
BW=500
BH=500

#좌표 텍스트 간격
BTL=0.4
BTR=0.5
BTT=0.5
BTB=0.5

#캔버스 원 반지름
SR=14
MR=3
CR=7
OR=10

#trigger-target 화살표 각도, 크기
TRAD=30
TR=3

#착수버튼
PX1=430+master_BX
PY1=500+master_BY
PW1=70
PH1=30

PX2=0+master_BX
PY2=500+master_BY
PW2=70
PH2=30

#되돌리기 버튼
LBX=300+master_BX
LBY=500+master_BY
LBW=30
LBH=30

#앞으로 버튼
RBX=350+master_BX
RBY=500+master_BY
RBW=30
RBH=30

#진행 횟수 라벨
CLX=210+master_BX
CLY=500+master_BY

CKLX=170+master_BX
CKLY=520+master_BY

TLX=425+master_BX
TLY=-20+master_BY

#옵션메뉴 활성화 라디오버튼
ORBX1=0+master_BX
ORBY1=-40+master_BY
ORBW1=150
ORBH1=15

ORBX2=0+master_BX
ORBY2=-20+master_BY
ORBW2=150
ORBH2=15

#테스트 마크 버튼
MRX=500+master_BX
MRY=50+master_BY

MBX=500+master_BX
MBY=150+master_BY

MOX=500+master_BX
MOY=250+master_BY

TDX=500+master_BX
TDY=350+master_BY

TBW=70
TBH=30


###옵션 메뉴 세팅값###
master_OMX=20
master_OMY=20

#전체 프레임
OMX=0+master_OMX
OMY=0+master_OMY
OMW=250
OMH=550

#상단, 하단 구분선 y값
OMSP=30

#상단 체크버튼
OMCX1=0
OMCY1=0
OMCW1=125
OMCH1=25

OMCX2=125
OMCY2=0
OMCW2=125
OMCH2=25

OMCX3=0
OMCY3=25
OMCW3=125
OMCH3=25

OMCX4=125
OMCY4=25
OMCW4=125
OMCH4=25

#Notebook 탭 텍스트 길이
NBT1=24
NBT2=24

NBT1_1=20
NBT1_2=18

#Notebook 사이 프레임 높이
LFH=7

#하단 2페이지 상단 프레임 높이
OMFH2_N=60

#하단 2페이지 중단 프레임 높이, separator y
OMFH2_M=20
OMSP2_M=10

#넘버 라벨
OMNLX1=5
OMNLY1=8
OMNLW1=10
OMNLH1=10

OMNLX2=5
OMNLY2=33
OMNLW2=10
OMNLH2=10

#콤보박스
OMCBX1=25
OMCBY1=5
OMCBW1=150
OMCBH1=20

OMCBX2=25
OMCBY2=30
OMCBW2=150
OMCBH2=20

#add 버튼
OMABX=185
OMABY=20
OMABW=40
OMABH=20

#버튼 프레임 높이
BFH=20

#옵션 목록
#D1_ATTACKL=[f"1차원 : {v3} {v1} {v2}"for v1 in ("공격","트리거")for v2 in range(1,4)for v3 in ("열린","닫힌")];D1_ATTACKL.insert(6,"1차원 : 공격 4")
#D1_DEFENSEL=[*[f"1차원 : 방어 {v1} :: {v2}등급"for v1 in range(1,4)for v2 in range(1,6)],"1차원 : 방어 4"]

#Dimension, stance, shape, type, prior_val 
D1_ATTACKL=[(0,0,v3,v1,v2)for v1 in (0,1)for v2 in range(1,4)for v3 in (0,1)];D1_ATTACKL.insert(6,(0,0,1,0,4))
D1_DEFENSEL=[*[(0,1,v2,0,v1)for v1 in range(1,4)for v2 in range(5)],(0,1,1,0,4),(0,1,4,0,4)]

#스크롤 휠 속도
SCRSPD=10

#스크롤 리스트 속 객체 세팅
#1_1
OBJW1_1=218
OBJH1_1=30

OBJW1_2=218
OBJH1_2=30

OBJW2_S=222
OBJH2_S=60
