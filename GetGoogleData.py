# 20170127 StevenWang
import pandas as pd
from urllib.request import urlopen

def fetch_google_data(file_name, ticker, days, interval):
    '''Get requested google finance data and store it as text in designated file.'''
    URL =  "https://www.google.com/finance/getprices?i=" + str(interval) + "&p=" + str(days) + "d&f=d,o,h,l,c,v&df=cpct&q=" + ticker
    response = urlopen(URL)
    with open(file_name, "w") as outfile:
        outfile.write(response.read().decode("ascii"))

def read_google_data(file_name):
    '''Read google finance data from a file and return a pandas dataframe'''
    start = 0
    my_data = pd.DataFrame(columns=['DATE', 'CLOSE', 'HIGH', 'LOW', 'OPEN', 'VOLUME'])

    with open(file_name, encoding="utf-8") as infile:

        # skiper the header
        for c in range(7):
            headers = infile.readline()
            if "INTERVAL" in headers:
                interval = int(headers[9:].rstrip())

        i = 0
        for line in infile:
            my_list = line.rstrip().split(',')
            
            # timestamping every entry
            if len(my_list[0]) > 10:
                start = int(my_list[0][1:11])
                my_list[0] = int(my_list[0][1:11])
            else:
                my_list[0] = (start + int(my_list[0])*int(interval))

            my_data.loc[i] = my_list
            i = i + 1
    return my_data



