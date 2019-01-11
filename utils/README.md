#### [BPE压缩技术](https://plmsmile.github.io/2017/10/19/subword-units/)

##### Byte Pair Encoding算法步骤如下
1. 初始化符号词表。用所有的字符加入到符号词表中。对所有单词的末尾加入特殊标记，如-。翻译后恢复原始的标记。
2. 迭代对所有符号进行计数，找出次数最多的(A, B)，用AB代替。
3. 每次合并，会产生一个新的符号，代表着n-gram字符
4. 常见的n-grams字符(或者whole words)，最终会被合并到一个符号
5. 最终符号词表大小=初始大小+合并操作次数。操作次数是算法唯一的超参数。

##### [Demo实现](./common_algo.py)
```
python common_algo.py
```