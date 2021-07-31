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
    def __init__(self, structure = None, rig = None, skill_reprocessing = 0, skill_reprocessing_efficiency = 0, implant = None):
        self.structure = structure
        self.rig = rig
        self.skill_repo = skill_reprocessing
        self.skill_repo_eff = skill_reprocessing_efficiency
        self.implant = implant
        
    def printdata(self):
        print("\n------------------------------current------------------------------")
        print(f"structure: {self.structure}")
        print(f"rig: {self.rig}")
        print(f"reprocessing skill level: {self.skill_repo}")
        print(f"reprocessing efficiency skill level: {self.skill_repo_eff}")
        print(f"implant: {self.implant}\n")
        est = self.get_bonus()
        print(f"estimated efficiency: {est}%")

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
    
    def check_all_ok(self):
        return all([self.structure != None and self.structure.lower() in ['tatara','athanor'],\
                             self.rig != None and self.rig.lower() in ['t1','t2'],\
                             self.skill_repo >= 0 and self.skill_repo <= 5,\
                             self.skill_repo_eff >= 0 and self.skill_repo_eff <= 5,\
                             self.implant == None or self.implant in [801,802,804]])
    
    def get_bonus(self):
        if self.check_all_ok():
            structure = 1.04 if self.structure.lower() == 'tatara' else 1.02
            rig = 0.51 if self.rig.lower() == 't1' else 0.53
            repo = 1 + 0.02 * self.skill_repo
            repo_eff = 1 + 0.03 * self.skill_repo_eff
            imp = 1 + 0.01*(self.implant%800) if self.implant in [801,802,804] else 1
            return round(structure*rig*repo*repo_eff*imp*100,3)
            
        else:
            return "N/A"