def main(nameofbac):
	fname=nameofbac+"_clust_allele_out"
	content=[]
	di={}
	fo = open(nameofbac+"_clust_allele_out_ind", "wb")
	with open(fname) as f:
		content = f.readlines()
		# Write names of individuals
		fo.write(content[0])
		# Add each unseen line of frequencies to a dict. If already seen, ignore.
		for i in xrange(1,len(content)):
			if content[i] in di:
				continue
			else:
				di[content[i]]=1
	hold=[]
	# Append each key in the dict to a list
	for k,v in di.iteritems():
		hold.append(k)
	# Add each thing in the list (a single copy of each seen line of frequencies) to a file
	for thing in hold:
		fo.write(thing)
	fo.close()
	f.close()
	
	# Reopen the file just made
	fname=nameofbac+"_clust_allele_out_ind"
	fo = open(nameofbac+"_end", "wb")
	with open(fname) as f:
		content = f.readlines()
		first=content[0].split()
		# Get number of individuals being looked at
		i=len(first)-1
		sterm=""
		# Get what the allele frequency line should look like if there are complete matches
		# If 'aaaa' for example: sterm= "1,4 1,4 1,4 1,4"
		for thing in xrange(0,i+1):
			sterm+=str(1)+','+str(i+1)+' '
		sterm=sterm.rstrip()
		sterm=sterm+"\n"
		for thing in content:
			# Only write lines that aren't complete matches
			if thing != sterm:
				fo.write(thing)
			else:
				continue
	fo.close()
