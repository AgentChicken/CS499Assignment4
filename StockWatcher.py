from __future__ import print_function
from yahoo_finance import *
from elasticsearch import *
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
        es = Elasticsearch(['http://search-cs499assignment4-u5u7mpa3siblnm74q2nzn2upia.us-west-2.es.amazonaws.com:80'])
        es.index(index='stockprices', doc_type='prices', id=counter, body={
            'symbol': stocksymbols[i],
            'name': stocks[i].get_name(),
            'price': stocks[i].get_price(),
            'change': stocks[i].get_change(),
            'tradetime': stocks[i].get_trade_datetime(),
            'time': time.time()
        })
        counter += 1
    time.sleep(30)
    main(counter)


if __name__ == '__main__':
    main(1)
