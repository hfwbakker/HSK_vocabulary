import pandas as pd

# read words from txt file
words = open("input/pleco_known_words.txt", "r")

# filter titles like // Words #1
skiplist = "abcdefghijklmnopqrstuvwxyz/\\"
lines = []
for i in words.readlines():
    if i[0] in skiplist:
        continue
    else:
        lines.append(i)

# create a list of (sub) lists: [cleaned chinese words, pinyin pronunciation]
words_list = []

for i in lines:
    sub = i.split("\t")
    sublist = []
    try:
        sublist.append(sub[0].split("[")[0])
        sublist.append(sub[1].strip())
        words_list.append(sublist)
    except:
        words_list.append(["ERROR", "ERROR"])


# df = pd.DataFrame(["Chinese"], ["Pinyin"])
df = pd.DataFrame(words_list, columns = ['Words', 'Pinyin'])

print(df)

df.to_excel("output/output.xlsx")
