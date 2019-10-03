#Make a story assignment
#Claire Menard

import random as r

def endGameRandom():
	num = r.randint(0,10)
	if num <=2:
		print("END OF GAME: random chance.")
		exit()

while 1:
	endGameRandom()
	try:
		choice1 = str(input("\nPart 1: It's your first day in your new lab! What's the first thing you want to do in your new role as research assistant? \n\n1. Check your email. \n2. Begin a new experiment. \n\nEnter 1 or 2: \n"))
		if choice1 == '2':
			break
		elif choice1 == '1':
			print("\nOh no! The PI walked in and saw that you weren't working! \nYou have been lab-shamed! CHOOSE AGAIN... \n---------------------------------------------------------------")
#			else:
#				print("Invalid choice, please choose 1 or 2.")
	except:
		print("Invalid choice, please choose 1 or 2.")
#			print(sys.exc_info())

if choice1 == '2':
	while 1:
		try:
			cho2opt1 = str("running Bowtie2 to align sample sequences")
			cho2opt2 = str("crossbreeding fruit to create an orange with the peel of a banana")

			choice2 = str(input("\nPart 2: An excellent choice, there's no time for frivolous, non-science things like email! \nWhat type of experiment would you like to run? \n\n1. " + cho2opt1 + "\n2. " + cho2opt2 + ", so that you can tell your friends, 'Orange you glad it isn't a banana?'"+ "\n\nEnter 1 or 2: \n"))
			if choice2 == '1' or choice2 == '2':
				break
#				else:
#					print("Invalid choice, please choose 1 or 2.")
#			except ValueError:
#				print("Please choose a numeric value (1 or 2).")
		except:
			print("Invalid choice, please choose 1 or 2.hi")


while 2:
	try:
		if choice2 == '1':
			print("\nWhat an excellent choice! Your investigation into... " + cho2opt1 + " will surely benefit all of human kind and revolutionize the way we think about everything!")
		elif choice2 == '2':
			print("\nWhat an excellent choice! Your investigation into... " + cho2opt2 + " will surely benefit all of human kind and revolutionize the way we think about everything! ")

		choice3 = str(input("\nPart 3: You make it a few steps in to your experiment when you suddenly spill chemicals all over the bench! Was it...\n\n1. Non-hazardous. \n2. Very hazardous. \n\nEnter 1 or 2: \n"))
		if choice3 == '1' or choice3 == '2':
			break
#			else:
#				print("Invalid choice, please choose 1 or 2.")
	except:
		print("Invalid choice, please choose 1 or 2.")


while 3:
	try:
		if choice3 == '1':
			print("\nOkay great, this isn't a problem!")
		elif choice3 == '2':
			print("\nUh oh, this requires some quick thinking...")

		choice4 = str(input("\nPart 4: Do you... \n\n1. Move down the bench to a different spot and pretend like it never happened. \n2. Clean up the spill, making sure to abide by proper cleaning protocol. \n\nEnter 1 or 2: \n"))
		if choice4 == '1' or choice4 == '2':
			break
#			else:
#				print("Invalid choice, please choose 1 or 2.")
	except:
		print("Invalid choice, please choose 1 or 2.")

if choice3 == '1' and choice4 == '1':
	print("\nThis will probably be okay, let's move on...")
	print("\nYou quickly work your way through the rest of the experiment, and to your surprise, the results are amazing! \nPride swells in your chest! Who would have thought you could have accomplished so much in the field of... Some science-y thing?... in just one day...")
elif choice3 == '2' and choice4 == '1':
	print("\nYou leave the spill where it is and move forward... \nLater that day, the postdoc who should have been supervising you eats a sandwich where you made the spill. \nOnce he stopped mutating, he really didn't mind the wings he grew, but the PI was really mad at you anyway. \nTime to look for another job! GAME OVER... \n------------------------------------------------------------")
	
	exit()
elif choice3 =='1' and choice4 =='2':
	print("\nYou do your due diligence and clean the spill up. Time to keep going!")
	print("\nYou quickly work your way through the rest of the experiment, and to your surprise, the results are amazing! \nPride swells in your chest! Who would have thought you could have accomplished so much in the field of... Something that hopefully makes your mom proud... in just one day...")
elif choice3 =='2' and choice4 =='2':
	print("\nDisaster averted! You kept your cool and aside from the minor chemical burns (only on the postdoc, of course) everything else was fine.")
	optionalChoice = str(" And with only the slight maiming of one postdoc! That's a win. ")
	print("\nYou quickly work your way through the rest of the experiment, and to your surprise, the results are amazing! \nPride swells in your chest! Who would have thought you could have accomplished so much in the field of... Science and Dreams... in just one day..." + optionalChoice)
		
while 4:
	try:

		choice5 = str(input("\nPart 5: Now that you have your amazing results, do you... \n\n1. Rush off to tell your PI? \n2. Attempt to replicate the results before telling your PI? \n3. Screw the PI, you did all the work anyway. Time to write a press release and practice your Nobel acceptance speech! \n\nEnter 1, 2, or 3: \n"))
		if choice5 == '1' or choice5 == '2' or choice5 == '3':
			break
#			else:
#				print("Invalid choice, please choose 1 or 2.")
	except:
		print("Invalid choice, please choose 1 or 2.")

if choice5 == '1':
	print("\nYour PI doesn't appreciate being bothered with unverified results, and quickly dismisses you from their office. Sometime later, the lazy postdoc repeats your experiment and verfies your results, but your initial contribution is largely forgotten. \n\nIn the end, you get mentioned in the acknowledgments of the paper the postdoc write in Science. \n\nGAME OVER... \n------------------------------------------------------------------")
	exit()
elif choice5 == '2':
	print("\nYour PI appreciates your diligence and commitment to reproducible science. You go on to publish the work in Nature, and upon graduating you receive numerous offers of prestigious postdoc positions. \n\nIn your memoirs, you write a touching dedication to the programming instructor who taught you the importance of verifying results. \n\nGAME OVER... \n--------------------------------------------------------------------")
	exit()
elif choice5 == '3':
	print("\nYour PI doesn't appreciate your attempt at going behind their back, but once media outlets pick up the story of your accomplishments, there's no stopping you. \n\nIn a surprise move, the University fires your PI and offers you their tenured position. Your experiment leads to numerous other breakthroughs, eventually leading \nto human life expectancy tripling and humanity's first contact with alien life (turns out they like waffle fries). \nA monument is built in dedication to you on New Earth. \n\nGAME OVER... \n-----------------------------------------------------------------------")
	exit()




















