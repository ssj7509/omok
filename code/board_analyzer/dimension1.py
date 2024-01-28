from abc import abstractmethod

from .header import *
from .parameter_set import ParameterSet
from .singleton import SingletonABC

class OneDimensionalAnalyzer(metaclass=SingletonABC):
    def set_dimension1_space(self,space_group):
        for space in space_group.get_dimension1_turn(BLACK).values():
            space.set_element()

        for space in space_group.get_dimension1_turn(WHITE).values():
            space.set_element()
    
    def analyze(self,space_group,check_list,stone,turn):
        for xyT in check_list:
            check_line=self.get_checkline(xyT)

            for i in range(4):
                scan_p=ParameterSet(SCAN,check_line[i],stone,turn,space_group,self.min_line((*xyT,i)))
                allyL=self.get_ally(scan_p)

                self.check_stone(allyL,scan_p)

    def get_checkline(self,xyT):
        x,y=xyT
        check_line=[[],[],[],[]]

        for i in range(11):
            check_line[0].append((x+i-5,y))
            check_line[1].append((x,y+i-5))
            check_line[2].append((x+i-5,y+i-5))
            check_line[3].append((x+i-5,y-i+5))

        return check_line

    def get_ally(self,scan_p):
        allyL=[5]
        for i in range(4):
            if self.include(i+6,ALLY,scan_p):
                allyL.append(6+i)
            elif self.include(i+6,ENEMY,scan_p):
                break
            
        return allyL

    def include(self,index,option,scan_p):
        xyT=scan_p.check_line[index]
        stone=scan_p.stone
        
        return ((option and xyT in stone.entire) or xyT in stone.turn_member(option^scan_p.turn))

    def get_parents(self,allyL,scan_p):
        return tuple(scan_p.check_line[x]for x in allyL)

    def min_line(self,T):
        if T[2]==0:
            return (0,T[1],T[2])
        elif T[2]==1:
            return (T[0],0,T[2])
        elif T[2]==2:
            return (T[0]-min(T[0],T[1]),T[1]-min(T[0],T[1]),T[2])
        else:
            return (T[0]-min(T[0],14-T[1]),T[1]+min(T[0],14-T[1]),T[2])

    @abstractmethod
    def check_stone(self,allyL,scan_p):
        pass

    @abstractmethod
    def check_space(self,stone,ban_dict):
        pass

