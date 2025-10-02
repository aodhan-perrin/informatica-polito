def month(day, month) -> str:
    match month:
        case 1 | 2 | 3:
            season = "winter"
        case 4 | 5 | 6:
            season = "spring"
        case 7 | 8 | 9:
            season = "summer"
        case 10 | 11 | 12:
            season = "fall"

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



