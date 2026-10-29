import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from file_manager import data_formatter

DATASET = pd.DataFrame(data_formatter()) # the dataframe will be created with a dict of lists

def overall_profitability():
    profit_all = DATASET[["Status", "Amount"]].groupby("Status").agg({"Status": "count","Amount": "sum"})
    p_rate = (DATASET.groupby("Status")["Amount"].sum() / 100000 * 100)
# This is a temporary printer.
    print(profit_all) 
    print() 
    print(p_rate.map(lambda x: f"{x:.2f}%")) 
    return profit_all

def montly_profitability():
    monthly = (DATASET.groupby(DATASET["Date"].dt.to_period("M"))["Amount"].sum())
    monthly_rate = (monthly / 100000) * 100
# This is a temporary printer.
    print(monthly_rate.map(lambda x: f"{x:.2f}%"))
    return monthly_rate

def montly_results(month, year):
    # This gets the earning and loss per month and the quantity of days 
    profit_mth = (DATASET[(DATASET["Date"].dt.month == int(month)) & (DATASET["Date"].dt.year == int(year))])
    total_earnings = profit_mth[["Status","Amount"]].groupby("Status").agg({"Status": "count", "Amount": "sum"})
# This is a temporary printer.
    print(profit_mth)
    print()
    print(total_earnings)
    return profit_mth, total_earnings

def highest_profit(data, day_count, month = None, year = None):
    option = 1

    if month > 0: option = 2
    match option:
        case 1:
            highest_profit = data[data["Status"] == "Profit"].nlargest(day_count, "Amount")
        case 2:    
            month_set = data[data["Date"].dt.month == month]
            highest_profit = month_set[month_set["Status"] == "Profit"].nlargest(day_count, "Amount")
        
    return highest_profit

def lowest_profit(data, day_count, month = None, year = None):
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

{

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
# print(highest_profit(DATASET, 3, 3, 2026))
# print(highest_profit(DATASET, 10))

# overall_profitability()
}

print("1 overall_profitability()\n2 montly_profitability() \n3 montly_results()\n4 highest_profit()\n5 Lowest_profit()\n6 In process")
while True:
    option = int(input("Elige tu opcion: "))
    print()
    match option:
        case 1:
            overall_profitability()
        case 2:
            montly_profitability()
        case 3:
            month = input("Enter the month number: ")
            if month == "0": # for testing purposes.
                print("\nGood bye!")
                break
            year = input("Enter the year number: ")
            profit1, profit2 = montly_results(month,year) # Here is the beef!
            print(profit1)
            print(profit2)
        case 4:
            month = input("Enter the month number: ")
            if month == "0": # for testing purposes.
                print("\nGood bye!")
                break
            year = input("Enter the year number: ")
            print(highest_profit(DATASET, 3, month, year))
        case 5:
            month = input("Enter the month number: ")
            if month == "0": # for testing purposes.
                print("\nGood bye!")
                break
            year = input("Enter the year number: ")
            print(lowest_profit(DATASET, 3, month, year))
        case 6:
            print("In process")
        case 9:
            break

