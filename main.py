from headers import HeaderFormatter
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

import pandas as pd

hf = HeaderFormatter()

data = fetch_california_housing(as_frame=True)
df = data.frame

print(hf.sub_header("Frame"))
print(df)

frame_head = df.head()
frame_desc = df.describe()
frame_corr = df.corr()["MedHouseVal"].sort_values()

print(hf.main_header("EDA"))
print(hf.sub_header("head"))
print(frame_head)

print(hf.sub_header("describe"))
print(frame_desc)

print(hf.sub_header("correlation"))
print(frame_corr)

# simulate None
df.iloc[::50, 0] = None
df = df.dropna()

print(hf.sub_header("clear data"))
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

print(hf.sub_header("Model"))
print(coef_df)

preds = model.predict(X_test)
print(hf.main_header("Applying model"))
print(hf.sub_header("First predictions"))
print(preds)

MAE = mean_absolute_error(y_test, preds)
print(hf.sub_header("Mean Absolute Error"))
print(MAE)

X_mean_df = X.mean().to_frame().T
model_pred = model.predict(X_mean_df)
print(hf.sub_header("Prediction for average House"))
print(model_pred)
