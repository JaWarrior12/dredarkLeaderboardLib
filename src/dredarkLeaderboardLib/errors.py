#__all__=('BadSearchKey')

class CustomError(Exception):
    pass

class BadSearchKey(Exception):
    """Bad Search Key; Key Not In Usable Keys List"""
    pass
    #def __init__(message):
        #self.value="BadSearchKey"
        #self.arg1 = searchTerms
        #self.arg2 = viableKeys
        #super(BadSearchKey, self).__init__(message)
    #def __str__(self):
        #return repr(self.value)