import pandas as pd
import numpy as np
from scipy.stats import chi2

chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    n = len(x)
    dof = n - 1
    chi_stat = sum([(o - e)**2.0 / e for o,e in zip(y, x)])
    return chi_stat >= chi2.ppf(q=1-0.09, df=dof)
