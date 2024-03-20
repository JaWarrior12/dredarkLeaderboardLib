from .errors import *

def linkCheck(type:str):
  """Checks Links For Validity With The Modules. Prevents Legacy Links With Base Module & Vice Versa
  """
  def wrap(func):
    def inner(*args,**kwargs):
      url=args[1]
      func(*args,**kwargs)
      if "?cat=leg" in url and type=="base":
        raise ImproperLink(url,"\n\n\n A legacy link was used with the base module. Please use a regular leaderboard link.")
      elif "?cat=leg" not in url and type=="legacy":
        raise ImproperLink(url,"\n\n\n A base link was used with the legacy module. Please use a legacy leaderboard link.")
    return inner
  return wrap