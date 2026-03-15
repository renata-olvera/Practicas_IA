beatles = []

integrantes = ["John Lennon", "Paul McCartney", "George Harrison"]

for persona in integrantes:
    beatles.append(persona)

extras = ["Stu Sutcliffe", "Pete Best"]

for persona in extras:
    beatles.append(persona)

beatles.remove("Stu Sutcliffe")
beatles.remove("Pete Best")

beatles.insert(0, "Ringo Starr")

print("Los Fav", len(beatles))