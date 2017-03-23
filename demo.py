#-*-coding:utf-8 -*-
import time
import random

def demo():
    start_height = 452379
    end_height = 452385
    candidates = []
    votes = []
    candidate_selected = []
    total = 13077
    valid = 6197
    invalid = 6880

    candidate_file = open('candidates.txt','r')
    lines = candidate_file.readlines()
    can_num = len(lines)
    for line in lines:
        line = line.strip()
        [candidate,vote] = line.split(' : ')
        candidates.append(candidate)
        votes.append(vote)

    candidate_file.close()

    voter_file = open('voters.txt', 'r')
    lines = voter_file.readlines()
    voters_num = len(lines)

    print('默认寻找时间为: 2017-02-10 15:10:00 至 2017-02-10 16:30:00\n')
    time.sleep(2)
    print('设置的十位候选人分别为：')
    time.sleep(1)

    for i in range(10):
        candidate = random.choice(candidates)
        candidate_selected.append(candidate)
        print(candidate)
        time.sleep(1)

    print('共有{}名合法投票者'.format(voters_num))
    time.sleep(3)

    print('开始寻找对应的比特币区块区间')
    print('loading...')
    time.sleep(7)
    print('比特币区间高度为：{} - {}\n'.format(start_height,end_height))

    print('正在读取交易数据')




if __name__ == "__main__":
    demo()
