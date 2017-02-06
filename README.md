# GetGoogleData
A simple script that helps you get Google Finance data more easily.


## Obtain real-time quote from Google
This script provides real-time trading data with "negligible delay"(generally speaking).  

You need to specify 1 argument: **ticker**.  
**ticker** is a list of stock ticker(s).  

(a). `import GetGoogleData`

(a). Call function `GetGoogleData.real_time_quote(ticker)`  
    This will return a list of dictionary(ies).





## Get historical data from Google

You need to specify 4 arguments: **file name, ticker, days, interval**  
eg.:
```
file_name = "my_data.txt"
ticker = "IBM"
days = 10
interval = 60
```
For interval, the unit is second, and the smallest interval that Google will accept is 60 seconds.

(a). `import GetGoogleData`

(a). Call function `GetGoogleData.fetch_google_data(file_name, ticker, days, interval)`  
    This will create a webpage link and grab its data, then store the data in a text format file.

(a). Call function `GetGoogleData.read_google_data(file_name)`  
    This will read from a text format file and covert it into a pandas DataFrame.  
    Please note this will also change the `DATE` column into `int32 UNIX timstamp` in the DataFrame.

#### The function `fetch_google_data`is slow, PLEASE enlighten me for improvement!
#### What other functions do you think are needed?


