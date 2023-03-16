from fuzzywuzzy import fuzz

string1 = "Ini adalah contoh kalimat pertama"
string2 = "Ini adalah contoh kalimat kedua"

ratio = fuzz.token_set_ratio(string1, string2)

print(ratio)
