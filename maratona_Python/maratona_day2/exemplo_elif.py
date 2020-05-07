
# Programa que pede 'Digite um número de 1 até 10',
#  e de acordo com o número fornecido pelo usuário
# , indicar qual o time está naquela posição do ranking.

#Por exemplo, a pessoa digita 1. O resultado é 'Palmeiras'.
#Digitou 2, deve printar 'Cruzeiro' etc.

#1-PALMEIRAS
#2- CRUZEIRO
#3- GREMIO
#4- SANTOS 
#5- ATLETICO
#6- CORINTHIANS
#7- FLAMENGO
#8- BOTAFOGO 
#9- ATLETICO PA
#10- INTERNACIONAL

resposta=int(input('Que colocação no ranking deseja saber: '))

if resposta == 1:
    print('Palmeiras! Vai porco!')

elif resposta == 2:
    print('Cruzeiro')

elif resposta == 3:
    print('Grêmio')

elif resposta == 4:
    print('Santos')

elif resposta == 5:
    print('Atlético-MG! Vai galo!')

elif resposta == 6:
    print('Timão!')

elif resposta == 7:
    print('Mengo!')

elif resposta == 8:

    print('Botafogo')
elif resposta == 9:

    print('Atlétito-PR')
elif resposta == 10:

    print('Internacional')

elif resposta == 0:
        print('Opção não válida!')

    
else:
    print('Só temos até o décimo!')