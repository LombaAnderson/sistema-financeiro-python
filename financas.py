from datetime import datetime
import json

try:
    with open('carteira.json', 'r') as c:
        carteira = json.loads(c.read())
    id_transacao = carteira["idtransacao"]
    carteira.pop("idtransacao")
    
except:
    carteira = {}
    id_transacao = 1

def listaTransacoes():
    if len(carteira) == 0:
        print('\nSem transações!')
        return
    print('\nSuas transações: ')

    for transacao in sorted(
        carteira.values(), 
        key=lambda transacao: str(transacao["identificador"]),
        reverse=True):
            print(f'{transacao["identificador"]} - {transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]:.2f}')


def adicionaTransacao():
    global id_transacao, saldo

    descricao = input('\nDigite a descrição da transação: ')
    valor = float(input('Digite o valor da transação (com sinal de - se for despesa): '))
    data = str(datetime.now())

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": str(id_transacao),
    }

    carteira["id_" + str(id_transacao)] = transacao
    id_transacao += 1
    print('Transação adicionada com sucesso!')


def deletaTransacao():
    identificador = "id_" + input('\nDigite o id da transação que quer deletar: ')
    transacao = carteira.pop(identificador)
    print(f'Transação {transacao["identificador"]} - "{transacao["descricao"]}", no valor de R${transacao["valor"]:.2f} foi excluída!')


def editaTransacao():
    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    identificador = "id_" + str(id_transacao)

    descricao = input('Digite a nova descrição da transação: ')
    valor = float(input('Digite o novo valor da transação: '))
    mudar_data = input('Digite S para mudar a data da transação para a data atual ou N para manter a data antiga: ').upper()
    if mudar_data == 'S':
        data = str(datetime.now())
    else:
        data = carteira[identificador]["data"]

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": id_transacao,
    }

    carteira["id_" + str(id_transacao)] = transacao

    print(f'Transação {id_transacao} editada com sucesso!')


def consultaSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    
    print(f'Seu saldo atual é R${saldo:.2f}')


def salvaCarteira():
    c = carteira.copy()
    
    c["idtransacao"] = id_transacao
    with open('carteira.json', 'w') as file:
        file.write(json.dumps(c))


while True:
    op = input("""\nDigite:
        \rL - Liste suas transações
        \rA - Adicione transação
        \rD - Delete suas transação
        \rE - Edite suas transação
        \rS - Consulte seu saldo atual
        \rQ - Sair do programa
        \rSua entrada: """).upper()

    if op == 'A':
        adicionaTransacao()
        salvaCarteira()
    elif op == 'D':
        deletaTransacao()
        salvaCarteira()
    elif op == 'E':
        editaTransacao()
        salvaCarteira()
    elif op == 'L':
        listaTransacoes()
    elif op == 'S':
        consultaSaldo()
    elif op == 'Q':
        exit()
    else:
        print('Operação incorreta!\n')

