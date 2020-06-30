from datetime import datetime, date

#-------------------------------------------------------------------------------------------------
#Metodos de verificação

#Calcula idade das pessoas
def idade(nascimento):
    hoje = date.today()
    dataNascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
    idade = hoje.year - dataNascimento.year - ((hoje.month, hoje.day) < (dataNascimento.month, dataNascimento.day))
    return idade

#Soma a renda da familia
def verificaRenda(renda):
    rendaFamilia = 0

    for r in renda:
        rendaFamilia += r['valor']

    return rendaFamilia

#Recebe a lista das pessoas da familia, verifica quais são os dependentes e a idade dos mesmo
#e retorna os pontos de acordo com os crirterios atendidos.
def verificaDependentes(pessoas):
    dependentesElegivel = 0
    for dependente in pessoas:
        tipo = dependente['tipo'].lower()
        if((tipo == 'dependente') and (idade(dependente['dataDeNascimento']) < 18)):
            dependentesElegivel += 1

    return dependentesElegivel

def verificaDataNascimentoPretendente(pessoas):
    dataNascimentoPretendente = ''

    for pretendente in pessoas:
        tipo = pretendente['tipo'].lower()
        if (tipo == 'pretendente'):
            dataNascimentoPretendente = pretendente['dataDeNascimento']

    return dataNascimentoPretendente

#-----------------------------------------------------------------------------------------------------

#Metodos que calculam os pontos das familias

#Calcula os pontos de acordo com a idade do pretendente
def pontosIdadePredentente(pessoas):
    pontos = 0
    idadePretendente = idade(verificaDataNascimentoPretendente(pessoas))
    if(idadePretendente>44): pontos = 3
    elif(idadePretendente<30): pontos = 1
    else: pontos = 2

    return pontos

#Calcula os pontos de acordo com a quantidade de dependentes
def pontosDependentes(pessoas):
    pontos = 0
    dependentes = verificaDependentes(pessoas)

    if(dependentes > 0 and dependentes < 3):
        pontos = 2
    else:
        pontos = 3

    return pontos

#Calcula os pontos de acordo com a renda da familia
def pontosRendaFamilia(renda):
    rendaFamilia = verificaRenda(renda)
    pontos = 0

    if (0 <= rendaFamilia <= 900): pontos = 5
    elif (901 <= rendaFamilia <= 1500): pontos = 3
    elif (1501 <= rendaFamilia <= 2000): pontos = 1
    else: pontos = 0

    return pontos

#--------------------------------------------------------------------------------------------------

#Recebe um dicionario com dados da familia e retorna outro com o id, pontos e criterios atendidos da familia para devolutiva
def verificaFamilia(familia):
    quantCriterios = 0
    pontosFamilia = 0
    data = date.today().strftime('%Y-%m-%d')

    idFamilia = familia['id']
    pessoas = familia['pessoas']
    rendas = familia['rendas']

    criterios = [pontosDependentes(pessoas), pontosIdadePredentente(pessoas), pontosRendaFamilia(rendas)]

    for cri in criterios:
        if (cri != 0):
            quantCriterios += 1
        pontosFamilia += cri

    familia = {'id': idFamilia, 'quantCriterios': quantCriterios, 'pontuacao': pontosFamilia, 'dataSelecao': data}

    return familia

