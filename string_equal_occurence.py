from collections import Counter

def are_occurrences_eq(s):
  occ_map = Counter(s)
  vals = occ_map.values()
  return True if len(set(vals)) == 1 else False

print(are_occurrences_eq("cchhuurrooss"))