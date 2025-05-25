

import os
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')


try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError(
        f"Nie znaleziono pliku model.pkl. Oczekiwano w: {MODEL_PATH}"
    )
