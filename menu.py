import this #Ele demonstra que é a msm variavel
import divisao
import soma #chamando a soma.py
import subtracao
import multiplicacao
import tabuada
import vetores

this.opcao = 0#Crio a variável global
num1 = 0
num2 = 0
def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input())
    #fim do def coletarNum1
def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())
    #fim do coletarNum2
def mostrarMenu():
    print('Escolha uma das opções abaixo\n' +
          '\n1. Soma' +
          '\n2. Subtração' +
          '\n3. Multiplicação' +
          '\n4. Divisão' +
          '\n5. Tabuada '+
          '\n6. Vetor ' +
          '\n0. Sair')

    this.opcao = int(input()) #Coletar a digitaçaõ do usuário
def operacao():

    #Mostrar o menu em tela
    while this.opcao != 5 :
        mostrarMenu()
        #Realizar as operações
        if this.opcao == 1:
            coletarNum1()
            coletarNum2()
            print(soma.somar(this.num1, this.num2))
            #fim do operacao para Soma
        elif this.opcao == 2:
            #Operação para a subtração
            coletarNum1()
            coletarNum2()
            print(subtracao.subtrair(this.num1, this.num2))
            #fim do subtrair
        elif this.opcao == 3:
            #Operaçaõ para a multiplicação
            coletarNum1()
            coletarNum2()
            print(multiplicacao.multiplicar(this.num1, this.num2))
        elif this.opcao == 4:
            #Operaçaõ para a dividir
            coletarNum1()
            coletarNum2()
            print(divisao.dividir(this.num1, this.num2))
        elif this.opcao == 5:

            coletarNum1()
            coletarNum2()
            print(tabuada.calcularTabuada(int(this.num1), int(this.num2)))
        elif this.opcao == 6:
            vetores.mostrarVetor()

        elif this.opcao == 0:
            print('Obrigado!')

        else:
            print('Opção escolhida inválida! Tente novamente')