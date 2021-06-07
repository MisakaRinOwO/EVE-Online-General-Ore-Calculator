from DataBase import*
from pprint import pprint
import os
from APIs import*

init_cache()
generate_regular_id_to_cache()
generate_additional_id_to_cache()
#l = yield_by_mineral('Tritanium')
#pprint(l)

yield_by_mineral('Tritanium')
pprint(yield_by_mineral('Tritanium','com_volume'))