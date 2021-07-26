# HSK_vocabulary

PROJECT
- Write a script that takes a list of characters that user knows, and matches them against a database of HSK1-6 Chinese words that user (should) know because they know the characters.
- These words can then be returned randomly to user as a flash card.
- Flash cards should display character, pinyin, and definition in English.


NEXT UP
- For some reason only 1 character words are shown? -> more sophisticated filtering needed. Look into filtering by function in this link: https://stackoverflow.com/questions/51589573/pandas-filter-data-frame-rows-by-function 
- Write a function that allows users to select which set of info they want to be prompted first (汉子, pinyin, or definition).
- Integrate with Jupyter notebook to view data?

LOG
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
