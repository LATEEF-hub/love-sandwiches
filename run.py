
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
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        # validate_data(sales_data)

        if validate_data(sales_data):
            print("Data is valid")

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


def update_sales_worksheet(data):
    """
    To update sales WORKSHEET, add new row to data list provided.
    """
    print("Updating worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Worksheet successfully updated.\n")

def calculate_surplus_data(sales_row): # To retrieve lastest stock order from Spreadsheet
    """
    """

    print("Calculating Surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    # print(stock_row)

    #To iterate through 2 list at a time
    surplus_data =[]
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data    


# We have to call the function for the CODE it to run...6.

def main():
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)

print("Welcome to Love Sandwiches")
main()    




