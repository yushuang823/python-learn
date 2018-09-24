if __name__ == '__main__':
    from datetime import datetime, timedelta, timezone
    now = datetime.now()
    print(now)
    dt = datetime(2018, 9, 23, 19, 53)  # 指定时间
    print(dt)
    t = dt.timestamp()  # datetime转换为timestamp
    print(t)
    # timestamp转换为datetime
    # 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
    print(datetime.fromtimestamp(t))  # 本地时间
    print(datetime.utcfromtimestamp(t))  # UTC时间
    # str转换为datetime
    # 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
    # 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)
    # datetime转换为str
    # 转换方法是通过strftime()
    # 实现的，同样需要一个日期和时间的格式化字符串：'%a, %b %d %H:%M'
    print(now.strftime('%a, %b %d %H:%M'))
    # datetime加减
    print(now + timedelta(hours=2))
    print(now + timedelta(days=1, hours=1))
    print(now - timedelta(days=1))
    # 本地时间转换为UTC时间
    # 一个datetime类型有一个时区属性tzinfo，但是默认为None，
    # 所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    t=now.replace(tzinfo=tz_utc_8)    # 强制设置为UTC+8:00
    print(t)
# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# 拿到UTC时间，并强制设置时区为UTC+0:00:
    utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
# astimezone()将转换时区为北京时间:
    bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
 # astimezone()将转换时区为东京时间:
    dj_t=utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(dj_t)
# astimezone()将bj_dt转换时区为东京时间:
    dj_t_2=bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(dj_t_2)
# 练习题
# 假设你获取了用户输入的日期和时间如2015 - 1 - 219: 01:30，
# 以及一个时区信息如UTC + 5: 00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    dt_tz=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc_get=re.match(r'UTC([+-]\d{1,2}):00$',tz_str)
    print(utc_get.group(1))
    day_get=timezone(timedelta(hours=int(utc_get.group(1))))
    dt_tz=dt_tz.replace(tzinfo=day_get)
    return dt_tz.timestamp()
# 测试:
if __name__ == '__main__':

     t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
     print(t1)

     t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
     print(t2)






