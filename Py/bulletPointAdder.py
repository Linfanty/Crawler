#! python3
# Adds wikipedia bullet points to starts of 
# each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# separate
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]
	# add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)