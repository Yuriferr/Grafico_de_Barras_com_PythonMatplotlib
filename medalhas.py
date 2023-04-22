import matplotlib.pyplot as plt

# lista de dicionários com informações dos países e suas medalhas
medalhas = [
    {"país": "Estados Unidos", "ouro": 39, "prata": 41, "bronze": 33},
    {"país": "China", "ouro": 38, "prata": 32, "bronze": 18},
    {"país": "Japão", "ouro": 27, "prata": 14, "bronze": 17},
    {"país": "Grã-Bretanha", "ouro": 22, "prata": 21, "bronze": 22},
    {"país": "ROC", "ouro": 20, "prata": 28, "bronze": 23},
    {"país": "Austrália", "ouro": 17, "prata": 7, "bronze": 22},
    {"país": "Holanda", "ouro": 10, "prata": 12, "bronze": 14},
    {"país": "França", "ouro": 10, "prata": 12, "bronze": 11},
    {"país": "Alemanha", "ouro": 10, "prata": 11, "bronze": 16},
    {"país": "Itália", "ouro": 10, "prata": 10, "bronze": 20},
]

# extrair as informações para criar o gráfico
paises = [d["país"] for d in medalhas]
ouro = [d["ouro"] for d in medalhas]
prata = [d["prata"] for d in medalhas]
bronze = [d["bronze"] for d in medalhas]

# criar o gráfico de barras
fig, ax = plt.subplots()
ax.bar(paises, ouro, label="Ouro", color="gold")
ax.bar(paises, prata, bottom=ouro, label="Prata", color="silver")
ax.bar(paises, bronze, bottom=[i+j for i,j in zip(ouro, prata)], label="Bronze", color="#CD7F32")
ax.set_ylabel("Número de medalhas")
ax.set_xlabel("Países")
ax.set_title("Medalhas nas Olimpíadas de 2020")
ax.legend()

plt.show()
