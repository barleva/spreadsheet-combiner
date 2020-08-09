import pandas as pd 
import numpy as np
import glob as gl

spreadsheets = []

for file in gl.glob("./*.xlsx"):
    spreadsheets.append(pd.read_excel(file))
    print("Appending: " + file)

new_file = "./combined_spreadsheet.xlsx"

if len(spreadsheets) > 0:
    spreadsheets = pd.concat(spreadsheets)
    spreadsheets.to_excel(new_file)
    print("Finished. Combined file stored at: " + new_file)
else:
    print("Failed to combine files.")
