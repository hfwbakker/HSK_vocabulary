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

set_df1()


### SELECT RANDOM WORD ###
def retrieve_word(df):
    global word_row
    word_row = random.randint(0, len(df.index-1))
    global retrieved_character
    global retrieved_pinyin
    global retrieved_definition
    retrieved_character = df.loc[word_row, 'char']
    retrieved_pinyin = df.loc[word_row, 'pinyin']
    retrieved_definition = df.loc[word_row, 'definition']
    return retrieved_character, retrieved_pinyin, retrieved_definition


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

        # Main display screen
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 15, 481, 100))
        label_font = QtGui.QFont()
        label_font.setPointSize(25)
        self.label.setFont(label_font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""background-color: lightblue; 
                                    border: 1px solid black;""")

        # Sub display #1
        self.labelSub1 = QtWidgets.QLabel(self.centralwidget)
        self.labelSub1.setGeometry(QtCore.QRect(40, (15 + 101), 481, 100))
        self.labelSub1.setFont(label_font)
        self.labelSub1.setObjectName("labelSub1")
        self.labelSub1.setStyleSheet("""background-color: lightgreen; 
                                        border: 1px solid black;""")
    
        # Sub display #2
        self.labelSub2 = QtWidgets.QLabel(self.centralwidget)
        self.labelSub2.setGeometry(QtCore.QRect(40, (15 + 202), 481, 100))
        self.labelSub2.setFont(label_font)
        self.labelSub2.setObjectName("labelSub2")
        self.labelSub2.setStyleSheet("""background-color: lightyellow; 
                                        border: 1px solid black;""")

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

        self.pushButton.clicked.connect(lambda: retrieve_word(df))
        self.pushButton.clicked.connect(lambda: self.label.setText(retrieved_character))
        self.pushButton.clicked.connect(lambda: self.labelSub1.setText(retrieved_pinyin))
        self.pushButton.clicked.connect(lambda: self.labelSub2.setText(retrieved_definition))
        self.pushButton.clicked.connect(lambda: self.pushButton.setText(f"NEXT ({word_row}/{len(df.index)})"))

        self.pushButton1.clicked.connect(lambda: self.label.setText("HSK 1 vocabulary"))
        self.pushButton2.clicked.connect(lambda: self.label.setText("HSK 2 vocabulary"))
        self.pushButton3.clicked.connect(lambda: self.label.setText("HSK 3 vocabulary"))
        self.pushButton4.clicked.connect(lambda: self.label.setText("Class vocabulary"))

        self.pushButton1.setText(_translate("H", "HSK 1"))
        self.pushButton1.clicked.connect(lambda: set_df1())

        self.pushButton2.setText(_translate("H", "HSK 2"))
        self.pushButton2.clicked.connect(lambda: set_df2())

        self.pushButton3.setText(_translate("H", "HSK 3"))
        self.pushButton3.clicked.connect(lambda: set_df3())

        self.pushButton4.setText(_translate("H", "Class vocabulary"))
        self.pushButton4.clicked.connect(lambda: set_df4())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    H = QtWidgets.QMainWindow()
    ui = Ui_H()
    ui.setupUi(H)
    H.show()
    sys.exit(app.exec_())
