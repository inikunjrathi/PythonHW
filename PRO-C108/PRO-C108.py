import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("C:/Users/confu/Desktop/PythonHW/PRO-C108/PRO-C108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["rating"])
fig.show()
