import re

def RNAseqParser(line):
	myPattern = re.search(r"\S+\s(\S+)\s\d+\.?\d*\s\d+\.?\d*\s(\d+\.?\d*)\s\d+\.?\d*", line)
	if myPattern:
		return myPattern.group(1)+'	'+myPattern.group(2)+'\n'

rhandle=open('CMdiff_RNAseq.txt','r')
whandle=open('output.txt','w')

for line in rhandle:
	data = line.rstrip()
	#print(data)
	extract = RNAseqParser(data)
	if extract==None: continue
	#print(extract)
	whandle.write(extract)

whandle.close()
rhandle.close()