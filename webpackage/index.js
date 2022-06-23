var Repro=0
var ReproEff=0
var Imp=0

var SimOre=0
var CohOre=0
var VarOre=0
var ComOre=0
var MerOre=0
var AbyOre=0

var Sec=0
var Str=0
var Rig=0

var SimOreEff=0.5
var CohOreEff=0.5
var VarOreEff=0.5
var ComOreEff=0.5
var MerOreEff=0.5
var AbyOreEff=0.5
var batch = {}

const SimOres=['Plagioclase','Pyroxeres','Scordite','Veldspar']
const CohOres=['Hemorphite','Hedbergite',,'Omber','Kernite','Jaspet']
const VarOres=['Gneiss','Dark Ochre','Crokite']
const ComOres=['Bistot','Arkonor','Spodumain']
const MerOres=['Mercoxit']
const AbyOres=['Bezdnacine','Rakovene','Talassonite']

const Minerals = ['Tritanium','Pyerite','Mexallon','Isogen','Nocxium','Zydrine','Megacyte','Morphite']
const Ores = ['Veldspar','Scordite','Pyroxeres','Plagioclase','Omber','Kernite','Jaspet','Hemorphite','Hedbergite','Gneiss','Dark Ochre','Crokite','Bistot','Arkonor','Mercoxit','Spodumain','Bezdnacine','Rakovene','Talassonite']
const Ores_Data = {'Veldspar':     {'Refinery':{'Tritanium':400},
                              'volume':0.1,'compressed_volume':0.0001, 'batch_compressed_volume':0.15},
                              
             'Scordite':     {'Refinery':{'Tritanium':150,'Pyerite':90},
                              'volume':0.15,'compressed_volume':0.0015, 'batch_compressed_volume':0.19},
             
             'Pyroxeres':    {'Refinery':{'Pyerite':90,'Mexallon':30},
                              'volume':0.3,'compressed_volume':0.003, 'batch_compressed_volume':0.16},
             
             'Plagioclase':  {'Refinery':{'Tritanium':175,'Mexallon':70},
                              'volume':0.35,'compressed_volume':0.0035, 'batch_compressed_volume':0.15},
             
             'Omber':        {'Refinery':{'Pyerite':90,'Isogen':75},
                              'volume':0.6,'compressed_volume':0.006, 'batch_compressed_volume':0.3},
             
             'Kernite':      {'Refinery':{'Mexallon':60,'Isogen':120},
                              'volume':1.2,'compressed_volume':0.012, 'batch_compressed_volume':0.19},
             
             'Jaspet':       {'Refinery':{'Mexallon':150,'Nocxium':50},
                              'volume':2.0,'compressed_volume':0.02, 'batch_compressed_volume':0.15},
             
             'Hemorphite':   {'Refinery':{'Isogen':240,'Nocxium':90},
                              'volume':3.0,'compressed_volume':0.03, 'batch_compressed_volume':0.86},
             
             'Hedbergite':   {'Refinery':{'Pyerite':90,'Nocxium':120},
                              'volume':3.0,'compressed_volume':0.03, 'batch_compressed_volume':0.47},
             
             'Gneiss':       {'Refinery':{'Pyerite':2000,'Mexallon':1500,'Isogen':800},
                              'volume':5.0,'compressed_volume':0.05, 'batch_compressed_volume':1.8},
             
             'Dark Ochre':   {'Refinery':{'Mexallon':1360,'Isogen':1200,'Nocxium':320},
                              'volume':8.0,'compressed_volume':0.08, 'batch_compressed_volume':4.2},
             
             'Crokite':      {'Refinery':{'Pyerite':800,'Mexallon':2000,'Nocxium':800},
                              'volume':16.0,'compressed_volume':0.16, 'batch_compressed_volume':7.81},
             
             'Bistot':       {'Refinery':{'Pyerite':3200,'Mexallon':1200,'Zydrine':160},
                              'volume':16.0,'compressed_volume':0.16, 'batch_compressed_volume':4.4},
             
             'Arkonor':      {'Refinery':{'Pyerite':3200,'Mexallon':1200,'Megacyte':120},
                              'volume':16.0,'compressed_volume':0.16, 'batch_compressed_volume':8.8},
             
             'Mercoxit':     {'Refinery':{'Morphite':140},
                              'volume':40.0,'compressed_volume':0.4, 'batch_compressed_volume':0.1},
             
             'Spodumain':    {'Refinery':{'Tritanium':48000,'Isogen':1000,'Nocxium':160,'Zydrine':80,'Megacyte':40},
                              'volume':16.0,'compressed_volume':0.16, 'batch_compressed_volume':28.0},
             
             'Bezdnacine':   {'Refinery':{'Tritanium':40000,'Isogen':4800,'Megacyte':180},
                              'volume':16.0,'compressed_volume':0.16},
             
             'Rakovene':     {'Refinery':{'Tritanium':40000,'Isogen':3200,'Zydrine':200},
                              'volume':16.0,'compressed_volume':0.16},
             
             'Talassonite':  {'Refinery':{'Tritanium':40000,'Nocxium':960,'Megacyte':32},
                              'volume':16.0,'compressed_volume':0.16},
    }

// #Variants have mineral yield modifier
const Ore_Variants = {'Veldspar':     {'Veldspar':1.00,'Concentrated':1.05,'Dense':1.10,'Stable':1.15},
                'Scordite':     {'Scordite':1.00,'Condensed':1.05,'Massive':1.10,'Glossy':1.15},
                'Pyroxeres':    {'Pyroxeres':1.00,'Solid':1.05,'Viscous':1.10,'Opulent':1.15},
                'Plagioclase':  {'Plagioclase':1.00,'Azure':1.05,'Rich':1.10,'Sparkling':1.15},
                'Omber':        {'Omber':1.00,'Silvery':1.05,'Golden':1.10,'Platinoid':1.15},
                'Kernite':      {'Kernite':1.00,'Luminous':1.05,'Fiery':1.10,'Resplendant':1.15},
                'Jaspet':       {'Jaspet':1.00,'Pure':1.05,'Pristine':1.10,'Immaculate':1.15},
                'Hemorphite':   {'Hemorphite':1.00,'Vivid':1.05,'Radiant':1.10,'Scintillating':1.15},
                'Hedbergite':   {'Hedbergite':1.00,'Vitric':1.05,'Glazed':1.10,'Lustrous':1.15},
                'Gneiss':       {'Gneiss':1.00,'Iridescent':1.05,'Prismatic':1.10,'Brilliant':1.15},
                'Dark Ochre':   {'Dark Ochre':1.00,'Onyx':1.05,'Obsidian':1.10,'Jet':1.15},
                'Crokite':      {'Crokite':1.00,'Sharp':1.05,'Crystalline':1.10,'Pellucid':1.15},
                'Bistot':       {'Bistot':1.00,'Triclinic':1.05,'Monoclinic':1.10,'Cubic':1.15},
                'Arkonor':      {'Arkonor':1.00,'Crimson':1.05,'Prime':1.10,'Flawless':1.15},
                'Mercoxit':     {'Mercoxit':1.00,'Magma':1.05,'Vitreous':1.10},
                'Spodumain':    {'Spodumain':1.00,'Bright':1.05,'Gleaming':1.10,'Dazzling':1.15},
                'Bezdnacine':   {'Bezdnacine':1.00,'Abyssal':1.05,'Hadal':1.10},
                'Rakovene':     {'Rakovene':1.00,'Abyssal ':1.05,'Hadal ':1.10},
                'Talassonite':  {'Talassonite':1.00,'Abyssal':1.05,'Hadal':1.10}
            }

function DisplayAndSave(obj, val){
    obj.nextElementSibling.value = obj.value
    SetVal(obj, val)
    // console.log(document.getElementById("attr").elements[2])
}

function SetVal(obj, val){
    var c=false
    switch(obj.id){
        case "Repro":
            Repro = parseFloat(val)
            break
        case "ReproEff":
            ReproEff = parseFloat(val)
            break
        case "simore":
            SimOre = parseFloat(val)
            break
        case "cohore":
            CohOre = parseFloat(val)
            break
        case "varore":
            VarOre = parseFloat(val)
            break
        case "comore":
            ComOre = parseFloat(val)
            break
        case "merore":
            MerOre = parseFloat(val)
            break
        case "abyore":
            AbyOre = parseFloat(val)
            break
        case "Imp":
            Imp = parseFloat(val)
            break
        case "sec":
            Sec = parseFloat(val)
            break
        case "stru":
            Str = parseFloat(val)
            break
        case "rig":
            Rig = parseFloat(val)
            break
    }
    // ParseAll()
    var SimYield = document.getElementById("SimYield")
    var CohYield = document.getElementById("CohYield")
    var VarYield = document.getElementById("VarYield")
    var ComYield = document.getElementById("ComYield")
    var MerYield = document.getElementById("MerYield")
    var AbyYield = document.getElementById("AbyYield")
    // console.log("Sec", Sec, 1+Sec)
    var BaseYield = ((50+Rig)*(1+Sec))*(1+Str)*(1+(0.03*Repro))*(1+(0.02*ReproEff))*(1+Imp)
    SimYield.innerHTML="Simple Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*SimOre))) +"%"
    CohYield.innerHTML="Coherent Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*CohOre))) +"%"
    VarYield.innerHTML="Variegated Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*VarOre))) +"%"
    ComYield.innerHTML="Complex Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*ComOre))) +"%"
    MerYield.innerHTML="Mercoxit Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*MerOre))) +"%"
    AbyYield.innerHTML="Abyssal Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*AbyOre))) +"%"
    SimOreEff=BaseYield*(1+(0.02*SimOre))/100
    CohOreEff=BaseYield*(1+(0.02*CohOre))/100
    VarOreEff=BaseYield*(1+(0.02*VarOre))/100
    ComOreEff=BaseYield*(1+(0.02*ComOre))/100
    MerOreEff=BaseYield*(1+(0.02*MerOre))/100
    AbyOreEff=BaseYield*(1+(0.02*AbyOre))/100
    // DisplayYield()
    // console.log(obj.id,val)
}



function SetCattrMax(){
    let repro = document.getElementById("Repro")
    repro.value=5
    DisplayAndSave(repro,5)
    let reproeff = document.getElementById("ReproEff")
    reproeff.value=5
    DisplayAndSave(reproeff,5)
    let imp = document.getElementById("Imp")
    imp.value=0.04
    SetVal(imp,0.04)
}

function SetOattrMax(){
    let simore = document.getElementById("simore")
    simore.value=5
    DisplayAndSave(simore,5)
    let cohore = document.getElementById("cohore")
    cohore.value=5
    DisplayAndSave(cohore,5)
    let varore = document.getElementById("varore")
    varore.value=5
    DisplayAndSave(varore,5)
    let comore = document.getElementById("comore")
    comore.value=5
    DisplayAndSave(comore,5)
    let merore = document.getElementById("merore")
    merore.value=5
    DisplayAndSave(merore,5)
    let abyore = document.getElementById("abyore")
    abyore.value=5
    DisplayAndSave(abyore,5)
}



function Round2(num){
    return Math.round(num * 100) /100
}

function DisplayOutput(){
    var leftover = {}
    var out = {}
    for(i=0;i<Minerals.length;i++){
        out[Minerals[i]]=0
    }
    var string = document.getElementById("oreinput").value
    l = string.split('\n')
    for(i=0;i<l.length;i++){
        var VarMultiplier=1
        item = l[i].split('\t')[0]
        val = parseFloat(l[i].split('\t')[1])
        batch[item] = val
        orename=item.split(' ')[item.split(' ').length-1]
        
        if(Ores.includes(orename)){
            OreYieldSize = Object.keys(Ores_Data[orename]["Refinery"]).length
            OreYieldMinerals = Object.keys(Ores_Data[orename]["Refinery"])
            OreYieldValues =  Object.values(Ores_Data[orename]["Refinery"])
            var Eff, SingleYield
            if(SimOres.includes(orename)){
                Eff = SimOreEff
            } else if(CohOres.includes(orename)){
                Eff = CohOreEff
            } else if(VarOres.includes(orename)){
                Eff = VarOreEff
            } else if(ComOres.includes(orename)){
                Eff = ComOreEff
            } else if(MerOres.includes(orename)){
                Eff = MerOreEff
            } else if(AbyOres.includes(orename)){
                Eff = AbyOreEff
            }
            
            if(item.length>1){
                orevar=item.split(' ')[item.split(' ').length-2]
                
                if(orevar!="Compressed"){
                    VarMultiplier = Ore_Variants[orename][orevar]
                }
            }
            else{
                // uncompressed ores
            }
            if(item.includes("Compressed")){
                // new compressed ores
                if(item.includes("Batch")){
                    // old compressed ores
                }
                else{
                    val/=100
                }
                for(c=0;c<OreYieldSize;c++){
                    SingleYield=OreYieldValues[c]*Eff*VarMultiplier
                    out[OreYieldMinerals[c]]+=SingleYield*val
                    console.log(out)
                }
            }
        }
    }
    
    // console.log(out)
    
    // area = document.getElementById("Trioutput")
    // area.innerHTML = Object.keys(batch)
    // DisplayOutput()
    // console.log(batch)

}



// function DisplayYield(){
//     ParseAll()
//     var SimYield = document.getElementById("SimYield")
//     var CohYield = document.getElementById("CohYield")
//     var VarYield = document.getElementById("VarYield")
//     var ComYield = document.getElementById("ComYield")
//     var MerYield = document.getElementById("MerYield")
//     console.log((50+Rig))
//     console.log(typeof(Rig),Rig)
//     var BaseYield = ((50+Rig)*(1+Sec))*(1+Str)*(1+(0.03*Repro))*(1+(0.02*ReproEff))*(1+Imp)
//     SimYield.innerHTML="Simple Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*SimOre))) +"%"
//     CohYield.innerHTML="Coherent Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*CohOre))) +"%"
//     VarYield.innerHTML="Variegated Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*VarOre))) +"%"
//     ComYield.innerHTML="Complex Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*ComOre))) +"%"
//     MerYield.innerHTML="Mercoxit Ore Efficiency: "+ Round2(BaseYield*(1+(0.02*MerOre))) +"%"
// }

// function Saveall(){
//     var form = document.getElementById("attr")
//     for(e=0; e<form.length;e++ ){
//         switch(form[e].id){
//             case "Repro":
//                 Repro = form[e].value
//             case "ReproEff":
//                 ReproEff = form[e].value
//             case "Imp":
//                 Imp = form[e].value
//             case "simore":
//                 SimOre = form[e].value
//             case "cohore":
//                 CohOre = form[e].value
//             case "varore":
//                 VarOre = form[e].value
//             case "comore":
//                 ComOre = form[e].value
//             case "merore":
//                 MerOre = form[e].value
//             case "sec":
//                 Sec = form[e].value
//             case "stru":
//                 Str = form[e].value
//             case "rig":
//                 Rig = form[e].value
//         }
//         console.log(form[e])
//     }
// }

// function displayall(){
//     console.log("Repro",Repro)
//     console.log("ReproEff",ReproEff)
//     console.log("Imp",Imp)
//     console.log("SimOre",SimOre)
//     console.log("CohOre",CohOre)
//     console.log("VarOre",VarOre)
//     console.log("ComOre",ComOre)
//     console.log("MerOre",MerOre)
//     console.log("Sec",Sec)
//     console.log("Str",Str)
//     console.log("Rig",Rig)
// }

// function Restore(){
//     var form = document.getElementById("attr")
//     for(e=0; e<form.length;e++ ){
//         switch(form[e].id){
//             case "Repro":
//                 form[e].value=Repro
//                 Display(form[e],Repro)
//             case "ReproEff":
//                 form[e].value=ReproEff
//                 Display(form[e],ReproEff)
//             case "Imp":
//                 form[e].value=Imp
//                 Display(form[e],Imp)
//             case "simore":
//                 form[e].value=SimOre
//                 Display(form[e],SimOre)
//             case "cohore":
//                 form[e].value=CohOre
//                 Display(form[e],CohOre)
//             case "varore":
//                 form[e].value=VarOre
//                 Display(form[e],VarOre)
//             case "comore":
//                 form[e].value=ComOre
//                 Display(form[e],ComOre)
//             case "merore":
//                 form[e].value=MerOre
//                 Display(form[e],MerOre)
//             case "sec":
//                 switch(Sec){
//                     case "ns":
//                         form[e].selectedIndex = 0
//                     case "ls":
//                         form[e].selectedIndex = 1
//                     case "hs":
//                         form[e].selectedIndex = 2
//                 }
//             case "stru":
//                 form[e].value=Str
//                 Display(form[e],Str)
//             case "rig":
//                 form[e].value=Rig
//                 Display(form[e],Rig)
//         }
//     }
// }