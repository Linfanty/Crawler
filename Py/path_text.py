import os

mid = os.getcwd()

print( mid )
print( os.path.getsize(mid+'\\pw.py') )


files = open('in.txt', 'a')
files.write('hello world!\n')
# files.close()

files = open('in.txt', 'r')
print(files.readlines())
files.close()