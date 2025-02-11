def roman_to_int(s: str):
  roman_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  sub_combinations = {
    "IV": 2,
    "IX": 2,
    "XL": 20,
    "XC": 20,
    "CD": 200,
    "CM": 200
  }

  to_int = 0
  for c in s:
    to_int += roman_map[c]

  for combination in sub_combinations.keys():
    comb_count = s.count(combination)
    if(comb_count > 0):
      to_int -= sub_combinations[combination] * comb_count

  return to_int

print(roman_to_int("VI"))