def waveProperties(length: float) -> tuple:
    if length > 10e-1:
        type = "Radio Wave"
        freq = "below 3e9Hz"
    elif length <= 10e-1 and length > 10e-3:
        type = "Microwave"
        freq = "between 3e9Hz and 3e11Hz"
    elif length <= 10e-3 and length > 7e-7:
        type = "Infared"
        freq = "between 3e11Hz and 4e14Hz"
    elif length <= 7e-7 and length > 4e-7:
        type = "Visible Light"
        freq = "between 4e14Hz and 7.5e14Hz"
    elif length <= 4e-7 and length > 1e-8:
        type = "Ultraviolet"
        freq = "between 7.5e14Hz and 3e16Hz"
    elif length <= 1e-8 and length > 1e-11:
        type = "X Ray"
        freq = "between 3e16Hz and 3e19Hz"
    else:
        type = "Gamma Ray"
        freq = "above 3e19Hz"
    
    return (type, freq)


length = float(input("input wavelength (m) -> "))
wave = waveProperties(length)

print(
    f"Wave Type: {wave[0]}\n"
    f"Wave Frequency: {wave[1]}"
)

