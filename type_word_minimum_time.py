def min_time_to_type(word: str) -> int:
  spent_time = len(word)
  last_iter_char = "a"

  for c in word:
    diff = (ord(c) - ord(last_iter_char)) % 26
    spent_time += min(diff, 26 - diff)
    last_iter_char = c

  return spent_time

min_time_to_type("bza")