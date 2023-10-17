import pandas as pd
from openpyxl import Workbook
import datetime

weeknumber = datetime.date.today().isocalendar()[1]
csv_path_willys = 'output/willys_promos' + '_w' + str(weeknumber) + '.csv'
csv_path_hemkop = 'output/hemkop_promos' + '_w' + str(weeknumber) + '.csv'
csv_path_coop = 'output/coop_promos' + '_w' + str(weeknumber) + '.csv'

store_names = ['Willys', 'Hemkop', 'Coop']
csv_files = [csv_path_willys, csv_path_hemkop, csv_path_coop]
output_file = "output/disctrack" + "_w" + str(weeknumber) + ".xlsx"

# Create a new Workbook
workbook = Workbook()
# Remove the default sheet created and use a new one
sheet = workbook.active

# Loop through the store names and CSV files, and load each CSV file into the Workbook
for store_name, csv_file in zip(store_names, csv_files):
    df = pd.read_csv(csv_file)
    data = [df.columns.tolist()] + df.values.tolist()  # Include column headers

    # Add a blank row before each store's data
    sheet.append(["", "", ""])
    # Add the store name as a label
    sheet.append([store_name, "", ""])
    # Add the data to the sheet
    for row in data:
        sheet.append(row)

# Save the workbook to the output XLSX file
workbook.save(output_file)

print(f"XLSX file '{output_file}' has been created.")