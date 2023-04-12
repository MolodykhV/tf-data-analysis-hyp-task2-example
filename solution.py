import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = MMD(compute_kernel='rbf', gamma=1).test(x, y)[1]
    return p_value < 0.09
