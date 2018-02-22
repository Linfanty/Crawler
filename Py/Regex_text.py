import re
message = 'My phone number is 181-4930-2835. 1717'

phone_regex = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = phone_regex.search(message)

print( mo.group(1) + ' ' + mo.group(3))
print( mo.groups() )

agentNames = re.compile( r'Agent (\w)\w*')
agentNames.sub( r'\1****', 'Agent ALICE told Agent Bill that Agent carol ' +
	'knew Agent Eve was a double agent' )