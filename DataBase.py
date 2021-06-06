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



