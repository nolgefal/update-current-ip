import gspread
import time
import requests

from oauth2client.service_account import ServiceAccountCredentials

# update ip to wordsheet
def update_cel(wordsheet):
    res = requests.get('https://ipinfo.io/ip')
    wordsheet.update_acell('A2', str(res.content))
    
# check internet
def internet_on():
    try:
        requests.get('http://216.58.192.142', timeout=1)
        return True
    except: 
        return False

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('current-ip.json', scope)

url = 'https://docs.google.com/spreadsheets/d/1k9pT0QNiz_wuILLgG9O7p_40IWSRjN8nn62f0XEvPEk/edit?usp=sharing'
print(url) # google sheet

if (internet_on()):
    try:
        gc = gspread.authorize(credentials)
        # sh = gc.create('current-ip') # create sheet-name current-ip

        # open link of wordsheet
        
        wks = gc.open_by_url(url).sheet1
        wks.update_acell('A1', 'IP')
        print("Updated at: %s" %time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
    except:
        print("Can't connect wordsheet now.")

while True:
    if (internet_on()):
        try:
            update_cel(wks)
        except:
            print("Can't update cel now.")
    else:
        print("Your network is down. Please wait..")
        time.sleep(300) # wait 300s for network
        
    time.sleep(60) # update cell each 60s
                

