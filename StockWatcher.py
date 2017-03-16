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
amd = Share("AMD")

stocks = [amazon, google, apple, ibm, microsoft, amd]
stocksymbols = ["AMZN", "GOOG", "AAPL", "IBM", "MSFT", "AMD"]
counter = 1

es = Elasticsearch(
                ['http://search-cs499assignment4-2-6rirx5boxmskqfjrhmfdkodj2q.us-west-2.es.amazonaws.com:80'])

def main(counter):
    for i in range(stocks.__len__()):
        try:
            es.index(index='stockprices', doc_type='prices', id=counter, body={
                'symbol': stocksymbols[i],
                'name': stocks[i].get_name(),
                'price': float(stocks[i].get_price()),
                'change': float(stocks[i].get_change()),
                'tradetime': stocks[i].get_trade_datetime(),
                'retrievetime': datetime.now()
            })
            stocks[i].refresh()
            counter += 1
            print({
                'symbol': stocksymbols[i],
                'name': stocks[i].get_name(),
                'price': float(stocks[i].get_price()),
                'change': float(stocks[i].get_change()),
                'tradetime': stocks[i].get_trade_datetime(),
                'retrievetime': datetime.now()
            })
        except TypeError:
            print("Type error!")
    time.sleep(30)
    main(counter)


if __name__ == '__main__':
    main(1)
