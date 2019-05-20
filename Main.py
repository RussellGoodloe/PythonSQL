import Create
import DB
import CustomerFile
import Update
import datetime

from DB import ReadData
from CustomerFile import Customer, Address, CustomerEmails, CustomerAddresses, CustomerPhoneNumbers
from datetime import date

def __main__():

    emails = ['''johnD@ugollc.com''','''JohhnyBoy@gmail.com''']
    emailList = CustomerEmails(1116969,emails)
    address1 = Address('1431 Hackberry Ln','Tuscaloosa','AL',35401)
    address2 = Address('1613 11th st','Tuscaloosa','AL',35401)
    addresses = [address1,address2]
    addressList = CustomerAddresses(1116969,addresses)
    phoNo = 2054318071
    phoNo2 = 2514087651
    phones = [phoNo,phoNo2]
    phoneList = CustomerPhoneNumbers(1116969, phones)
    johnDoe = Customer(1116969,date(2018,5,5),date(2019,4,8),25,100,4,600,24,'Active','John Doe',emailList,addressList,phoneList)
    Create.AddCustomer(johnDoe)
    try:
        #Create.WriteToCustomerList()
        Create.AddCustomer(johnDoe)
        print ('no way')
    except:
        print ('no dice brah')
    input()

# def PrintCustomers(allCustomers):
#     for customer in allCustomers:
#         print (customer.ToStringSmall(customer))

# def MakeThemCustomers(oldList):
#     customers = []
#     for columnResult in oldList:
#         customers.append(Customer(columnResult[0],columnResult[1],columnResult[2],columnResult[3],columnResult[4],columnResult[5],columnResult[6], columnResult[7],columnResult[8],columnResult[9]))
#     return customers


if __name__ == "__main__":
    __main__()