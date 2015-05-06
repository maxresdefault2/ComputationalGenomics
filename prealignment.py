import combine
import os
import newpullseqs
import pullhigh
import getbestseqs

if __name__== '__main__':
	print "Enter the full name of the bacteria you wish to use. Ex: 'Staphylococcus aureus'"
	nameofbac=raw_input('>')
	nbac,num=combine.main(nameofbac)
	print str(num)+" matches found"
	print "Making files in db..."
	os.system("makeblastdb -in "+nbac+"_all_combined.fna -out db/blast/"+nbac+"_all_combined -dbtype nucl -parse_seqids")
	print "Done making files in db"
	print "Enter the name of the file to run against. Ex: 'Staphylococcus_aureus_11p4.GCA_000636755.1.26.cds.all.fa'"
	filename=raw_input('>')
	print "Running gene search..."
	os.system('blastn -query '+filename+' -db db/blast/'+nbac+'_all_combined -outfmt "7 qseqid sseqid stitle pident sseq" -max_target_seqs '+str(num)+' -out '+nbac+'_results.txt')
	print "Done with gene search"
	print "Getting top alignments for each individual for each gene..."
	newpullseqs.main(nbac+'_results.txt',nbac)
	print "Done getting top alignments"
	print "Getting individuals with best matches..."
	pullhigh.main(nbac+"_intfile.txt",nbac)
	print "Done getting best matches"
	print "Creating file with best matches..."
	getbestseqs.main(nbac)
	print "Done creating file with best matches"
	print "Go to http://mafft.cbrc.jp/alignment/server/ and run file:"
	print nbac+"_final.txt"
	print ""
	print "When finished, save CLUSTAL version of file as:"
	print nbac+"_clust.txt"
	print ""
	print "Then proceed to postalignment.py"
