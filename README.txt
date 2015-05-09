Bacterial population phylogeny

----------------------------Contents---------------------------------
1) What is each .py, input and output file?
2) How to run the example
3) How to run your own

-------------------------What are the files?-----------------------

~~~~~~~~~~~~~~~~~~~~~~~~.py~~~~~~~~~~~~~~~~~~~~~~
prealignment.py - This file takes in any name of bacteria that one would wish
	to create a population phylogeny for. It also takes in a gene sequence 
	file, which we procured from Ensembl (will be described in more detail 
	in  pt 3. The only real work this code does is create a BLAST database of 
	individuals of the given species and run the genes of these individuals 
	against the genes from the reference individual (Ensembl file). Otherwise, 
	it simply acts as an interface to run the following Python code (to 
	prepare the sequences for alignment): combine.py, newpullseqs.py, 
	pullhigh.py and getbestseqs.py. Note: Line 18 of code allows for 
	customization, by way of the number of gene matches the program will 
	return. 
	> .....-max_target_seqs '+str(num)+' -out....
	Str(num) is currently set to the number of individuals of the species 
	found in the BLAST database. This is because the query returns the top 
	str(num) matches from the individuals (or as close as it can get), and 
	we  wish to initially consider all individuals as possibilities. It 
	then creates a results file "genus_species_results.txt", which is the 
	result from the comparison of BLAST individuals to the reference 
	Ensembl file.

combine.py - This code searches the BLAST bacterial database for individuals 
	that match the species name the user entered in prealignment.py. It 
	then adds all matches to a file, later called in prealignment.py (which 
	is what the database created in that section consists of).

newpullseqs.py- This code creates a simplified version of the results file 
	created in prealignment.py. In short, this takes in the results file 
	"genus_species_results.txt", and removes all information except the 
	name of the gene, the identifier of the current individual, and 
	corresponding sequence that was found.
	
pullhigh.py- This code pulls the 10 (or the closest it can get to 10) 
	individuals with the highest number of found matches to the genes that 
	were ran against in the reference individual. Since BLAST has a fairly 
	small database of bacteria, we do not run the risk of only ending up 
	with individuals from the same population. Quite the contrary, it is a 
	VERY rare case where there are ever two individuals from the same 
	population that are chosen, though these still show differences.
	
getbestseqs.py- Using the list of best individuals acquired from pullhigh.py, 
	the generated file "genus_species_intfile.txt" (generated from 
	newpullseqs.py) is ran against this list, and matches are found. The gene 
	sequences from each individual in the intfile list are concatenated and 
	written into the file "genus_species_final.txt" to be sent for alignment.
	
postalignment.py- This file takes in the name of the species that the user has 
	been working with, and sends files between and creates files from the 
	other python code: formatfile.py, newal.py, and abrfiles.py. Finally, 
	this program zips the allele frequency file, preparing it to be sent into 
	the treemix program.
	
formatfile.py- This code takes in the output of running MSA via MAFFT and 
	formats it into neat, concatenated lines--one for each individual. It also
	asks the user to input the proper names	for each individual, since 
	previously it has only been using numerical identifiers that do not give a
	good idea of the actual population the individual was taken from. Currently,
	there is no programmatic way to do this, and the user needs to compare the
	identifiers with the lines in the initial "genus_species_result.txt" file
	to get the full individual's names.
	
newal.py- This file generates allele frequencies. It finds the major and minor
	allele at the same position for all individuals. If a major and minor allele
	cannot be found, the sequence is ignored, and the program moves forward. The
	presence of a major allele is written as 1,0, and a minor allele is written 
	as 0,1. 
	
abrfile.py- This file takes in the allele frequency file generated in newal.py, 
	and removes all lines that are duplicates, making sure only there is only 
	one of each allele frequency line. This method is done as it was by the 
	treemix devs, because having will not affect the data, but will incur a 
	much higher time cost to treemix's running time.
	

~~~~~~~~~~~~~~~~~~ I/O files ~~~~~~~~~~~~~~~~~~~~

genus_species_allcombined.fna- This file contains a concatenation of the full 
	genome for each individual found for the specified species in the BLAST 
	database. 

genus_species_results.txt - This file contains the full list of genes from all 
	individuals of the species that were found to match the reference gene.
	
genus_species_intfile.txt- This is a formatted version of 
	"genus_species_results.txt", which contains only the individuals name, 
	sequence, and the gene that was being matched. 
	
genus_species_high_nums.txt - This file contains a list of the top 10 (or if 
	less, the maximum closest to 10) matches, ranked by the number of gene 
	matches that were found when compared to the reference genes from the 
	Ensembl file. 
	
genus_species_final.txt- This file contains the concatenated sequence list for
	each of best individuals that were identified in the 
	"genus_species_high_nums.txt" file. On the line before each individual's 
	sequence is ">identifier_of_individual". 
	
genus_species_clust.txt- This is the output of the MAFFT aligner. It contains 
	blocks of individuals lined up in their aligned format. 
	
genus_species_clust_rw.txt- This is the rewritten version of 
	"genus_species_clust.txt", which removes all non-sequence characters and 
	text, and replaces all mismatches, which are written as '-' in the MAFFT
	output,	as 'X'. This is done to make the later text files not skip to a 
	new line when a '-' is encountered.
	
genus_species_clust_out_int.txt- This file contains the concatenated versions
	of each individual, with the proper names of the individuals at the top 
	of the file.
	
genus_species_clust_out.txt- This is the final version to be used of 
	"genus_species_clust_out_int.txt", rewritten such that the trailing blank
	line is removed.
	
genus_species_clust_allele_out.txt- This is the file where the calculated allele
	frequencies are written to. The top line contains space-delineated proper 
	names of individuals (in order of sequence listing), and each line 
	following this is the allele frequency calculated for each respective 
	alignment of base pairs.
	
genus_species_clust_allele_out_ind.txt- This file contains the same lines from 
	"genus_species_clust_allele_out.txt", except duplicate lines of allele 
	frequencies are removed. 
	
genus_species_end- This is the final allele frequency file, after final formatting
	and final check to make sure that the allele frequency where all lines are the
	same major allele match. This should have already been done, and is a fragment
	from the previous version of the code, but it is kept in just as a fail-safe. 
	This file is zipped, therefore the file itself will not be found in the 
	directory.
	
genus_species_end.gz- This is the final zipped version of the allele frequency 
	file, ready to be inserted into treemix.
	

	
---------------------------How to run the example--------------------

-------------------------How to run your own bacteria-----------------

NOTE: The output of our population trees (calculated by the following method) is 
	at: https://compgenapp.herokuapp.com/
	
    (This is excluding the "Human population", which was a test file given by 
	the treemix devs.)


1) Download BLAST!
  http://www.ncbi.nlm.nih.gov/books/NBK52640/
  

2) Download bacteria!
  >wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/all.fna.tar.gz
  

3) Know what bacteria you want to look at!

  After you have decided go here: http://bacteria.ensembl.org/index.html
  
  Under "Search for a genome", enter the name of the bacteria and click on any of the
	resulting files of the correct species.
  On the next page, on the right side under "Gene annotation", go to the subheading 
	"Download genes", and click "FASTA".
  Go to the cds/ folder, and download the ...cds.all.fa.gz file. 
  Extract this file in the location from which you will be running your code (should be
	inside of the "ncbi-blast-#..." directory). 
  
  
4) Compare genes, find best matches, and concat them all together!
  Run prealignment.py in the location with the bacteria and Ensembl file.
  

5) MSA!
  Go to: http://mafft.cbrc.jp/alignment/server/index.html
  Under "input" click "choose file" and upload "Mybacgenus_mybacspecies_final.txt". This 
	file was created for you as the output of prealignmet.py.
  After this runs, click "CLUSTAL" and save the results into 
	"Mybacgenus_mybacspecies_clust.txt". 
  NOTE: Be sure to save ENTIRE FILE, including the starting line "Clustal..." and spaces.
  
  
6) Generate allele frequencies!
  Run postalignment.py.
  NOTE: You will be asked for the names of the individuals. You can either enter arbitrary names (not recommended), or get
  the names on the lines of "Mybacgenus_mybacspecies_clust.txt" (also not recommended), or match the names on the lines of
  "Mybacgenus_mybacspecies_clust.txt" with their corresponding individual names by matching them within 
  "Mybacgenus_mybacspecies_infile.txt" (recommended, but will require manual searching; will automate this in a later 
  version).
  
  
7) Download treemix!
  First, download the Boost Graph Library and the GNU Scientific Library.
  Next, install:
  >tar -xvf treemix-1.12.tar.gz
  >cd treemix-1.12
  >./configure
  >make
  >make install
    
    
8) Run through treemix!
  Make sure the file "Mybacgenus_mybacspecies_final.gz" is in the treemix-1.12 directory.
  To build a plain tree:
  >treemix -i "Mybacgenus_mybacspecies_final.gz" -o "Mybacgenus_mybacspecies"
  
  To build a tree with a number of migrations:
  >treemix -i "Mybacgenus_mybacspecies_final.gz" -m <#migrations> -o "Mybacgenus_mybacspecies"
  
  
9) Get a tree!
  Run R on a terminal.
  Change the source:
  >source("home/user/treemix-1.12/src/plotting_funcs.R")
  
  Plot the tree:
  >plot_tree("home/user/treemix-1.12/Mybacgenus_mybacspecies")
  
  
...Voila! A tree of bacterial splits (and maybe migrations)!
