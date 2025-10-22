def find_season(day: int, month: int) -> str:
    match month:
        case 1 | 2 | 3:
            season = "winter"
        case 4 | 5 | 6:
            season = "spring"
        case 7 | 8 | 9:
            season = "summer"
        case 10 | 11 | 12:
            season = "fall"
        case _:
            season = "that's not a month bro"

    if month % 3 == 0 and day >= 21:
        match season:
            case "winter":
                season = "spring"
            case "spring":
                season = "summer"
            case "summer":
                season = "fall"
            case _:
                season = "winter"

    return season


date = int(input("date -> "))
month = int(input("month -> "))

print(f"the season is {find_season(date, month)}")    
