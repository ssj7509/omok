from .header import *

class ParameterSet:
    def __init__(self,value_type,*p):
        if value_type==SCAN:
            self.set_scan_value(*p)

        elif value_type==OPTION:
            self.set_option_value(*p)

        elif value_type==MEASURE:
            self.set_measure_value(*p)
    
    def set_scan_value(self,check_line,stone,turn,space_group,lineT):
        self.update_parameter(locals())

    def set_option_value(self,shape_N,stance,shape_type,element_type):
        self.update_parameter(locals())

    def set_measure_value(self,e_left,e_right,r_left,r_right,dr_left,dr_right):
        self.update_parameter(locals())

    def update_parameter(self,local_dict):
        self.__dict__.update(local_dict)

    def get_parameters(self):
        return tuple(self.__dict__.values())
