import os
import formatfile
import newal
import abrfiles

if __name__== '__main__':
	print "Enter the full name of the bacteria you wish to use. Ex: 'Staphylococcus aureus'"
	nameofbac=raw_input('>')
	nameofbac=nameofbac.replace(" ","_")
	print "Formatting Clustalw file..."
	formatfile.main(nameofbac)
	print "Done formatting file"
	print "Calculating allele frequencies..."
	newal.main(nameofbac)
	print "Done calculating allele frequencies"
	print "Getting rid of instances of homozygosity or repeats..."
	abrfiles.main(nameofbac)
	print "Done with allele frequency file"
	os.system("gzip "+nameofbac+"_final")
	print "The allele frequency file has been zipped and is ready to run through treemix"
	print "The name of this file is:"
	print nameofbac+"_final.gz"
