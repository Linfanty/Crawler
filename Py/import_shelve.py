import shelve

shelveFile = shelve.open('mydata')
cats = ['Zmm', 'Pmm', 'Smm']
shelveFile['cats'] = cats
shelveFile.close()

shelveFile = shelve.open('mydata')
print( type(shelveFile))
print( shelveFile['cats'] )
shelveFile.close()