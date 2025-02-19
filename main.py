from pathlib import Path

import pandas as pd
import glob
import openpyxl
from fpdf import FPDF

filepaths = glob.glob("xlsx_files/*.xlsx")

for index, filepath in enumerate(filepaths):
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice_nr {invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")


