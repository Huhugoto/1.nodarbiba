print("Biļešu cenas kalkulators")

vecums = int(input("Ievadi savu vecumu: "))

# TODO: ar if, elif un else nosaki pareizo cenu
if vecums <= 6:
    cena = 0
    print(f"Biļetes cena ir {cena} EUR.")
if vecums >= 7 and vecums <= 17:
    cena = 3
    print(f"Biļetes cena ir {cena} EUR.")
if vecums >= 18 and vecums <= 64:
    cena = 7
    print(f"Biļetes cena ir {cena} EUR.")
if vecums >= 65:
    cena = 4
    print(f"Biļetes cena ir {cena} EUR.")





