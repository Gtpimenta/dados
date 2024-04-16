#PARTE 1: Importação de bibliotecas
# Para mudar uma collection de uma DB para outra dentro do MongoDB, utilizamos a biblioteca Pymongo. Para ter um controle do código usei a biblioteca datetime, mas não é crucial para o processo.

from pymongo import MongoClient
from datetime import datetime

#PARTE 2: Conexão com o Banco de dados
# Nesse caso, a transferência foi de uma collection para outra, dentro de um mesmo banco. Se for passar para outro client, basta repetir a linha com o endereço do segundo client.
client = MongoClient("servidor_mongodb")

#PARTE 3: Definições
# Neste ponto definimos qual será a collection de origem e qual será o destino. No meu caso, trabalhei com as duas no mesmo client, porém com diferentes DB's (os nomes foram alterados por fins de confidencialidade).

#origem:
collection_origem = client["db_origem"]["collection_origem"]

#destino:
collection_to_insert = client["db_destino"]["collection_destino"]

#PARTE 4: Transferir os registros
# Da mesma maneira que faríamos com listas com poucos elementos, essa operação vai correr todos os registros e vai enviar para a nova DB.
#EXTRA: Adicionei um print com auxílio da biblioteca datetime para termos controle dos dados.
print(f'[{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}] - Operação iniciada')

for record in collection_origem.find():
    collection_to_insert.insert_one(record)

#PARTE 5: Finalização
# Apenas deixei um print para marcar a hora em que foi encerrada a operação. Dessa forma temos a informação de quanto tempo levou para concluir a atividade.
print(f'[{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}] - Operação concluída')
client.close()