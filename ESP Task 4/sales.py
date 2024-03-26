import datetime
import pandas as pd
import matplotlib.pyplot as plt
 
# Function to load data from CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, index_col='ID')
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
 
file_path = 'Task_4a_data.csv'
df = load_data(file_path)
if df is None:
    # Handle the case where the file is not found
    exit()
 
# Function for the main menu
def main_menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    choice = int(input(""))
    return choice
 
# Function for the reports menu
def reports_menu():
    print("**** Reports Dashboard ****")
    print("1. Individual Employee Report")
    choice = int(input(""))
    return choice
 
# Function to generate individual employee report
def generate_individual_report(df, employee_id, start_date, end_date):
    df_report = df.loc[df.index == employee_id] 
    df_report = df_report.T[3:]
    df_report.reset_index(inplace=True)
    df_report['Date'] = pd.to_datetime(df_report['index'], format='%d/%m/%Y')
    start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
    end_date = pd.to_datetime(end_date, format='%d/%m/%Y')
    mask = (df_report['Date'] >= start_date) & (df_report['Date'] <= end_date)
    df_search = df_report.loc[mask]
    print(df_search)
    print('Total by id = {} is {}'.format(employee_id, sum(df_search[employee_id])))
    plt.bar(df_search['index'], df_search[employee_id])
    plt.xticks(rotation=90)
    plt.show()
 
# Main function to run the program
def main():
    file_path = 'Task_4a_data.csv'
    df = load_data(file_path)
    while True:
        choice = main_menu()
        if choice == 1:
            try:
                employee_id = int(input("Enter the Staff ID "))
                if employee_id not in df.index.values:
                    print('Invalid Staff ID')
                    continue
                date = input("Enter Date in dd/mm/yy: ")
                day, month, year = date.split("/")
                date = datetime.date(int(year), int(month), int(day))
                if date > datetime.datetime.today().date():
                    print("Date is in the future")
                    continue
                cost = float(input("Enter the cost : "))
                df.loc[employee_id, date.strftime('%d/%m/%Y')] = cost
            except Exception as e:
                print(f"Error occurred: {e}")
        elif choice == 2:
            reports_choice = reports_menu()
            if reports_choice == 1:
                try:
                    employee_id = int(input("Enter the Employee Id : "))
                    start_date = input("Enter Starting Date in dd/mm/yyyy: ")
                    day, month, year = start_date.split("/")
                    start_date = datetime.date(int(year), int(month), int(day))
                    end_date = input("Enter Date in dd/mm/yyyy: ")
                    day, month, year = end_date.split("/")
                    end_date = datetime.date(int(year), int(month), int(day))
                    generate_individual_report(df, employee_id, start_date, end_date)
                except Exception as e:
                    print(f"Error occurred: {e}")
        else:
            print("Invalid choice")
 
if __name__ == "__main__":
    main()