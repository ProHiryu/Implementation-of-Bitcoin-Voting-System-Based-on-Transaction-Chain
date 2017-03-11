# Implementation-of-Bitcoin-Voting-System-Based-on-Transaction-Chain

My Graduate Project

> 由于bitcoin core的数据还在下载，所以今天的主要目的就是利用api等各种获取数据的方法，对近期产生的交易稍微做一些分析，主要之前有一些这方面的经验，做起来应该会比较顺利

# resources

> 列出两个主要网络的API

- [block meta]("https://blockmeta.com/docs#id_s1_s2-4")
- [block chain]("https://blockchain.info/zh-cn/api/blockchain_api")

一些将要使用的API会在下面列出来

# blockchain python api

> [python_blockchain]("https://github.com/blockchain/api-v1-client-python")

```python
pip install blockchain
```

利用GitHub上这个开源库可以很顺利地得到一些信息

调用测试过程中出现了一个很严重的问题：

![]("/image/error1.png")

**_最后证明这个问题的来源是我的脚本文件名字也是blockchain.py，所以系统会直接从这个文件夹当中去寻找blockexplorer，将名字改了就没事了，哇，弄了一上午终于发现了这个愚蠢的问题，我感觉自己很傻_**

## objects

### Block

```
hash : str
version : int
previous_block : str
merkle_root : str
time : int
bits : int
fee : int
nonce int
n_tx : int
size : int
block_index : int
main_chain : bool
height : int
received_time : int
relayed_by : string
transactions : array of Transaction objects
```

### Transaction

```
double_spend : bool
block_height : int (if -1, the tx is unconfirmed)
time : int
relayed_by : str
hash : str
tx_index : int
version : int
size : int
inputs : array of Input objects
outputs: array of Output objects
```

### Input

```
n : int
value : int
address : str
tx_index : int
type : int
script : str
script_sig : str
sequence : int
```

Note: if coinbase transaction, then only script and script_siq will be populated.

### Output

```
n : int
value : int
address : str
tx_index : int
script : str
spent : bool
```

### Address

```
hash160 : str
address : str
n_tx : int
total_received : int
total_sent : int
final_balance : int
transactions : array of Transaction objects
```

### UnspentOutput

```
tx_hash : str
tx_index : int
tx_output_n : int
script : str
value : int
value_hex : str
confirmations : int
```

### LatestBlock

```
hash : str
time : int
block_index : int
height : int
tx_indexes : array of TX indexes (integers)
```

### SimpleBlock

```
height : int
hash : str
time : int
main_chain : bool
```

### InventoryData

```
hash : str
type : str
initial_time : int
initial_ip : str
nconnected : int
relayed_count : int
relayed_percent : int
```

# 执行过程

通过下面这段代码可以得到最近一个区块当中的交易输入输出的数据，这里出现了一个错误就是无论怎么调用属性都会报错，显示input类当中没有这种属性，事实上很可能存在没有input的交易过程，output就不存在这种问题，之前遇到过这种问题，所以加一个try语句顺利解决报错

```python
latest_block = blockexplorer.get_latest_block()

block = blockexplorer.get_block(latest_block.hash)
transactions = []

transactions = block.transactions

for transaction in transactions:
    inputs = transaction.inputs
    outputs = transaction.outputs
    for ip in inputs:
        try:
            print('- - - - -' + ip.address)
        except AttributeError:
            print ('')
    for op in outputs:
        print (op.address)
```

初步能得到一些交易区块上的数据，后续需要通过一些可视化的过程将其展示出来

在运行过程中出现以下错误：

```python
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "blockchain_test.py", line 19, in <module>
    latest_block = blockexplorer.get_latest_block()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/blockchain/blockexplorer.py", line 100, in get_latest_block
    response = util.call_api(resource)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/blockchain/util.py", line 25, in call_api
    response = urlopen(base_url + resource, payload, timeout=TIMEOUT).read()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 163, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 466, in open
    response = self._open(req, data)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 484, in _open
    '_open', req)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 444, in _call_chain
    result = func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1297, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1256, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
```

查阅资料发现应该是网络问题，尝试ping blockchain.com发现并不能ping通，所以应该是代理出现了问题，稍微等一会

- atom turn off key board resolver --- cmd + .
- get unique elements in list --- set function

dict sorted:

```python
last = sorted(results.items(), key=lambda t: t[1], reverse=True)
# get tuple back
```

关于格林尼治时间戳的转换很简单，只需要调用time和datetime库就可以了，但是有一个问题，在发送API数据的时候，无论如何都得不到对应当天的blocks，最后我通过对比[网站]("https://blockchain.info/blocks/1487928323455")上不同天数对应的时间戳最后得到相应形式，就是：

'xxxx-xx-xx 17:25:23'

部分代码如下：

```python
str_start_time = str_start_time_init[0:10] + ' 17:25:23'
str_end_time = str_end_time_init[0:10] + ' 17:25:23'


print('The time: ',str_start_time+ ' - ',str_end_time)

tuple_start_time = time.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
tuple_end_time = time.strptime(str_end_time, '%Y-%m-%d %H:%M:%S')

unix_start_time = int(time.mktime(tuple_start_time))
unix_end_time = int(time.mktime(tuple_end_time))

print(unix_end_time, unix_start_time)
```

调用的是：

```python
blockexplorer.get_blocks()
```
