import json
import requests
import os
import sys

from pathlib import Path
#from work_with_backend import *
#func()


p = Path(__file__)
print(p) # шлях до файлу
print(p.parent) # шлях до папки де він лежить
print(p.parent.parent)
import lets_do_it as ldit
#print(sys.path)
ldit.spam()
sys.path.insert(0, str(p.parent.parent))
#print(sys.path)
#print(dir(sys)) # в  сіс
#print(dir()) # в  нашому коді
print(ldit.__name__)
# from . import name
# from .. import name

x = 10
def some():
    x = 30
    def get_x():
        nonlocal x
        #x = 20
        return x
    print(x)
    print(get_x())


some()
print(x)