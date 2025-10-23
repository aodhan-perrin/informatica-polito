s = "Testing 3."

print("only letters: ",s.isalpha())
print("only upper: ", s.isupper())
print("only lower: ", s.islower())
print("only digit: ", s.isdigit())
print("is alphanumeric: ", s.isalnum())
print("[0] is upper: ", s[0].isupper())
print("ends in dot: ", s[-1] == '.')