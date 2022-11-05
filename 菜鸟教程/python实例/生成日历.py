import calendar
import datetime
yy = int(input('年份：'))  # 不用int，默认是str！！！
mm = int(input('月份：'))
print(calendar.month(yy, mm))   # 参数必须是int！！！

monthrange = calendar.monthrange(2015, 9)
print(monthrange)
# 输出的是一个元组
# 第一个元素是所查月份的第一天对应的是星期几（0-6）
# 第二个元素是这个月的天数

