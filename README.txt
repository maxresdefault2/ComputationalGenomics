Bacterial population phylogeny

----------------------------Contents---------------------------------
1) What is each .py, input and output file?
2) How to run the example
3) How to run your own

-------------------------What are the files?-----------------------

~~~~~~~~~~~~~~~~~~~~~~~~.py~~~~~~~~~~~~~~~~~~~~~~
prealignment.py - This file takes in any name of bacteria that one would wish
	to create a population phylogeny for. It also takes in a gene sequence file,
	which we procured from Ensembl (will be described in more detail in pt. 3).
	The only real work this code does is create a BLAST database of individuals of
	the given species and run the genes of these individuals against the genes from
	the reference individual (Ensembl file). Otherwise, it simply acts as an interface
	to run the following Python code (to prepare the sequences for alignment): combine.py,
	newpullseqs.py, pullhigh.py and getbestseqs.py. Note: Line 18 of code allows for 
	customization, by way of the number of gene matches the program will return. 
	> .....-max_target_seqs '+str(num)+' -out....
	Str(num) is currently set to the number of individuals of the species found in the
	BLAST database. This is because the query returns the top str(num) matches from the 
	individuals (or as close as it can get), and we wish to initially consider
	all individuals as possibilities. It then creates a results file "genus_species_results.txt", 
	which is the results from the comparison of BLAST individuals to the reference Ensembl file.

combine.py - This code searches the BLAST bacterial database for individuals that match
	the species name the user entered in prealignment.py. It then adds all matches to a
	file, later called in prealignment.py (which is what the database created in that 
	section consists of).

newpullseqs.py- This code creates a simplified version of the results file created in
	prealignment.py. In short, this takes in the results file "genus_species_results.txt",
	and removes all information except the name of the 
	
---------------------------How to run the example--------------------

-------------------------How to run your own bacteria-----------------

NOTE: The output of our population trees (calculated by the following method) is at: https://compgenapp.herokuapp.com/
      (This is excluding the "Human population", which was a test file given by the treemix devs.)


1) Download BLAST!
  http://www.ncbi.nlm.nih.gov/books/NBK52640/
  

2) Download bacteria!
  >wget ftp://ftp.ncbi.nlm.nih.gov/genomes/Bacteria/all.fna.tar.gz
  

3) Know what bacteria you want to look at!

  After you have decided go here: http://bacteria.ensembl.org/index.html
  
  Under "Search for a genome", enter the name of the bacteria and click on any of the resulting files of the correct species.
  On the next page, on the right side under "Gene annotation", go to the subheading "Download genes", and click "FASTA".
  Go to the cds/ folder, and download the ...cds.all.fa.gz file. 
  Extract this file in the location from which you will be running your code (should be inside of the "ncbi-blast-#..." 
  directory). 
  
  
4) Compare genes, find best matches, and concat them all together!
  Run prealignment.py in the location with the bacteria and Ensembl file.
  

5) MSA!
  Go to: http://mafft.cbrc.jp/alignment/server/index.html
  Under "input" click "choose file" and upload "Mybacgenus_mybacspecies_final.txt". This file was created for you as the
  output of prealignmet.py.
  After this runs, click "CLUSTAL" and save the results into "Mybacgenus_mybacspecies_clust.txt". 
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
