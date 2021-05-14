
from datetime import datetime, timedelta

def convert_time():
    duration = int(input('Ведите промежуток времени в секундах '))
    sec = timedelta(seconds=duration)
    res = datetime(1, 1, 1) + sec

    result = ""

    if duration <= 60:
        result = '{} сек'.format(duration)
    elif duration >= 60 and duration <= 3599:
        result = '{0} мин {1} сек'.format(res.minute, res.second)
    elif duration >= 35600 and duration <= 86399:
        result = '{0} час {1} мин {2} сек'.format(res.hour, res.minute, res.second)
    elif duration >= 86400 and duration <= 604799:
        result = '{0} день {1} час {2} мин {3} сек'.format(res.day - 1, res.hour, res.minute, res.second)
    elif duration >= 604800 and duration <= 2629742:
        result = '{0} мес {1} день {2} час {3} мин {4} сек'.format(res.month, res.day - 1, res.hour, res.minute, res.second)
    elif duration >= 2629742 and duration <= 31556925:
        result = '{0} год {1} мес {2} день {3} час {4} мин {5} сек'.format(res.year, res.month, res.day - 1, res.hour, res.minute, res.second)

    return result


print(convert_time())
