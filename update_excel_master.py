import pandas as pd

#read the current file and update other files
workbook=pd.read_excel( "C:\Users\suma4\Downloads\P1 White Coat Students 2023.xlsx")
updateFile=pd.read_excel("C:\Users\suma4\Downloads\P1 White Coat Students 2023.xlsx")

updateFile['PROFIT']= updateFile["REVENUE"]- updateFile['COGS']

workbook= pd.concat([workbook, updateFile])

workbook.to_excel('"C:\Users\suma4\Downloads\P1 White Coat Students 2023.xlsx"')