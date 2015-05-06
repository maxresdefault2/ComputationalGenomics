def main(nameofbac):
	fname=nameofbac+"_clust_out.txt"
	content=[]
	with open(fname) as f:
	    content = f.readlines()
	holdstr=""
	vallist=[]
	
	fo = open(nameofbac+"_clust_allele_out", "wb")
	# Writing the top line again so this will work for the allelefreq stuff
	fo.write(content[0])
	
	for i in xrange(0,len(content[1])-1):
	    vallist=[]
	    # 0=a, 1=t, 2=c, 3=g, 4=gap
	    for num in xrange(0,5):
		vallist.append(50)
	    # Initially adding 50 so I can calculate the min value without having to
	    # discard things that appear 0 times. 
	    try:
		# For each line with sequences
	        for j in xrange(1,len(content)):
	            if content[j][i]=='a':
		        # If the value is seen for the first time
			if vallist[0]==50:
				vallist[0]=1
			# If the value has already been seen
	                else:
	                	vallist[0]+=1
	            elif content[j][i]=='t':
	                if vallist[1]==50:
				vallist[1]=1
			else:
	                	vallist[1]+=1
	            elif content[j][i]=='c':
	                if vallist[2]==50:
				vallist[2]=1
			else:
	                	vallist[2]+=1
		    elif content[j][i]=='g':
		        if vallist[3]==50:
				vallist[3]=1
			else:
	                	vallist[3]+=1
		    # In the case of a gap
	            # Pe'er said at one point to treat a gap as another bp
	            else:
	                if vallist[4]==50:
				vallist[4]=1
			else:
	                	vallist[4]+=1
	
		# Get the min value (x) and its index in the list
		# If there is a tie, it'll just take the first
		# Min value should be the variant (or at least we'll pretend it is)
		x=min(vallist)
		m=vallist.index(x)
	
		# Figure out what bp the min value corresponds to
		minall=''
		if m==0:
			minall='a'
		elif m==1:
			minall='t'
		elif m==2:
			minall='c'
		elif m==3:
			minall='g'
		else:
			minall='-'
	
		if vallist[0]==50:
			vallist[0]=-1
		if vallist[1]==50:
			vallist[1]=-1
		if vallist[2]==50:
			vallist[2]=-1
		if vallist[3]==50:
			vallist[3]=-1
		if vallist[4]==50:
			vallist[4]=-1
		vallist[m]=-1
	
		y=max(vallist)
		n=vallist.index(y)
	
		maxall=''
		if n==0:
			maxall='a'
		elif n==1:
			maxall='t'
		elif n==2:
			maxall='c'
		elif n==3:
			maxall='g'
		else:
			maxall='-'
	
		# Get ready to create the string of allele frequencies
	        holdstr=""
	        for j in xrange(1,len(content)):
		    # If the value is the same as the variant, do 1,#times variant seen
	            if content[j][i]==minall:
	                holdstr+=str(0)+','+str(1)+' '
		    elif content[j][i]==maxall:
			holdstr+=str(1,)+','+str(0)+' '
		    # If not the same, 0,0
	            else:
	                holdstr=''
			break
	
	    # Remnant from my old method. Still probably good to keep in
	    # If this occurs, there is probably a blank line at the bottom of the file you're reading from
	    except IndexError:
		print "Index error"
	    if holdstr!='':
	    	fo.write(holdstr.rstrip())
	    	fo.write('\n')
	    
	fo.close()
