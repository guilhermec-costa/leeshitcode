from typing import List

def longest_common_prefix(strs: List[str]):
  prefix = ""

  min_length = min(list(map(lambda x: len(x), strs)))
  for i in range(min_length):
    idx_formed_prefix = ""
    for word in strs:
      idx_formed_prefix += word[i]

    unique_chars = list(set(idx_formed_prefix))
    if len(unique_chars) == 1:
      prefix += unique_chars[0]
      continue

  return prefix;


input = ["flower","flow","flight"]
print(longest_common_prefix(input))
  