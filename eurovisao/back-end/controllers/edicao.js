var Edicao = module.exports
const axios = require('axios')

function myNormalize(r) {
    return r.results.bindings.map(o =>{
        var novo = {}
        for (let [k, v] of Object.entries(o)) {
            novo[k] = v.value
        }
        return novo;
    })
}

var prefixes = `
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX c: <http://www.di.uminho.pt/prc2021/eurovision#>
`

var getLink = "http://localhost:7200/repositories/Eurovisao" + "?query=" 


Edicao.getLista = async function(){
    
    var query = `select ?ano ?organizador ?vencedor ?musicaVencedora ?link where { 
        ?ed rdf:type c:Edição .
        ?ed c:anoEdição ?ano .
        ?ed c:organizadaPor ?pais .
        ?pais c:nome ?organizador. 
        ?ed c:temPaísVencedor ?Pvencedor .
        ?Pvencedor c:nome ?vencedor.
        ?Pvencedor c:temMúsica ?musica .
        ?musica c:título ?musicaVencedora.
        ?musica c:anoEdição ?ano.
        ?musica c:link ?link.
     
        
    } ` 
    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    } 
}

Edicao.getEdicao = async function(id){
    var query = `select ?organizador ?paisVencedor ?musicaVencedora where { 
        c:${id} c:anoEdição ?ano .
        c:${id} c:organizadaPor ?paisOrg .
        ?paisOrg c:nome ?organizador .
        c:${id} c:temPaísVencedor ?paisVenc .
        ?paisVenc c:nome ?paisVencedor .
        ?paisVenc c:temMúsica ?musica .
        ?musica c:anoEdição ?ano .
        ?musica c:título ?musicaVencedora.
    } ` 
    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    } 
}




Edicao.getPais = async function(id){
    var query = `select ?p ?lugar ?juri ?total ?televoto ?musica ?artista where { 
        ?class rdf:type c:Classificação .
        ?class c:anoEdição ${id} .
        ?class c:foiClassificadoCom ?pais.
        ?pais c:nome ?p.
    	?pais c:temMúsica ?m .
    	?m c:anoEdição ${id} .
    	?m c:título ?musica .
    	?m c:éInterpretadaPor ?a.
    	?a c:nome ?artista .
        ?class c:lugar ?lugar.
        OPTIONAL {?class c:totalPontos ?total}.
        OPTIONAL {?class c:televoto ?televoto}.
        OPTIONAL {?class c:juri ?juri}.
}` 
    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    } 
}


Edicao.getMusicas = async function(){
    
    var query = `select distinct ?ano (group_concat(distinct ?link; separator = ' ; ') as ?links) (group_concat(distinct ?m; separator = ' ; ') as ?musicas) ?pais ?lugar ?televoto ?juri ?total ?artista where { 
        ?musica rdf:type c:Música .
        ?musica c:título ?m.
        ?musica c:anoEdição ?ano.
        ?musica c:link ?link.
        ?p c:temMúsica ?musica.
        ?musica c:éInterpretadaPor ?art.
        ?art c:nome ?artista.
        ?p c:nome ?pais.
        ?p c:temClassificação ?class .
        ?class c:anoEdição ?ano .
        ?class c:lugar ?lugar.
        OPTIONAL {?class c:totalPontos ?total}.
        OPTIONAL {?class c:televoto ?televoto}.
        OPTIONAL {?class c:juri ?juri}.
    }
    
group by ?ano ?pais ?lugar ?televoto ?total ?juri ?artista
` 
    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    } 
}


Edicao.getMusicas_L_C = async function(){
    
    var query = `select distinct ?musica (group_concat(distinct ?liricista; separator = ' ; ') as ?liricistas) (group_concat(distinct ?compositor; separator = ' ; ') as ?compositores)  where { 
        ?m rdf:type c:Música .
        ?m c:título ?musica.
        ?m c:escritaPor ?lir.
        ?lir c:nome ?liricista.
        ?m c:compostaPor ?com.
        ?com c:nome ?compositor.
    }
    
    group by ?musica ` 
    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    } 
}


