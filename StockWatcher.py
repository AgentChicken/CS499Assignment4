from __future__ import print_function
from yahoo_finance import *
from elasticsearch import *
from datetime import datetime
import time

amazon = Share("AMZN")
google = Share("GOOG")
apple = Share("AAPL")
ibm = Share("IBM")
microsoft = Share("MSFT")
intel = Share("INTC")
amd = Share("AMD")

stocks = [amazon, google, apple, ibm, microsoft, intel, amd]
stocksymbols = ["AMZN", "GOOG", "AAPL", "IBM", "MSFT", "INTC", "AMD"]
counter = 1


def main(counter):
    for i in range(stocks.__len__()):
        es = Elasticsearch(['http://search-cs499assignment4-1-jmjogfowz5kwm4lwi5zsoo2afi.us-west-2.es.amazonaws.com:80'])
        es.index(index='stockprices', doc_type='prices', id=counter, body={
            'symbol': stocksymbols[i],
            'name': stocks[i].get_name(),
            'price': float(stocks[i].get_price()),
            'change': float(stocks[i].get_change()),
            'tradetime': stocks[i].get_trade_datetime(),
            'retrievetime': datetime.now()
        })
        counter += 1
    time.sleep(30)
    main(counter)


if __name__ == '__main__':
    main(1)
