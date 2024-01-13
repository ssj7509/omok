from .dimension3 import ThreeDimensionalAnalyzer
from .end_checker import EndChecker
from .stone_group import StoneGroup
from .updated_dict import Dict
from .singleton import Singleton

class BoardAnalyzer(metaclass=Singleton):
    dimension3=ThreeDimensionalAnalyzer()
    end_checker=EndChecker()
    

    def main_play(self,recordL):
        dimension2=self.dimension3.dimension2    #임시
        
        stone=StoneGroup(recordL)
        
        turn=len(stone.entire)%2

        space_group=dimension2.analyze(stone,turn)
        
        return space_group,turn

    def end_check(self,recordL):
        stone=StoneGroup(recordL)
        
        return self.end_checker.check_space(stone,Dict())
        
    def get_data(self,space_dict):
        spaceL=space_dict.values()
        max_abs=max(space.max_abs for space in spaceL)

        candidate_spaceL=[space for space in spaceL if space.max_abs==max_abs]

        return ([space.xyT for space in candidate_spaceL],
                tuple([space.space_matrix for space in candidate_spaceL]))
