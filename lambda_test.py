import pandas as pd

xls = pd.ExcelFile('data/HSK_vocabulary.xlsx')
words_df = pd.read_excel(xls, 'TEST')

pleco_file = open("data/pleco_cards.txt", "r")
lines = pleco_file.readlines()
known_characters = []
skiplist = "abcdefghijklmnopqrstuvwxyz/\\"

for i in lines:
	if i[0] in skiplist:
		continue
	known_characters.append(i[0])

known_letters = ['a', 'b', 'c', 'd']

all_words = words_df['word'].tolist()

filtered_words = []
for i in all_words:
	valid = True
	for j in i:
		if j in known_letters:
			continue
		else:
			valid = False
	if valid == True:
		filtered_words.append(i)
	else:
		continue

print(words_df[words_df['word'].isin(filtered_words)])








# words_df['known_or_not'] =  words_df['word'].isin(known_letters)

# words_df['known_or_not'] = all([e in words_df['word'] for e in known_characters if e in words_df['word']])

# print(words_df)

# learnable = [word for word in words_to_learn if all(letter in known_letters for letter in word)]

# print(learnable)


# filt = (all(letter in known_letters.values for letter in word) for word in words_to_learn.values)

# filter = (all(letter in known_characters.values for letter in word) for word in faux_df)


# learnable = words_to_learn[filt]


# learnable = faux_df[filter]

# print(learnable)

# print(faux_df['char'].values)


# print(faux_df)
# new_df = faux_df['char'].isin(known_characters)

# df[(df['C']==True) | (df['D']==True)]

# faux_df['known?'] = faux_df['char'].isin(known_characters)
# faux_df['known?'] = faux_df.char.isin(known_characters)
# print(faux_df)

# print(faux_df['char'][0])
# print(type(faux_df))
# print(type(faux_df['char']))
# print(faux_df['char'][0])
# print(type(faux_df['char'][0]))
# print("bal".contains("bal"))


#df2['optimal_fruit'] = [x * y - z for x in df2['apples'] for y in df2['oranges'] for z in df2['bananas']]

# faux_df['known'] = [i in known_characters for i in faux_df['char']]

# faux_df['known'] = all([e in faux_df['char'] for e in known_characters if e in faux_df['char']])

# faux_df['known'] = all(list(map(lambda x: x in known_characters, faux_df['char'])))

# print(faux_df)

# test_word = '酋批'
# test_list = ['你', '好', '马']

# print([e in test_word for e in known_characters if e in test_word])

# print([e in test_word for e in test_list if e in test_word])

# print(list(map(lambda x: x in known_characters, test_word))) # seems to work as desired!

# print(all(list(map(lambda x: x in known_characters, test_word)))) # seems to work as desired!

# print(all([i in known_characters for i in test_word]))


#######################################
#######################################
#######################################


# def test_filtering(row):
# 	contains = True

# 	for i in row:
# 		if i in known_characters:
# 			continue
# 		else:
# 			contains = False
	
# 	return contains



# list(map(lambda x: print(x), known_characters))


# test_word = "你好"

# print(list(map(lambda x: x in test_word, known_characters))) # works sorta

# print(list(map(lambda x: x in known_characters, test_word))) # seems to work as desired!

# now need to turn this one in to a lambda one-liner that returns true if all values are true, 
# or false if one or more return false
# lambda within lambda -> is possible I think
# above lambda returns an array of True or False statements e.g. [True, False, True]
# lambda x: (previous lambda function) -> do things to it that returns either True or False

# test_list = [True, True]

# print(all(test_list))

# bal = all(list(map(lambda x: x in known_characters, test_word)))

# print(bal)

# newdf = df1[df1.apply(all(list(map(lambda x: x in known_characters, test_word))))]
