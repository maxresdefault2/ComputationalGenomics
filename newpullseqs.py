def main(fname,nbac):
	content=[]
	addr=0
	fo = open(nbac+"_intfile.txt", "wb")
	gene=""
	curseq=""
	with open(fname) as f:
		content = f.readlines()
		for thing in content:
			if thing[0]=="#" and thing[2]=="Q" and thing[7]==':':
				gsplit=thing.split()
				gene=gsplit[2]
			th=thing.split()
			if th[0]==gene:
				if curseq==th[1]:
					continue
				else:
					curseq=th[1]
					fo.write(gene+' '+curseq+' '+th[-1]+'\n')
			elif th[0]!='#':
				gene=th[0]
				curseq=th[1]
				fo.write(gene+' '+curseq+' '+th[-1]+'\n')
			else:
				continue
		
			
