def listCompanies(group):
	#Companies [company, amount, price]
	#program reads in data from txt doc for companies instead of beginning with that info
	buyers = []
	for line in group:
		line = line.strip() #No more \n woohoo! 
		line = line.split(' ')
		sub = []
		for item in line:
			sub.append(item)
		buyers.append(sub)
	return(buyers)

def pricePer(customers):
	buyers = customers
	#Calculate the price per unit that each company is buying for
	sellTo = {}
	track = 1
	for x in buyers:
		name = buyers[0][track]
		amount = int(buyers[1][track])
		price = int(buyers[2][track])
		ppunit = price/amount #price per unit
		sale = price * amount

		#add company price per units to a dictionary
		sellTo[name] = ppunit
		track += 1
		#break
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

	#Give me a list filtered by price per unit (high to low)
	sortList = [(k,v) for v,k in sorted([(v,k) for k,v in ppunit.items()], reverse = True)] #Sorting by values (price per unit)
	#Got help from http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/  Stupid Python Tricks 
	track = 0
	for i in sortList: #This loop prints a prettier (relatively speaking :( )) list 
		print(sortList[track])
		track += 1

main()








