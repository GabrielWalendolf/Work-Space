import numpy as np
import random

# Definição das vagas para cada setor
setores = ['A', 'B', 'C']
vagas_por_setor = 5

# Inicialização dos arrays para armazenar as vagas
vagas = {}
for setor in setores:
    vagas[setor] = np.array([True] * vagas_por_setor)

# Função para ocupar vaga no estacionamento
def ocupar_vaga(placa):
    for setor in setores:
        vagas_livres = np.where(vagas[setor])[0]
        if len(vagas_livres) > 0:
            vaga_escolhida = random.choice(vagas_livres)
            vagas[setor][vaga_escolhida] = False
            print(f"Veículo {placa} estacionado na vaga {vaga_escolhida+1} do setor {setor}")
            return
    print("Não há vagas disponíveis")

# Função para liberar vaga
def liberar_vaga(placa):
    for setor in setores:
        for i, vaga in enumerate(vagas[setor]):
            if not vaga:
                vagas[setor][i] = True
                print(f"Veículo {placa} liberou a vaga {i+1} do setor {setor}")
                return
    print("Veículo não encontrado")

# Função para exibir as vagas disponíveis no estacionamento
def exibir_vagas():
    for setor in setores:
        vagas_livres = np.where(vagas[setor])[0]
        print(f"Setor {setor}: {len(vagas_livres)} vagas disponíveis")

# Função para consultar veículo estacionado
def consultar_veiculo(placa):
    for setor in setores:
        for i, vaga in enumerate(vagas[setor]):
            if not vaga:
                print(f"Veículo {placa} estacionado na vaga {i+1} do setor {setor}")
                return
    print("Veículo não encontrado")

# Fnção para teste do sistema
def teste_sistema():
    placas = []
    while True:
        print("\n1 - Ocupar vaga")
        print("2 - Liberar vaga")
        print("3 - Exibir vagas")
        print("4 - Consultar veículo")
        print("5 - Adicionar veículo")
        print("6 - Sair do sistema")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            placa = input("Digite a placa do veículo: ")
            if placa in placas:
                print("Placa já existe! Por favor, informe uma placa diferente.")
            else:
                placas.append(placa)
                ocupar_vaga(placa)
        elif opcao == 2:
            placa = input("Digite a placa do veículo: ")
            if placa not in placas:
                print("Veículo não encontrado!")
            else:
                liberar_vaga(placa)
        elif opcao == 3:
            exibir_vagas()
        elif opcao == 4:
            placa = input("Digite a placa do veículo: ")
            if placa not in placas:
                print("Veículo não encontrado!")
            else:
                consultar_veiculo(placa)
        elif opcao == 5:
            break
        else:
            print("Opção inválida!")

# Execução do programa
teste_sistema()