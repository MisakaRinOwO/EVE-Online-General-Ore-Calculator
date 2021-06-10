import os, inspect
from pathlib import Path
from APIs import*
#Based on the first resource distribution update
#https://www.eveonline.com/news/view/resource-distribution-update

#Here is an easy-read chart:
#             |   Tritanium  |  Pyerite  |  Mexallon  |  Isogen  |  Nocxium  |  Zydrine  |  Megacyte  |  Morphite
#Veldspar     |      400     |           |            |          |           |           |            |
#Scordite     |      150     |    90     |            |          |           |           |            |
#Pyroxeres    |              |    90     |     30     |          |           |           |            |
#Plagioclase  |      175     |           |     70     |          |           |           |            |
#Omber        |              |    90     |            |    75    |           |           |            |        
#Kernite      |              |           |     60     |    120   |           |           |            |
#Jaspet       |              |           |     150    |          |    50     |           |            |
#Hemorphite   |              |           |            |    240   |    90     |           |            |
#Hedbergite   |              |    450    |            |          |    120    |           |            |          
#Gneiss       |              |   2000    |    1500    |    800   |           |           |            |
#Dark Ochre   |              |           |    1360    |   1200   |    320    |           |            |
#Crokite      |              |    800    |    2000    |          |    800    |           |            |          
#Bistot       |              |   3200    |    1200    |          |           |    160    |            | 
#Arkonor      |              |   3200    |    1200    |          |           |           |    120     |            
#Mercoxit     |              |           |            |          |           |           |            |     140
#Spodumain    |      48000   |           |            |   1000   |    160    |    80     |    40      |        
#Bezdnacine   |      40000   |           |            |   4800   |           |           |    128     |         
#Rakovene     |      40000   |           |            |   3200   |           |    200    |            |
#Talassonite  |      40000   |           |            |          |    960    |           |    32      |         
Minerals = ['Tritanium','Pyerite','Mexallon','Isogen','Nocxium','Zydrine','Megacyte','Morphite']

Ores = ['Veldspar','Scordite','Pyroxeres','Plagioclase','Omber','Kernite','Jaspet','Hemorphite','Hedbergite','Gneiss','Dark Ochre','Crokite','Bistot','Arkonor','Mercoxit','Spodumain','Bezdnacine','Rakovene','Talassonite']



#Data for ores are based on 100 unit of base ores
#   or 1 unit of compressed base ores
Ores_Data = {'Veldspar':     {'Refinery':{'Tritanium':400},
                              'volume':0.1,'compressed_volume':0.15},
                              
             'Scordite':     {'Refinery':{'Tritanium':150,'Pyerite':90},
                              'volume':0.15,'compressed_volume':0.19},
             
             'Pyroxeres':    {'Refinery':{'Pyerite':90,'Mexallon':30},
                              'volume':0.3,'compressed_volume':0.16},
             
             'Plagioclase':  {'Refinery':{'Tritanium':175,'Mexallon':70},
                              'volume':0.35,'compressed_volume':0.15},
             
             'Omber':        {'Refinery':{'Pyerite':90,'Isogen':75},
                              'volume':0.6,'compressed_volume':0.3},
             
             'Kernite':      {'Refinery':{'Mexallon':60,'Isogen':120},
                              'volume':1.2,'compressed_volume':0.19},
             
             'Jaspet':       {'Refinery':{'Mexallon':150,'Nocxium':50},
                              'volume':2.0,'compressed_volume':0.15},
             
             'Hemorphite':   {'Refinery':{'Isogen':240,'Nocxium':90},
                              'volume':3.0,'compressed_volume':0.86},
             
             'Hedbergite':   {'Refinery':{'Pyerite':90,'Nocxium':120},
                              'volume':3.0,'compressed_volume':0.47},
             
             'Gneiss':       {'Refinery':{'Pyerite':2000,'Mexallon':1500,'Isogen':800},
                              'volume':5.0,'compressed_volume':1.8},
             
             'Dark Ochre':   {'Refinery':{'Mexallon':1360,'Isogen':1200,'Nocxium':320},
                              'volume':8.0,'compressed_volume':4.2},
             
             'Crokite':      {'Refinery':{'Pyerite':800,'Mexallon':2000,'Nocxium':800},
                              'volume':16.0,'compressed_volume':7.81},
             
             'Bistot':       {'Refinery':{'Pyerite':3200,'Mexallon':1200,'Zydrine':160},
                              'volume':16.0,'compressed_volume':4.4},
             
             'Arkonor':      {'Refinery':{'Pyerite':3200,'Mexallon':1200,'Megacyte':120},
                              'volume':16.0,'compressed_volume':8.8},
             
             'Mercoxit':     {'Refinery':{'Morphite':140},
                              'volume':40.0,'compressed_volume':0.1},
             
             'Spodumain':    {'Refinery':{'Tritanium':48000,'Isogen':1000,'Nocxium':160,'Zydrine':80,'Megacyte':40},
                              'volume':16.0,'compressed_volume':28.0},
             
             #uncompressable ores starts here
             'Bezdnacine':   {'Refinery':{'Tritanium':40000,'Isogen':4800,'Megacyte':180},
                              'volume':16.0},
             
             'Rakovene':     {'Refinery':{'Tritanium':40000,'Isogen':3200,'Zydrine':200},
                              'volume':16.0},
             
             'Talassonite':  {'Refinery':{'Tritanium':40000,'Nocxium':960,'Megacyte':32},
                              'volume':16.0},
    }

#Variants have mineral yield modifier
Ore_Variants = {'Veldspar':     {'Veldspar':1.00,'Concentrated Veldspar':1.05,'Dense Veldspar':1.10,'Stable Veldspar':1.15},
                'Scordite':     {'Scordite':1.00,'Condensed Scordite':1.05,'Massive Scordite':1.10,'Glossy Scordite':1.15},
                'Pyroxeres':    {'Pyroxeres':1.00,'Solid Pyroxeres':1.05,'Viscous Pyroxeres':1.10,'Opulent Pyroxeres':1.15},
                'Plagioclase':  {'Plagioclase':1.00,'Azure Plagioclase':1.05,'Rich Plagioclase':1.10,'Sparkling Plagioclase':1.15},
                'Omber':        {'Omber':1.00,'Silvery Omber':1.05,'Golden Omber':1.10,'Platinoid Omber':1.15},
                'Kernite':      {'Kernite':1.00,'Luminous Kernite':1.05,'Fiery Kernite':1.10,'Resplendant Kernite':1.15},
                'Jaspet':       {'Jaspet':1.00,'Pure Jaspet':1.05,'Pristine Jaspet':1.10,'Immaculate Jaspet':1.15},
                'Hemorphite':   {'Hemorphite':1.00,'Vivid Hemorphite':1.05,'Radiant Hemorphite':1.10,'Scintillating Hemorphite':1.15},
                'Hedbergite':   {'Hedbergite':1.00,'Vitric Hedbergite':1.05,'Glazed Hedbergite':1.10,'Lustrous Hedbergite':1.15},
                'Gneiss':       {'Gneiss':1.00,'Iridescent Gneiss':1.05,'Prismatic Gneiss':1.10,'Brilliant Gneiss':1.15},
                'Dark Ochre':   {'Dark Ochre':1.00,'Onyx Ochre':1.05,'Obsidian Ochre':1.10,'Jet Ochre':1.15},
                'Crokite':      {'Crokite':1.00,'Sharp Crokite':1.05,'Crystalline Crokite':1.10,'Pellucid Crokite':1.15},
                'Bistot':       {'Bistot':1.00,'Triclinic Bistot':1.05,'Monoclinic Bistot':1.10,'Cubic Bistot':1.15},
                'Arkonor':      {'Arkonor':1.00,'Crimson Arkonor':1.05,'Prime Arkonor':1.10,'Flawless Arkonor':1.15},
                'Mercoxit':     {'Mercoxit':1.00,'Magma Mercoxit':1.05,'Vitreous Mercoxit':1.10},
                'Spodumain':    {'Spodumain':1.00,'Bright Spodumain':1.05,'Gleaming Spodumain':1.10,'Dazzling Spodumain':1.15},
                }

#Returns yield by mineral entered, sorted by key
#Keys:  default/None      - return mineral yield from database
#       volume            - return mineral yield from database per 100 units of uncompressed ore
#       compressed_volume - return mineral yield from database per 1 unit of compressed ore
class IDError:
    pass

def yield_search(ore:str, mineral:str, key:str = 'default') -> int:
    if f"yield_search({ore},{mineral},{key})" not in cache:
        if key == 'default':
            cache[f"yield_search({ore},{mineral},{key})"] = (r := Ores_Data[ore]['Refinery'][mineral] if mineral in Ores_Data[ore]['Refinery'] else 0)
            cache_update()
            return r
        elif key == 'volume':
            cache[f"yield_search({ore},{mineral},{key})"] = (r := round(Ores_Data[ore]['Refinery'][mineral]/Ores_Data[ore]['volume']/100,3)\
                                                             if mineral in Ores_Data[ore]['Refinery'] else 0)
            cache_update()
            return r
        elif key == 'com_volume':
            cache[f"yield_search({ore},{mineral},{key})"] = (r := round(Ores_Data[ore]['Refinery'][mineral]/Ores_Data[ore]['compressed_volume'],3)\
                                                             if mineral in Ores_Data[ore]['Refinery'] and 'compressed_volume' in Ores_Data[ore] else 0)
            cache_update()
            return r
    else:
        return cache[f"yield_search({ore},{mineral},{key})"]


#Returns a ore ranking list of yields by mineral entered, sorted by key
def yield_by_mineral(mineral:str, key:str = 'default', variants:bool = None) -> list:
    if f"yield_by_mineral({mineral},{key},{variants})" not in cache:
        if variants == None:
            cache[f"yield_by_mineral({mineral},{key},{variants})"] = \
            (r:=[o + f": {yield_search(o,mineral,key)}" for o in\
                 sorted([i for i in Ores_Data], key = lambda i:yield_search(i,mineral,key), reverse = True)])
        cache_update()
        return r
    else:
        return cache[f"yield_by_mineral({mineral},{key},{variants})"]

#Initial cache variable from locak cache file
def init_cache():
    global cache
    if file_exists('cache.rin'):
        f = open(os.getcwd()+'\\cache.rin','r')
        rl = f.readline()
        if rl != '':
            cache = eval(rl)
        else:
            cache = dict()
        f.close()
    else:
        f = open(os.getcwd()+'\\cache.rin','x')
        cache = dict()
        f.close()

#Updates the local cache file with current cache variable
def cache_update():
    f = open(os.getcwd()+'\\cache.rin','w')
    f.write(str(cache))
    f.close()

#check whether or not local file/directories exists
def file_exists(name):
    return any(name in str(p) for p in list(Path(os.getcwd()).iterdir()))

#fetch item id for minerals and basic ores from API and add them to local cache file
def generate_regular_id_to_cache():
    if 'ID' not in cache or (len(cache['ID']) != len(Ores)+len(Minerals) and len(cache['ID']) != sum_variants()+len(Minerals)+3):
        cache['ID'] = dict()
        for ore in Ores:
            if ore not in cache['ID']:
                query = get_item_id(ore)
                cache['ID'][query['typeName']] = str(query['typeID'])
        for mineral in Minerals:
            if mineral not in cache['ID']:
                query = get_item_id(mineral)
                cache['ID'][query['typeName']] = str(query['typeID'])
        cache_update()
        
#get total counts of ore variants, including the basic variant
def sum_variants():
        return sum([len(i) for i in list(Ore_Variants.values())])
    
#fetch item id for all ore variants from API and add them to local cache file
def generate_additional_id_to_cache():
    if 'ID' not in cache:
        raise IDError('ID not in cache, please run generate_regular_id_to_cache() first.')
    if len(cache['ID']) != sum_variants()+len(Minerals)+3:
        for variants in list(Ore_Variants.values()):
            for variant in variants:
                if variant not in cache['ID']:
                    query = get_item_id(variant)
                    cache['ID'][query['typeName']] = str(query['typeID'])
        cache_update()


def get_cache(filter: str = 'all') -> dict:
    r = dict()
    if filter == 'all':
        return cache
    elif filter == 'history':
        for c in cache:
            if c != 'ID':
                r.update({c:cache[c]})
        return r


#Decorator function for quick cache uppdates(update cache)
def uc(f):
    def wrapper():
        pass
    return wrapper



#Explanations about reprocessing:
#   usually reprocessing happens in structure Tatara or Athanor
#   Tatara has a role bonus of 4%, Athanor has 2%
#   skill_reprocessing: max at 5 levels, +3% yield per level
#   skill_reprocessing_efficiency: max at 5 levels, +2% yield per level



class reprocessing:
    def __init__(self,structure = None, rig = None, skill_reprocessing = 0, skill_reprocessing_efficiency = 0, implant = None):
        self.structure = structure
        
        
        

        
        
        
        