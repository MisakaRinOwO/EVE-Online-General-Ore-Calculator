from DataBase_Ore import*
import os
from pathlib import Path

class Profile:
    def __init__(self,name:str):
        self.local_check(name)
    
    def local_check(self,name):
        if not file_exists('Profiles'):
            os.mkdir('Profiles')
        if not any(name+'.txt' in str(d) for d in list(Path(os.getcwd()+'\\Profiles').iterdir())):
            f = open(Path(os.getcwd()+'\\Profiles\\' + name+'.txt'),'x')
            f.close()