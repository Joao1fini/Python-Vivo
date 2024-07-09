import random 
from random import randint
# lista=[n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
# print(lista)
# numero = {1,2}
# numero2= {3,4}

# seila=numero.symmetric_difference(numero2)
# print(seila)
# for indice,numero in enumerate(numero):
#     print(f"{indice}:{numero}")

dicc= {"usuario1":{"nome":"joao","idade":"18"}}
# print(dicc)
id=randint(0,1000)
inscricao=input("escreva se nome ")
idade=int(input("escreva sua idade "))
dicc[str(id)] = {}
dicc[str(id)]["nome"]=inscricao
dicc[str(id)]["idade"]=idade
for k,v in dicc.items():
    print(v)