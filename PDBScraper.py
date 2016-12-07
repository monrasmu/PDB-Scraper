# PDB Scraper
# Project is intended to quick search through PDB text files
# Gives instances of desired motif, as well as those of similar activities
# NOTE: 'similar activities' is subjective. For my purposes this means 
# grouping aromatics in one group, negatively charged in another, small
# hydrophobics in a third, etc.

import unittest
from collections import Counter

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
	counter = Counter()
	motifKeys = []

	filename = raw_input("Enter the filename you wish to search in: ")
	motif = raw_input("Enter the motif you wish to search (in single letters, no spaces): ")
	
	# Take user input and assign it to 3-letter vals
	for char in motif:
		#if char in aminoAcidKeys:
		motifKeys.append(aminoAcidKeys[char])
	print motifKeys,'\n'

	with open(filename + '.pdb', 'r') as file:
		for line in file:
			# Find section with residue sequences
			if "SEQRES" in line and any(aa in line for aa in aminoAcids):
				mylist = line.split()
				for word in mylist:
					if word in aminoAcids:
						counter[word] += 1

	print counter




class Test(unittest.TestCase):
	ex1 = """SEQRES   1 A  239  GLY ARG ARG ILE GLN GLY GLN ARG ARG GLY ARG GLY THR
		  SEQRES   2 A  239  SER THR PHE ARG ALA PRO SER HIS ARG TYR LYS ALA ASP        
		  SEQRES   3 A  239  LEU GLU HIS ARG LYS VAL GLU ASP GLY ASP VAL ILE ALA         
		  SEQRES   4 A  239  GLY THR VAL VAL ASP ILE GLU HIS ASP PRO ALA ARG SER          
		  SEQRES   5 A  239  ALA PRO VAL ALA ALA VAL GLU PHE GLU ASP GLY ASP ARG          
		  SEQRES   6 A  239  ARG LEU ILE LEU ALA PRO GLU GLY VAL GLY VAL GLY ASP          
		  SEQRES   7 A  239  GLU LEU GLN VAL GLY VAL ASP ALA GLU ILE ALA PRO GLY          
		  SEQRES   8 A  239  ASN THR LEU PRO LEU ALA GLU ILE PRO GLU GLY VAL PRO          
		  SEQRES   9 A  239  VAL CYS ASN VAL GLU SER SER PRO GLY ASP GLY GLY LYS          
		  SEQRES  10 A  239  PHE ALA ARG ALA SER GLY VAL ASN ALA GLN LEU LEU THR          
		  SEQRES  11 A  239  HIS ASP ARG ASN VAL ALA VAL VAL LYS LEU PRO SER GLY          
		  SEQRES  12 A  239  GLU MET LYS ARG LEU ASP PRO GLN CYS ARG ALA THR ILE          
		  SEQRES  13 A  239  GLY VAL VAL GLY GLY GLY GLY ARG THR ASP LYS PRO PHE          
		  SEQRES  14 A  239  VAL LYS ALA GLY ASN LYS HIS HIS LYS MET LYS ALA ARG          
		  SEQRES  15 A  239  GLY THR LYS TRP PRO ASN VAL ARG GLY VAL ALA MET ASN          
		  SEQRES  16 A  239  ALA VAL ASP HIS PRO PHE GLY GLY GLY GLY ARG GLN HIS          
		  SEQRES  17 A  239  PRO GLY LYS PRO LYS SER ILE SER ARG ASN ALA PRO PRO          
		  SEQRES  18 A  239  GLY ARG LYS VAL GLY ASP ILE ALA SER LYS ARG THR GLY          
		  SEQRES  19 A  239  ARG GLY GLY ASN GLU """ 

	def test_pdbScraper(self):
		for [test_pdb, expected] in self.ex1:
			actual = pdb_Scraper(test_pdb)
			self.assertEqual(actual, expected)


if __name__ == "__main__":
	pdbScraper()
    #unittest.main()