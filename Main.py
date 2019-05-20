import Create
import DB
import CustomerFile
import Update

from DB import ReadData
from CustomerFile import Customer



def __main__():
    allCustomersRaw = ReadData('SELECT * FROM Customer')
    allCustomers = MakeThemCustomers(allCustomersRaw)
    PrintCustomers(allCustomers)
    input()

def PrintCustomers(allCustomers):
    for customer in allCustomers:
        print (customer.ToStringSmall(customer))

def MakeThemCustomers(oldList):
    customers = []
    for columnResult in oldList:
        customers.append(Customer(columnResult[0],columnResult[1],columnResult[2],columnResult[3],columnResult[4],columnResult[5],columnResult[6], columnResult[7],columnResult[8],columnResult[9]))
    return customers


if __name__ == "__main__":
    __main__()