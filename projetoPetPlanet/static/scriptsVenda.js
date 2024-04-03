function addProdutoALista(produto_id){
    var tabela = document.getElementById('tabelaPDV');
    var novaLinha = tabela.insertRow(-1);
    var celulaID = novaLinha.insertCell(0);
    var celulaNome = novaLinha.insertCell(1);
    var celulaPreco = novaLinha.insertCell(2);
    var celulaQuantidade = novaLinha.insertCell(3);
    var celulaPrecoTotal = novaLinha.insertCell(4);
    var celulaExcluir = novaLinha.insertCell(5);

    var produto_nome = document.querySelector('select[name=produtos]').options[document.querySelector('select[name=produtos]').selectedIndex].text;
    var produto_preco = 2; // puxar do DB
    var produto_quantidade = document.querySelector('input[name=quantidade]').value;

    celulaID.innerHTML = produto_id;
    celulaNome.innerHTML = produto_nome;
    celulaPreco.innerHTML = produto_preco;
    celulaQuantidade.innerHTML = produto_quantidade;
    celulaPrecoTotal.innerHTML = produto_preco*produto_quantidade;
    celulaExcluir.innerHTML = 'Excluir' //Cadastrar função
    


    console.log('addProdutoALista() executado por completo');
}