# GetGoogleData
A simple script that helps you get Google Finance data more easily.
Place the script in desirable path(Usually the folder of codes).

## Obtain real-time quote from Google
This script provides real-time trading data with "negligible delay"(generally speaking).  

**ticker** is 'string'.  

1. `import GetGoogleData`

2. Call function `GetGoogleData.real_time_quote(ticker)`  
    This will return a list of dictionary(ies).

#### Sample in
```
ticker = "AMD"
GetGoogleData.real_time_quote(ticker)
```
#### Sample out
```
[{'Absolute Change': '-0.05',
  'Exchange': 'NASDAQ',
  'Internal Google Security ID': '327',
  'Last Price': '12.23',
  'Last Trade Date': 'Feb 3, 4:00PM EST',
  'Last Trade Date/Time': '2017-02-03T16:00:02Z',
  'Last Trade Time': '4:00PM EST',
  'Percentage Change': '-0.37',
  'Ticker': 'AMD'}]
```


## Get historical data from Google

4 arguments are required: **file name, ticker, days, interval**  
**file name, ticker** are 'string'; **days, interval** are 'int'.

For interval, the unit is second, and the smallest interval that Google will accept is 60 seconds.

1. `import GetGoogleData`

2. Call function `GetGoogleData.fetch_google_data(file_name, ticker, days, interval)`  
    This will create a webpage link and grab its data, then store the data in a text format file.

3. Call function `GetGoogleData.read_google_data(file_name)`  
    This will read from a text format file and covert it into a pandas DataFrame.  
    Please note this will also change the `DATE` column into `int32 UNIX timstamp` in the DataFrame.

**One can also achieve step 2&3 at the same time by calling:**  
`GetGoogleData.fetch_read_google_data(file_name, ticker, days, interval)`

#### Sample in
```
file_name = "my_data.txt"
ticker = "AMD"
days = 10
interval = 60
GetGoogleData.fetch_google_data(file_name, ticker, days, interval)
GetGoogleData.read_google_data(file_name)
```
or
```
file_name = "my_data.txt"
ticker = "AMD"
days = 10
interval = 60
GetGoogleData.fetch_read_google_data(file_name, ticker, days, interval)
```

#### Sample out
```
           DATE   CLOSE    HIGH     LOW    OPEN  VOLUME
0  1.485182e+09  9.6924  9.6924    9.68    9.68  260266
1  1.485182e+09    9.71    9.74    9.68    9.69   89222
2  1.485182e+09   9.765    9.77  9.7099  9.7199  105005
3  1.485182e+09    9.77    9.82    9.75  9.7699  233767
4  1.485182e+09    9.79    9.84    9.77    9.77  112415
......
3905  1.486155e+09   12.23  12.23  12.21  12.215   268370
3906  1.486155e+09   12.23  12.23  12.22  12.225   130856
3907  1.486155e+09   12.23  12.23  12.22   12.23   245933
3908  1.486156e+09  12.225  12.23  12.22  12.225   230239
3909  1.486156e+09  12.235  12.24  12.22  12.225  1654800
```

#### The function `fetch_google_data`is slow, PLEASE enlighten me for improvement!
#### What other functions do you think are needed?


