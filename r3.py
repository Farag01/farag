peso = input("Digite o seu peso: ")
peso = float(peso)

altura = input("Digite a sua altura: ")
altura = float(altura)
IMC=peso/altura**2

if IMC<20: 
    print(" abaixo do peso")
elif IMC <25: 
    print("peso normal")
elif IMC <30: 
    print("sobrepeso")    
elif IMC <40: 
    print("obeso")   
elif IMC >=40: 
    print("obeso morbito")   
