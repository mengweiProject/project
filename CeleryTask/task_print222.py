import sys
from time import sleep

sys.path.append("../..")
sys.path.append("..")

from CeleryTask import app

@app.task
def print222(i):
    sleep(20)
    print('本次计算耗时10s，结果为：', i)

@app.task
def main_calc():
    print('我是主函数，任务发布函数')
    for i in range(100):
        print222.delay(i)
    print('end...')

if __name__ == '__main__':
    main_calc.delay()