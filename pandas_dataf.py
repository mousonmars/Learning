import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd

df = pd.read_csv(r"E:\Lerning\Learning\test4.csv", encoding='utf-8', sep=';')
# mit sep kann man das Trennzeichen der csv definieren !
print(df)
print(df.iloc[0,0])
print(df.loc[0,"Nachname"])
print(df.loc[1,"Name"])

print(df.iloc[1])
