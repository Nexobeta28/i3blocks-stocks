# constants
SYMBOL = "TSLA"
API_KEY = "your-api-key-here"

# imports
import urllib, json
from datetime import datetime, timedelta

# get data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=%s' % (SYMBOL, API_KEY)
response = urllib.urlopen(url)

# get date
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
dayBeforeYesterday = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')

#calculate
data = json.loads(response.read())['Time Series (Daily)']

yesterdayData = float(data[yesterday]['4. close'])
dayBeforeYesterdayData = float(data[dayBeforeYesterday]['4. close'])

percentage = round(((100 * yesterdayData) / dayBeforeYesterdayData) - 100, 2)

# print
print(SYMBOL + " (daily)" + ": " + str(percentage) + "%")
