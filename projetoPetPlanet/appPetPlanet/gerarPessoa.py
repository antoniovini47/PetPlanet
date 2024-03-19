import requests
import json


def gerarDadosCliente():
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.4devs.com.br',
        'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
    }
    data = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='
    solicitacao = requests.post(url, headers=header, data=data).json()
    dadosBrutos = json.dumps(solicitacao)
    dadosBrutos = dadosBrutos.replace("[", "")
    dadosBrutos = dadosBrutos.replace("]", "")
    dadosPessoa = json.loads(dadosBrutos)
    args = {
        'nomeCliente': dadosPessoa['nome'],
        'cpfCliente': dadosPessoa['cpf'],
        'emailCliente': dadosPessoa['email'],
        'telefoneCliente': dadosPessoa['celular'],
        'enderecoCliente': dadosPessoa['endereco'],
        'numeroCliente': dadosPessoa['numero'],
        'bairroCliente': dadosPessoa['bairro'],
        'cidadeCliente': dadosPessoa['cidade'],
        'estadoCliente': dadosPessoa['estado'],
        'enderecoCompletoCliente': str(dadosPessoa['endereco']) + ", "
        + str(dadosPessoa['numero']) + ", "
        + str(dadosPessoa['bairro']) + ", "
        + str(dadosPessoa['cidade']) + " - "
        + str(dadosPessoa['estado']),
    }
    return args
