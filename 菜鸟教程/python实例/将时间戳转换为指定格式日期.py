import time
import datetime

# 获取当前时间时间戳
now = int(time.time())
# 转换为其他日期格式
time_array = time.localtime(now)
other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
print(other_style_time)


# 获取当前时间
now = datetime.datetime.now()
# 转换为指定格式
other_style_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(other_style_time)


# 指定时间戳
timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)


# 指定时间戳
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
