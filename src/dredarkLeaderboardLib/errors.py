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

class ImproperLink(Exception):
  """Improper Link Used
  
  Attributes:
      link -- input link which caused the error
      message -- explanation of the error

  """
  def __init__(self, link, message):            
    # Call the base class constructor with the parameters it needs

    # Now for your custom code...
    #self.errors = errors

    super().__init__(message) #Initiate Error Message

class DeprecatedModule(Exception):
  """Deprecated Module Used

  Attributes:
      Module -- Deprecated Module
      message -- explanation of the error

  """
  def __init__(self, module, message):            
    # Call the base class constructor with the parameters it needs

    # Now for your custom code...
    #self.errors = errors

    super().__init__(message)