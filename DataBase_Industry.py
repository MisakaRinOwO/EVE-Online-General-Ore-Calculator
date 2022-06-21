import os, inspect
from pathlib import Path
from APIs import*


###This is a database for ship manufacturing costs###
cap_parts = ['capital armor plate', 'capital capacitor battery', 'capital cargo bay', 'capital clone vat bay', 'capital computer system', 'capital construction parts', 'capital corp hangar bay', 'capital doomsday weapon mount']
Cargo Bay
Vat Bay
Computer System
Construction Parts
Corp Hangar Bay
Doomsday Weapon mt
Drone Bay
Jump Bridge Array
Jump Drive
Lacuncher Hard pt
Power Generatior
Propulsion Engiine
Sensor Cluster
Shield Emitter
Ship Maintenance Bay
Siege Array
Turret Hard pt]

ships = {'capital ships' :
            {'dreadnoughts' : 
                {'revelation' : {},
                 'phoenix' :    {},
                 'moros' :      {},
                 'naglfar' :    {}},
            
             'carriers' :
                {'archon' :     {},
                 'chimera' :    {},
                 'Thanatos' :   {},
                 'nidhoggur' :  {}},
            
             'industrial' :
                {'rorqual' :    {}},
                
             'force auxiliaries' :
                {'apostle' :    {},
                 'minokawa' :   {},
                 'ninazu' :     {},
                 'lif' :        {}},
                
            'freighters' :
                {'providence' : {},
                 'charon'     : {},
                 'obelisk'    : {},
                 'fenrir'     : {}}
            }
        }