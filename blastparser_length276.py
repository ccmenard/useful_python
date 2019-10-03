#Claire Menard
#Blast output parser- part of progrmaming project for broccoli miRNAs that are shorter than 276 in length
#Make class that models hits
#Look through the file for the classes, write a function that takes a file and creates instances of each class, return an array of instances (hit.length)
#Within that instance, you have the stored properties (we at least want the length)
#Loop through that array of hits and remove ones that don't meet our length requirement, writes each line as output to txt file

class blast_hits:
	def __init__(self, file):
		self.file = file
		self.sequence = []
		self.idFound = False
		self.queryStarted = False
		self.sequenceFound = False
		self.query = None
		self.resultsArray = []
		with open(self.file, 'r') as f:
			for line in f:
				if line.startswith("Query= "):
					query = line.split(" ")[1]
					self.idFound = True
				if line.startswith(">"):
					self.sequenceFound = True
				if line.startswith("Length") and self.idFound == True and self.sequenceFound == True:
					length = int(line.split("=")[1])
					if length < 276 :
						self.sequence.append(query)
						self.sequence.append(length)
						self.sequenceFound = False
				if line.startswith("*") and self.idFound == True and self.sequenceFound == False:
					query = None

	def print_seq(self):
		print(self.sequence)
	
		
file = blast_hits("small_blastoutput-1-1.txt")
file.print_seq()

