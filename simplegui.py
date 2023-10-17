#!/usr/bin/env python
import PySimpleGUI as sg
import pandas as pd
import datetime

# Yet another example of showing CSV data in Table
global weeknumber
weeknumber = datetime.date.today().isocalendar()[1]
year = datetime.date.today().year

global store_title_font, title_font
store_title_font = ('Helvetica', 17)
title_font = ('Helvetica', 25, 'bold')

def fetch_csv_data(csv_path):
    if csv_path is not None:
        
        df = pd.read_csv(csv_path, sep=',', engine='python', header=None)
        data = df.values.tolist()               # read everything else into a list of rows
    
    return data

def create_table(store_values):
    table_header = ['Vara', 'Pris', 'Beskrivning']

    table = sg.Table(values=store_values,
                  headings=table_header,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=max(25, len(store_values)))
    return table

def create_columns(path, storename):
    list = fetch_csv_data(path)
    table = create_table(list)
    column = sg.Column([[sg.Text(storename, font=store_title_font)], 
                                [table]], vertical_alignment='top')
    return column

def update_week():
    pass

def step_week(step):
    global weeknumber
    curr_hemkop_path = './output/hemkop_promos_w' + str(weeknumber+step) + '.csv'
    curr_willys_path = './output/willys_promos_w' + str(weeknumber+step) + '.csv'
    curr_coop_path = './output/coop_promos_w' + str(weeknumber+step) + '.csv'
    try: 
        hemkop_list = fetch_csv_data(curr_hemkop_path)
        coop_list = fetch_csv_data(curr_coop_path)
        willys_list = fetch_csv_data(curr_willys_path)
    except FileNotFoundError:
        sg.popup("File Not Found")

    hemkop_table = create_table(hemkop_list)
    coop_table = create_table(coop_list)
    willys_table = create_table(willys_list)

    willys_column = sg.Column([[sg.Text("WILLY:S", font =store_title_font)], 
                                [willys_table]], vertical_alignment='top')
    hemkop_column = sg.Column([[sg.Text('Hemköp', font=store_title_font)], 
                                [hemkop_table]], vertical_alignment='top')
    coop_column = sg.Column([[sg.Text('Coop', font=store_title_font)], 
                                [coop_table]], vertical_alignment='top')

    #Button functionality
    prev_button = sg.Button("Previous week")
    next_button = sg.Button("Next week")
    stats_button = sg.Button("Stats...")


    #Assemble layout
    layout = [[sg.Text('Rabatter vecka ' + str(weeknumber+step) + ' ' + str(year), font=title_font), prev_button, next_button, stats_button],
        [willys_column, hemkop_column, coop_column]
    ]
    
    weeknumber += step
    return layout
    




    
def create_layout():
    sg.set_options(auto_size_buttons=True)
    
    curr_hemkop_path = './output/hemkop_promos_w' + str(weeknumber) + '.csv'
    curr_willys_path = './output/willys_promos_w' + str(weeknumber) + '.csv'
    curr_coop_path = './output/coop_promos_w' + str(weeknumber) + '.csv'

    
    hemkop_list = fetch_csv_data(curr_hemkop_path)
    hemkop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))]
    

    coop_list = fetch_csv_data(curr_coop_path)
    coop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))] 
    
    willys_list = fetch_csv_data(curr_willys_path)
    willys_header = ['column' + str(x) for x in range(len(willys_list[0]))]

    
    table_header = ['Vara', 'Pris', 'Beskrivning']

    #Create table elements
    hemkop_table = create_table(hemkop_list)
    coop_table = create_table(coop_list)
    willys_table = create_table(willys_list)
    
    #Build titled columns 
    willys_column = sg.Column([[sg.Text("WILLY:S", font =store_title_font, key='-Willys-')], 
                                [willys_table]], vertical_alignment='top')
    hemkop_column = sg.Column([[sg.Text('Hemköp', font=store_title_font, key='-Hemköp-')], 
                                [hemkop_table]], vertical_alignment='top')
    coop_column = sg.Column([[sg.Text('Coop', font=store_title_font, key= '-Coop-')], 
                                [coop_table]], vertical_alignment='top')

    #Button functionality
    prev_button = sg.Button("Previous week")
    next_button = sg.Button("Next week")
    stats_button = sg.Button("Stats...")

    #Assemble layout
    layout = [[sg.Text('Rabatter vecka ' + str(weeknumber) + ' ' + str(year), font=title_font), prev_button, next_button, stats_button],
        [willys_column, hemkop_column, coop_column]
    ]
    return layout

def main():

    # sg.set_options(auto_size_buttons=True)
    
    # curr_hemkop_path = './output/hemkop_promos_w' + str(weeknumber) + '.csv'
    # curr_willys_path = './output/willys_promos_w' + str(weeknumber) + '.csv'
    # curr_coop_path = './output/coop_promos_w' + str(weeknumber) + '.csv'

    
    # hemkop_list = fetch_csv_data(curr_hemkop_path)
    # hemkop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))]
    

    # coop_list = fetch_csv_data(curr_coop_path)
    # coop_header = ['column' + str(x) for x in range(len(hemkop_list[0]))] 
    
    # willys_list = fetch_csv_data(curr_willys_path)
    # willys_header = ['column' + str(x) for x in range(len(willys_list[0]))]

    # global store_title_font
    # store_title_font = ('Helvetica', 17)

    # title_font = ('Helvetica', 25, 'bold')
    # table_header = ['Vara', 'Pris', 'Beskrivning']

    # #Create table elements
    # hemkop_table = create_table(hemkop_list)
    # coop_table = create_table(coop_list)
    # willys_table = create_table(willys_list)
    
    # #Build titled columns 
    # willys_column = sg.Column([[sg.Text("WILLY:S", font =store_title_font)], 
    #                             [willys_table]], vertical_alignment='top')
    # hemkop_column = sg.Column([[sg.Text('Hemköp', font=store_title_font)], 
    #                             [hemkop_table]], vertical_alignment='top')
    # coop_column = sg.Column([[sg.Text('Coop', font=store_title_font)], 
    #                             [coop_table]], vertical_alignment='top')

    # #Button functionality
    # prev_button = sg.Button("Previous week")
    # next_button = sg.Button("Next week")
    # stats_button = sg.Button("Stats...")

    # #Assemble layout
    # layout = [[sg.Text('Rabatter vecka ' + str(weeknumber) + ' ' + str(year), font=title_font), prev_button, next_button, stats_button],
    #     [willys_column, hemkop_column, coop_column]
    # ]
    global layout
    layout = create_layout()
    window = sg.Window('DiscScrape', layout, size=(1200,700 ), grab_anywhere=True)
    while True:
        event, values = window.read()
        print(event, values)
        if event == "Previous week":
            try:
                new_layout = step_week(-1)
                window.close()
                window = sg.Window('DiscScrape', new_layout, size=(1200,700 ), grab_anywhere=True)
            except TypeError: 
                sg.popup("CSV don't exist")
            except: 
                sg.popup("Error")
        if event == "Next week":
            new_layout = step_week(1)
            window.close()
            window = sg.Window('DiscScrape', new_layout, size=(1200,700 ), grab_anywhere=True)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()

main()