import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


first_name = input("Enter Player First Name: ")
last_name = input("Enter Player Last Name: ")

from_first = first_name[:2]
from_last = last_name[:5]
first_from_last = last_name[:1]


url = f"https://www.basketball-reference.com/players/{first_from_last}/{from_last}{from_first}01.html".lower()

# Reads the url and stores it
dfs = pd.read_html(url)
# Looks for the first dataframe in the page (The table with the data)
df = dfs[0]

# Using seaborn, it plots the data stored into df as a graph
sns.lineplot(x="Age",y="PTS",data=df)
plt.title("Correlation Between Age and Points Scored")
plt.show()






