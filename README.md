# desafio_tecnico

Para resolver o problema proposto eu utilizei a linguam Python, a aplicação basicamente pega um arquivo Json com os dados das familias e retorna um novo arquivo Json com o id, total de pontos e criterios atendidos para a seleção.

Na aplicação tem um arquivo funcoes onde se encontram os metodos que fazem as validações e contagem de pontos e um arquivo listaFamilias que ira abrir o arquivo Json, verificar as familias que se enquadram para a seleção, familias com status 0, chamar o metodo de validação verificaFamilias e então incluir em uma lista para que depois seja gerado o arquivo Json.

O arquivo gera_base serve apenas para gerar um pequena base de teste. Rodando a aplicação diretamente na maquina para uma base com 100 mil familias o arquivo de retorno saiu relativamente rapido.
