from time import ctime,sleep
import threading


# def music(func, loop):
#     for i in range(loop):
#         print('I am listening to %s ! %s' % (func, ctime()))
#         sleep(2)
#
#
# def movie(func, loop):
#     for i in range(loop):
#         print('I am watching %s ! %s' % (func, ctime()))
#
#
# threads = []
#
# t1 = threading.Thread(target=music, args=('爱情买卖', 2))
# threads.append(t1)
# t2 = threading.Thread(target=movie, args=('阿凡达', 2))
# threads.append(t2)


def super_player(func, loop):
    for i in range(loop):
        print('start playing %s ! %s' % (func, ctime()))

play_list = {'爱情买卖': 2, '阿凡达': 2}
threads = []
for name, times in play_list.items():
    t = threading.Thread(target=super_player, args=(name, times))
    threads.append(t)


if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end:%s' % ctime())