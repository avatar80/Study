from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime
from pytz import timezone


url = 'http://info.finance.naver.com/marketindex/?tabSel=exchange#tab_section'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
usd = soup.find('span', {'class':'value'}).contents
cur_usd = usd[0].replace(',', '')[:4]

cur_time = datetime.now(timezone('Asia/Seoul')) #현재 시간 가져옴

#이전 USD 값 확인
with open('usdkor.txt', 'r') as wonDollor:
    last_usd = int(wonDollor.readline().strip()[:4])

if int(cur_usd) != int(last_usd) :
    with open('usdkor.txt', 'w') as wonDollor:
        wonDollor.write(cur_usd)
        printWonDollor = 'WON-DOLLAR ' + usd[0] + ' (KOREAN TIME ' + cur_time.strftime("%H:%M:%S %m-%d-%y") + ')'
        print(printWonDollor)


