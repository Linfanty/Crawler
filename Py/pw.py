#! python3
# pw.py - An insecure password locker program.

PASSWORD = {'email': 'abcd',
	'blog': 'def',
	'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [accout] - copy account password')
	sys.exit()

account = sys.argv[1] #account name

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print('password for ' + account + ' copied to cliboard.')
else:
	print('There is no account named ' + account)

"""sys.argv是你接收的参数的列表 []
比如你这段代码名字叫做test.py
运行python test.py 192.168.0.1 test.txt
sys.argv[0] ----test.py
sys.argv[1] ----192.168.0.1

sys.argv[2] ----test.txt
"""