from DataBase import*
from pprint import pprint
import os

init_cache()
#l = yield_by_mineral('Tritanium')
#pprint(l)

yield_by_mineral('Tritanium')
pprint(yield_by_mineral('Tritanium','com_volume'))
