import json
import funcoes
from timeit import default_timer as timer


start = timer()

with open('familias.json', 'r', encoding="utf-8") as f:
    familias = json.load(f)

familiasElegiveis = []


for index, familia in enumerate(familias):

    if(int(familia['status']) != 0):
        continue
    else:
        familiasElegiveis.append(funcoes.verificaFamilia(familia))


familiasElegiveis = sorted(familiasElegiveis, key=lambda k: k['pontuacao'], reverse = True)

with open('familias-elegiveis.json', 'w', encoding="utf-8") as f:
  json.dump(familiasElegiveis, f, ensure_ascii=False)


end = timer()
print(end - start)