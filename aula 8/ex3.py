frase = input("Digite uma frase: ").lower()
frase_codificada = ""
frase_decodificada = ""


codificada = frase.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
print(codificada)
decodificada = codificada.replace("1", "a").replace("2", "e").replace("3", "i").replace("4", "o").replace("5", "u")
print(decodificada)
