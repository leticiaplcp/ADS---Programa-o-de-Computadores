print("Uma fonte inesgotável")
print("Uma fonte mágica precisa atingir 100 litros, usando baldes de 8 litros e colocando um balde por minuto. Calcule quanto tempo leva para encher.")
print("Use um loop while para simular o processo. Cada interação do loop é um minuto")

litros = 0; 
balde = 8;
tempo = 0; 

while litros < 100:
    litros += balde
    tempo += 1

print(f"Leva {tempo} minutos para encher a fonte até 100 litros.")
