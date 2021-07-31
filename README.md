# HSK_vocabulary

PROJECT
- Write a script that takes a list of characters that user knows, and matches them against a database of HSK1-6 Chinese words that user (should) know because they know the characters.
- These words can then be returned randomly to user as a flash card.
- Flash cards should display character, pinyin, and definition in English.


NEXT UP
- Filtering still not working properly -> look into application of boolean filtering in pandas. Refer to lambda_test.py for some test results regarding one line statements that return the right Boolean value I need.
- Write a function that allows users to select which set of info they want to be prompted first (汉子, pinyin, or definition).
- Integrate with Jupyter notebook to view data?

LOG
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
