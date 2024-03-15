def info():
    menu_is_running = (True)
    while menu_is_running == True:
        a = str(input("Введіть ім'я антагоніста:"))
        if a == "Dio" or a == "dio":
            dios = DIO()
            print(f"Name: {dios.Name}\nAge: {dios.Age}\nStand: {dios.Stand}\nParts: {dios.Parts}")
        elif a == "Kars" or a == "kars":
            karsus = KARS()
            print(f"Name: {karsus.Name}\nAge: {karsus.Age}\nStand: {karsus.Stand}\nParts: {karsus.Parts}")
        elif a == "Kira" or a == "kira":
            yoshikagus = YOSHIKAGE()
            print(f"Name: {yoshikagus.Name}\nAge: {yoshikagus.Age}\nStand: {yoshikagus.Stand}\nParts: {yoshikagus.Parts}")
        elif a == "Diavolo" or a == "diavolo" or a == "Doppio" or a == "doppio":
            diavolos = DIAVOLO()
            print(f"Name: {diavolos.Name}\nAge: {diavolos.Age}\nStand: {diavolos.Stand}\nParts: {diavolos.Parts}")
        elif a == "Pucci" or a == "pucci":
            puccis = PUCCI()
            print(f"Name: {puccis.Name}\nAge: {puccis.Age}\nStand: {puccis.Stand}\nParts: {puccis.Parts}")
        b = str(input("Ви хочите продовжити?"))
        if b == "No" or b == "no" or b == "Ні" or b =="ні":
            menu_is_running = (False)

class DIO:
    Name = "Dio Burandō"
    Age = "123"
    Stand = "The World"
    Parts = "Part 1, Part 3, Par 6"
    dioskils = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
    }

class KARS:
    Name = "Kāzu"
    Age = "102,000"
    Stand = "None"
    Parts = "Part 2"
    karsskils = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
    }

class YOSHIKAGE:
    Name = "Yoshikage Kira"
    Age = "33"
    Stand = "Killer Queen"
    Parts = "Part 4"
    yoshikageskils = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
    }

class DIAVOLO:
    Name = "Diaboro Vinegar Doppio"
    Age = "33"
    Stand = "King Crimson"
    Parts = "Part 5"
    diavoloskils = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
    }
class PUCCI:
    Name = "Enrico Pucci"
    Age = "39"
    Stand = "Whitesnake, C-Moon, Made in Heaven"
    Parts = "Part 6"
    pucciskils = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
    }

info()
