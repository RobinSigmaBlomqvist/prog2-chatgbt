
# Enkel planeringsapp

sysslor = {
    "Skola": [],
    "Hem": [],
    "Fritid": [],
    "Övrigt": []
}

def visa_sysslor():
    for kategori, lista in sysslor.items():
        print(f"\n{kategori}:")
        if lista:
            for nummer, syssla in enumerate(lista, 1):
                print(f"{nummer}. {syssla}")
        else:
            print("Inga sysslor ännu.")

def lagg_till():
    print("\nVälj kategori:")
    kategorier = list(sysslor.keys())

    for i, kategori in enumerate(kategorier, 1):
        print(f"{i}. {kategori}")

    val = input("Kategori: ")

    if val.isdigit() and 1 <= int(val) <= len(kategorier):
        kategori = kategorier[int(val) - 1]
        syssla = input("Vad ska du göra? ")
        sysslor[kategori].append(syssla)
        print("Sysslan har lagts till!")
    else:
        print("Ogiltigt val.")

while True:
    print("\n=== PLANERINGSAPP ===")
    print("1. Visa sysslor")
    print("2. Lägg till syssla")
    print("3. Avsluta")

    val = input("Välj: ")

    if val == "1":
        visa_sysslor()
    elif val == "2":
        lagg_till()
    elif val == "3":
        print("Hejdå!")
        break
    else:
        print("Försök igen.")
