import urllib.request
import urllib.parse

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
station_id = input('지역 코드 : ')  # 전국 108, 수도권 109, 강원 105, 제주 184 ...
values = {'stnld' : station_id}

parameters = urllib.parse.urlencode(values)
url = api + '?' + parameters

print(url)

