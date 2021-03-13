# kansuji2num

文字列の中の漢数字をアラビア数字に変換する

## Install

`> pip install "git+https://github.com/tetutaro/kansuji2num.git"`

## Usage

as a global command

```
usage: kansuji2num [-h] [--chop-dai] text

convert kansuji in given text to arabic numerals

positional arguments:
  text        text you want to convert

optional arguments:
  -h, --help  show this help message and exit
  --chop-dai  chop "第" before kansuji from text
```

as a Python library

```
> from kansuji2num import kansuji2num
> original_text = '第〇一億二千万三千四五〇回'
> converted_text = kansuji2num(original_text)
> print(converted_text)
第120003450回
> converted_text = kansuji2num(text=original_text, chop_dai=True)
> print(converted_text)
120003450回
```
