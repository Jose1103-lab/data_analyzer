import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from file_manager import data_formatter

DATASET = pd.DataFrame(data_formatter()) # the dataframe will be created with a dict of lists

def overall_profitability():
    profit_all = False    

    return profit_all

def montly_profitability(month, year):

    return

def montly_results(month, year):
    # This gets the earning and loss per month and the quantity of days 
    profit_mth = (DATASET[(DATASET["Date"].dt.month == int(month)) & (DATASET["Date"].dt.year == int(year))])
    total_earnings = profit_mth[["Status","Amount"]].groupby("Status").agg({"Status": "count", "Amount": "sum"})

    return profit_mth, total_earnings

def highest_profit(data, day_count, month = 0, year = 0):
    option = 1

    if month > 0: option = 2
    match option:
        case 1:
            highest_profit = data[data["Status"] == "Profit"].nlargest(day_count, "Amount")
        case 2:    
            month_set = data[data["Date"].dt.month == month]
            highest_profit = month_set[month_set["Status"] == "Profit"].nlargest(day_count, "Amount")
        
    return highest_profit

def lowest_profit(data, day_count, month = 0, year = 0):
    option = 1

    if month > 0: option = 2
    match option:
        case 1:
            lowest_profit = data[data["Status"] == "Loss"].nsmallest(day_count, "Amount")
        case 2:
            month_set = data[data["Date"].dt.month == month]
            lowest_profit = month_set[month_set["Status"] == "Loss"].nsmallest(day_count, "Amount")
    
    return lowest_profit

def add_records(data):
    op_result = "Record added!"
    return op_result


# print(dataset[["Status","Amount"]].groupby("Status")
#     .agg({"Status": "count", "Amount": "sum"}))
# print(DATASET[DATASET["Status"] == "Loss"]) 
# print(lowest_profit(DATASET,5).to_string())

# profits.plot(kind = "line", y="Date")
# plt.show()

# print(montly_profitability(10,2025).to_string())

# while(True):
#     month = input("Enter the month number: ")
#     if month == "0": # for testing purposes.
#         print("\nGood bye!")
#         break
#     year = input("Enter the year number: ")
    
#     profit1, profit2 = montly_results(month,year)
#     print(profit1)
#     print(profit2)

# print(lowest_profit(DATASET, 3, 3, 2026))
# print(lowest_profit(DATASET, 3).plot(y="Amount"))
# plt.show()
print(highest_profit(DATASET, 3, 3, 2026))
print(highest_profit(DATASET, 3))