from .errors import *

ARCHIVE_IDENTIFIER="score_archive"

def linkCheck(type:str):
  """Checks Links For Validity With The Modules. Prevents Archive Links With Base Module & Vice Versa
  """
  def wrap(func):
    def inner(*args,**kwargs):
      url=args[1]
      func(*args,**kwargs)
      if ARCHIVE_IDENTIFIER in url and type=="base":
        raise ImproperLink(url,"\n\n\n A archive link was used with the base module. Please use a regular leaderboard link.")
      elif ARCHIVE_IDENTIFIER not in url and type=="archive":
        raise ImproperLink(url,"\n\n\n A base link was used with the archive module. Please use an archive leaderboard link.")
      elif ARCHIVE_IDENTIFIER not in url and type=="legacy":
        raise ImproperLink(url,"\n\n\n A base link was used with the legacy module. Please use an legacy leaderboard link.")
    return inner
  return wrap

def linkFormatCheck(type:str):
  """Checks Links For Validity With The Modules. Prevents Archive Links With Base Module & Vice Versa
  """
  def wrap(func):
    def inner(*args,**kwargs):
      url=args[1]
      func(*args,**kwargs)
      if ARCHIVE_IDENTIFIER in url and type=="base":
        raise ImproperLink(url,"\n\n\n A archive link was used with the base module. Please use a regular leaderboard link.")
      elif ARCHIVE_IDENTIFIER not in url and type=="archive":
        raise ImproperLink(url,"\n\n\n A base link was used with the archive module. Please use an archive leaderboard link.")
      elif ARCHIVE_IDENTIFIER not in url and type=="legacy":
        raise ImproperLink(url,"\n\n\n A base link was used with the legacy module. Please use an legacy leaderboard link.")
    return inner
  return wrap