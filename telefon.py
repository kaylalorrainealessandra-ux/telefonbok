telefonbok = []

person1 = {
    "navn": "Sverre",
    "nummer": "46576760"
}
person2 = {
    "navn": "Andreas",
    "nummer": 41226625
}

telefonbok.append(person1)
telefonbok.append(person2)

def vis_alle():
    for element in telefonbok: 
        print(f"{element["navn"]} sitt nummer er: {element["nummer"]}")

vis_alle()

def legg_til(): 
    nynavn = input("hva heter du?: ")
    nynummer = input("hva er nummeret ditt?: ")
    person3 = {
        "navn": nynavn, 
        "nummer": nynummer
    }
    telefonbok.append(person3)
    print(f"{nynavn} ble lagt til i telefonboka!")
legg_til()
