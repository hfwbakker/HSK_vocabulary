import pandas as pd
import random

### HSK WORDS LOGIC ###
xls = pd.ExcelFile('data/HSK_vocabulary.xlsx')
df1 = pd.read_excel(xls, 'HSK_1')
df2 = pd.read_excel(xls, 'HSK_2')
df3 = pd.read_excel(xls, 'HSK_3')


### KNOWN CHARACTERS LOGIC ###
pleco_file = open("data/pleco_cards.txt", "r")
lines = pleco_file.readlines()
known_characters = []
skiplist = "abcdefghijklmnopqrstuvwxyz/\\"

for i in lines:
	if i[0] in skiplist:
		continue
	known_characters.append(i[0])

### SELECT WORD LIST ###
def select_list():
	choice = input("""
	Select HSK word list: \n
	1. HSK 1\n
	2. HSK 2\n
	3. HSK 3\n
	>
	""")
	if choice == '1':
		print("Selected HSK 1.")
		df = filter_df(df1, known_characters)
	elif choice == '2':
		print("Selected HSK 2.")
		df = filter_df(df2, known_characters)
	elif choice == '3':
		print("Selected HSK 3.")
		df = filter_df(df3, known_characters)
	else:
		print("Choice unclear, plese reenter.")
		select_list()
	return df




### FILTER DF ###
def filter_df(df, chars):
	filtered_df = df[df.char.isin(known_characters)]
	final_df = filtered_df.reset_index(drop=True)
	return final_df


### SELECT RANDOM WORD ###
def retrieve_word(df):
	choice = input("Press enter for next word. Type exit to quit.")
	if choice == "exit":
		exit(0)
	word_row = random.randint(1, len(df.index))
	print(df.loc[word_row, 'char'])
	input('Press enter to reveal pinyin.')
	print(df.loc[word_row, 'pinyin'])
	input('Press enter to reveal definition.')
	print(df.loc[word_row, 'definition'])
	print("\n")
	retrieve_word(df)


### EXECUTION LOGIC ###
print("\n")
print("######################################")
print("###Welcome to HSK Vocabulary Tester###")
print("######################################")
print("\n")


# df = filter_df(df3, known_characters)

retrieve_word(select_list())

# select_list()


