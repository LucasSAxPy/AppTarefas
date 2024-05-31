from os import system, name

def limpa_tela():
	if name == "nt":
		_=system("cls")
	else:
		_=system("clear")

def adiciona_tarefa(tarefas):
	nome = input("Nome da tarefa: ")
	descricao = input("Descrição da tarefa: ")
	tarefa = {"Nome": nome, "Descrição": descricao, "Concluido": False}
	tarefas.append(tarefa)
	print("Tarefa adicionada com sucesso!")

def mostrar_tarefas(tarefas):
	print("Tarefas: ")
	for index, tarefa in enumerate(tarefas, start=1):
		concluido = "✓" if tarefa["Concluido"]  else " "
		nome = tarefa["Nome"]
		descricao = tarefa["Descrição"]
		print(f"{index}- [{concluido}] Nome: {nome} Descrição: {descricao}")

def mostrar_tarefas_concluidas(tarefas):
	print("Tarefas concluidas: ")
	for index, tarefa in enumerate(tarefas, start=1):
		concluido = "✓" if tarefa["Concluido"]  else " "
		nome = tarefa["Nome"]
		descricao = tarefa["Descrição"]
		index_verdadeiro = index - 1
		if tarefas[index_verdadeiro]["Concluido"]:
			print(f"{index}- [{concluido}] Nome: {nome} Descrição: {descricao}")

def mostrar_tarefas_nao_concluidas(tarefas):
	print("Tarefas não concluidas: ")
	for index, tarefa in enumerate(tarefas, start=1):
		concluido = "✓" if tarefa["Concluido"]  else " "
		nome = tarefa["Nome"]
		descricao = tarefa["Descrição"]
		index_verdadeiro = index - 1
		if tarefas[index_verdadeiro]["Concluido"] == False:
			print(f"{index}- [{concluido}] Nome: {nome} Descrição: {descricao}")

def altera_tarefa(tarefas):
	mostrar_tarefas(tarefas)
	try:
		index = int(input("Digite o numero da tarefa para alterar: "))
		index -= 1
		tarefas[index]["Nome"] = input("Nome da tarefa: ")
		tarefas[index]["Descrição"] = input("Descrição da tarefa: ")
		print("Tarefa atualizada!")
	except ValueError and IndexError:
		print("Opção inválida!")

def deleta_tarefa(tarefas):
	mostrar_tarefas(tarefas)
	try:
		index = int(input("Digite a tarefa a ser deletada: "))
		index -= 1
		del(tarefas[index])
		print("Tarefa removida!")
	except ValueError and IndexError:
		print("Opção inválida!")

def marca_concluido(tarefas):
	mostrar_tarefas(tarefas)
	try:
		index = int(input("Qual o número da tarefa a concluir: "))
		index -= 1
		tarefas[index]["Concluido"] = True
		print("Tarefa concluida")
	except ValueError and IndexError:
		print("Opção inválida!")

def desmarca_concluido(tarefas):
	mostrar_tarefas(tarefas)
	try:
		index = int(input("Qual o número da tarefa a desmarcar conclusão: "))
		index -= 1
		tarefas[index]["Concluido"] = False
		print("Desmarcou a conclusão")
	except ValueError and IndexError:
		print("Opção inválida!")