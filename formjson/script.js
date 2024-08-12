function EnviarFormulario() {
    var contaCliente = new Object()

    contaCliente.nome = document.getElementById("Nome").value
    contaCliente.agencia = document.getElementById("Agencia").value
    contaCliente.conta = document.getElementById("Conta").value

    var json = JSON.stringify(contaCliente)

    console.log(json)
}

document.getElementById("form").addEventListener('submit', (e) => {
    e.preventDefault()
})