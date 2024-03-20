import random

nomesPet = ["Bolinha", "Rex", "Mel", "Thor", "Luna", "Bob", "Lola", "Billy", "Cleitin",
            "Marley", "Cleberson", "Spike", "Chiquinha", "Espuleta", "Snoopy", "Renato", "Max", "Coco", "Bela", "Chalize"]
adjetivosPet = ["Fofinho", "Bagunceiro", "Peludo", "Ronronante", "Lambão", "Saltitante", "Preguiçoso", "Sapeca", "Felpudo",
                "Pirata", "Guloso", "Esperto", "Pipoca", "Esparramado", "Fujão", "Rabugento", "Pirado", "Pintado", "Peludão", "Dengoso"]

especiesPet = ["Canino", "Felino", "Bovino", "Suíno"]

racasPet = ["Vira-lata Caramelo", "Labrador", "Salsicha", "Golden Retriever",
            "Beagle", "Poodle", "Chihuahua", "Yorkshire", "Bulldog"]

sexosPet = ["Masculino", "Feminino"]

portesPet = ["Minúsculo", "Pequeno", "Médio", "Grande", "Gigantesco"]

alergiasPet = ["Capim", "Pelos", "Dipirona",
               "Sair pra passear", "Grama", "Brincar"]


def gerarNomePet():
    nomePet = random.choice(nomesPet) + ' ' + random.choice(adjetivosPet)
    return nomePet


def gerarDadosPet():
    dadosPet = {
        'nomePet': gerarNomePet(),
        'especiePet': random.choice(especiesPet),
        'racaPet': random.choice(racasPet),
        'idadePet': str(random.randint(1, 100)),
        'sexoPet': random.choice(sexosPet),
        'portePet': random.choice(portesPet),
        'alergiasPet': random.choice(alergiasPet),
    }
    return dadosPet
