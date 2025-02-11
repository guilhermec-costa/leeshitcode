from typing import List, Tuple

def two_sum(iter: List[int], targ: int) -> Tuple[int, ...]:
  for idx_i in range(len(iter)):
    for idx_j in range(idx_i + 1, len(iter)):
      if iter[idx_i] + iter[idx_j] == targ:
        return (idx_i, idx_j)

  return (-1)


