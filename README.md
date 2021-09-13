# HSK_vocabulary

PROJECT
- Write a script that takes a list of characters that user knows, and matches them against a database of HSK1-6 Chinese words that user (should) know because they know the characters.
- These words can then be returned randomly to user as a flash card.
- Flash cards should display character, pinyin, and definition in English.


NEXT UP
- PyQt GUI to add:
    * Add buttons and functionality for all 4 lists.
    * Click-to-reveal functionality. Right now it shows all through values at the same time.
    * When selected a list to practice, a message should display something like "xxx out of total amount words xxx displayed" to indicate how many words are still "unreadable".
- Implement classes. Classes classes classes.
- Write a function that allows users to select which set of info they want to be prompted first (汉子, pinyin, or definition).
- Write a function where you can select how many words you want to test and then keep score.
- Create a sample version and upload to forum for feedback.

LOG
--- Monday September 13th 2021 ---
- Added background coloring to certain elements in the GUI for easier distinction
- Added 2 "sub displays" with the intention to allow for seperately display characters, pinyin, and definition.
- Three displays now correctly show chars, pinyin, and definition each and have right functionality added.
- Next button now shows which row out of how many rows is currently being shown.
- word_row = 118 throws keyerror when using HSK_1 list. Possibly need to reset index. FIXED: issue was with randomized row number, if resulting in max length of df index it would return a number that was 1 outside of df range and therefore threw a keyerror.

--- Wednesday September 8th 2021 --- 
- Reviewing design of app, adding buttons and info display.
- Cleaned up excess code.
- Created HSK 2 and HSK 3 buttons (inc. functionality)

--- Tuesday September 7th 2021 ---
- Created a new folder called "pleco" with scripts for filtering pleco input. Scripts output in to data folder.
- deleted lambda_test.py
- Created a script that takes pleco words list, cleans it up, and puts it into an excel sheet
- Organized pleco folder with sub folders for in and output for clarity.

--- Wednesday August 25 2021 ---
- Basics for a PyQt5 GUI are now there.
- Figured out how to properly make buttons interactive.
- Can now select a dataframe with in-app buttons.

--- Monday August 16 2021 ---
- Started developing a PyQt5 GUI.
- Added work in progress file gui_script.py that has a simplified script integrated with a simple PyQt GUI script.
- Simplified version is functional, 1 list is selected (HSK3) and clicking "NEXT" rotates through random characters displaying 'char', 'pinyin', and 'definition' simultaneously for now.

--- Wednesday August 11 2021 ---
- PyQt5 research. Not much progress except for sorting out what might work or not.

--- Tuesday August 10 2021 ---
- Developing Qt GUI create with => pyuic5 -x qt-test.ui -o test.py
- Doing PyQt5 course online.

--- Monday Augst 9 2021 ---
- Installed PyQt5
- Installed Qt Designer, will use to create a UI for app.

--- Saturday August 7 2021 ---
- Updated pleco words and characters. Need to work on script to sort the words from pleco.
- Added a list for words learned in class.

--- Sunday August 1st 2021 ---
- That works! Filtering now works properly.
- New idea: turn word series into a list, filter out each word based on known character list, then filter pandas df based on if the words in df match the words i know list.

--- Saturday July 31st 2021 ---
- The filter I need is still not working, even after asking Reddit so far no result. Will try again tomorrow.
- Install Jupyter
- Still not working. Looking in to list comprehension filters.
- OR: ask pandas if there values in 'char' that are NOT in "known_characters".
- Realization: I can make a new colum that evaluates to True or False based on if all characters in 'char' exists in 'known_characters' so I can simply create that new column and THEN based on this True/False column filter the words I need.

--- Tuesday July 27th 2021 ---
- LAMBDA is also not clearly the answer so far. I manage to make LAMBDA or "checking membership"(need to look in to that...) statement that returns True when all characters do indeed exist in the known_characters list, but its not immediately clear how to use that statement to filter a pandas dataframe column (in this case referred to as a Series as I understand). Perhaps need to look in to pandas filtering with Booleans.
- Created lambda_test.py for further testing one line statements and functions.
- The filter by function link was unfruitful, but I have found out that LAMBDA is likely the technique I will need to use for "function filtering" rows in pandas. Tangent incoming.

--- Monday July 26th 2021 ---
- Fired up the script again, cannot get it to work on Windows because (presumably) the Chinese character throw an encoding error I don't know how to fix yet. Tried updating Python to 3.9.6 and updated encoding related stuff but didn't work, even after restarting.
- Found out that the script only returns 1 character words because the filter_df() function only returns true for single character entries that match the known_characters list. Trying to find a work around using a function filter.

--- Sunday July 18th 2021 ---
- Figured out the key error - editing the dataframe without resetting the index causes gaps in the index that if called throw a key error (hence key error corresponding with no. input). Fixed.
- User can now select with word list to choose and the logic does the rest.

--- Saturday July 17th 2021 ---
- Wrote logic that displays chinese to user, followed by pinyin and definition by pressing enter respectively.
- Tried to get a filtered version of HSK words database tested against known characters but something goes wrong there that throws a keyerror equal to the row number entered when printing values (inside the retrieve_word function).

--- Thursday July 15th 2021 ---
- Created Excel lists of HSK1 - 3 words.
- Imported pleco_cards as a txt file.
- Created python script that reads HSK words excel file.
- Created virtual environment with pandas and openpyxl installed.

--- Sunday July 11th 2021 ---
- Created project.
