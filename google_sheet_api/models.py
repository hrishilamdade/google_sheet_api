import gspread

gc= gspread.service_account(filename = "static\keys.json")

def get_data(sheet_id):
    sh=gc.open_by_key(sheet_id)
    worksheet=sh.sheet1
    res=worksheet.get_all_records()
    return res