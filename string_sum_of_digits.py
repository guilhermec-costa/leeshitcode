def sum_of_digits(s: str, k: int) -> int:
  digits_str = ""
  base_char = 97
  for c in s:
    digits_str += str(ord(c) + 1 - base_char)

  for _ in range(k):
    sum = 0
    for c in digits_str:
      sum += int(c)

    digits_str = str(sum)

  return sum

print(sum_of_digits("leetcode", 2))