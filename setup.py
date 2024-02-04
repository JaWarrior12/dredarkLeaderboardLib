from setuptools import setup

setup(
   name='dredarkLeaderboardLib',
   version='1.0.0-alpha',
   description='A Library to fetch from the Deep Space Airships leaderboards.',
   author='JaWarrior12',
   packages=['dredarkLeaderboardLib'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)