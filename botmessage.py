import pyupbit
import telepot
import datetime
import time

access = "iTQthqW1iVimROXhZyL3JCd8M0CGhxP8l5qiGMZe"
secret = "W6eIJwzIC9UtR8e9ukQgN79d70ePIbcpUJOPfU49"
upbit = pyupbit.Upbit(access, secret)

token = "1508570773:AAHPyymSrNoJYhlfCmeVyEsazfa7YI_o1nE"
mc = "1597576562"
bot = telepot.Bot(token)

while 0<1:
    dt = datetime.datetime.now()
    if (20 < int(dt.hour) <22) and (57 < int(dt.minute) < 59) :
        bot.sendMessage(mc,upbit.get_balance("KRW"))
        
    time.sleep(20)
