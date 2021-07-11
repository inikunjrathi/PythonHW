  
import csv
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px
df = pd.read_csv('PRO-C107\data.csv')

mean=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
fig=px.scatter(mean,x='student_id',y='level',color='attempt')

fig.show()