import pandas as pd
from IPython.display import display
from Information import Information

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

info = Information()
train_info = info.get_missing_values(train)
test_info = info.get_missing_values(test)

display(train_info)
display(test_info)