def pricePer(customers):
	buyers = customers
	#Calculate the price per unit that each company is buying for
	sellTo = {}
	track = 0
	for x in buyers:
		name = buyers[track][0]
		amount = buyers[track][1]
		price = buyers[track][2]
		ppunit = price/amount #price per unit
		sale = price * amount

		#add company price per units to a dictionary
		sellTo[name] = ppunit
		track += 1
	return(sellTo)

def main():
	#Companies [company, amount, price]
	buyers = [['Company A',1,1],['Company B',2,5],['Company C',3,8],['Company D',4,9],['Company E',5,10],['Company F',6,17],['Company G',7,17],['Company H',8,20],['Company I',9,24],['Company',10,30]] #Data
	ppunit = pricePer(buyers)
	print(sorted(ppunit.values()))


main()