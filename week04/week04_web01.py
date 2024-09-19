import urllib.request
import urllib.parse

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
station_id = input('지역 코드 : ')  # 전국 108, 수도권 109, 강원 105, 제주 184 ...
values = {'stnld' : station_id}

url = api + '?' + values

print(url)

"""
Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\uni\BigData2\week04\week04_web01.py", line 8, in <module>
    url = api + '?' + values
          ~~~~~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "dict") to str
"""