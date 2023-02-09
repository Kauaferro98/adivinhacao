import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = round (random.randrange(1,11))
#print(numero_secreto)
total_de_tentativas = 0
rodada = 1
print ("Qual o nível de dificuldade?")
print ("(1) Fácil (2) Médio (3)Dificil")

nivel = int (input("defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2 ):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5        

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    if (chute <1 or chute>10):
        print ("Você deve digitar um número entre 1 e 10!!")
        continue
    

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    rodada = rodada + 1

print("Fim do jogo")
