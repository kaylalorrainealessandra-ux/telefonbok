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

