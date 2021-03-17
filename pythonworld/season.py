#Написать функцию season, принимающую 1 аргумент — 
# номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(mounth: int) -> str:
    try:
        if mounth == 1 or mounth == 2 or mounth == 12:
            return "winter"
        elif mounth >= 3: 
            if mounth <= 5:
                return "autumn"
            elif mounth <= 8:
                return "summer"
            elif mounth <= 11:
                return "fall"
    except mounth > 12:
        return "none"
    except mounth < 1:
        return "none"

print(season(int(input("Please enter a number: "))))        