import pandas as pd
from file_manager import data_formatter

dataset = pd.DataFrame(data_formatter()) # the dataframe will be created with a dict of lists

print(dataset.to_string())