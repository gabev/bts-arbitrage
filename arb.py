from bitshares.market import Market
import pandas as pd
import numpy as np
#from bitshares.price import Price


market = Market("BRIDGE.BTC:BTS")
market1 = Market("RUDEX.BTC:BTS")
market2 = Market("GDEX.BTC:BTS")
market3 = Market("EASYDEX.BTC:BTS")
market4 = Market("OPEN.BTC:BTS")

latest = (market.ticker())['latest']
latest1 = (market1.ticker())['latest']
latest2 = (market2.ticker())['latest']
latest3 = (market3.ticker())['latest']
latest4 = (market4.ticker())['latest']

print('CryptoBridge:'+ str(latest))
print('RuDex :'+ str(latest1))
print('GDEX :' + str(latest2))
print('EASYDEX :' + str(latest3))
print('OPENLEDGER :' + str(latest4))
print()

print('Arbitrage RuDex-BRIDGE:', (float(latest1))-(float(latest)), 'BTS')
print('Arbitrage GDEX-RuDex:', (float(latest2))-(float(latest1)), 'BTS')
print('Arbitrage GDEX-EasyDex:', (float(latest2))-(float(latest3)), 'BTS')

print()
data = market.ticker()
print(data)
print(list(data))

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#print ("dict['Name']: ", dict['Name'])
#print ("dict['Age']: ", dict['Age'])
print ("24H Volume:", data['quoteVolume'])
print ("% Change:", data['percentChange'])
print ("Price:", float(data['latest']),'BTS')
