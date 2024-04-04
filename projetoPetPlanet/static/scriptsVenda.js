function addProdutoALista(produto_id){
    var tabela = document.getElementById('tabelaPDV');
    var novaLinha = tabela.insertRow(-1);

    var celulaID = novaLinha.insertCell(0);
    var celulaNome = novaLinha.insertCell(1);
    var celulaPreco = novaLinha.insertCell(2);
    var celulaQuantidade = novaLinha.insertCell(3);
    var celulaPrecoTotal = novaLinha.insertCell(4);
    var celulaExcluir = novaLinha.insertCell(5);

    fetch(`getDadosProduto/${produto_id}`)
    .then(response => response.json())
    .then(dadosProduto => {

        produto_preco = parseInt(dadosProduto.preco);
        produto_quantidade = parseInt(document.querySelector('input[name=quantidade]').value);

        celulaID.innerHTML = produto_id;
        celulaNome.innerHTML = dadosProduto.nome;
        celulaPreco.innerHTML = produto_preco;
        celulaQuantidade.innerHTML = produto_quantidade;
        celulaPrecoTotal.innerHTML = produto_preco*produto_quantidade;
        celulaExcluir.innerHTML = `<a id="linha${tabela.getElementsByTagName('tr').length}" onclick="excluirProduto(${tabela.getElementsByTagName('tr').length})">Excluir</a>`; //Cadastrar função
    });
}

function excluirProduto(idLinha){
    var linha = document.getElementById(`linha${idLinha}`).parentElement.parentElement;
    linha.remove();
}

function attPrecos(produto_id){    
    var aExibeValor = document.getElementById("precoProduto");
    var aExibeValorTotal = document.getElementById("precoProdutoTotal");
    var inputQuantidade = document.getElementById("inputQuantidade");
    var quantidadeSelecionada = inputQuantidade.value;

    fetch(`getDadosProduto/${produto_id}`)
    .then(response => response.json())
    .then(dadosProduto => {
        aExibeValor.innerText = dadosProduto.preco;
        aExibeValorTotal.innerText = dadosProduto.preco * quantidadeSelecionada;
    });
}