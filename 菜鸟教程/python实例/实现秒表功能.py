# 使用time模块实现秒表功能
import time
print('按下回车开始计时，按下 ctrl+c 停止计时。')

while True:
    input("")
    start_time = time.time()
    print("开始")
    try:
        while True:
            print('\r计时：', round(time.time() - start_time, 0), '秒', end="")  # 显示每秒变化
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n结束')  # 换行
        end_time = time.time()
        print("总共的时间为：", round(end_time - start_time, 2), 'secs')
        break
# CTRL + C 不起作用，？？？
