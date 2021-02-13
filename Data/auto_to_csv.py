from openpyxl import load_workbook

STOP_2001 = load_workbook(filename="2001 STOP Summary.xlsx", data_only=True)


Class_1 = STOP_2001["Class 1"]

for row in range(1,50):
    if (Class_1[f'C{row}'].value != None):
        print(Class_1[f'C{row}'])


Class_1_csv = STOP_2001.create_sheet("Class 1 csv")

cond_col = "A"
def yield_excel_cols(cond_col):
    new_col = ""
    if(len(cond_col)==1):
        if(str(chr(ord(cond_col[0])+1))=="["):
            new_col = "AA"
        else:
            new_col = str(chr(ord(cond_col[0])+1))
    else:
        if(str(chr(ord(cond_col[-1])+1))=="["):
            new_col = str(chr(ord(cond_col[0])+1)) + "A"
        else:
            new_col = cond_col[0] + str(chr(ord(cond_col[-1])+1))
    
    return new_col



for row in range(1,200):
    if (Class_1[f'C{row}'].value != None and row!=49):
        print(row, " : ", Class_1[f'C{row}'].value)
        Class_1_csv[f"{cond_col}2"] = Class_1[f'C{row}'].value
        cond_col = yield_excel_cols(cond_col)

STOP_2001.save('2001 STOP Summary.xlsx')

