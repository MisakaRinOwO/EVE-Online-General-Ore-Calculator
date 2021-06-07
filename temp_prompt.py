from DataBase import*
from pprint import pprint
import os,Profile
from APIs import*

init_cache()
generate_regular_id_to_cache()
generate_additional_id_to_cache()
yield_by_mineral('Tritanium')
#pprint(l)
pprint(get_cache('history'))

print(list(Path(os.getcwd()).iterdir()))
p = Profile.Profile('tat')
