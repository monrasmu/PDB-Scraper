# PDB Scraper
# Project is intended to quick search through PDB text files
# Gives instances of desired motif, as well as those of similar activities
# NOTE: 'similar activities' is subjective. For my purposes this means 
# grouping aromatics in one group, negatively charged in another, small
# hydrophobics in a third, etc.

from collections import Counter
from colorama import init, Fore


# !OJO! Get rid of and just use AAKEys?
aminoAcids = ['GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'PRO', 
			  'PHE', 'TYR', 'TRP', 'SER', 'THR', 'CYS',
			  'MET', 'ASN', 'GLN', 'LYS', 'ARG', 'HIS',
			  'ASP', 'GLU']
similar = {}
similar[1] = ['ASP', 'GLU']
similar[2] = ['TYR', 'TRP', 'PHE']
similar[3] = ['ALA', 'GLY']
similar[4] = ['LEU', 'ISO', 'VAL']
aminoAcidKeys = {'G':'GLY', 'A':'ALA', 'V':'VAL', 'L':'LEU', 'I':'ILE',
				 'P': 'PRO', 'F':'PHE', 'Y':'TYR', 'W':'TRP', 'S':'SER',
				 'T':'THR', 'C':'CYS', 'M':'MET', 'N':'ASN', 'Q':'GLN',
				 'K':'LYS', 'R':'ARG', 'H':'HIS','D':'ASP', 'E':'GLU'}



def pdbScraper():
	init()
	counter = Counter()
	motifKeys = []

	filename = raw_input("Enter the filename you wish to search in: ")
	motif = raw_input("Enter the motif you wish to search (in capital letters, no spaces): ")
	
	# Take user input and assign it to 3-letter vals
	for char in motif:
		try:
			motifKeys.append(aminoAcidKeys[char])
		except:
			print "***Incorrect user input***"
			break

	with open(filename + '.pdb', 'r') as file:
		for line in file:
			# Find section with residue sequences
			if "SEQRES" in line and any(aa in line for aa in aminoAcids):
				mylist = line.split()
				for word in mylist:
					if word in aminoAcids:
						counter[word] += 1
	
	#print(Fore.RED + string)



if __name__ == "__main__":
	pdbScraper()