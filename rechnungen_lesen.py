import pandas as pd

df = pd.read_excel("rechnungen.xlsx")

print(df)
rechnungen = df.to_dict(orient="records")
print(rechnungen)