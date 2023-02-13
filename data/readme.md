#Data section

In the section, the code to extract historical data (k-lines) from the Binance (+a sample of data, 
preferably) will be included.

Usage: 

1. Download the data from Binance api endpoint using below guide:
    # -h	show help messages
    # -s	Single symbol or multiple symbols separated by space
    # -y	Single year or multiple years separated by space
    # -m	Single month or multiple months separated by space
    # -d	single date or multiple dates separated by space
    # -startDate	Starting date to download in [YYYY-MM-DD] format
    # -endDate	Ending date to download in [YYYY-MM-DD] format
    # -folder	Directory to store the downloaded data
    # -c	1 to download checksum file, default 0
    # -i	single kline interval or multiple intervals separated by space
    # -t	Trading type: spot, um (USD-M Futures), cm (COIN-M Futures)

    # e.g download ETHUSDT BTCUSDT BNBBUSD kline of 1 week interval from year 2020, month of Feb and Dec with CHECKSUM file:
    # python3 download-kline.py -s ETHUSDT BTCUSDT BNBBUSD -i 1w -y 2020 -m 02 12 -c 1

    # eg. download ETHUSDT kline from 2020-01-01 to 2021-02-02 with the interval of 1 day to directory /Users/bob/Binance:
    # python3 download-kline.py -s BTCUSDT -startDate 2021-09-01 -endDate 2021-09-30 -folder '/Users/bob/Binance' -i 1d
    
2. Extract downloaded data using ~ python3 data_extract.py 
    (change the destination path to the downloaded data's folder, and source to the preferred path)
