import pandas as pd

dataframe = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

x = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

z = pd.DataFrame({'tom': ['chacolate', 'cake'], 'rome': ['strawberry icecreame', 'biscuits']}, index=['Product A',
                                                                                                      'Product B'])
print(z)

print(dataframe)

print(x)



