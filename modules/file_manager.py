import csv
from datetime import datetime as dt
import pandas as pd

def monthfixer(date): 
    # uses a dict to change the month to english if the record has them in spanish
    months = {
    "Ene": "Jan",
    "Feb": "Feb",
    "Mar": "Mar",
    "Abr": "Apr",
    "May": "May",
    "Jun": "Jun",
    "Jul": "Jul",
    "Ago": "Aug",
    "Sep": "Sep",
    "Oct": "Oct",
    "Nov": "Nov",
    "Dic": "Dec"
    }
    
    day, month, year = date.split("/")
    return f"{day}/{months.get(month, month)}/{year}"

def date_formatter(date, case):
    # This handles any error in case of language and formats the date to (YYYY-MM-DD)
    try:
        rdate = dt.strptime(date, "%d/%b/%Y")
    except ValueError: 
        rdate = dt.strptime(monthfixer(date), "%d/%b/%Y")

    if case == 1:
        return rdate.strftime("%d-%b-%Y")
    else:
        return rdate.strftime("-%Y-%b-%d")

def csv_extractor():
    with open('data/data.csv') as data:
        next(data)
        records = data.readlines()
    return records

def data_formatter( ):
    transactions = {
        "Date" : [],
        "Amount" : [],
        "Status" :[]
    }
    for item in csv_extractor():
        transaction = item.split(",") 
    # This condition labels the output [loss, profit]
        if "-)" in transaction[1].split("("):
            op_output = "Loss"
        else:
            op_output = "Profit"

        raw_number = transaction[2].replace('"',"")
        raw_number = raw_number.replace('.','') # In case of any number greater than 999, removes the '.'
        decimal_point = transaction[3].replace('"',"")
        amount = float(raw_number.replace('$',"") + "." + decimal_point)

        transactions["Date"].append(date_formatter(transaction[0], 1)) 
        transactions["Amount"].append(amount) 
        transactions["Status"].append(op_output)

        #print(f"{op_output} | {amount} | {date_formatter(transactions[0], 1)}")
    
    return transactions



# data_formatter(csv_extractor())    


