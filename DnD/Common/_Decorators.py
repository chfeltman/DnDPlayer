import os, inspect, enum
from DnD.Common._HelperFunctions import *

class ValidationDecorator(object):
    def __init__(self, isValid, errorMessage, args):
        for index, value in enumerate(args):
            if value != None and not isValid(value):
                raise ValueError("Args[" + str(index) + "]: " + errorMessage)
        self.args = args
        
    def ValidateValue(self, validationArg, value):
        pass
        
    def __call__(self, func):
        # funcSig = inspect.getargspec(func)
        # print(funcSig)
        # if len(funcSig.args)-1 != len(self.args):
            # raise TypeError("Validation and Function must have the same number of arguments")
            
        def Validate(*args):
            exceptions = []
            for index, validationArg in enumerate(self.args, 1):
                try:
                    if not None == validationArg:
                        self.ValidateValue(validationArg, args[index])
                except Exception as e:
                    exceptions.append("Arg[" + str(index - 1) + "] -> " + str(e))
                    
            if len(exceptions) != 0:
                raise Exception(os.linesep + str.join(os.linesep, exceptions))
                
            func(*args)                
        
        return Validate
        

class ValidateType(ValidationDecorator):
    def __init__(self, *args):
        super().__init__( \
            lambda value: isinstance(value, (type(type), type(enum.Enum))), \
            "Must use an object type for validation",
            args)

    def ValidateValue(self, validationArg, value):
        _typename = validationArg.__name__
        if not isinstance(value, validationArg):
            raise ValueError("Value must be of type: " + _typename)
        
class ValidateMinimum(ValidationDecorator):
    def __init__(self, *args):
        super().__init__( \
            isNumeric, \
            "Minimum must be a numeric type",
            args)
            
    def ValidateValue(self, validationArg, value):
        minStr = str(validationArg)
        if value < validationArg:
            raise ValueError("Value must be greater than or equal to " + minStr)

class ValidateRange(ValidationDecorator):
    def __init__(self, *args):
        super().__init__( \
            lambda value: \
                isinstance(value, type([])) and \
                len(value) == 2 and \
                isNumeric(value),                
            "Range must be a list of numeric types",
            args)
            
    def ValidateValue(self, validationArg, value):
        maxVal = max(validationArg)
        minVal = min(validationArg)
        if value < min:
            raise ValueError("Value must be greater than or equal to " +str(min))

        if not value > max:
            raise ValueError("Value must be less than or equal to " + str(max))
