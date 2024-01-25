import random
import numpy as np
def xanadu_generator():
    for char in ["迷えば", "道を", "見失う", "故に", "試練が", "必要なのだ"]:
        n = int(abs(np.random.normal(0, 5)))
        [print(char, end="") for _ in range(n)]

if __name__ == "__main__":
    xanadu_generator()