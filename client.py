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

# check if workbook exits
try: 
    wb = openpyxl.load_workbook(sample_sheet)
    print(f"Workbook found: {sample_sheet}")
except FileNotFoundError:
    # create workbook
    wb = openpyxl.Workbook()
    print(f"Workbook not found. Created worksheet: {sample_sheet}")

sheet = wb.active() # open workbook

# go through sheet and update library


@app.route('/')
def index():
    return render_template('index.html') 


if __name__ == '__main__':
    # reloader has not run yet, open browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("https://localhost:7777/login")

    app.run(port=7777, debug=True)