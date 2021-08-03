#Explanations about reprocessing:
#   usually reprocessing happens in structure Tatara or Athanor
#   Tatara has a role bonus of 4%, Athanor has 2%
#   skill_reprocessing: max at 5 levels, +3% yield per level
#   skill_reprocessing_efficiency: max at 5 levels, +2% yield per level
#   needs to add special ore skills later
from numpy.doc import structured_arrays
class InvalidParamError:
    pass


class reprocessing:
    def __init__(self, structure = None, rig = None, skill_reprocessing = 0, skill_reprocessing_efficiency = 0, implant = None, security = None):
        self.structure = structure
        self.rig = rig
        self.skill_repo = skill_reprocessing
        self.skill_repo_eff = skill_reprocessing_efficiency
        self.implant = implant
        self.sec = 'hs'
        self.orelst = ['arkonor','bistot','crokite','darkochre','gneiss','hedbergite','hemorphite','hydromagnetic','jaspet',\
                        'kemite','mercoxit','omber','plagioclase','pyroxers','scordite','spodumain','veldspar']
        self.special_ore_skill_init()
        
    def special_ore_skill_init(self):
        for ore in self.orelst:
            self.__dict__[ore+'_proc'] = 0
        
    def special_set_all_5(self):
        for ore in self.orelst:
            self.__dict__[ore+'_proc'] = 5 
            
    def print_ore_list(self):
        for ore in self.orelst:
            print(ore)
            
    def print_ore_skills(self):
        for ore in self.orelst:
            print(f"{ore} processing: {self.__dict__[ore+'_proc']}")
    
    def print_ore_efficiency(self):
        for ore in self.orelst:
            print(f"{ore} efficiency: {self.get_indv_ore_bonus(ore)}%   lv:{self.__dict__[ore+'_proc']}")
            
    def printdata(self):
        print("\n------------------------------current------------------------------")
        print(f"structure: {self.structure}")
        if self.sec.lower() == 'hs':
            print("space: High Sec")
        elif self.sec.lower() == 'ls':
            print("space: Low Sec")
        else:
            print("space: Null Sec")
        print(f"rig: {self.rig}")
        print(f"reprocessing skill level: {self.skill_repo}")
        print(f"reprocessing efficiency skill level: {self.skill_repo_eff}")
        print(f"implant: {self.implant}\n")
        est = self.get_bonus()
        print(f"estimated efficiency: {est}%\n")

    def set_structure(self,structure):
        if type(structure) != str or structure.lower() not in ['tatara','athanor']:
            raise InvalidParamError()
        else:
            self.structure = structure
    
    def set_rig(self,rig):
        if type(rig) != str or rig.lower() not in ['t1','t2']:
            raise InvalidParamError()
        else:
            self.rig = rig
    
    def set_skill_repo(self,skill):
        if type(skill) != int or skill < 0 or skill > 5:
            raise InvalidParamError()
        else:
            self.skill_repo = skill
    
    def set_skill_repo_eff(self,skill):
        if type(skill) != int or skill < 0 or skill > 5:
            raise InvalidParamError()
        else:
            self.skill_repo_eff = skill
    
    def set_implant(self,implant):
        if implant != None and implant not in [801,802,804]:
            raise InvalidParamError()
        else:
            self.implant = implant
            
    def set_security(self,sec):
        if type(sec) != str or sec.lower() not in ['hs','ls','null']:
            raise InvalidParamError()
        else:
            self.sec = sec
    
    def check_all_ok(self):
        return all([self.structure != None and self.structure.lower() in ['tatara','athanor'],\
                             self.rig == None or self.rig.lower() in ['t1','t2'],\
                             self.skill_repo >= 0 and self.skill_repo <= 5,\
                             self.skill_repo_eff >= 0 and self.skill_repo_eff <= 5,\
                             self.implant == None or self.implant in [801,802,804],\
                             self.sec.lower() in ['hs','ls','null']])
    
    def get_bonus(self):
        if self.check_all_ok():
            structure = 1.04 if self.structure.lower() == 'tatara' else 1.02
            repo = 1 + 0.02 * self.skill_repo
            repo_eff = 1 + 0.03 * self.skill_repo_eff
            imp = 1 + 0.01*(self.implant%800) if self.implant in [801,802,804] else 1
            
            if self.rig == None:
                rig = 1
            elif self.rig.lower() == 't1':
                rig = 0.51 
            else:
                rig = 0.53

            if self.sec.lower() == 'ls':
                sec = 1.06
            elif self.sec.lower() == 'null':
                sec = 1.12
            else:
                sec = 1
                
            return round(structure*rig*repo*repo_eff*imp*sec*100,3)
            
        else:
            return "N/A"
        
    def get_indv_ore_bonus(self, ore):
        if ore.lower() == 'dark ochre':
            return round(self.get_bonus()*(1 + 0.02*self.darkochre_proc), 3)
        elif ore.lower() in self.orelst:
            return round(self.get_bonus()*(1 + 0.02*self.__dict__[ore+'_proc']), 3)
            
    def set_special_ore_skill(self, ore , lv):
        if lv <= 0 or lv > 5:
            raise InvalidParamError()
        elif ore.lower() == 'dark ochre':
            self.darkochre_proc = lv
        elif ore.lower() in self.orelst:
            self.__dict__[ore+'_proc'] = lv
        else:
            raise InvalidParamError()
            