
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')  
SCOPED_CREDS = CREDS.with_scopes(SCOPE)  
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) #To authorize the scope
SHEET = GSPREAD_CLIENT.open('love_sandwiches') #Using open method on Gsheet file 'love-sandwiches

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """
    Get sales figures inpurt from user 
    """
    print("Enter sales data from the last market.,\nData should be six numbers, separated by commaes,\nExample: 10,20,3,4,5,5")

    data_str = input("Enter your data here: ")
    
    print(f"\nThe data you provided is {data_str} ")

get_sales_data()        