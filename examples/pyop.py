substr = 'annotation.281589974882081151405605020939'
substr = substr[11:]
with open('write.json','r') as f:
    while True:
    	l = f.readline()
        line = l.rstrip()
        if(str(line).find(substr)>0):
            final = line
            break
print final
f.close()


'''
index = a.find(substr)
id_index = a.find('id',0,index)
print index, id_index
'''