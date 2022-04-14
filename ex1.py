from sys import argv

script, filename = argv

txt = open(filename, 'w')


def multiply(a, b):
    print(f"Transakcija: {a} * {b}")
    return a * b


print("DOBRODOSLI U 'shonexYEAH' menjacnicu, pravo mesto za klepanje!")
celokupan_iznos = input("Unesite iznos: ")
iznos = input(f"Trenutno stanje je {celokupan_iznos}, unesite tacan iznos za sl.transakciju: ")
prva = input("Iz koje valute? [EUR], [USD], [HUF], [RSD]: ")
druga = input("U koju valutu? [EUR], [USD], [HUF], [RSD]: ")

if prva.upper() == "EUR" and druga.upper() == "RSD":
    konverzija = multiply(float(iznos), 117.5)
    print(f"Vas iznos je: {konverzija} RSD.")
if prva.upper() == "EUR" and druga.upper() == "USD":
    konverzija = multiply(float(iznos), 1.09)
    print(f"Vas iznos je: {konverzija} USD.")
if prva.upper() == "EUR" and druga.upper() == "HUF":
    konverzija = multiply(float(iznos), 376.81)
    print(f"Vas iznos je: {konverzija} HUF.")

if prva.upper() == "RSD" and druga.upper() == "EUR":
    konverzija = multiply(float(iznos), 0.0085)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva.upper() == "RSD" and druga.upper() == "USD":
    konverzija = multiply(float(iznos), 0.0092)
    print(f"Vas iznos je: {konverzija} USD.")
if prva.upper() == "RSD" and druga.upper() == "HUF":
    konverzija = multiply(float(iznos), 3.20)
    print(f"Vas iznos je: {konverzija} HUF.")

if prva.upper() == "USD" and druga.upper() == "EUR":
    konverzija = multiply(float(iznos), 0.92)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva.upper() == "USD" and druga.upper() == "HUF":
    konverzija = 0
    print("Nije moguce izvrsiti transakciju iz usd u HUF.")
if prva.upper() == "USD" and druga.upper() == "RSD":
    konverzija = multiply(float(iznos), 108.20)
    print(f"Vas iznos je: {konverzija} RSD.")

if prva.upper() == "HUF" and druga.upper() == "EUR":
    konverzija = multiply(float(iznos), 0.0027)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva.upper() == "HUF" and druga.upper() == "USD":
    konverzija = multiply(float(iznos), 0.0029)
    print(f"Vas iznos je: {konverzija} USD.")
if prva.upper() == "HUF" and druga.upper() == "RSD":
    konverzija = multiply(float(iznos), 0.31)
    print(f"Vas iznos je: {konverzija} RSD.")

print("\n")
txt.write("Dana 14.04.2022.")
txt.write("\n")
txt.write(f"***Uspesno ste promenili {iznos} {prva}. u {konverzija} {druga}.***")
txt.write("\n")
txt.write("\n")
txt.write("Hvala Vam sto koristite nasu menjacnicu!")
txt.close()

txt = open(filename)

print(txt.read())

print("Ne zaboravite Vas isecak!")
print("\n")
preostalo_stanje = float(celokupan_iznos) - float(iznos)
print(f"Preostalo stanje: {preostalo_stanje}")
odgovor = input("Da li zelite da nastavite? [da/ne]: ")
