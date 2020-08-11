# ***************************
# spreadsheet_combiner.py
# Author: Aaron Barlev
# Date created: Aug 10, 2020
# ***************************

import pandas as pd 
import numpy as np
import glob as gl

# Create array to store spreadsheet files
spreadsheets = []

# Add all .xlsx files in current directory to array
for file in gl.glob("./*.xlsx"):
    spreadsheets.append(pd.read_excel(file))
    print("Appending: " + file)

# Create path to store combined spreadsheet
new_file = "./combined_spreadsheet.xlsx"

# Concatenate spreadsheets into combined spreadsheet
if len(spreadsheets) > 0:
    spreadsheets = pd.concat(spreadsheets)
    spreadsheets.to_excel(new_file)
    print("Finished. Combined file stored at: " + new_file)
else:
    print("Failed to combine files.")
