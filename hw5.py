#!/bin/bash/python3
#Homework for BINF6112 completed Spring 2019
import glob

class geneExpressionTCGA:
	def __init__(self, variable):
		self.variable = variable
		self.dictionary = {}
		self.variable = glob.glob("/Users/clairechristelmenard1/Desktop/Programming_2_S19/hw4-TCGA/TCGA-A6-"+str(variable)+"*")
		with open(self.variable[0], 'r') as f:
			for line in f.readlines():
				line = line.strip('\n').strip()
				cols = line.split('\t')
				gene_name = cols[0]
				expression_values = cols[1]
				if expression_values != 'null':
					expression_values = float(cols[1])
				else:
					expression_values = 0
				self.dictionary[gene_name] = expression_values
				
	
	def expression_value(self):
		return self.dictionary.values()

def expression_sample_value(sampleid, gene_name):
	data1 = geneExpressionTCGA(sampleid)
	print("Given the sampleID and geneName, this is the expression value:  " + str(data1.dictionary[gene_name]))



def difference_out(sampleID1, sampleID2):
	data1 = geneExpressionTCGA(sampleID1)
	data2 = geneExpressionTCGA(sampleID2)
	with open("/Users/clairechristelmenard1/Desktop/Programming_2_S19/hw4-TCGA/output_file.txt", "w") as out:
		out.write("geneName" + "\t" "2670" + "\t" "2683" + "\t" + "Difference" + "\n")
		for key1, value1 in data1.dictionary.items():
			for key2, value2 in data2.dictionary.items():
				if key1 == key2:
					difference_calc = abs(value1 - value2)
					difference_EXTRA = str(round(difference_calc, 4))
					out.write (key1 + "	" + str(value1) + "	" + str(value2) + "	" + difference_EXTRA + "\n")

data1 = geneExpressionTCGA("2670")

data2 = geneExpressionTCGA("2683")

print(data1.expression_value())
expression_sample_value("2670", "ELMO2")
difference_out("2670", "2683")

print('Name: Claire Menard')
print('Email: cmenard@uncc.edu')

