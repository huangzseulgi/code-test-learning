# 森林运动会
# 对rabbit tortoise elephant wolf tiger bear等动物跑100m排名
import threading
import random
import time

ranking = []
distance = 10

def run_method(step, max_sleep_time):
    for i in range(distance):
        # todo: 获取当前进程
        t = threading.current_thread()
        if i % step == 0 and i != 0:
            sleep_time = random.randint(1, max_sleep_time)
            print("{}进入休眠：{}秒".format(t.name, sleep_time))
            time.sleep(sleep_time)
        print("{}跑的距离是：{}".format(t.name, i))

    ranking.append(t.name)
    print("{}完成了比赛".format(t.name))


# 兔子线程类
class RabbitThread(threading.Thread):
    def run(self) -> None:
        run_method(5, 4)


# 乌龟线程类
class TortoiseThread(threading.Thread):
    def run(self) -> None:
        run_method(1, 1)


# 大象线程类
class ElephantThread(threading.Thread):
    def run(self) -> None:
        run_method(2, 5)


# 狼线程类
class WolfThread(threading.Thread):
    def run(self) -> None:
        run_method(5, 2)


# 老虎线程类
class TigerThread(threading.Thread):
    def run(self) -> None:
        run_method(6, 2)

# 实例化所有线程类 此时可以对线程类命名
rabbit = RabbitThread(name="rabbit")
tortoise = TortoiseThread(name='tortoise')
elephant = ElephantThread(name='elephant')
wolf = WolfThread(name='wolf')
tiger = TigerThread(name='tiger')

rabbit.start()
tortoise.start()
elephant.start()
wolf.start()
tiger.start()

rabbit.join()
tortoise.join()
elephant.join()
wolf.join()
tiger.join()

print(ranking)
