from openpyxl import load_workbook


for year in range(2001, 2019):
    print(f"Processing year {year}")
    classes = list(map(str, range(1, 8)))
    if int(year) >= 2009:
        classes.append("3+")
        classes.append("4+")

    if(year == 2011):
        continue
    # Load up the year workbook and use the values calculated from the last time the workbook was opened(Rather than maintaining the formulas within each cell.)
    STOP = load_workbook(filename=f"{year} STOP Summary.xlsx", data_only=True)

    for class_num in classes:
        print(f"Removing class {class_num} formatted")
        try:
            STOP.remove(STOP[f"Class {class_num} Formatted"])
        except KeyError:
            print(
                f"KeyError: 'Worksheet Class {class_num} Formatted does not exist.'")
            continue

    # Better save if we want to see our changes
    STOP.save(f'{year} STOP Summary.xlsx')
