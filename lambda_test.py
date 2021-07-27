import pandas as pd

xls = pd.ExcelFile('data/HSK_vocabulary.xlsx')
faux_df = pd.read_excel(xls, 'TEST')
known_characters = ['你', '好', '马', '么', '谁']

test_word = '你好马光'

# print(faux_df)
# new_df = faux_df['char'].isin(known_characters)
# print(new_df)

# print([e in test_word for e in known_characters if e in test_word])

word = 'aad'
c_list = ['a', 'b', 'c']
print(all([i in known_characters for i in test_word]))


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
