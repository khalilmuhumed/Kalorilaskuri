def laske_bmr(paino, pituus, ika, sukupuoli):
    #Laskee ja palauttaa perusaineenvaihdunnan (BMR) käyttäen Harris-Benedictin kaavaa.
    if sukupuoli.lower() == "mies":
        return 88.362 + (13.397 * paino) + (4.799 * pituus) - (5.677 * ika)
    else:
        return 447.593 + (9.247 * paino) + (3.098 * pituus) - (4.330 * ika)

def suositeltu_kalorimaara(bmr, tavoite):
    #Määrittää suositellun päivittäisen kalorimäärän perusteella tavoitteen.
    if tavoite.lower() == "nosto":
        return bmr + 750
    elif tavoite.lower() == "pudotus":
        return bmr - 500
    return bmr

def maarita_treeni(sukupuoli, tavoite):
    #Määrittää käyttäjälle sopivan treeniohjelman sukupuolen ja tavoitteen perusteella.
    if sukupuoli.lower() == "mies":
        if tavoite.lower() == "nosto":
            return "Voimannostotreeni"
        elif tavoite.lower() == "pudotus":
            return "Kardiotreeni"
    else:
        if tavoite.lower() == "nosto":
            return "Lihaskuntotreeni"
        elif tavoite.lower() == "pudotus":
            return "Aerobinen treeni"
    return "Yleiskuntoharjoittelu"

def tulosta_viikko_ohjelma(treeni):
    #Tulostaa viikonpäiväkohtaisen treeniohjelman taulukkona.
    viikonpaivat = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
    if treeni == "Voimannostotreeni":
        ohjelma = ["Penkkipunnerrus, 3x10", "Jalkakyykky, 3x10", "Lepopäivä", "Maastaveto, 3x10", "Lepopäivä", "Olkapääpunnerrus, 3x10", "Lepopäivä"]
    elif treeni == "Kardiotreeni":
        ohjelma = ["Juoksu, 5 km", "Lepopäivä", "Pyöräily, 20 km", "Lepopäivä", "Juoksu, 10 km", "Uinti, 1 tunti", "Lepopäivä"]
    elif treeni == "Lihaskuntotreeni":
        ohjelma = ["Koko kehon kiertoharjoittelu", "Lepopäivä", "Alakropan harjoitukset", "Lepopäivä", "Yläkropan harjoitukset", "Lepopäivä", "Venyttely"]
    elif treeni == "Aerobinen treeni":
        ohjelma = ["Pitkä kävely, 1 tunti", "Lepopäivä", "Spinning, 45 min", "Lepopäivä", "Step-aerobic, 1 tunti", "Lepopäivä", "Jooga"]
    else:
        ohjelma = ["Lepopäivä"] * 7

    taulukko = "\n".join([f"# {paiva:2}: {harjoitus}" for paiva, harjoitus in zip(viikonpaivat, ohjelma)])
    return taulukko

#Validaatiofunktiot
def get_valid_input(prompt, type_cast, low, high):
    while True:
        try:
            value = type_cast(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Annettu arvo ei ole sallitulla välillä ({low}-{high}). Yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte. Yritä uudelleen.")

def get_goal():
    while True:
        goal = input("Onko tavoitteesi painonpudotus vai -nosto? (pudotus/nosto) ")
        if goal.lower() in ['pudotus', 'nosto']:
            return goal
        print("Virheellinen tavoite. Syötä 'pudotus' tai 'nosto'.")

def get_gender():
    while True:
        gender = input("Oletko mies vai nainen? ")
        if gender.lower() in ['mies', 'nainen']:
            return gender
        print("Virheellinen sukupuoli. Syötä 'mies' tai 'nainen'.")

#Käyttäjän syötteet
pituus = get_valid_input("Anna pituutesi senttimetreinä: ", float, 50, 250)
paino = get_valid_input("Anna painosi kilogrammoina: ", float, 30, 175)
ika = get_valid_input("Anna ikäsi vuosina: ", int, 0, 100)

if ika < 18:
    vuosia_jaljella = 18 - ika
    print(f"Ohjelma on K-18. Odota vielä {vuosia_jaljella} vuotta, jotta pystyt käyttämään ohjelmaa.")
else:
    sukupuoli = get_gender()
    tavoite = get_goal()

    #Lasketaan BMR ja suositeltu kalorimäärä
    bmr = laske_bmr(paino, pituus, ika, sukupuoli)
    kalorimaara = suositeltu_kalorimaara(bmr, tavoite)

    #Määritetään treeni
    treeni = maarita_treeni(sukupuoli, tavoite)

    #Tulostetaan tulokset
    print("")
    print("-" * 50)
    print(f"# Perusaineenvaihduntasi (BMR) on: {bmr:.2f} kcal")
    print(f"# Suositeltu päivittäinen kalorimääräsi on: {kalorimaara:.2f} kcal")
    print("-" * 50)

    #Tulostetaan viikko-ohjelma
    print(f"# Treeniohjelmasi viikolle:")
    print(f"# Sopiva treeniohjelma sinulle on: {treeni}")    
    print("-" * 50)
    print(tulosta_viikko_ohjelma(treeni))
    print("-" * 50)
