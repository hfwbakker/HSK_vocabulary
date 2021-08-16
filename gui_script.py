import pandas as pd
import random
from PyQt5 import QtCore, QtGui, QtWidgets

### HSK WORDS LOGIC ###
#summarized to only inlcude HSK3
xls = pd.ExcelFile('data/HSK_vocabulary.xlsx')
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



### FILTER DF ###
def filter_df(df, chars):
	all_df_words = df['char'].tolist()

	filtered_words = []
	for i in all_df_words:
		valid = True
		for j in i:
			if j in chars:
				continue
			else:
				valid = False
		if valid == True:
			filtered_words.append(i)
		else:
			continue

	filtered_df = df[df['char'].isin(filtered_words)]
	final_df = filtered_df.reset_index(drop=True)
	print(final_df)
	return final_df


### SELECT WORD LIST ###
# summarized to only HSK3 df for sake of testing
df = filter_df(df3, known_characters)



### SELECT RANDOM WORD ###
# summarized for sake of testing
def retrieve_word(df):
	word_row = random.randint(1, len(df.index))
	return f"{df.loc[word_row, 'char']} \n{df.loc[word_row, 'pinyin']} \n{df.loc[word_row, 'definition']}"
	# print(df.loc[word_row, 'char'])
	# input('Press enter to reveal pinyin.')
	# print(df.loc[word_row, 'pinyin'])
	# input('Press enter to reveal definition.')
	# print(df.loc[word_row, 'definition'])
	# print("\n")
	# retrieve_word(df)

rand_char = retrieve_word(df)


### GUI LOGIC ###
class Ui_H(object):
    def setupUi(self, H):
        H.setObjectName("H")
        H.resize(569, 600)
        self.centralwidget = QtWidgets.QWidget(H)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 36, 481, 271))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        H.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(H)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 22))
        self.menubar.setObjectName("menubar")
        H.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(H)
        self.statusbar.setObjectName("statusbar")
        H.setStatusBar(self.statusbar)
        self.retranslateUi(H)


        self.pushButton.clicked.connect(lambda: self.label.setText(retrieve_word(df)))
        QtCore.QMetaObject.connectSlotsByName(H)

    def retranslateUi(self, H):
        _translate = QtCore.QCoreApplication.translate
        H.setWindowTitle(_translate("H", "HSK VOCABULARY"))
        self.pushButton.setText(_translate("H", "NEXT"))
        self.label.setText(_translate("H", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    H = QtWidgets.QMainWindow()
    ui = Ui_H()
    ui.setupUi(H)
    H.show()
    sys.exit(app.exec_())
