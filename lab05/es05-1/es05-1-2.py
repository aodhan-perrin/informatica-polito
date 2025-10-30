VOWELS = "aeiou"
PLURALS = ["etats-unis", "pays-bas"]
EXCEPTIONS = ["belize", "camboge", "mexique", "mozanbique", "zaire", "zimbabwe"]


country = input("insert country -> ")

if country.lower() in PLURALS:
    country = "les " + country
elif country[0].lower() in VOWELS:
    country = "l\'" + country 
elif country[-1] != 'e' or country.lower() in EXCEPTIONS:
    country = "le " + country
else:
    country = "la " + country

print(country)