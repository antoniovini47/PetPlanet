import random

nomesPet = ["Bolinha", "Rex", "Mel", "Thor", "Luna", "Bob", "Lola", "Billy", "Sophie",
            "Marley", "Duke", "Spike", "Maggie", "Rocky", "Snoopy", "Daisy", "Max", "Coco", "Bella", "Charlie"]
adjetivosPet = ["Fofinho", "Bagunceiro", "Peludo", "Ronronante", "Lambão", "Saltitante", "Preguiçoso", "Sapeca", "Felpudo",
                "Pirata", "Guloso", "Esperto", "Pipoca", "Esparramado", "Fujão", "Rabugento", "Pirado", "Pintado", "Peludão", "Dengoso"]


def gerarNomePet():
    nomePet = random.choice(nomesPet) + ' ' + random.choice(adjetivosPet)
    return nomePet
