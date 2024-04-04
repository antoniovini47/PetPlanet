function addProdutoALista(produto_id){
    var tabela = document.getElementById('tabelaPDV');
    var novaLinha = tabela.insertRow(-1);

    var celulaID = novaLinha.insertCell(0);
    var celulaNome = novaLinha.insertCell(1);
    var celulaPreco = novaLinha.insertCell(2);
    var celulaQuantidade = novaLinha.insertCell(3);
    var celulaPrecoTotal = novaLinha.insertCell(4);
    var celulaExcluir = novaLinha.insertCell(5);

    dados = {
        'id_produto': produto.id_produto,
        'nome': produto.nome,
        'preco': produto.preco,
        'estoque': produto.estoque,
        'validade': produto.validade,
        'categoria': produto.categoria,
    }

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
        console.log(tabela.getElementsByTagName('tr').length);
        celulaExcluir.innerHTML = `<a onclick="excluirProduto(${tabela.getElementsByTagName('tr').length})">Excluir</a>`; //Cadastrar função
    });

    console.log('addProdutoALista() executado por completo');
}

function excluirProduto(idLinha){
    console.log(`Função excluirProduto iniciada, idLinha: ${idLinha}`);
    var tabela = document.getElementById('tabelaPDV');
    tabela.deleteRow(idLinha-1);
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

    console.log('attPrecos() executado por completo');
}