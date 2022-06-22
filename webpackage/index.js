var Repro=0
var ReproEff=0
var Imp=0

var SimOre=0
var CohOre=0
var VarOre=0
var ComOre=0
var MerOre=0

var Sec="ns"
var Str="cit"
var Rig=0

function Display(obj, val){
    obj.nextElementSibling.value = obj.value
    // console.log(document.getElementById("attr").elements[2])
}

function Saveall(){
    var form = document.getElementById("attr")
    for(e=0; e<form.length;e++ ){
        switch(form[e].id){
            case "Repro":
                Repro = form[e].value
            case "ReproEff":
                ReproEff = form[e].value
            case "Imp":
                Imp = form[e].value
            case "simore":
                SimOre = form[e].value
            case "cohore":
                CohOre = form[e].value
            case "varore":
                VarOre = form[e].value
            case "comore":
                ComOre = form[e].value
            case "merore":
                MerOre = form[e].value
            case "sec":
                Sec = form[e].value
            case "stru":
                Str = form[e].value
            case "rig":
                Rig = form[e].value
        }
        // console.log(form[e])
    }
    
}



function SetCattrMax(){
    let repro = document.getElementById("Repro")
    repro.value=5
    Display(repro,5)
    let reproeff = document.getElementById("ReproEff")
    reproeff.value=5
    Display(reproeff,5)
    let imp = document.getElementById("Imp")
    imp.value=804
}

function SetOattrMax(){
    let simore = document.getElementById("simore")
    simore.value=5
    Display(simore,5)
    let cohore = document.getElementById("cohore")
    cohore.value=5
    Display(cohore,5)
    let varore = document.getElementById("varore")
    varore.value=5
    Display(varore,5)
    let comore = document.getElementById("comore")
    comore.value=5
    Display(comore,5)
    let merore = document.getElementById("merore")
    merore.value=5
    Display(merore,5)
}

function displayall(){
    console.log("Repro",Repro)
    console.log("ReproEff",ReproEff)
    console.log("Imp",Imp)
    console.log("SimOre",SimOre)
    console.log("CohOre",CohOre)
    console.log("VarOre",VarOre)
    console.log("ComOre",ComOre)
    console.log("MerOre",MerOre)
    console.log("Sec",Sec)
    console.log("Str",Str)
    console.log("Rig",Rig)
}

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