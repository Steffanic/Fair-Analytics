from typing import Iterable
from openpyxl import load_workbook


def remove_rows(rows, sheet, wrkbk):
    try:
        iter(rows)
    except:
        wrkbk[sheet].delete_rows(rows)
        return
    for row in rows:
        wrkbk[sheet].delete_rows(row)

def remove_cols(cols, sheet, wrkbk):
    for col in cols:
        wrkbk[sheet].delete_cols(col)

def remove_cell(row, col, sheet, wrkbk):
    (wrkbk[sheet])[f'{col}{row}'].value=""

wrkbks = [load_workbook(filename=f"{year} STOP Summary.xlsx", data_only=True) for year in range(2001, 2019) if year != 2011]

# 2001 Manual Edits
remove_cell(4,"BD","Class 3 Formatted",wrkbks[0])

# 2002 
remove_cell(4,"BO","Class 4 Formatted",wrkbks[1])

# 2003
remove_cell(7,"BV","Class 5 Formatted",wrkbks[2])

# 2004
remove_rows(10, "Class 4 Formatted", wrkbks[3])

# 2005
remove_rows(21, "Class 2 Formatted", wrkbks[4])
remove_rows(4, "Class 5 Formatted", wrkbks[4])

# 2006
remove_rows(21, "Class 2 Formatted", wrkbks[5])
remove_rows(5, "Class 7 Formatted", wrkbks[5])

# 2007
remove_rows(19, "Class 3 Formatted", wrkbks[6])

# 2012
remove_rows(12, "Class 1 Formatted", wrkbks[10])
remove_rows(10, "Class 2 Formatted", wrkbks[10])
remove_rows(7, "Class 3 Formatted", wrkbks[10])
remove_rows(15, "Class 3+ Formatted", wrkbks[10])

# 2013
remove_rows(12, "Class 1 Formatted", wrkbks[11])
remove_rows(11, "Class 2 Formatted", wrkbks[11])
remove_rows(15, "Class 3+ Formatted", wrkbks[11])

# 2014
remove_rows(12, "Class 1 Formatted", wrkbks[12])
remove_rows(7, "Class 1 Formatted", wrkbks[12])
remove_rows(6, "Class 3 Formatted", wrkbks[12])
remove_rows(4, "Class 5 Formatted", wrkbks[12])
remove_cols([52,53-1,86-2], "Class 1 Formatted", wrkbks[12])
remove_cols([54,84-1], "Class 2 Formatted", wrkbks[12])
remove_cols([56,57-1,90-2], "Class 3 Formatted", wrkbks[12])
remove_cols([56,57-1,90-2], "Class 4 Formatted", wrkbks[12])
remove_cols([53,54-1,85-2], "Class 5 Formatted", wrkbks[12])
remove_cols([55,56-1,87-2], "Class 6 Formatted", wrkbks[12])
remove_cols([54,55-1,85-2], "Class 7 Formatted", wrkbks[12])
remove_cols([56,86-1], "Class 3+ Formatted", wrkbks[12])
remove_cols([55,56-1,87-2], "Class 4+ Formatted", wrkbks[12])


# 2015
remove_cols([57,58-1,89-2], "Class 1 Formatted", wrkbks[13])
remove_cols([56,57-1,88-2], "Class 2 Formatted", wrkbks[13])
remove_cols([56,57-1,88-2], "Class 3 Formatted", wrkbks[13])
remove_cols([56,57-1,88-2,89-3], "Class 4 Formatted", wrkbks[13])
remove_cols([57,58-1,90-2], "Class 5 Formatted", wrkbks[13])
remove_cols([57,58-1,90-2], "Class 6 Formatted", wrkbks[13])
remove_cols([57,58-1,90-2], "Class 7 Formatted", wrkbks[13])
remove_cols([56,57-1,88-2], "Class 3+ Formatted", wrkbks[13])
remove_cols([57,58-1,90-2], "Class 4+ Formatted", wrkbks[13])

# 2016
remove_rows(6, "Class 3 Formatted", wrkbks[14])
remove_cols([58,59-1,96-2], "Class 1 Formatted", wrkbks[14])
remove_cols([58,59-1,95-2], "Class 2 Formatted", wrkbks[14])
remove_cols([58,59-1,96-2], "Class 3 Formatted", wrkbks[14])
remove_cols([58,59-1,95-2,96-2], "Class 4 Formatted", wrkbks[14])
remove_cols([59,60-1,98-2], "Class 5 Formatted", wrkbks[14])
remove_cols([59,60-1,98-2], "Class 6 Formatted", wrkbks[14])
remove_cols([60,61-1,99-2], "Class 7 Formatted", wrkbks[14])
remove_cols([58,59-1,96-2], "Class 3+ Formatted", wrkbks[14])
remove_cols([2,59-1,60-2,98-3], "Class 4+ Formatted", wrkbks[14])

# 2017
remove_cols([59,60-1,97-2], "Class 1 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2], "Class 2 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2], "Class 3 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2,98-3], "Class 4 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2], "Class 5 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2], "Class 6 Formatted", wrkbks[15])
remove_cols([60,61-1,98-2], "Class 7 Formatted", wrkbks[15])
remove_cols([59,60-1,97-2], "Class 3+ Formatted", wrkbks[15])
remove_cols([59,60-1,98-2], "Class 4+ Formatted", wrkbks[15])

# 2018
remove_rows(6, "Class 3 Formatted", wrkbks[16])
remove_rows(6, "Class 7 Formatted", wrkbks[16])
remove_rows(2, "Class 4+ Formatted", wrkbks[16])
remove_cols([62,63-1,101-2], "Class 1 Formatted", wrkbks[16])
remove_cols([62,63-1,101-2], "Class 2 Formatted", wrkbks[16])
remove_cols([62,63-1,101-2], "Class 3 Formatted", wrkbks[16])
remove_cols([62,63-1,101-2,102-3], "Class 4 Formatted", wrkbks[16])
remove_cols([63,64-1,103-2], "Class 5 Formatted", wrkbks[16])
remove_cols([63,64-1,103-2], "Class 6 Formatted", wrkbks[16])
remove_cols([64,65-1,104-2], "Class 7 Formatted", wrkbks[16])
remove_cols([62,63-1,101-2], "Class 3+ Formatted", wrkbks[16])
remove_cols([2,63-1,6-2,103-3], "Class 4+ Formatted", wrkbks[16])

i=0
for year in range(2001, 2019):
    if year==2011:
        continue
    wrkbks[i].save(f"{year} STOP Summary.xlsx")
    i+=1
