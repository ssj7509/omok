from .singleton import Singleton
from .header import *

class ThreeDimensionalAnalyzer(metaclass=Singleton):
    dimension2=TwoDimensionalAnalyzer()
    
    
