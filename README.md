# HSK_vocabulary

PROJECT
- Write a script that takes a list of characters that user knows, and matches them against a database of HSK1-6 Chinese words that user (should) know because they know the characters.
- These words can then be returned randomly to user as a flash card.
- Flash cards should display character, pinyin, and definition in English.


NEXT UP
- Write a function that allows players to select which set of info they want to be prompted first (汉子, pinyin, or definition).
- Finetune.
- Check if all the logic is correct (like the filtering of rows is done correctly).

LOG
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
