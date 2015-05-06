import os
def main(nameofbac):
	fname=nameofbac+"_clust.txt"
	os.system("sed -i 's/*/ /g' "+fname)
	os.system("sed -i 's/:/ /g' "+fname)
	os.system("sed -i 's/\.//g' "+fname)
	os.system("sed -i 's/-/X/g' "+fname)
	
	name=""
	content=[]
	fo=open(nameofbac+"_clust_rw.txt","wb")
	with open(fname) as f:
		content = f.readlines()
		for thing in xrange(3, len(content)):
			if content[thing][0]=='g':
				cont=content[thing].split()
				fo.write(cont[1])
				fo.write("\n")
			else:
				fo.write(content[thing])
	fo.close()


	fname=nameofbac+"_clust_rw.txt"
	with open(fname) as f:
		print("Enter the names of the species (in the correct order), separated by space.")
		print("Ex: 'Iowa Hauke Hino Arizona'")
		name=raw_input(">")
		content = f.readlines()
		i=0
		num=0
		holdlist={}
		for thing in content:
			if thing =="\n":
				break
			else:
				num+=1
		for k in xrange(0,num+1):
			holdlist[k]=""
		
		
	    	for thing in content:
			if thing == "\n":
				i=0
			else:
				holdlist[i]+=(thing.rstrip())
				i+=1
			
		
	fo = open(nameofbac+"_clust_out_int.txt", "wb")
	fo.write(name+"\n")
	for k in xrange(0,num+1):
		fo.write(holdlist[k])
		if k!=num:
			fo.write("\n")	
	fo.close()
	
	fname=nameofbac+"_clust_out_int.txt"
	fo=open(nameofbac+"_clust_out.txt","wb")
	with open(fname) as f:
		content = f.readlines()
		for thing in xrange(0, len(content)-1):
			fo.write(content[thing])
