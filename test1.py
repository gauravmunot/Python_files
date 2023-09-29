import pandas as pd

data = pd.read_csv("medical_insurance.csv")

data

data['sex'].value_counts()

print(data['region'].value_counts())
print("Hello Gaurav")
