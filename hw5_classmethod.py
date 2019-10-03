#!/bin/bash/python3
#hw 5 with a class method
print('Claire Menard')
print('cmenard@uncc.edu')
import os 

class geneExpression:
	@classmethod
	def __init__(self, file):
		self.file = file
	@classmethod
	def overall_parse(self, file):
		self.dictionary = {}
		self.sampleID = ''
		with open(self.file, 'r') as f:
			for line in f.readlines():
				line = line.strip('\n').strip()
				cols = line.split('\t')
				key = cols[0]
				value = cols[1]
				self.dictionary[key] = value
			file_name = os.path.basename(self.infile1)
			Sample_ID = file_name.split("-")
			self.Sample_ID = Sample_ID[2]
	print('pass')

	def expression_valuesprint(self):
		return self.dictionary()




file1 = geneExpression("/Users/clairechristelmenard1/Desktop/Programming_2_S19/hw4-TCGA/TCGA-A6-2670-01A-02R-0821-07-geneExpression.txt")
print(file1.expression_valuesprint())
