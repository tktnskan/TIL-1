"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=837
"""
import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'
got = requests.get(URL)

print(got)

key = 'bb642f0cb96ebaeee948e4492b2aea19'
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt=20190113'