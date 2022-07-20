#!/usr/bin/env python
import PySimpleGUI as sg
import pandas as pd
import datetime

# Yet another example of showing CSV data in Table

weeknumber = datetime.date.today().isocalendar()[1]

def fetch_table_data(csv_path):
    if csv_path is not None:
        try:
            # Header=None means you directly pass the columns names to the dataframe
            df = pd.read_csv(csv_path, sep=',', engine='python', header=None)
            data = df.values.tolist()               # read everything else into a list of rows
        except:
            sg.popup_error('Error reading file')
            return
    
    return data


def table_example():

    
    sg.set_options(auto_size_buttons=True)
    # filename = sg.popup_get_file(
    #     'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # # --- populate table with file contents --- #


    curr_hemkop_path = './output/hemkop_promos_w' + str(weeknumber) + '.csv'
    curr_willys_path = './output/willys_promos_w' + str(weeknumber) + '.csv'
    curr_coop_path = './output/coop_promos_w' + str(weeknumber) + '.csv'

    print(curr_hemkop_path)

    
    hemkop_list = fetch_table_data(curr_hemkop_path)
    hemkop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))]

    coop_list = fetch_table_data(curr_coop_path)
    coop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))] 
    
    willys_list = fetch_table_data(curr_willys_path)
    willys_header = ['column' + str(x) for x in range(len(willys_list[0]))]


    # filename = ''
    # data = []
    # if filename is not None:
    #     try:
    #         # Header=None means you directly pass the columns names to the dataframe
    #         df = pd.read_csv(filename, sep=',', engine='python', header=None)
    #         data = df.values.tolist()               # read everything else into a list of rows
    #         header_list = ['column' + str(x) for x in range(len(data[0]))]
    #     except:
    #         sg.popup_error('Error reading file')
    #         return

    layout = [
        [sg.Table(values=hemkop_list,
                  headings=hemkop_header,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=max(25, len(hemkop_list))),
        sg.Table(values=coop_list,
                  headings=coop_header,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=max(25, len(coop_list))),
        sg.Table(values=willys_list,
                  headings=willys_header,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=max(25, len(willys_list)))
      ]
    ]

    window = sg.Window('RabattApp', layout, size=(1200,700 ), grab_anywhere=True)
    event, values = window.read()
    window.close()

table_example()