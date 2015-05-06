import operator

def main(fname,nbac):
	content=[]
	di={}
	fo = open(nbac+"_high_nums.txt", "wb")
	curseq=""
	with open(fname) as f:
		content = f.readlines()
		for thing in content:
			thing=thing.split()
			curseq=thing[1]
			if curseq in di:
				di[curseq]+=1
			else:
				di[curseq]=1
	s = sorted(di.iteritems(), key=operator.itemgetter(1), reverse=True)
	kh=0
	hold=[]
	for k,v in s:
		if kh!=10:
			hold.append(k)
			kh+=1
	for thing in hold:
		fo.write(thing+'\n')
