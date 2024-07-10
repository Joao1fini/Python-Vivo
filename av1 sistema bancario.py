def saque(*,saldo,valor,extrato,limite_saque):
    while True:
        print(f"saldo atual: {saldo}")
        valor=int(input("Quanto deseja sacar? "))
        if valor<saldo:
            break
    if limite_saque>0 and saldo>0 and valor<500:
        saldo-=valor
        extrato+=f"quantidade sacada foi de R${valor} \n"
        print(f"quantidade sacada foi de R${valor} \n")
        limite_saque-=1
    elif valor>saldo:
            print("saldo insuficiente")
    elif valor>500 or valor <=0:
        print("saques apenas acima de R$0 e menores que R$500.00")
    else:
        print("limite de saques atingido")
    return saldo,extrato,limite_saque

def deposito(saldo,valor,extrato):
    valor=int(input("Quanto deseja depositar? "))
    if valor<=0:
        print("apenas valores acima de 0 são permitidos ")
    else:
        saldo+=valor
        extrato+=f"valor depositado foi de: R${valor} \n"
        print(f"valor depositado foi de: R${valor}")

    return saldo,extrato
    
def extrato_atualizado(saldo,/,*,extrato):
    extrato_menu=f"""
_________________________________

saldo total:{saldo}                   
{extrato}                                                         
_________________________________
    """
    if extrato>"":
        print(extrato_menu)
    else:
        print("nenhuma movimentação bancaria foi feita")
    return extrato

def usuario(nome,nascimento,cpf,endereço):
    print(f"nome: {nome}")
    print(f"idade: {nascimento}")
    print(f"cpf: {cpf}")
    print(endereço)

def conta_corrente(agencia, nrm, usuario):
    menu3 = f"""
==============================
Nome: {usuario}
Agência: {agencia}
Conta N°: {nrm}
==============================
"""
    print(menu3)
def criar_conta_corrente(agencia,usuario):
    global nrm
    nrm+=1
    usuario=input("Digite seu nome completo: ")
    return usuario,nrm

def banco(cpf):
    menu= """ 
________________________________
                                |
        1-  Depositar           |
        2-  Sacar               |
        3-  Extrato             |
        4-  dados usuario       |
        5-  conta corrente      |
        6-  criar conta corrente|
        0-  Sair                | 
________________________________|
"""
    saldo=0
    valor=0
    extrato=""
    limite_saque=3
    while True:
        pergunta=int(input(f"{menu}"))
        if pergunta==1:
            saldo,extrato = deposito(saldo,valor,extrato)
        elif pergunta==2:
            saldo,extrato,limite_saque=saque(saldo=saldo,valor=valor,extrato=extrato,limite_saque=limite_saque)
        elif pergunta==3:
            extrato_atualizado(saldo,extrato=extrato)   
        elif pergunta==4:
            usuario(dic[cpf]["nome"],dic[cpf]["idade"],cpf,dic[cpf]["endereço"])
        elif pergunta==5:
            conta_corrente(agencia,nrm,cpf)
        elif pergunta==6:
            criar_conta_corrente(agencia,cpf)
        elif pergunta==0:
            break
menu_principal= """ 
____________________________________
                                    |
        1-  fazer login             |
        2-  registrar novo usuario  |
        3-  sair                    |           
____________________________________|
"""

usuarios=[]
dic={}
limite_saque=3
nrm=1
agencia="0001"
while True:
    pergunta1=int(input(menu_principal))
    if pergunta1==1:
        cpf=input("digite seu cpf: ")
        if cpf in dic:
            senha=input("qual a senha: ")
            if senha == dic[cpf]["senha"]:
                banco(cpf)
            else:
                print("senha incorreta")
        else:
            print("usuario nao encontrado")
    elif pergunta1==2:
        cpf=input("digite seu cpf: ")
        if len(cpf)>11:
            continue
        if cpf in dic:
            print("usuario ja existe")
            continue
        dic[cpf]={}
        nome=input("digite seu nome: ")
        dic[cpf]["nome"]=nome
        usuarios+=nome
        senha=input("Digite sua senha: ")
        dic[cpf]["senha"]=senha
        nascimento=int(input("Digite sua idade: "))
        dic[cpf]["idade"]=nascimento
        endereço=input("qual sua cidade? ")
        dic[cpf]["endereço"]={}
        dic[cpf]["endereço"]["cidade"]=endereço
        endereço=input("qual seu UF? ")
        dic[cpf]["endereço"]["UF"]=endereço
        dic[cpf]["tranferencia"]={0}

    elif pergunta1==3:
        break