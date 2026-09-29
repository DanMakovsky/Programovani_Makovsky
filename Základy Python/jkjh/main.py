vek = int(input("jaký je váš věk ? "))

if vek >= 18:
    print("Jsi dospělý")
elif vek >= 15:
      print("Jsi dospivající")
elif vek > 0:
      print("Jsi dítě")
else:
      print("Jsi neplatný")