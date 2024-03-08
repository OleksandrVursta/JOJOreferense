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

    def info(self):
        a = str(input("Введіть ім'я персонажа"))
        if a == "Dio" or "dio":
            print(f"Name: {self.Name}\nAge: {self.Age}\nStand: {self.Stand}\nParts: {self.Parts}")
        elif a == "Kars" or "kars":
            print(f"Name: {KARS.Name}\nAge: {KARS.Age}\nStand: {KARS.Stand}\nParts: {KARS.Parts}")


dios = DIO()
dios.info()

karsus = KARS()
karsus.info()


