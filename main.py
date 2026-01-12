from colorama import Back, Fore, init, Style
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

# simulate None
df.iloc[::50, 0] = None
df = df.dropna()

print(Back.GREEN + " === === clear data === === ")
print(df)

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_
})

print(Back.GREEN + " === === = Model = === === ")
print(coef_df)
