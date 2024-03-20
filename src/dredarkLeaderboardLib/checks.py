from .errors import *

def linkCheck(expectedType : str, link : str):
  """Checks Links For Validity With 
  """
  #pass
  if link.contains("?cat=leg") and expectedType=="base":
    raise ImproperLink(link,"A legacy link was used with the base module. Please use regular")