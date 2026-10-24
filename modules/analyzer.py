import pandas as pd
import matplotlib.pyplot as plt
from file_manager import data_formatter
DATASET = pd.DataFrame(data_formatter()) # the dataframe will be created with a dict of lists

def overall_profitability(DATASET):
    profit_all = False    

    return profit_all

def montly_profitability(data):
    profit_mth = False

    return profit_mth

def highest_profit(data, day_count, month = "none", year = "none"):
    highest_profit = ((data[data["Status"] == "Profit"])
                         .sort_values(by="Amount")).tail(day_count)
        

    return highest_profit

def lowest_profit(data, day_count, month = "none", year = "none"):
    lowest_profit = ((data[data["Status"] == "Loss"])
                     .sort_values(by="Amount")).head(day_count)
    
    return lowest_profit

def add_records(data):

    
    op_result = "Record added!"
    return op_result


# print(dataset[["Status","Amount"]].groupby("Status")
#     .agg({"Status": "count", "Amount": "sum"}))
# print(DATASET[DATASET["Status"] == "Loss"]) 

print(lowest_profit(DATASET,5).to_string())
print()
lowest_profit(DATASET,5005).plot()
plt.show()