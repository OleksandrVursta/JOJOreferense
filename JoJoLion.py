def info():
    menu_is_running = (True)
    while menu_is_running == True:
        a = str(input("Введіть ім'я антагоніста:"))
        if a == "Dio" or a == "dio":
            dios = DIO()
            print(f"Name: {dios.Name}\nAge: {dios.Age}\nStand: {dios.Stand}\nParts: {dios.Parts}")
            print(dioskils.keys)
            print(dioskils.values)
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
        b = str(input("Ви впевнені в виборі?"))
        if b == "Yes" or b == "yes" or b == "Так" or b =="так":
            menu_is_running = (False)


class DIO:
    Name = "Dio Burandō"
    Age = "123"
    Stand = "The World"
    Parts = "Part 1, Part 3, Par 6"
    dioskils = {
        1: "Block",
        2: "Donut",
        3: "Knives",
        4: "Time Stop",
        5: "Road Roller Da",
    }

class KARS:
    Name = "Kāzu"
    Age = "102,000"
    Stand = "None"
    Parts = "Part 2"
    karsskils = {
        1: "Intake",
        2: "Punch",
        3: "Strong rush-down",
        4: "Light Blades",
        5: "Ultimate Thing",
    }

class YOSHIKAGE:
    Name = "Yoshikage Kira"
    Age = "33"
    Stand = "Killer Queen"
    Parts = "Part 4"
    yoshikageskils = {
        1: "Block",
        2: "Coin",
        3: "Stray cat",
        4: "Sheer Heart Attack",
        5: "Bite The Dust",
    }

class DIAVOLO:
    Name = "Diaboro Vinegar Doppio"
    Age = "33"
    Stand = "King Crimson"
    Parts = "Part 5"
    diavoloskils = {
        1: "Punch",
        2: "Donut",
        3: "Blood in the eyes",
        4: "Time Erasure",
        5: "Epitaph",
    }
class PUCCI:
    Name = "Enrico Pucci"
    Age = "39"
    Stand = "Whitesnake, C-Moon, Made in Heaven"
    Parts = "Part 6"
    pucciskils = {
        1: "Illusions",
        2: "Whitesnake Punch",
        3: "C-Moon Punch",
        4: "Take The Stand Disk",
        5: "Reboot",
    }

info()
