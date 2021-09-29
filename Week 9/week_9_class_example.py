import pandas as pd

dataframe = pd.read_csv("w09water.csv")

# meterColumn = dataframe["meterSize"]

filteredDataframe = dataframe[dataframe["meterSize"] < .8]
