import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)  # To authorize the scope
# Using open method on Gsheet file 'love-sandwiches
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()

# print(data)


def get_sales_data():
    """
    Get sales figures inpurt from user 
    """
    while True:
        print("Enter sales data from the last market.,\nData should be six numbers, separated by commaes,\nExample: 10,20,3,4,5,5")
        data_str = input("Enter your data here: \n")
        sales_data = data_str.split(",")
        # validate_data(sales_data)

        if validate_data(sales_data):
            print("\n")
            print("Data is valid\n")

            break

    return sales_data

    # print(f"\nThe data you provided is {data_str} ")

    # print(sales_data)


def validate_data(values):
    """
    Use Try and Exception method to validate, Inside Try convert all Str to Int
    Raise errors if less than 6 or greater and if Str cannot be converted.
    """
    try:
        [int(value) for value in values]  # To convert all value to Int
        if len(values) != 6:
            raise ValueError(
                f'Enter 6 figures exactly, you provided {len(values)} '
            )
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False
    return True

    

def update_worksheet(data, worksheet):
    """
    update worksheet
    """ 
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} Worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Calc surplus
    """    
    print("Calculating Surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    # print(f"Stock row:{stock_row}")
    # print(f"Sales row:{sales_row}")

     #To iterate through 2 list at a time
    surplus_data =[]
    for stock, sales in zip(stock_row, sales_row):
       surplus = int(stock) - sales
       surplus_data.append(surplus)
    #    print(f"Surplus Data:{surplus_data}\n")
    return surplus_data  


def get_last_5_entries():
    """
    Collect column of data from sales worksheet, last 5 entries for 
    each Sandwich and return data as list of lists
    """    
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:]) #To get the last 5 entries
    # pprint(columns)    
    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data=[]

    for column in data:
        int_column =[int(num) for num in column] # To convert list to INT
        average = sum(int_column) / len(int_column) # To get the average
        stock_num = average * 1.1 # to increase stock by 10%
        new_stock_data.append(round(stock_num))

    return new_stock_data 



def main():
    """
    Run all programs function
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    
    # print(new_surplus_data)
    sales_column = get_last_5_entries()
    stock_data = calculate_stock_data(sales_column)
    update_worksheet(stock_data,"stock")
    print(stock_data)
    
print("")
print("Welcome to Love Sandwiches")
main()    





