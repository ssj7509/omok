from .updated_dict import Dict

class DimensionGroup:
    def __init__(self,option):
        self.D1=Dict()
        self.D2=Dict()
        self.D3=Dict()

        if option:
            self.set_check_dict()

    def set_check_dict(self):
        self.check_dict=Dict()

    def get_dimension1_dict(self):
        return self.D1

    def get_check_dict(self):
        return self.check_dict

