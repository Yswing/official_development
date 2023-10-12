import time
import winsound

def focus_timer(total_time, work_interval, break_interval):
    while total_time > 0:
        print("Work for {} minutes".format(work_interval))
        time.sleep(work_interval * 60)
        total_time -= work_interval

        if total_time > 0:
            winsound.Beep(500, 1000)  # 提醒声音

        print("Take a break for {} minutes".format(break_interval))
        time.sleep(break_interval * 60)
        total_time -= break_interval

        if total_time > 0:
            winsound.Beep(500, 1000)  # 提醒声音

    print("Focus timer complete!")

if __name__ == "__main__":
    total_time = int(input("输入总时间（分钟）: "))
    work_interval = int(input("输入工作时间（分钟）: "))
    break_interval = int(input("输入休息时间（分钟）: "))
    
    focus_timer(total_time, work_interval, break_interval)
