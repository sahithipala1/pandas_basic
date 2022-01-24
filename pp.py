import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_chocolate_bar_brands')

print(df)
