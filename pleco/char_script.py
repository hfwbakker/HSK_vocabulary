# save pleco characters as pleco_known_chars.txt
# run script
# output to data/known_chars.txt

input_file = open("input/pleco_known_chars.txt", "r")

known_chars_list = []

lines = input_file.readlines()

skiplist = "abcdefghijklmnopqrstuvwxyz/\\"

for i in lines:
	if i[0] in skiplist:
		continue
	known_chars_list.append(i[0])

print(known_chars_list)

output_file = open("../data/known_chars.txt", "w")

for i in known_chars_list:
    output_file.write(i + "\n")

input_file.close()
output_file.close()