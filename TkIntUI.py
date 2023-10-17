import tkinter as tk
from tkinter import ttk
import pandas as pd

def get_store_path(store_id,weeknumber):
    return './output/' + str(store_id) + '_promos_w' + str(weeknumber) + '.csv'

def get_store_values(store_id,weeknumer):
    path = get_store_path(store_id, weeknumer)
    df = pd.read_csv(path, sep=',', engine='python', header=None)
    data = df.values.tolist()               # read everything else into a list of rows
    return data

    def populate_column(tree):pass
def update_prices(weeknumber):
    # Fetch and update price data from CSV files or other sources.
    # You can load CSV data into the tables here.
    # For this example, let's assume you have loaded data into 'store_data'.
    
    store_data = []
    for store in store_ids:
        store_data.append(get_store_values(store, weeknumber))

    # Clear existing data in the tables
    for tree in [store1_tree, store2_tree, store3_tree]:
        tree.delete(*tree.get_children())

    # Populate the tables with the new data
    for i, store_items in enumerate(store_data):
        for item_data in store_items:
            if i == 0:
                store1_tree.insert("", "end", values=item_data)
            elif i == 1:
                store2_tree.insert("", "end", values=item_data)
            elif i == 2:
                store3_tree.insert("", "end", values=item_data)


# --MAIN--
# Create the main window
root = tk.Tk()
root.title("DiscScrape 2.0")

# Create a 3x2 grid to hold the tables for the three stores
for j in range(2):
    root.rowconfigure(j, weight=1)  # Make each row expandable
    for i in range(3):
        root.columnconfigure(i, weight=1)  # Make each column expandable
        

#Store IDs, used to fetch CSV data and label the tables
store_ids = ['willys', 'hemkop', 'coop']


# Create tables (Treeview widgets) for each store
column_names = ("Vara", "Pris/Rabatt", "Beskrivning")
store1_tree = ttk.Treeview(root, columns=column_names, show="headings")
store2_tree = ttk.Treeview(root, columns=column_names, show="headings")
store3_tree = ttk.Treeview(root, columns=column_names, show="headings")

# Set column headings
for tree in [store1_tree, store2_tree, store3_tree]:
    tree.heading(column_names[0], text=column_names[0])
    tree.heading(column_names[1], text=column_names[1])
    tree.heading(column_names[2], text=column_names[2])

# Grid layout for tables
store1_tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
store2_tree.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
store3_tree.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Create a "Refresh" button
refresh_button = tk.Button(root, text="Refresh", command=update_prices)
refresh_button.grid(row=1, column=0, columnspan=3)

# Initialize the application by fetching and displaying initial data
update_prices(40)

# Configure the rows to expand vertically as the window is resized
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

# Start the Tkinter main loop
root.mainloop()
