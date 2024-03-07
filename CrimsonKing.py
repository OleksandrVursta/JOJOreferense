variable = (True and False or None)
# VAR = print("True")if variable == True else print("False")
if variable == (True):
    print(True)
    print(type(variable))
elif variable == (False):
    print(False)
    print(type(variable))
else:
    print("Bruh")
    print(type(variable))

var1 = 0
while var1 < 2:
    for var in range(51):
        print(var)
    var1 +=1

menu_is_running = (True)
while menu_is_running == True:
    age = int(input("Введіть свій вік"))
    if age < 0 and age > 150:
        print("Ви не пройшли провірку")
    elif age >= 18 and age <= 35:
        print("Ви пройшли провірку")
    elif age <= 18 :
        print("Too small")
    else:
        print("вік не відповідає вимогам")

    variable = True if age >= 18 and age <= 35  else False

    if variable:
        menu_is_running = False