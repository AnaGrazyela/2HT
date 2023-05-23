m = int(2);
band = "V";
numero = int(input("Digite o número:  "))
while ((band == "V") and (m < numero)):
        if((numero % m) == 0):
            band = "F";
        else:
            m = m + 1;
if (band == "V"):
        print("É um número primo")
else:
23-	        print("Não é numero primo")
