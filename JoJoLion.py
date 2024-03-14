def info(Name, Age, Stand, Parts):
    a = str(input("Введіть ім'я персонажа"))
    if a == "Dio" or "dio":
        print(f"Name: {Name}\nAge: {Age}\nStand: {Stand}\nParts: {Parts}")
    elif a == "Kars" or "kars":
        print(f"Name: {Name}\nAge: {Age}\nStand: {Stand}\nParts: {Parts}")

class DIO:
    Name = "Dio Burandō"
    Age = "123"
    Stand = "The World"
    Parts = "Part 1, Part 3, Par 6"

class KARS:
    Name = "Kāzu"
    Age = "102,000"
    Stand = "None"
    Parts = "Part 2"




dios = DIO()
info(dios.Name, dios.Age, dios.Stand, dios.Parts)

karsus = KARS()
info(karsus.Name, karsus.Age, karsus.Stand, karsus.Parts)


