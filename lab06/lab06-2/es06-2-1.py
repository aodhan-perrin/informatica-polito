def sussidio(reddito: int, figli: int) -> int:
    if reddito < 20000 and figli:
        return figli * 2000
    elif reddito >= 20000 and reddito < 30000 and figli >= 2:
        return figli * 1500
    elif reddito >= 30000 and reddito < 40000 and figli >= 3:
        return figli * 1000
    else:
        return 0


agg_familia = True

while agg_familia:
    reddito = int(input("inserisci reddito -> "))
    figli = int(input("inserisci il n. di figli -> "))

    print(f"il sussidio annuo e': €{sussidio(reddito, figli)}")

    continua = input("\ninserisci nuova famiglia? [y/n] -> ")

    match continua:
        case "y":
            pass
        case 'n':
            agg_familia = False
