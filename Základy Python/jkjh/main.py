muj_list = [
    "Ostrava",
    "Kladno",
    "Praha",
    "Liberec",
    "Opava",
    "České Budějovice",
    "Litoměřice"
]

vstup = int(input("Zadejte index města: "))

for index, mesto in enumerate(muj_list, start=1):
    print(f"{index}. město: {mesto}")