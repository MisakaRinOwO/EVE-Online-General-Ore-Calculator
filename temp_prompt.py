from DataBase import*
from refinary_bonus import*
from pprint import pprint
import os,Profile
from APIs import*
'''
init_cache()
generate_regular_id_to_cache()
generate_additional_id_to_cache()
yield_by_mineral('Tritanium')
#pprint(l)
pprint(get_cache('history'))

print(list(Path(os.getcwd()).iterdir()))
p = Profile.Profile('tat')
'''

r = reprocessing()
r.set_implant(804)
r.set_rig("t2")
r.set_skill_repo(5)
r.set_skill_repo_eff(5)
r.set_structure("tatara")
r.printdata()