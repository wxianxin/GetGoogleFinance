# GetGoogleData
A simple script that helps you get Google Finance data more easily.
You need to specify four arguments: **file name, ticker, days, interval**
eg.:
```
file_name = "my_data.txt"
ticker = "IBM"
days = 10
interval = 60
```
For interval, the unit is second, and the smallest interval that Google will accept is 60 seconds.

1. Call function `GetGoogleData.fetch_google_data(file_name, ticker, days, interval)`:
	This will create a webpage link and grab its data, then store the data in a text format file.
2. Call function `read_google_data(file_name)`:
	This will read from a text format file and covert it into a pandas DataFrame.
	Please note this will also change the `DATA` column into `int32 UNIX timstamp` in the DataFrame.


## What other function do you think is needed?


