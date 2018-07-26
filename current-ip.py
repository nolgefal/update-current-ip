import gspread
import time
import requests

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('current-ip-791006403458.json', scope)

gc = gspread.authorize(credentials)
url = '<your-googlesheet-link>'
wks = gc.open_by_url(url).sheet1
wks.update_acell('A1', 'IP')
print(url)

while True:
    res = requests.get('https://ipinfo.io/ip')
    wks.update_acell('A2', str(res.content))
    time.sleep(60) #update each 60s