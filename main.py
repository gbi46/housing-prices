from sklearn.datasets import fetch_california_housing

import pandas as pd

data = fetch_california_housing(as_frame=True)
df = data.frame

print(df)
