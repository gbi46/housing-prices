from colorama import Back, Fore, init, Style
from sklearn.datasets import fetch_california_housing

import pandas as pd

init(autoreset=True)

data = fetch_california_housing(as_frame=True)
df = data.frame

print(Back.GREEN + " === === Frame === ===")
print(df)

frame_head = df.head()
frame_desc = df.describe()
frame_corr = df.corr()["MedHouseVal"].sort_values()

print(Back.BLUE + "   === == = EDA = == ===")
print(Back.GREEN + " === === head === ===")
print(frame_head)

print(Back.GREEN + " === === describe === ")
print(frame_desc)

print(Back.GREEN + " === === correlation === === ")
print(frame_corr)
