import requests 
import json
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=5NUW7CKWG93NYG2M")
data = json.loads(response.text)
print data['Meta Data']['5. Time Zone']
