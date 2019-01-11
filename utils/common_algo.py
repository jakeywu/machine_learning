import jieba
import collections
from utils.prepare_data import PrepareData

en = """
You know, the large crowd roared in approval as Mark Knopfler played the first few bars of "Money for Nothing".
"""
ch = """
你知道的, 就像马克·诺弗勒早期演唱的歌曲《金钱无用》一样，绝大多数的人依然高呼赞成“金钱无用论”。
"""


class BPE(object):
    def __init__(self, op_num):
        assert isinstance(op_num, int)
        self.opNum = op_num

    @staticmethod
    def _count_words(space_words):
        """
        词频统计
        """
        return collections.Counter(space_words.split())

    @staticmethod
    def split_char(vocab_dict, endtag="-"):
        """
        分割字符, 末尾添加特殊标记
        """
        ch_vocab = dict()
        for k, v in vocab_dict.items():
            ch_vocab["".join([" " + _k for _k in k + endtag])] = v
        return ch_vocab

    @staticmethod
    def produce_symbol_pairs(vocab_dict):
        """
        或词所有字符对, 返回top1
        """
        pairs = dict()
        for k, v in vocab_dict.items():
            symbols = k.split()
            for i in range(len(symbols)-1):
                _k = (symbols[i], symbols[i+1])
                if _k in pairs.keys():
                    pairs[_k] += v
                else:
                    pairs[_k] = v
        if not pairs:
            return
        return sorted(pairs.items(), key=lambda x: x[1], reverse=True)[0][0]

    @staticmethod
    def merge_bigram(vocab_dict, most_pair):
        """
        合并常见字符
        """
        bigram = "".join(most_pair)
        merge_vocab = dict()
        for k, v in vocab_dict.items():
            k = k.replace(" ".join(most_pair), bigram)
            merge_vocab[k] = v
        return merge_vocab

    @staticmethod
    def word_segment(sentence, _jieba):
        if not _jieba:
            return sentence
        return " ".join(jieba.cut(sentence))

    def produce_bpe(self, sentence, _jieba=False):
        """
        Byte pair encoding
        """
        sentence = self.word_segment(sentence, _jieba)
        deal_sentence = []
        for char in sentence:
            if PrepareData.is_punctuation(char):
                deal_sentence.append(" ")
            deal_sentence.append(char)
        sentence = "".join(deal_sentence).lower()
        vocab_dict = self._count_words(sentence)
        vocab_dict = self.split_char(vocab_dict)
        for i in range(self.opNum):
            most_pair = self.produce_symbol_pairs(vocab_dict)
            if not most_pair:
                break
            vocab_dict = self.merge_bigram(vocab_dict, most_pair)

        return vocab_dict


if __name__ == "__main__":
    bpe = BPE(10)
    print(bpe.produce_bpe(en))
    print(bpe.produce_bpe(ch, _jieba=True))
