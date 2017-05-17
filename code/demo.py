#-*-coding:utf-8 -*-
import time
import random
from set_voters import set_voters


def demo():
    start_height = 452379
    end_height = 452385
    candidates = []
    votes = []
    voters = []
    candidate_selected = []
    inputs_address = []
    outputs_address = []

    voters_init = set_voters()

    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'r')

    for line in input_file.readlines():
        line = line.strip()
        inputs_address.append(line.split(' '))

    for line in output_file.readlines():
        line = line.strip()
        outputs_address.append(line.split(' '))

    candidate_file = open('candidates.txt', 'r')
    lines = candidate_file.readlines()
    can_num = len(lines)
    for line in lines:
        line = line.strip()
        [candidate, vote] = line.split(' : ')
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

    print('\n')
    print('共有{}名合法投票者\n'.format(voters_num))
    time.sleep(3)

    print('开始寻找对应的比特币区块区间\n')
    print('loading...')
    time.sleep(7)
    print('比特币区间高度为：{} - {}\n'.format(start_height, end_height))

    print('正在读取交易数据\n')
    time.sleep(1)

    print('开始统计票数')

    valid = 0
    invalid = 0

    total = len(inputs_address)

    for i in range(len(inputs_address)):
        if len(outputs_address[i]) > 1:
            # print('第{}条交易记录，多次输出，无效'.format(i + 1))
            # time.sleep(0.05)
            continue
        else:
            for address in inputs_address[i]:
                if address in voters_init:
                    if address not in voters:
                        if outputs_address[i][0] not in candidate_selected:
                            # print('该投票地址不是候选人')
                            # time.sleep(0.05)
                            continue
                        else:
                            print('候选人 {} 得到 {} 的1票'.format(
                                outputs_address[i][0], address))
                            voters.append(address)
                            time.sleep(0.05)
                            candidate_selected.append(outputs_address[i][0])
                            valid += 1
                    else:
                        pass
                        # print('该选民已经投过票了')
                        # time.sleep(0.05)
                else:
                    continue

    results = dict()

    for candidate in set(candidate_selected):
        results[candidate] = candidate_selected.count(candidate)

    last = sorted(results.items(), key=lambda t: t[1], reverse=True)

    print('\n最终的票结果为：')
    for (x, y) in last:
        print(x, ' : ', y)

    invalid = total - valid
    print('\n总票数为 : ', total, '\n有效票数为 : ',
          valid, '\n无效票数为 : ', invalid)


if __name__ == "__main__":
    demo()
