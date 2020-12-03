import os
from termcolor import colored

print('Hello', colored(os.getlogin(),'yellow'), 'Welcomeback')

print('this is your current working directory:', (colored(os.getcwd(),'yellow')))