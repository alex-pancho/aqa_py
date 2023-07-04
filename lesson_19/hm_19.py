import time
from datetime import datetime

lines = [
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0300|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0240|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0120|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0090|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:00 Key TSTFEED0060|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0030|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:40 Key TSTFEED0020|7E3E|0400 TradePrice 5 TradeSize 0 }',
    '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:35 Key TSTFEED0015|7E3E|0400 TradePrice 5 TradeSize 0 }'
]
# dictionary to store last seen timestamps for each key
last_seen={}

def calc_time():
    prev_time=None
    for line in lines:
        timestamp=line.split ('Timestamp ')[1].split (' Key')[0]  # извлекаем метку времени из строки
        current_time=datetime.strptime (timestamp, "%H:%M:%S")  # преобразуем в объект datetime
        if prev_time is not None:
            diff=current_time - prev_time
            print (f"{prev_time.strftime ('%H:%M:%S')} -> {current_time.strftime ('%H:%M:%S')}: {diff}")  # выводим результат разницы
            prev_time=current_time

calc_time()