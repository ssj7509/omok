from .singleton import Singleton
from .dimension2 import TwoDimensionalAnalyzer
from .header import *

class ThreeDimensionalAnalyzer(metaclass=Singleton):
    dimension2=TwoDimensionalAnalyzer()
    
    
