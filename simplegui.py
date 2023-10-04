#!/usr/bin/env python
import PySimpleGUI as sg
import pandas as pd
import datetime

# Yet another example of showing CSV data in Table

weeknumber = datetime.date.today().isocalendar()[1]
year = datetime.date.today().year

def fetch_csv_data(csv_path):
    if csv_path is not None:
        try:
            df = pd.read_csv(csv_path, sep=',', engine='python', header=None)
            data = df.values.tolist()               # read everything else into a list of rows
        except:
            sg.popup_error('Error reading file')
            return
    
    return data

def create_table(store_values):
    table_header = ['Vara', 'Pris', 'Beskrivning']

    table = sg.Table(values=store_values,
                  headings=table_header,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=max(25, len(store_values)))
    return table

def main():

    sg.set_options(auto_size_buttons=True)
    
    curr_hemkop_path = './output/hemkop_promos_w' + str(weeknumber) + '.csv'
    curr_willys_path = './output/willys_promos_w' + str(weeknumber) + '.csv'
    curr_coop_path = './output/coop_promos_w' + str(weeknumber) + '.csv'

    print(curr_hemkop_path)

    
    hemkop_list = fetch_csv_data(curr_hemkop_path)
    hemkop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))]
    

    coop_list = fetch_csv_data(curr_coop_path)
    coop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))] 
    
    willys_list = fetch_csv_data(curr_willys_path)
    willys_header = ['column' + str(x) for x in range(len(willys_list[0]))]

    store_title_font = ('Helvetica', 17)

    title_font = ('Helvetica', 25, 'bold')
    table_header = ['Vara', 'Pris', 'Beskrivning']

    #Create table elements
    hemkop_table = create_table(hemkop_list)
    coop_table = create_table(coop_list)
    willys_table = create_table(willys_list)
    
    #Build titled columns 
    willys_column = sg.Column([[sg.Text("WILLY:S", font =store_title_font)], 
                                [willys_table]], vertical_alignment='top')
    hemkop_column = sg.Column([[sg.Text('Hemköp', font=store_title_font)], 
                                [hemkop_table]], vertical_alignment='top')
    coop_column = sg.Column([[sg.Text('Coop', font=store_title_font)], 
                                [coop_table]], vertical_alignment='top')

    #Assemble layout
    layout = [[sg.Text('Rabatter vecka ' + str(weeknumber) + ' ' + str(year), font=title_font)],
        [willys_column, hemkop_column, coop_column]
    ]


    window = sg.Window('DiscScrape', layout, size=(1200,700 ), grab_anywhere=True)
    event, values = window.read()
    window.close()

main()