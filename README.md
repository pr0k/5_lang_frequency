# Frequency Analysis of Words

The Program shows the most commonly used words in the text file to the console in descending order


# How to use

Just run the script specifying the path to the file with the text data.

You can use an optional parameter `-c` or `--count` to specify the number of output words. Default value is 10.

For detail run this with `-h` or `--help`

```bash

$ python lang_frequency.py [-h] [-c, --count] path/to/text/file/*.*
# possibly requires call of python3 executive instead of just python

example:

$ python lang_frequency.py -c 15 Liang-Xiao-Sheng.txt

Word:

文革              	is meets 15 times
北京日报            	is meets 10 times
燕山夜话            	is meets 10 times
和               	is meets 9 times
三家村札记           	is meets 8 times
我               	is meets 8 times
的               	is meets 6 times
吴晗              	is meets 6 times
同学们             	is meets 6 times
三家村             	is meets 6 times
战斗檄文            	is meets 6 times
没有              	is meets 5 times
我说              	is meets 5 times
该杀              	is meets 5 times
解放军报            	is meets 5 times

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
