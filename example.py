# class Car(object):
#     def __init__(self,price,speed,fuel,mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if (self.price > 10000):
#             self.tax = 0.15
#         else:
#             self.tax = 0.12
#         self.displayAll()

#     def displayAll(self):
#         print "Price: $" +str(self.price)
#         print "Speed: " +str(self.speed)+ " MPH"
#         print "Mileage: " +str(self.mileage)+ " MPG"
#         print "Fuel: " +self.fuel
#         print "Tax: " +str(self.tax)
#         print "\n"

# car1 = Car(9000,60,"Full",22) 
# car2 = Car(2100,30,"Full",17) 
# car3 = Car(5500,70,"Empty",98) 
# car4 = Car(91000,160,"Full",8) 
# car5 = Car(300,21,"Half",2700)
# car6 = Car(40000, 45, "Empty", 206007)

class Product(object):
    def __init__(self, price, itemName, weight, brand, Cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = Cost
        self.status = "for sale"
        

    def display_info(self):
        print 'Price: {}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}'.format(str(self.price), str(self.itemName), str(self.weight), str(self.brand),str(self.cost), self.status)
        print ""
        return self

    def sell(self):
        self.status = "sold"
        return self
        
    def addTax(self):
        tax = .08*self.price
        total = self.price + tax
        return total

    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "for sale"
            self.price *= .8
        return self


turkey = Product(30, "turkey", "0.5 lbs", "Trader Joes", 20)
turkey.display_info()
print turkey.addTax()
print ""
turkey.returnItem("opened").display_info()