import pandas as pd
import random
from PyQt5 import QtCore, QtGui, QtWidgets

### HSK WORDS LOGIC ###
#summarized to only inlcude HSK3
xls = pd.ExcelFile('data/HSK_vocabulary.xlsx')
df1 = pd.read_excel(xls, 'HSK_1')
df2 = pd.read_excel(xls, 'HSK_2')
df3 = pd.read_excel(xls, 'HSK_3')
df4 = pd.read_excel(xls, 'CLASS_WORDS')


### KNOWN CHARACTERS LOGIC ###
pleco_file = open("data/known_chars.txt", "r")
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
	# print(final_df)
	return final_df


### SELECT WORD LIST ###
# summarized to only HSK3 df for sake of testing

def set_df1():
    global df
    df = filter_df(df1, known_characters)
    return df

def set_df2():
    global df
    df = filter_df(df2, known_characters)
    return df

def set_df3():
    global df
    df = filter_df(df3, known_characters)
    return df

def set_df4():
    global df
    df = filter_df(df4, known_characters)
    return df

set_df4()


### SELECT RANDOM WORD ###
# summarized for sake of testing
def retrieve_word(df):
	word_row = random.randint(1, len(df.index))
	return f"{df.loc[word_row, 'char']} \n{df.loc[word_row, 'pinyin']} \n{df.loc[word_row, 'definition']}"

rand_char = retrieve_word(df)


### GUI LOGIC ###
class Ui_H(object):
    def setupUi(self, H):
        H.setObjectName("H")
        H.resize(569, 700)
        self.centralwidget = QtWidgets.QWidget(H)
        self.centralwidget.setObjectName("centralwidget")

        # NEXT button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButtonMain")

        # HSK 1 button
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(30, 461, 250, 91))
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

       # HSK 2 button
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(30, (461 + 91), 250, 91))
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")

        # HSK 3 button
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(280, 461, 250, 91))
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")

        # Class vocab button
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(280, (461 + 91), 250, 91))
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")

        # Display screen
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 36, 481, 271))
        label_font = QtGui.QFont()
        label_font.setPointSize(50)
        self.label.setFont(label_font)
        self.label.setObjectName("label")

        # I THINK that this is the top menu bar
        H.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(H)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 22))
        self.menubar.setObjectName("menubar")
        H.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(H)
        self.statusbar.setObjectName("statusbar")
        H.setStatusBar(self.statusbar)
        self.retranslateUi(H)

        QtCore.QMetaObject.connectSlotsByName(H)

    def retranslateUi(self, H):
        _translate = QtCore.QCoreApplication.translate
        H.setWindowTitle(_translate("H", "HSK VOCABULARY en shoarma"))
        self.pushButton.setText(_translate("H", "NEXT"))
        self.label.setText(_translate("H", "Main display"))

        self.pushButton.clicked.connect(lambda: self.label.setText(retrieve_word(df)))
        self.pushButton1.clicked.connect(lambda: self.label.setText("HSK 1 button"))
        self.pushButton2.clicked.connect(lambda: self.label.setText("HSK 2 button"))
        self.pushButton3.clicked.connect(lambda: self.label.setText("HSK 3 button"))
        self.pushButton4.clicked.connect(lambda: self.label.setText("Class vocabulary"))

        self.pushButton1.setText(_translate("H", "HSK 1"))
        self.pushButton1.clicked.connect(lambda: set_df1())
        self.pushButton1.clicked.connect(lambda: print(df))

        self.pushButton2.setText(_translate("H", "HSK 2"))
        self.pushButton2.clicked.connect(lambda: set_df2())
        self.pushButton2.clicked.connect(lambda: print(df))

        self.pushButton3.setText(_translate("H", "HSK 3"))
        self.pushButton3.clicked.connect(lambda: set_df3())
        self.pushButton3.clicked.connect(lambda: print(df))

        self.pushButton4.setText(_translate("H", "Class vocabulary"))
        self.pushButton4.clicked.connect(lambda: set_df4())
        self.pushButton4.clicked.connect(lambda: print(df))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    H = QtWidgets.QMainWindow()
    ui = Ui_H()
    ui.setupUi(H)
    H.show()
    sys.exit(app.exec_())
