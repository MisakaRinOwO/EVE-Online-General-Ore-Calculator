from DataBase import*
import os
from pathlib import Path

class Profile:
    def __init__(self,name:str):
        self.local_check(name)
    
    def local_check(self,name):
        if not file_exists('Profiles'):
            os.mkdir('Profiles')
        if not any(name+'.rin' in str(d) for d in list(Path(os.getcwd()+'\\Profiles').iterdir())):
            f = open(Path(os.getcwd()+'\\Profiles\\' + name+'.rin'),'x')
            f.close()