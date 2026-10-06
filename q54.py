import pandas as pd



# 1. Series from a List
list_data = [10, 20, 30, 40, 50]
series1 = pd.Series(list_data)
print("Series from List:")
print(series1)


# 2. Series from a Set
set_data = {10, 20, 30, 40, 50}
series2 = pd.Series(list(set_data))
print("\nSeries from Set:")
print(series2)


# 3. Series from a Dictionary
dict_data = {
    "A": 10,
    "B": 20,
    "C": 30
}
series3 = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(series3)
