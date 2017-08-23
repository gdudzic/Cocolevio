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
		track += 1
		x+=1
	return(sellTo)


def main():

	#Get list of sample data buyer companies
	possComp = input("Enter name of data sheet: ")
	buyerss = "./{}".format(possComp)
	buyertxt = open(buyerss, "r")
	buyers = listCompanies(buyertxt)
	buyertxt.close()
	#print(buyers)

	#Calculate price at which each company is buying material per unit 
	ppunit = pricePer(buyers)

	#Give me a list filtered by price per unit (high to low). Convert dictionary to list
	sortList = [(k,v) for v,k in sorted([(v,k) for k,v in ppunit.items()], reverse = True)] #Sorting by values (price per unit)
	#Got help from http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/  Stupid Python Tricks 
	
	#Print the list out for humans to (easily) read
	print('\n')
	print("Customer Companies Ranked by Profit Yields (highest to lowest)")
	track = 0
	for i in sortList: #This loop prints a prettier (relatively speaking :( )) list 
		print(str(sortList[track][0]) + " buys one unit for $%.2f" % (sortList[track][1]))
		track += 1
	print('\n')
main()








