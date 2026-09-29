from flask import Flask, request, url_for, redirect, render_template
import requests
import json
import webbrowser
import os
import pandas as pd
import statistics
from book import *
from library import *
import openpyxl 

app = Flask(__name__)

# open spreadsheet and store locally
sample_sheet = "data/sample.xlsx"

target_folder = "data/"
file_name = "sample.xlsx"

created_ws = False

# check if workbook exits
try: 
    wb = openpyxl.load_workbook(sample_sheet)
    print(f"Workbook found: {sample_sheet}")
except FileNotFoundError:
    # create workbook
    wb = openpyxl.Workbook()
    created_ws = True
    print(f"Workbook not found. Created worksheet: {sample_sheet}")

sheet = wb.active() # open workbook

# make sure label is correct
if created_ws:
    # add labels to worksheet
    sheet.title = "Sample Sheet"
    sheet['A1'] = "title"
    sheet['B1'] = "author"
    sheet['C1'] = "year"
    sheet['D1'] = "publisher"
    sheet['E1'] = "series"
    sheet['F1'] = "book_num"
    sheet['G1'] = "date_started"
    sheet['H1'] = "date_finished"
    sheet['I1'] = "read_count"
    sheet['J1'] = "summary"
    sheet['K1'] = "ranking"

books = list() # will hold list of book
rows = sheet.max_row
cols = sheet.max_column

# go through sheet and update library
for i in range(2,rows+1):
    tmp_book = Book(
        sheet.cell(row=i, col=1),
        sheet.cell(row=i,col=2),
        sheet.cell(row=i, col=3),
        sheet.cell(row=i,col=4),
        sheet.cell(row=i, col=5),
        sheet.cell(row=i,col=6),
        sheet.cell(row=i, col=7),
        sheet.cell(row=i,col=8),
        sheet.cell(row=i, col=9),
        sheet.cell(row=i,col=10),
        sheet.cell(row=i, col=11)
    )

    books.append(tmp_book)

library = Library(books) # creates the library based off the books

# should save when app is closed or when client requsests save
def save(target_folder, file_name, wb):
    full_path = os.path.join(target_folder, file_name)
    wb.save(full_path)


@app.route('/')
def index():
    return render_template('index.html') 


if __name__ == '__main__':
    # reloader has not run yet, open browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("https://localhost:7777/login")

    app.run(port=7777, debug=True)