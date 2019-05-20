import DB
import CustomerFile
import datetime

from DB import ReadData as DBReadData, WriteData as DBWriteData, SelectData as DBSelectData
from CustomerFile import Customer
from datetime import date

def AddCustomer(johnDoe):
    AddtoCustomer(johnDoe)
    AddToCustomerListID(johnDoe)
    AddToEmail(johnDoe)
    AddToPhoneNumbers(johnDoe)
    AddToAddresses(johnDoe)

def AddtoCustomer(johnDoe):
    default = 'INSERT INTO Customer(CustID, Created, LastSeen, TotalNoOfOrders, BasketSum, BasketAvg, PriceSum, PriceAvg, CustStatus, CustName) VALUES'
    unique = "("+str(johnDoe.custID) +",'"+ToAcceptableDate(johnDoe.created)+"','"+ToAcceptableDate(johnDoe.lastSeen)+"',"+str(johnDoe.totalNoOfOrders)+","+ str(johnDoe.basketSum)+","+str(johnDoe.basketAvg)+","+str(johnDoe.priceSum)+","+ str(johnDoe.priceAvg)+",'"+johnDoe.custStatus+"','"+johnDoe.custName+"')"
    query = default + unique
    DB.SelectData('SELECT * FROM Customer')
    DBWriteData(query)

def AddToCustomerListID(johnDoe):
    d1 = date(2015,1,1)
    d2 = date(2016,1,1)
    d3 = date(2017,1,1)
    d4 = date(2018,1,1)
    d5 = date(2019,1,1)
    custListID = '2015' if d1 <= johnDoe.created < d2 else '2016' if d2 <= johnDoe.created < d3 else '2017' if d3 <= johnDoe.created < d4 else '2018' if d4 <= johnDoe.created < d5 else '2019'
    query = 'INSERT INTO Customer_ListID(ListID, CustID) VALUES (' + custListID + ',' + str(johnDoe.custID)+')'
    DBWriteData(query)

def AddToEmail(johnDoe):
    default = 'INSERT INTO Customer_Email(CustID, Email) VALUES '
    for email in johnDoe.emails.emails:        
        DBWriteData(default + '(' + str(johnDoe.custID) + ",'"+ email +"')")

def AddToPhoneNumbers(johnDoe):
    default = 'INSERT INTO Customer_PhoneNo(PhoneNo, CustId) VALUES '
    for number in johnDoe.numbers.numbers:
        DBWriteData(default + '('+str(number)+','+str(johnDoe.custID)+')')

def AddToAddresses(johnDoe):
    default = 'INSERT INTO Customer_Address(StreetAddress, City, CState, ZipCode, CustId) VALUES '
    for address in johnDoe.addresses.addresses:
        DBWriteData(default + "('"+ address.streetAddress+"','"+address.city+"','"+address.state+"',"+str(address.zipCode)+','+str(johnDoe.custID) +')')

def WriteToCustomerList():
    query = '''INSERT INTO CustomerList(ListID, Title) VALUES
            ('2015', 'title'),
            ('2016', 'another?'),
            ('2017', 'title2?'),
            ('2018', 'another2?'),
            ('2019', 'again')'''
    DBWriteData(query)

def ToAcceptableDate(temp):
    return str(temp.year) + '-' + TwoDig(temp.month) + '-' + TwoDig(temp.day)

def TwoDig(number):
    return str(number) if number >= 10 else '0'+str(number)