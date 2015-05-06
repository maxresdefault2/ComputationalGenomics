import os

def main(nameofbac):
	print "Looking for files..."
	nameofbac=nameofbac.replace(" ","_")
	f = open(nameofbac+'_all_combined.fna', 'w')
	num=0
	for root, dirs, files in os.walk("all.fna"):
    		for file in files:
        		if file.endswith(".fna"):
        		     if nameofbac in os.path.join(root):
				num+=1
				print os.path.join(root)
        	     		with open(os.path.join(root, file)) as infile:
		            		for line in infile:
		                		f.write(line)
	f.close()
	print "Finished looking for files"
	return nameofbac, num
