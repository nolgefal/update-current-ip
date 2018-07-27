import gspread
import time
import requests

from oauth2client.service_account import ServiceAccountCredentials

# check internet
def internet_on():
    try:
        global ip
        ip = requests.get('https://ipinfo.io/ip', timeout=1)
        return True
    except: 
        return False
    

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('current-ip.json', scope)

while True:
    if (internet_on()):        
        try:
            # credentials
            gc = gspread.authorize(credentials)
            sh = gc.open('current-ip')
        except gspread.SpreadsheetNotFound:
            # print('Sheet is not found')
            sh = gc.create('current-ip')
            sh.share('your_email_address', perm_type='user', role='writer')
            sh.share('your_friend_email_address', perm_type='user', role='writer')
            sh.sheet1.update_acell('A1', 'IP')
            sh.sheet1.update_acell('A2', str(ip.content))
        except:
            print("Can't authorize")
        
        try:            
            sh.sheet1.update_acell('A2', str(ip.content))
        except:
            print("Can't update cel now.")
    else:
        print("Your network is down. Please wait..")
        time.sleep(300) # wait 300s for network
        
    time.sleep(60) # update cell each 60s
                

