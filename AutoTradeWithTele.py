import time
import pyupbit
import datetime
import telepot

access = "H5eigvTP8YJejvDib9wO1JvEkExjTZ9g8TCoKsk1"
secret = "sFk8Hhn36wnuoJNRKuNrnxWNQw0F4QxqLzLxqAin"

token = "1508570773:AAHPyymSrNoJYhlfCmeVyEsazfa7YI_o1nE"
mc = "1597576562"
bot = telepot.Bot(token)

start_message = "pyupbit is working."
working_message = "It's Woring"
buy_message = "I just buy ETH"
sell_messge = "I just sell ETH"


def get_target_price(ticker, k):
    """volatility breakthrough strategy"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """Check the start time"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15 days of movement average check"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """Check the Balance"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """Current Price"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# Login
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# Start Message
bot.sendMessage(mc, start_message)

while 0<1:

    now = datetime.datetime.now()
    start_time = get_start_time("KRW-ETH")
    end_time = start_time + datetime.timedelta(days=1)

    if 54 < int(now.minute) < 56:
        bot.sendMessage(mc,working_message)

    if start_time < now < end_time - datetime.timedelta(seconds=10):
        target_price = get_target_price("KRW-ETH", 0.5)
        ma15 = get_ma15("KRW-ETH")
        current_price = get_current_price("KRW-ETH")
        if target_price < current_price and ma15 < current_price:
            krw = get_balance("KRW")
            if krw > 5000:
                buy_result = upbit.buy_market_order("KRW-ETH", krw*0.9995)
                bot.sendMessage(mc, buy_message)
    else:
        btc = get_balance("KRW-ETH")
        if btc > 0.00008:
            sell_result = upbit.sell_market_order("KRW-ETH", btc*0.9995)
            bot.sendMessage(mc, sell_messge)
    time.sleep(10)