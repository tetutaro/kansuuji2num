#!/usr/bin/env python
# -*- coding:utf-8 -*-
__version__ = '0.1.1'

# 数字と判定する文字
_DIGIT_WORDS = set(
    '〇一二三四五六七八九十百千０１２３４５６７８９0123456789'
)
# 直前の文字が数字の場合に数字と判定する文字
_PLACE_WORDS = set('万億兆京,，')
# 小数点を表す文字
_DECIMAL_WORDS = set('.．')
# 漢数字を数字に変換するテーブル
_DIGIT_TRANS = str.maketrans(
    '〇一二三四五六七八九', '0123456789'
)


def _kan2num_by10(text: str) -> int:
    ret = ppos = 0
    places = '千百十'
    for i, p in enumerate(places):
        pos = text.find(p)
        if pos == -1:
            continue
        elif ppos == pos:
            block = 1
        else:
            block = int(text[ppos:pos].translate(_DIGIT_TRANS))
        ret += block * (10 ** (3 - i))
        ppos = pos + 1
    if ppos < len(text):
        ret += int(text[ppos:].translate(_DIGIT_TRANS))
    return ret


def _kan2num(text: str) -> int:
    ret = ppos = 0
    places = '京兆億万'
    text = text.translate(str.maketrans({',': None, '，': None}))
    for i, p in enumerate(places):
        pos = text.find(p)
        if pos == -1:
            continue
        else:
            block = _kan2num_by10(text[ppos:pos])
        ret += block * (10 ** (4 * (4 - i)))
        ppos = pos + 1
    if ppos < len(text):
        ret += _kan2num_by10(text[ppos:])
    return ret


def _add_num(digits, decimal_place) -> str:
    val = _kan2num(digits)
    if decimal_place > 0:
        if val == 0:
            return ''
        else:
            return '.' + str(val).zfill(decimal_place - 1)
    return str(val)


def kansuji2num(text: str, chop_dai: bool = False) -> str:
    ret = digits = ''
    decimal_place = 0
    for c in text:
        if c in _DIGIT_WORDS or (
            len(digits) > 0 and c in _PLACE_WORDS
        ):
            if chop_dai and (
                len(digits) == 0
            ) and (
                len(ret) > 0
            ) and (
                ret[-1] == '第'
            ):
                ret = ret[:-1]
            digits += c
            if decimal_place > 0 and c not in _PLACE_WORDS:
                decimal_place += 1
        elif len(digits) > 0 and c in _DECIMAL_WORDS:
            ret += _add_num(digits, decimal_place)
            digits = '0'
            decimal_place = 1
        else:
            if len(digits) > 0:
                ret += _add_num(digits, decimal_place)
                digits = ''
            decimal_place = 0
            ret += c
    if len(digits) > 0:
        ret += _add_num(digits, decimal_place)
    return ret
