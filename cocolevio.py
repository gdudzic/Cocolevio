
def profits(company, amount, price, material):
	#Calculate sale for sub company A
	sale = price * amount

	#Calculate total sale of all material to sub company A
	numPurchase = 1
	materialOrig = material
	while(material >= 0):
		newSale = price * numPurchase #sub Company A purchasing material
		material = material - amount #Material avaiable to purchase decreasing
		numPurchase += 1 #setting up loop for next purchase from sub company A
	finalSale = newSale
	materialLeft = material
	print("Company, " + company + ", makes " + str(numPurchase)+ " purchases of " + str(materialOrig - materialLeft) + " units of material for a total of $" + str(finalSale))

def main():
	test = profits("Bob's Bytes", 10, 30, 600)
		
main()