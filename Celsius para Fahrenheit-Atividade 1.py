celsius = float(input("Digite a temperatura da sua cidade em C°: ")) 
conversao_fahrenheit = 1.8*celsius+32
print("A sua temperatura convertida de celsius para fahrenheit é: ", conversao_fahrenheit, " °F")
fahrenheit = float(input("Digite a temperatura da sua cidade em F°: "))
conversao_celsius = (fahrenheit-32)//1.8
print("A sua temperatura convertida de celsius para fahrenheit é: ", conversao_celsius, " °C")