# CS499Assignment4: A Stock Watcher
StockWatcher.py is a simple program that uploads stock price data for several tech companies, including Amazon,
Alphabet, and a few others, to AWS ES every 30 seconds. The program uses the Yahoo Finance API to grab stock data
and the official Elasticsearch library to interact with the ES instance.

The associated Kibana dashboard includes a table and bar graph representing the stock performances of each respective 
company, a line graph that represents the performances of the respective companies over time, and a line graph that 
plots the average change in stock prices with respect to prices themselves.
