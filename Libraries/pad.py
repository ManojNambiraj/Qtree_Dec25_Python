# Pandas

import pandas as pd

# Series

    # s = pd.Series([1,3,5,7,9], index=["a", "b", "c", "d", "e"])

    # print(s)

    # data = {'apple': 3, 'banana': 5, 'cherry': 7}

    # s = pd.Series(data)

    # print(s * 2)

# DataFrame

data = {
    'Name': ['John', "Charlie", "Raj", "Geetha"],
    'Age': [25, 30, 15, 42],
    'City': ['NY', 'LA', 'US', 'Chicago']
}

df = pd.DataFrame(data)

print(df)