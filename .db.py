#!/usr/bin/python3
# coding: utf-8
from time import sleep # para simular delays
funcao = (lambda x: '-=-' * x) # armazena uma função dentro de uma variavel
DadosArray = [] # inicializa um array

class Banco_de_dados(object): # cria uma classe pai (superclasse)
	def __init__(self, base): # metodo construtor que necessita de um parametro como a "base"
		self.base = str(base)
	def Criar_base(self): # metodo
		sleep(1)
		db_variavel = '\n#Criar banco de dados\nCREATE DATABASE IF NOT EXISTS {0};\nUSE {0};\n'.format(base_input)
		try: # tenta o bloco de comandos abaixo
			with open(file_input, 'w') as f: # cria uma variavel temporaria
				f.write(db_variavel) # escreve dentro do arquivo especificado
				f.close() # fecha o arquivo
		except: # caso dê errado executa os comandos abaixo
			print('\033[1;41mVocê digitou um formato de arquivo errado!!\033[0;0m')
			exit() # termina o programa
		print(db_variavel)
		sleep(1)
		
class Tabela(Banco_de_dados): # cria a classe Tabela que herda caracteristicas da classe Banco_de_dados
	def __init__(self, base, tabela):
		super(Tabela, self).__init__(base) # puxa os metodos construtores de sua superclasse
		self.tabela = tabela
	def Criar_tabela(self): # cria um metodo
		sleep(1)
		table_variavel = '\n#Criar tabela\nCREATE TABLE IF NOT EXISTS {0} (\n{1} varchar(2000)\n);\n'.format(table_input, column_input)
		print(table_variavel)
		sleep(1)
		with open(file_input, 'a') as f: # variavel temporaria
			f.write(table_variavel) # escreve no arquivo
			f.close() # fecha-o
		
class Coluna(Tabela): # Coluna herda de Tabela
	def __init__(self, base, tabela, coluna): # metodo construtor
		super(Coluna, self).__init__(base, tabela) # herda metodos construtores
		self.coluna = coluna
	def __str__(self): # converte a classe em string
		sleep(1)
		return '\033[1;32m\n{}\nNome da base: {}\nNome da tabela: {}\nNome da coluna: {}\nNome do arquivo: {}\nQuantidade de itens na tabela: {}\n{}\n\033[0;0m'.format(funcao(10), self.base, self.tabela, self.coluna, file_input, len(DadosArray), funcao(10))
		sleep(1)
	def Manipular_dados(self, condicao): # metodo que precisa de um parametro "condicao"
		condicao = condicao # condicao é igual ao dado passado como parametro
		if (condicao == 0): #printar array
			convertido = str(DadosArray).strip('[]')
			print(convertido)
			sleep(1)
			printar = '\n#Mostrar dados da tabela\nSELECT * FROM {};\n'.format(table_input)
			print(printar)
			with open(file_input, 'a') as f:
				f.write(printar)
				f.close()
		elif (condicao == 1): # remover um item
			print('Digite a linha na qual você deseja remover começando por 0 -> ')
			try:
				sleep(1)
				decisao_linha = int(input('Digite a linha na qual você deseja remover -> '))
				DadosArray.pop(decisao_linha)
				remover = '\n#Remover um item\nDELETE FROM {}\nWHERE id = {}\n'.format(table_input, decisao_linha)
				sleep(1)
				print(remover)
				with open(file_input, 'a') as f:
					f.write(remover)
					f.close()
			except IndexError:
				print('\033[1;41mEsta linha não existe!\033[0;0m')
				pass
			except ValueError:
				print('\033[1;41mDigite um número inteiro!\033[0;0m')
				pass
			sleep(1)
		elif (condicao == 2): # modificar valor
			print('Digite a linha na qual você deseja remover começando por 0 -> ')
			try:
				decisao_altera_linha = int(input('Qual linha você deseja modificar? -> '))
				decisao_altera = str(input('O que você deseja inserir? -> '))
				DadosArray[decisao_altera_linha] = decisao_altera
				modificar = '\n#Modificar uma linha\nUPDATE {}\nSET {} = "{}"\nWHERE id = {}\n'.format(table_input, column_input, decisao_altera, decisao_altera_linha)
				sleep(1)
				print(modificar)
				with open(file_input, 'a') as f:
					f.write(modificar)
					f.close()
			except IndexError:
				print('\033[1;41mEssa linha não existe!\033[0;0m')
				pass
			except ValueError:
				print('\033[1;41mDigite apenas numeros inteiros!\033[0;0m')
				pass
		elif (condicao == 3): # fim do script
			print('Saindo...')
			sleep(1)
			print('Bye bye :)')
			exit()
		elif (condicao == 4): # excluir tudo
			decisao_apagar = str(input('Você tem certeza que deseja apagar todos os seus dados? [Y/n] -> '.lower()))
			if (decisao_apagar == 'y'):
				DadosArray.clear()
				sleep(1)
				apagar = '\n#Apaga todos os dados da tabela\nTRUNCATE TABLE {};\n'.format(table_input)
				print(apagar)
				with open(file_input, 'a') as f:
					f.write(apagar)
					f.close()
				sleep(1)
			else:
				pass
		elif (condicao == 5): # insere dados
			decisao_inclui = str(input('O que você deseja inserir dentro da tabela? -> '))
			DadosArray.append(decisao_inclui)
			sleep(1)
			insert = '\n#Insere valores\nINSERT INTO {}\nVALUES\n("{}");\n'.format(table_input, decisao_inclui)
			print(insert)
			with open(file_input, 'a') as f:
				f.write(insert)
				f.close()
		else:
			pass
			
sleep(1)
print('''\033[1;33m                                            ,----..                  
    ,---,        ,---,.             ,---,.   /   /   \  ,--,     ,--,  
  .'  .' `\    ,'  .'  \          ,'  .' |  /   .     : |'. \   / .`|  
,---.'     \ ,---.' .' |        ,---.'   | .   /   ;.  \; \ `\ /' / ;  
|   |  .`\  ||   |  |: |        |   |   .'.   ;   /  ` ;`. \  /  / .'  
:   : |  '  |:   :  :  /        :   :  :  ;   |  ; \ ; | \  \/  / ./   
|   ' '  ;  ::   |    ;         :   |  |-,|   :  | ; | '  \  \.'  /    
'   | ;  .  ||   :     \        |   :  ;/|.   |  ' ' ' :   \  ;  ;     
|   | :  |  '|   |   . |        |   |   .''   ;  \; /  |  / \  \  \    
'   : | /  ; '   :  '; |        '   :  '   \   \  ',  /  ;  /\  \  \   
|   | '` ,/  |   |  | ;         |   |  |    ;   :    / ./__;  \  ;  \  
;   :  .'    |   :   /          |   :  \     \   \ .'  |   : / \  \  ; 
|   ,.'      |   | ,'           |   | ,'      `---`    ;   |/   \  ' | 
'---'        `----'             `----'                 `---'     `--`  
# Telegram: @Foxxer_SA
# Se inscreve lá @AcervoHackerBR!!!
# GitHub: foxx3r                                           
''' +'\033[0;0m')
print(funcao(10))
sleep(1)

file_input = str(input('Digite um nome de arquivo (pode ser com extensão) -> '))
base_input = str(input('Digite o nome do seu banco de dados -> '))
db = Banco_de_dados(base_input)
db.Criar_base()
print(funcao(10))
table_input = str(input('Digite o nome da sua tabela -> '))
tbl = Tabela(base_input, table_input)
column_input = str(input('Digite o nome da sua 1° e única coluna -> '))
tbl.Criar_tabela()
clm = Coluna(base_input, table_input, column_input)

var_de_saida = 5
while var_de_saida == 5:
	print(funcao(10))
	main = int(input('''Cadastro de Clientes
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta
5 - Excluir tudo
6 - Estatisticas
-> '''))
	
	print(funcao(10))
	if (main == 0):
		clm.Manipular_dados(3)
	elif (main == 1):
		clm.Manipular_dados(5)
	elif (main == 2):
		clm.Manipular_dados(2)
	elif (main == 3):
		clm.Manipular_dados(1)
	elif (main == 4):
		clm.Manipular_dados(0)
	elif (main == 5):
		clm.Manipular_dados(4)
	elif (main == 6):
		print(clm)
	else:
		print('\033[1;41mDigite um numero de 1 a 6!!!\033[0;0m')
		pass
