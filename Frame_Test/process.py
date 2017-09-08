from time import ctime,sleep
import multiprocessing


def super_palyer(file, time):
    for i in range(time):
        print('Start playing:%s ! %s' % (file, ctime()))
        sleep(2)

play_list = {'爱情买卖': 2, '阿凡达': 2}
process = []

for file_name, time in play_list.items():
    p = multiprocessing.Process(target=super_palyer, args=(file_name, time))
    process.append(p)

if __name__ == '__main__':
    for p in process:
        p.start()
    for p in process:
        p.join()
    print('all finished')