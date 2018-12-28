# coding=utf-8
import six
import unicodedata

if six.PY3:
    UNICODE = str
    UTF8 = bytes
elif six.PY2:
    UNICODE = unicode
    UTF8 = str
else:
    raise ValueError("Not running on Python2 or Python 3?")

ENCODING = ["utf8", "gbk", "gb2312", "gb18030"]


class PrepareData(object):
    """
    该类含有常规文本预处理方法和文本通用方法
    clean_text有如下步骤组成:
        1. 统一将文本转换为unicode编码  convert_to_unicode
        2. 标准化所有文本  standard_text
        3. 去除重音标志  strip_out_accents
        4. 去除控制类字符, 用空格替代空白符号以及\n \r \t常用符号
    is_chinese_char  判定字符是否为中文字符
    is_punctuation  判定字符是否为标点符号

    """
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        """
        常规文本第一轮预处理, 遍历文本的每一个字符, 针对字符预处理
        1. 先判定是否是不可见空白符号,和特殊字符
        2. 判定是否为控制类字符, "\t"之类的例外
        3. 判定是否为空白符, 用" "代替
        """
        text = self.convert_to_unicode(self.text)
        text = self.standard_text(text)
        text = self.strip_out_accents(text)
        output = []
        for char in text:
            cp = ord(char)
            if cp == 0 or cp == 0xfffd or self.is_control(char):  # 0: 不可见空白符, 0xfffd: �, 即特殊符号
                continue
            if self.is_whitespace(char):
                output.append(" ")
            else:
                output.append(char)
        return "".join(output)

    @staticmethod
    def convert_to_unicode(text):
        """
        将文本转换为unicode编码
        python3  str  bytes
        python2 str utf8 gbk gb2312 gb18030
        """
        if isinstance(text, UNICODE):
            return text
        if isinstance(text, UTF8):
            for _encode in ENCODING:
                try:
                    return text.decode(_encode, errors="strict")
                except UnicodeDecodeError:
                    continue
        raise ValueError("encoding type not exists in: %s" % ",".join(ENCODING))

    @staticmethod
    def standard_text(text):
        """
        将unicode文本标准化,NFC/NFD均可  如下两自负代表同一个Spicy Jalapeño:
        s1 = 'Spicy Jalape\u00f1o'
        s2 = 'Spicy Jalapen\u0303o'
        """
        return unicodedata.normalize("NFD", text)

    @staticmethod
    def is_whitespace(char):
        """
        判定是否为空白字符
        \r \n \r 虽然为控制类字符, 我们通常当作空白字符处理
        Zs 为space类字符, 即空白符
        """
        if char == " " or char == "\t" or char == "\n" or char == "\r":
            return True
        cat = unicodedata.category(char)
        if cat == "Zs":
            return True
        return False

    @staticmethod
    def is_control(char):
        """
        判断是否为控制类别符号
        \r \n \r常当作空白符处理
        C 为Control等控制类符号
        """
        if char == "\t" or char == "\n" or char == "\r":
            return False
        cat = unicodedata.category(char)
        if cat.startswith("C"):
            return True
        return False

    @staticmethod
    def strip_out_accents(text):
        """
        消除重音标记, 例如: é  >> e
        """
        output = []
        for char in text:
            cat = unicodedata.category(char)
            if cat == "Mn":
                continue
            output.append(char)
        return "".join(output)

    @staticmethod
    def is_chinese_char(char):
        """
        判定是否为CJK字符  中文/朝鲜/日本...
        """
        char_ascii = ord(char)
        if (
                (0x4E00 <= char_ascii <= 0x9FFF) or (0x3400 <= char_ascii <= 0x4DBF) or (
                0x20000 <= char_ascii <= 0x2A6DF) or
                (0x2A700 <= char_ascii <= 0x2B73F) or (0x2B740 <= char_ascii <= 0x2B81F) or (
                0x2B820 <= char_ascii <= 0x2CEAF) or
                (0xF900 <= char_ascii <= 0xFAFF) or (0x2F800 <= char_ascii <= 0x2FA1F)):
            return True

        return False

    @staticmethod
    def is_punctuation(char):
        """
        判断是否为标点符号  ^ $ ` 作为标点符号处理
        """
        char_ascii = ord(char)
        if (
                (33 <= char_ascii <= 47) or (58 <= char_ascii <= 64) or (91 <= char_ascii <= 96) or
                (123 <= char_ascii <= 126)):
            return True
        cat = unicodedata.category(char)
        if cat.startswith("P"):
            return True
        return False


if __name__ == "__main__":
    pd = PrepareData("你好 \u00f1 \n, Spicy Jalapeño， Hello\tworld")
    print(pd.clean_text())
