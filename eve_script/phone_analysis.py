#功能说明：
#统计../data/hzpy-utf8.txt文件中每一行的第二个字段音节的总个数,及常用字的音节总个数
#测试结果：417，401
#统计声母的话，将13行和17行的part[1]改为part[2]即可
#统计韵母的话，将13行和17行的part[1]改为part[3]即可
#
with open('D:/lkg/1. pinyin/5. program/words_lib/hanzipinyin/data/hzpy-utf8.txt', 'r', encoding='utf-8') as f:
    phone_dict = {}
    normal_phone_dict = {}
    for line in f:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            if parts[3] == '':#特殊的有一个字没有韵母 嗯，发音ng，还有一个字呒，发音m时，声母和韵母都为m
                print(parts)
            phone_dict[parts[1]] = 1# 1 音节 2 声母 3 韵母 4 unicode码 5 是否常用字
            if int(parts[-1]) > 0:
                normal_phone_dict[parts[1]] = 1# 1 音节 2 声母 3 韵母 4 unicode码 5 是否常用字
phone_dict = sorted(phone_dict.items(), key=lambda x: x[0])
normal_phone_dict = sorted(normal_phone_dict.items(), key=lambda x: x[0])
with open('D:/lkg/1. pinyin/5. program/words_lib/hanzipinyin/out/all_phone.txt', 'w', encoding='utf-8') as f:
    for item in phone_dict:
        f.write(item[0] + '\n')
with open('D:/lkg/1. pinyin/5. program/words_lib/hanzipinyin/out/normal_phone.txt', 'w', encoding='utf-8') as f:
    for item in normal_phone_dict:
        f.write(item[0] + '\n')
print(len(phone_dict))
print(len(normal_phone_dict))