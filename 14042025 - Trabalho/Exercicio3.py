print("O mapa das estrelas")
print("Decifre um mapa estelar onde cada estrela é representada por um número. Exiba apenas as estrelas 'brilhantes' (números pares entre 1 a 20)")
print("Use um loop para listar as estrelas brilhantes")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Estrelas brilhantes:")
for estrela in lista:
    if estrela % 2 == 0:
        print(estrela)
