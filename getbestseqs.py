def main(nbac):
	finame=nbac+"_high_nums.txt"
	fname=nbac+"_intfile.txt"
	seqdict={}
	with open(finame) as fi:
		content=fi.readlines()
		for thing in content:
			thing = thing.replace("\n", "")
			seqdict[thing]=""
	content=[]
	addr=0
	fo = open(nbac+"_final.txt", "wb")
	gene=""
	curseq=""
	bps=""
	with open(fname) as f:
		content = f.readlines()
		for thing in content:
			thing=thing.split()
			gene=thing[0]
			curseq=thing[1]
			bps=thing[2]
			bps=bps.rstrip()
			if curseq in seqdict:
				seqdict[curseq]+=bps
			else:
				continue
	
	for k,v in seqdict.items():
		v=v.rstrip()
		fo.write('>'+k+'\n')
		fo.write(v+'\n')
