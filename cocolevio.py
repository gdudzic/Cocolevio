def listCompanies(group):
	#program reads in data from txt doc for companies instead of beginning with that info
	buyers = []
	for line in group:
		line = line.strip()
		line = line.split(' ')
		sub = []
		for item in line:
			sub.append(item)
		buyers.append(sub)
	return(buyers)

def pricePer(customers):
	#Calculate the price per unit that each company is buying for
	buyers = customers
	sellTo = {}
	amnts = {}
	
	#Get number of companies
	length = 0  
	for sublist in buyers:
		for comps in sublist:
			length += 1
		break
	#print(length)

	#Get price per unit for each company
	track = 1 
	x = 0
	while(x <= (length)): #why plus one??? 
		if(track == (length)):
			track = 1
		name = buyers[0][track]
		amount = int(buyers[1][track])
		price = int(buyers[2][track])
		ppunit = price/amount #price per unit
		#sale = price * amount

		#add company price per units to a dictionary
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
		matAmnt = matAmnt - amnt
		if(matAmnt >= 0):
			price = (amounts[next][1]) * amnt #because this is price per unit
			totalSale += price #assuming table gives total amount paid for amount of material in table
			theseGuys.append(amnt)
			next += 1
			newMat -= amnt
	return(theseGuys, newMat, totalSale)


def main():

	matAmnt = float(input("Enter the amount of material available: "))
	initCost = float(input("Enter the amount the material was bought for: "))
	#Get list of sample data buyer companies
	possComp = input("Enter name of data sheet: ")
	buyerss = "./{}".format(possComp)
	buyertxt = open(buyerss, "r")
	buyers = listCompanies(buyertxt)
	buyertxt.close()
	#print(buyers)

	#Calculate price at which each company is buying material per unit 
	ppunit, amnts = pricePer(buyers)

	#Give me a list filtered by price per unit (high to low). Convert dictionary to list
	sortList = [(k,v) for v,k in sorted([(v,k) for k,v in ppunit.items()], reverse = True)] #Sorting by values (price per unit)
	amntList = [(k,v) for v,k in sorted([(v,k) for k,v in amnts.items()], reverse = True)]
	#print(amntList)
	#Got help from http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/  Stupid Python Tricks 
	
	#Get the customer names that should be sold to given the amount of material available 
	print('\n')
	print("Sell To: ")
	who, leftOver, totalSale = materialConstraints(matAmnt, amntList)
	customers = []
	counter = 0
	for person in who:
		print(str(sortList[counter][0] )+ " who will buy " + str(who[counter]) + " units")
		counter+=1
	print("For a total profit of: $%.2f" % (totalSale - initCost))
	print("With a remaining " + str(leftOver) + " units of material left over")

	



	#Print the list out for humans to (easily) read
	print('\n')
	print("Customer Companies Ranked by Price Payabale Per Unit")
	track = 0
	for i in sortList: #This loop prints a prettier (relatively speaking :( )) list 
		print(str(sortList[track][0]) + " at $%.2f" % (sortList[track][1]))
		track += 1
	print('\n')


main()






