import time
import datetime

# 先获得时间数组格式的日期
three_day_ago = (datetime.datetime.now()-datetime.timedelta(days=3))
# 转换为时间戳
time_stamp = int(time.mktime(three_day_ago.timetuple()))
# 转换为其他字符串格式
other_style_time = three_day_ago.strftime("%Y-%m-%d %H:%M:%S")
print(other_style_time)


# 给定时间戳
time_stamp = 1557502800
date_array = datetime.datetime.utcfromtimestamp(time_stamp)
three_day_ago = date_array - datetime.timedelta(days=3)
print(three_day_ago)
