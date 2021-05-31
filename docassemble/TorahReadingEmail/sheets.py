import gspread
import json
from docassemble.base.util import get_config, log
from oauth2client.service_account import ServiceAccountCredentials
credential_info = json.loads(get_config('google').get('service account credentials'), strict=False)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
__all__ = ['read_sheet','append_to_sheet','update_column_for_uuid']

def read_sheet(sheet_name, worksheet_index):
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    return sheet.get_all_records()

def append_to_sheet(sheet_name, vals, worksheet_index=0):
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    try:
        sheet.append_row(vals)
        response = True
    except: 
        response = False
    return response
  
def update_column_for_uuid(sheet_name, vals, column_number, row_uuid, worksheet_index=0):
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    cell = sheet.find(row_uuid)
    try: 
        sheet.update_cell(cell.row, column_number, vals)
        response = True
    except:
        response = False
    return response