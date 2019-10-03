#This program asks a user for a sequence input, prints the complementary strand, 
#reverse complementary strand, locates any invalid bases or characters, and any start codons and their position. 
#This was part of a homework/lab assignment, completed in BINF6111 Fall 2018
#Claire Menard


def getSequence(seq):
	CompSeq = ""
	invalid = ""
	for base in seq:
		if base == "A":
			CompSeq += "T"
		elif base == "T":
			CompSeq += "A"
		elif base == "C":
			CompSeq += "G"
		elif base == "G":
			CompSeq += "C"
		else:
			CompSeq += "N"
	print("This is the complementary sequence: " + CompSeq + "\n--------------------------------------")
	for n in range(len(CompSeq)):
		if CompSeq[n] == "N":
			invalid += ((str(n+1)) + "  ")
		else:
			continue
	print("Invalid base character found at: " + invalid + "\n--------------------------------------")

def getRevSequence(seq):
	RevCompSeq = ""
	invalid2 = ""
	for base in seq:
		if base == "A":
			RevCompSeq = "T" + RevCompSeq
		elif base == "T":
			RevCompSeq = "A" + RevCompSeq
		elif base == "C":
			RevCompSeq = "G" + RevCompSeq
		elif base == "G":
			RevCompSeq = "C" + RevCompSeq
		else:
			RevCompSeq = "N" + RevCompSeq
	print("This is the reverse complementary sequence: " + RevCompSeq + "\n--------------------------------------")
	for n in range(len(RevCompSeq)):
		if RevCompSeq[n] == "N":
			invalid2 += ((str(n+1)) + "  ")
		else:
			continue
	print("Invalid base character found at: " + invalid2 + "\n--------------------------------------")
	return RevCompSeq


def findStartCodon(RevCompSeq):
	startCodons = ""
	for x in range(len(RevCompSeq)):
		if RevCompSeq[x:x+3] == "ATG":
			startCodons += ((str(x+1)) + "  ")
	print("Start codons found at position: " + startCodons + "\n--------------------------------------")


def main():
	seq = input("Enter a sequence: ")
	getSequence(seq)
#	getRevSequence(seq)
	start = getRevSequence(seq)
	findStartCodon(start)



if __name__ == "__main__":
	main()


