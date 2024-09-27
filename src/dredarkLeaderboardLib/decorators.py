from .errors import *
from .checks import *

import time

MAX_CALLS=5 #Max Calls Per Period
PERIOD=20 #In Seconds

def rate_limits():
  def decorator(func):
      calls = 0
      last_reset = time.time()

      def wrapper(*args, **kwargs):
          nonlocal calls, last_reset

          # Calculate time elapsed since last reset
          elapsed = time.time() - last_reset

          # If elapsed time is greater than the period, reset the call count
          if elapsed > PERIOD:
              calls = 0
              last_reset = time.time()

          # Check if the call count has reached the maximum limit
          if calls >= MAX_CALLS:
              raise Exception(f"Rate limit exceeded. Please try again later. Rate Limit is {MAX_CALLS} calls per {PERIOD} seconds.")

          # Increment the call count
          calls += 1

          # Call the original function
          return func(*args, **kwargs)

      return wrapper
  return decorator