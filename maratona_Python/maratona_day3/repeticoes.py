# LAÇOS DE REPETIÇÃO

# FOR AND WHILE

# FOR = PARA
#  WHILE = ENQUANTO
# SINTAXE

# FOR {REFERENCIA} IN  { SEQUENCIA}:

#               {BLOCO A SER EXECUTADO}

# WHILE {CONDIÇÃO}
#    {EXECUTAR ALGUMA COISA}
#       break
#   ELSE: {BLOCO DE CODIGO }
'''
cont = 1
while cont <= 100:
  print(cont, end='')
cont += 1
if cont == 100:
     print()
break
print()
'''

'''
contador = 0
somador = 4 
while contador <5:
    contador = contador  +1
    valor = float(input('Digite o '+ str(contador)+ "º valor: "))
somador= somador+ valor
print('Soma é igual a: ', somador)

]
'''

soma = 0

for i in range(0,20):
 soma = soma +i
print(soma)

# exemplo de soma de 0 a 
 
listaNotas = []
media = 0

print ('Informe suas 4 notas')

for i in range(4):
      listaNotas.append(float(input('Nota'+ str(i+1)+ ':\n')))
      media += listaNotas[0]
      media= media/4
      print(listaNotas)
      print (media)
