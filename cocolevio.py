def listCompanies(group):
	#Assuming the program doesn't have info on buyer companies, program reads in data from txt doc for info on buyer companies
	buyers = []
	for line in group:
		line = line.strip()
		line = line.split(' ')
		sub = []
		for item in line:
			sub.append(item)
		buyers.append(sub)
	return(buyers) #List of buyer info [[company][amount][price]]

def pricePer(buyers):
	#Calculate the price that each company is paying for one unit of material
	sellTo = {} #Dictionary of Company names and their corresponding prices per unit
	amnts = {} #Dictionary of the amount of material they buy and their prices per unit (ranking)
	
	#Get number of companies, assuming each selling company has a different number of potential buyers
	length = 0  
	for sublist in buyers:
		for comps in sublist:
			length += 1
		break

	#Get price per unit for each company
	track = 1 
	x = 0
	while(x <= (length)):  #Do this for each company
		if(track == (length)): #Look at each category and repeat for each company
			track = 1
		name = buyers[0][track]
		amount = int(buyers[1][track])
		price = int(buyers[2][track])
		ppunit = price/amount #price per unit

		#add company price per units to dictionaries
		sellTo[name] = ppunit
		amnts[amount] = ppunit
		track += 1 
		x+=1 
	return(sellTo,amnts)

def materialConstraints(matAmnt, amounts):
	count = 0
	next = 0
	totalSale = 0
	theseGuys = []
	newMat = matAmnt
	for item in amounts:
		amnt = amounts[next][0]
		price = (amounts[next][1]) * amnt #because this is price per unit
		matAmnt = matAmnt - amnt
		if(matAmnt >= 0):
			totalSale += price #assuming table gives total amount paid for amount of material in table
			theseGuys.append(amnt)
			newMat -= amnt
		else:
			matAmnt = newMat
			theseGuys.append(-1)
		next += 1
	return(theseGuys, newMat, totalSale)


def main():

	#Let's get some info first
	matAmnt = float(input("Enter the amount of material available: "))
	initCost = float(input("Enter the amount the material was bought for: "))
	
	#Get list of sample data buyer companies, assuming that info is in a reachable file
	possComp = input("Enter name of data sheet: ")
	buyerss = "./{}".format(possComp)
	buyertxt = open(buyerss, "r")
	buyers = listCompanies(buyertxt)
	buyertxt.close()

	#Calculate price at which each company is buying material per unit, as well as amounts required by each company
	ppunit, amnts = pricePer(buyers)

	#Give me a list filtered by price per unit (high to low). Convert dictionary to list
	sortList = [(k,v) for v,k in sorted([(v,k) for k,v in ppunit.items()], reverse = True)] #Sorting by values (price per unit)
	amntList = [(k,v) for v,k in sorted([(v,k) for k,v in amnts.items()], reverse = True)]
	# ^^^ Got help from http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/  Stupid Python Tricks
	
	#Get the customer names that should be prioritzed, given the amount of material available 
	#The companies you should sell to, how much material is left after all sales, how much you profit
	who, leftOver, totalSale = materialConstraints(matAmnt, amntList)
	print('\n')
	print("Sell To: ")
	counter = 0
	for person in who: #Skip over the names of companies we don't want to sell to (parallel name list)
		if(who[counter] == -1):
			counter +=1
		else: #Print who we do want to sell to
			print(str(sortList[counter][0] )+ " who will buy " + str(who[counter]) + " units")
			counter+=1
	print("For a total profit of: $%.2f" % (totalSale - initCost))
	print("With a remaining " + str(leftOver) + " units of material left over")

	
	#Print the list of prices per unit out for humans to (easily) read, so buying companies can make alternated decisions
	print('\n')
	print("Customer Companies Ranked by Price Payabale Per Unit")
	track = 0
	for i in sortList: #This loop prints a prettier (relatively speaking :( )) list 
		print(str(sortList[track][0]) + " at $%.2f" % (sortList[track][1]))
		track += 1
	print('\n')


main()






