peso = int(input("Me diga o seu peso: "))
altura = int(input("Me diga a sua altura: "))

imc = (peso / (altura*altura)) *10000

if (imc <= 18.5):
    print ("Seu IMC é: ", "%.1f" % imc,", Você esta abaixo do peso.")
elif ((imc >= 18.6) and (imc <= 24.9)):
    print ("Seu IMC é: ", "%.1f" % imc,", Você esta com o peso adequado.")
else:
    print("Seu IMC é: ", "%.1f" % imc,", Você esta acima do peso.")
