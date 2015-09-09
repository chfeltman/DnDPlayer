from DnD.Common._Constants import *
from DnD.Common._Decorators import * 

class Description(object):
    def __init__(self):
        self.__brief = None
        self.__full = None
                
    @property
    def Brief(self):
        return self.__brief
        
    @Brief.setter
    @ValidateType(str)
    def Brief(self, value):
        self.__brief = value
        
    @property
    def Full(self):
        return self.__full
        
    @Brief.setter
    @ValidateType(str)
    def Full(self, value):
        self.__full = value
