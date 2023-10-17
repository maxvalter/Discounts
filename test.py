import tkinter as tk
from tkinter import ttk
import pandas as pd
# Sample data for three stores as a list of lists
# Global store IDs

def get_store_path(store_id,weeknumber):
    return './output/' + str(store_id) + '_promos_w' + str(weeknumber) + '.csv'

def get_store_values(store_id,weeknumer):
    path = get_store_path(store_id, weeknumer)
    df = pd.read_csv(path, sep=',', engine='python', header=None)
    data = df.values.tolist()               # read everything else into a list of rows
    return data

def update_prices():
    # Fetch and update price data from the list of lists
    # You can load the data into the tables here
    # For this example, we assume you have already loaded data into 'store_data'

    for i, store_items in enumerate(store_data):
        # Clear existing data in the tables for each store
        for _, tree in store_frames:
            tree.delete(*tree.get_children())

        # Populate the tables with the new data for each store
        for item_data in store_items:
            _, tree = store_frames[i]
            tree.insert("", "end", values=item_data)

# Create the main window
root = tk.Tk()
root.title("Price Aggregator")

# Apply background color to the main window
root.configure(bg="#FFE4E1")

# Create a 3x1 grid to hold the tables for the three stores
for i in range(3):
    root.columnconfigure(i, weight=1)  # Make each column expandable

store_ids = ['willys', 'hemkop', 'coop']
weeknumber = 40

store_data = []
for store in store_ids:
    store_data.append(get_store_values(store, weeknumber))


# Create store labels and tables in separate frames for each store
store_frames = []
for i, store_id in enumerate(store_ids):
    frame = ttk.Frame(root, style="StoreFrame.TFrame")
    frame.grid(row=0, column=i, padx=5, pady=5)

    # Create store label with styling
    label = tk.Label(frame, text=store_id, font=("Georgia", 16, "bold"), bg="#FFA07A", fg="white")
    label.grid(row=0, column=0, padx=5, pady=5)

    # Create table (Treeview widget) for the store
    tree = ttk.Treeview(frame, columns=("Item", "Price", "Availability"), show="headings", style="Custom.Treeview")
    tree.grid(row=1, column=0, padx=5, pady=5)

    # Set column headings with styling
    tree.heading("Item", text="Item")
    tree.heading("Price", text="Price")
    tree.heading("Availability", text="Availability")

    # Styling for treeview rows
    tree.tag_configure("oddrow", background="#FFE4E1")
    tree.tag_configure("evenrow", background="#FFDAB9")

    store_frames.append((frame, tree))

# Create a "Refresh" button with styling
refresh_button = tk.Button(root, text="Refresh", command=update_prices, font=("Georgia", 14), bg="#FF6347", fg="white")
refresh_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Initialize the application by fetching and displaying initial data
update_prices()

# Configure the rows of store_frames to expand vertically as the window is resized
for frame, _ in store_frames:
    frame.rowconfigure(1, weight=1)

# Define the custom styles for frames and Treeview widgets
style = ttk.Style()
style.configure("StoreFrame.TFrame", background="#FFE4E1")
style.configure("Custom.Treeview.Heading", font=("Georgia", 12, "bold"))
style.configure("Custom.Treeview", font=("Georgia", 12))
style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

# Start the Tkinter main loop
root.mainloop()
