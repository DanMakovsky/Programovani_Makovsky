operace = input("napište znamínko matematické operace ")
cislo1 = int(input("číslo 1 ? "))
cislo2 = int(input("číslo 2 ? "))

if operace == "+" :
 vysledek = cislo1 + cislo2
elif operace == "-" :
 vysledek = cislo1 - cislo2
elif operace == "/" :
 vysledek = cislo1 / cislo2
elif operace == "*" :
 vysledek = cislo1 * cislo2

print( cislo1, operace , cislo2, "=", vysledek)