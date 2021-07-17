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

df = df3[df3['char'].isin(known_characters)]


def retrieve_word():
	ask_to_continue = input("Type exit and hit enter to quit or just hit enter to continue.\n>")
	if ask_to_continue == "exit":
		exit(0)
	word_row = random.randint(1, len(df3.index))
	print(df3.loc[word_row, 'char'])
	input('Press enter to reveal pinyin.')
	print(df3.loc[word_row, 'pinyin'])
	input('Press enter to reveal definition.')
	print(df3.loc[word_row, 'definition'])
	print("\n")
	retrieve_word()


### EXECUTION LOGIC ###
print("\n")
print("######################################")
print("###Welcome to HSK Vocabulary Tester###")
print("######################################")
print("\n")

retrieve_word()
