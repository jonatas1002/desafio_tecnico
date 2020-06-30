import json

familia = {
  "id": "3dac7da3-d742-4e51-95f9-bbb37f522413",
  "pessoas": [
    { "id": "5e65eea1-aa72-407e-9a67-88045c07b5de", "nome": "João", "tipo": "Pretendente", "dataDeNascimento": "1989-12-30" },
    { "id": "d467781a-8f06-45ba-be6f-879cf32a9f7e", "nome": "Maria", "tipo": "Cônjuge", "dataDeNascimento": "1989-12-30" },
    { "id": "79820382-a181-42d2-bfae-6c012489e65e", "nome": "José", "tipo": "Dependente", "dataDeNascimento": "2015-12-30" },
    { "id": "80fa071e-17fb-4b87-99db-a7db0bfc23c2", "nome": "Angela", "tipo": "Dependente", "dataDeNascimento": "2015-12-30" }
  ],
  "rendas": [
    { "pessoaId": "5e65eea1-aa72-407e-9a67-88045c07b5de", "valor": 1000 },
    { "pessoaId": "d467781a-8f06-45ba-be6f-879cf32a9f7e", "valor": 950 }
  ],
  "status": "1"
}
familia2 = {
  "id": "3dac7da3-d742-4e51-95f9-bbb37f522413",
  "pessoas": [
    { "id": "5e65eea1-aa72-407e-9a67-88045c07b5de", "nome": "João", "tipo": "Pretendente", "dataDeNascimento": "1970-12-30" },
    { "id": "d467781a-8f06-45ba-be6f-879cf32a9f7e", "nome": "Maria", "tipo": "Cônjuge", "dataDeNascimento": "1989-12-30" },
    { "id": "79820382-a181-42d2-bfae-6c012489e65e", "nome": "José", "tipo": "Dependente", "dataDeNascimento": "2015-12-30" },
    { "id": "80fa071e-17fb-4b87-99db-a7db0bfc23c2", "nome": "Angela", "tipo": "Dependente", "dataDeNascimento": "2015-12-30" }
  ],
  "rendas": [
    { "pessoaId": "5e65eea1-aa72-407e-9a67-88045c07b5de", "valor": 899},
    { "pessoaId": "d467781a-8f06-45ba-be6f-879cf32a9f7e", "valor": 0 }
  ],
  "status": "0"
}

familias = []
aux = 1

for i in range(100000):
  if(aux == 1):
    familias.append(familia)
    aux += 1
  elif(aux == 2):
    familias.append(familia2)
    aux -= 1



with open('familias.json', 'w', encoding="utf-8") as f:
  json.dump(familias, f, ensure_ascii=False)


