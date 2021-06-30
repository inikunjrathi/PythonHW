import plotly.express as px
import pandas as pd
df = pd.read_csv("PRO-C103\PRO-C103.csv")
fig = px.scatter(df, x="date", y="cases",
                 color="country")
fig.show()
