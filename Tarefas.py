from modulos import *

# Cria uma lista vazia
tarefas = []

#Bloco de repetição para continuar o programa
while True:

#Imprime as opção possiveis para o usúario
	print("-"*20 + "Bloco de Tarefas" + "-"*20)
	print("  1- Adicionar uma tarefa")
	print("  2- Mostrar tarefas")
	print("  3- Excluir/Alterar tarefa")
	print("  4- Marcar ou desmarcar concluido")
	print("  5- Sair")

#Usúario escolhe a opção
	try:
		resposta = int(input("Escolha a opção: "))
	except ValueError:
		print("Opção inválida!")
		continue
#Opção de adicionar tarefas
	if resposta == 1:
		limpa_tela()
		adiciona_tarefa(tarefas)
		print("Adicionado com sucesso!")

#Opção de mostrar tarefas
	elif resposta == 2:
		limpa_tela()
		print("  1- Mostrar todas tarefas")
		print("  2- Mostrar tarefas concluidas")
		print("  3- Mostrar tarefas não concluidas")
		try:
			resposta = int(input("Escolha a opção: "))

#Mostra todas tarefas
			if resposta == 1:
				mostrar_tarefas(tarefas)

#Mostra apenas tarefas concluidas
			elif resposta == 2:
				mostrar_tarefas_concluidas(tarefas)

#Mostra apenas tarefas não concluidas
			elif resposta == 3:
				mostrar_tarefas_nao_concluidas(tarefas)

			else:
				print("Opção inválida!")
		except ValueError:
			print("Opção inválida!")
#Opção de excluir ou alterar tarefas
	elif resposta == 3:
		limpa_tela()
		print("  1- Excluir tarefa")
		print("  2- Alterar tarefa")
		try:	
			resposta = int(input("Escolha a opção: "))

#Exclui
			if resposta == 1:
				deleta_tarefa(tarefas)

#Altera
			elif resposta == 2:
				altera_tarefa(tarefas)

			else:
				print("Opção inválida!")
		except ValueError:
			print("Opção inválida!")

#Opção de marcar ou desmarcar conclusão da tarefa
	elif resposta == 4:
		limpa_tela()
		print("  1- Marcar concluido")
		print("  2- Desmarcar concluido")
		try:
			resposta = int(input("Escolha a opção: "))

	#Marca conclusão
			if resposta == 1:
				marca_concluido(tarefas)

	#Desmarca conclusão
			elif resposta == 2:
				desmarca_concluido(tarefas)

			else:
				print("Opção inválida!")
		except ValueError:
			print("Opção inválida!")
#Para o programa
	elif resposta == 5:
		break