menu= """ 
______________________________
                              |
        1-  Depositar         |
        2-  Sacar             |
        3-  Extrato           |
        0-  Sair              | 
______________________________|
"""
deposito=qnt_deposito=saque=0
extrato=""
limite_de_saque=3

while True:
    pergunta=int(input(f"{menu}"))
    if pergunta==1:
        qnt_deposito=int(input("quanto deseja depositar? "))
        if qnt_deposito<=0:
            print("nao é possivel fazer um deposito de R$0 ou menos")
        else:
            deposito+=qnt_deposito
            extrato+=f"quantidade depositada de R${qnt_deposito}  \n"
            print(f"quantidade depositada de R${qnt_deposito} \n")

    elif pergunta==2 and deposito>0 and limite_de_saque>0:
        saque=int(input("Quanto deseja sacar? "))
        if saque<500 and saque>=0 and saque<=deposito:
            deposito-=saque
            extrato+=f"quantidade sacada foi de R${qnt_deposito} \n"
            print(f"quantidade sacada foi de R${saque} \n")
            limite_de_saque-=1
        elif saque>deposito:
            print("saldo insuficiente")
        elif limite_de_saque==0:
            print("Você excedeu seus limites de saques diarios")
        else:
            print("Não são permitidos saques maiores que 500 reais e menores que 0")
    elif pergunta==2 and limite_de_saque==0:
        print("Você excedeu o limite de saques diarios. (O limite é 3 saques diarios)")

    elif pergunta==2 and deposito<0:
        print("Você nao tem nada para sacar")

    elif pergunta==3:
        extrato_menu=f"""
_________________________________

saldo total:{deposito}                   
{extrato}  
                                                                
_________________________________
    """
        if extrato>"":
            print(extrato_menu)
        else:
            print("nenhuma movimentação bancaria foi feita")
    elif pergunta==0:
        break