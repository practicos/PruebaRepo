# Programa para comparar una cadena para saber si es palindroma.
#1.Se captura la palabra a evaluar.
Captura=input("Ingrese palabra a evaluar:")
#2.Se Invierte la palabra 
Torcido= "".join(reversed(Captura))
#Se realiza la condicion se quitan espacios si existen para asegurar la palabra 
if Captura.replace(" ","")==Torcido.replace(" ",""):
    print("La palabra "+ Captura + " es palindroma")
else: 
    print("La palabra "+ Captura + " No es palindroma")