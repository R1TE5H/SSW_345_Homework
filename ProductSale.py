# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __remaining_inventory: int # A new private variable for inventory remaining

    def __init__(self, sale: Sale, number: int): # Added a parameter for initializing inventory
        self.__lastSale = sale
        self.__remaining_inventory = number
        print(f"Product created with {self.getInventory()} items in inventory")

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self
    
    def getInventory(self) -> int:
        return self.__remaining_inventory           # Method for getting inventory
    
    def productSold(self):
        self.__remaining_inventory -= 1         # Method for updating inventory after sale

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].productSold()          # Calling Method to update inventory

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, number=10)
productTwo = Product(sale=None, number=9)


saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"\nLast Sale Number for Product One{productOne.getLastSale.getSaleNumber} \nLast Sale Number for Product Two{productTwo.getLastSale.getSaleNumber}\n")
print(f"Number of Product One remaining: {productOne.getInventory()} \nNumber of Product Two remaining: {productTwo.getInventory()}")
