# 3.1_zadanie 1

LISTA_ZAKUPÓW = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów")

for sklep, produkty in LISTA_ZAKUPÓW.items():

    produkty_lista = ", ".join(produkty)
    sklep = sklep.title()
    produkty = [produkt.title() for produkt in produkty]
    
    print(f"Idę do {sklep}, kupuję tu następujące rzeczy: {produkty}.")

suma_produktow = sum(len(produkty) for produkty in LISTA_ZAKUPÓW.values())

print("W sumie kupuję", suma_produktow, "produktów.")


# 3.1|-zadanie 2

for liczby in range(101) :
    if liczby % 5 == 0 :     
        print(liczby)
        print(liczby**3)

# lub

for liczby in range(0, 101, 5) : 
    print(liczby)
    print(liczby**3)