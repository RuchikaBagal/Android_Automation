import openpyxl

def read_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    first = True
    for row in sheet.iter_rows(values_only=True):
        if first:  # Skip header
            first = False
            continue
        if not row or len(row) < 3:
            continue
        data.append({
            "FromCity": row[0],
            "ToCity": row[1],
            "Date": row[2]
        })
    return data
