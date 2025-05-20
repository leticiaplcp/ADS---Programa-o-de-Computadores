def somaDoisValores(a,b):
    a = a + b
    return a

#Utilizando o input
print(somaDoisValores(10,5))

#Armazenar o resultado em uma variavel
resultado = somaDoisValores(10,7)
print(resultado)

#concatenar o resultado diretamente em texto
print("soma dos dois valores é:"+str(somaDoisValores(10,8)))

#usar format com resultado em variavel
resultado = somaDoisValores(10,6)
print(f"Soma de dois valores: {resultado}")
