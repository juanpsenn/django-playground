from openpyxl import Workbook
from io import BytesIO


def export_excel_report(title, header, data):
    # Create an instance of the Workbook class
    wb = Workbook()

    # Add a sheet to the workbook
    ws = wb.active
    ws.title = title

    # Write some data to the sheet
    ws.append(header)
    for row in data:
        ws.append(row)

    # Save the workbook to a BytesIO object
    output = BytesIO()
    wb.save(output)
    # 0110111000111
    # ^
    # Seek to the beginning of the file
    output.seek(0)

    return output
