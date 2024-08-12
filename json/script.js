var json = '{"nome" : "Tavin", "profissao" : "Chaveado de quebra", "curso" : "Desenvolvimento"}'

var dados = JSON.parse(json)

console.log(dados)

document.getElementById("content").innerHTML = dados.profissao
