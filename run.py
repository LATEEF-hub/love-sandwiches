
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
    print("Enter sales data from the last market.,\nData should be six numbers, separated by commaes,\nExample: 10,20,3,4,5,5")

    data_str = input("Enter your data here: ")
    # print(f"\nThe data you provided is {data_str} ")
    sales_data = data_str.split(",")
    # print(sales_data)
    validate_data(sales_data)

def validate_data(values):
        """
        Use Try and Exception method to validate, Inside Try convert all Str to Int
        Raise errors if less than 6 or greater and if Str cannot be converted.
        """
        try:
            if len(values) != 6:
                raise ValueError(
                    f'Enter 6 figures exactly, you provided {len(values)} '
                )
        except ValueError as e:
            print(f"Invalid data: {e}, Please try again.\n")
         
        
get_sales_data() #We have to call the function for the CODE it to run...6.
