from .header import *
from .ban_checker import BanChecker
from .normal_checker import NormalChecker
from .updated_dict import Dict
from .singleton import Singleton

class TwoDimensionalAnalyzer(metaclass=Singleton):
    normal_checker=NormalChecker()
    ban_checker=BanChecker()

    def analyze(self,stone,turn):
        ban_dict=self.ban_checker.check_space(stone,Dict())
        space_group=self.normal_checker.check_space(stone,ban_dict)

        return space_group

    def update_D1_trigger(self,space_dict):
        search_set=set()

        for trigger_xyT,obj in space_dict.items():
            search_set.update((trigger_xyT,target)for target in obj.target_set if space_dict.get(target))

        while search_set:
            trigger,target=next(iter(search_set))
            valueL=space_dict[trigger].trigger_valueL
            
            self.trigger_DFS(search_set,space_dict,trigger,target,valueL)

    def trigger_dfs(self,search_set,space_dict,trigger,target,valueL):
        search_set.discard((trigger,target))
        
        trigger,obj=target,space_dict[target]
        targetL=[*obj.target_set]
        
        if self.update_valueL(valueL):
            search_set.update((trigger,target)for target in targetL)

        if (trigger,target) not in search_set:
            return

        for target in targetL:
            self.trigger_dfs(search_set,space_dict,trigger,target,valueL)

    def update_valueL(self,valueL):
        pass

