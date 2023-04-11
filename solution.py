import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 451783978 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    _, p_value = ks_2samp(x, y)
    return p_value < 0.1 # Ваш ответ, True или False
