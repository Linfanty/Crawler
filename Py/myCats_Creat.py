import pprint
cats = [{'name': 'Z', 'desc': 'B'},
		{'NAME':'P', 'DESC': 'R'}]
# pprint.pformat(cats)

files = open('myCats.py', 'w')
files.write('cats = ' + pprint.pformat(cats) + '\n')
files.close()
