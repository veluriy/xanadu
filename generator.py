import random
import numpy as np
def xanadu_generator():
    for char in ["迷", "道", "見失", "故", "試練", "必要"]:
        n = int(abs(np.random.normal(0, 5)))
        [print(char, end="") for _ in range(n)]

if __name__ == "__main__":
    xanadu_generator()