import DB
import CustomerFile
import datetime

from DB import ReadData
from CustomerFile import Customer
from datetime import date

def AddCustomer(johnDoe):
    print ('started add to customer')
    AddtoCustomer(johnDoe)
    print ('passed add to cust. Started custlist')
    AddToCustomerList(johnDoe)
    print ('pass that, on to emails')
    AddToEmail(johnDoe)
    print ('passed that, on to numbers')
    AddToPhoneNumbers(johnDoe)
    print ('passed that, on to addresses')
    AddToAddresses(johnDoe)

def AddtoCustomer(johnDoe):
    default = 'INSERT INTO Customer(CustID, Created, LastSeen, TotalNoOfOrders, BasketSum, BasketAvg, PriceSum, PriceAvg, CustStatus, CustName) VALUES'
    print ('add check 1')
    unique = '('+johnDoe.CustID +','+johnDoe.Created+','+johnDoe.CustID+','+johnDoe.LastSeen+','+johnDoe.TotalNoOfOrders+','+johnDoe.BasketSum+','+johnDoe.BasketAvg+','+johnDoe.PriceSum+','+johnDoe.PriceAvg+','+johnDoe.CustStatus+','+johnDoe.CustName+')'
    print ('add check 2')
    query = default + unique
    print (query)
    DB.WriteData(query)

def AddToCustomerList(johnDoe):
    d1 = date(2015,1,1)
    d2 = date(2016,1,1)
    d3 = date(2017,1,1)
    d4 = date(2018,1,1)
    d5 = date(2019,1,1)
    custListID = '2015' if d1 <= johnDoe.Created < d2 else '2016' if d2 <= johnDoe.Created < d3 else '2017' if d3 <= johnDoe.Created < d4 else '2018' if d4 <= johnDoe.Created < d5 else '2019'
    query = 'INSERT INTO Customer_ListID(ListID, CustID) VALUES (' + custListID + ',' + johnDoe.CustID+')'
    DB.WriteData(query)

def AddToEmail(johnDoe):
    default = 'INSERT INTO Customer_Emails(Email, CustID) VALUES'
    for email in johnDoe.emails.emails:
        unique = '('+email+ ',' +johnDoe.CustID+')'
        query = default + unique
        DB.WriteData(query)

def AddToPhoneNumbers(johnDoe):
    default = 'INSERT INTO Customer_PhoneNo(PhoneNo, CustId) VALUES'
    for number in johnDoe.numbers.numbers:
        unique = '('+number+','+johnDoe.CustID+')'
        query = default + unique
        DB.WriteData(query)

def AddToAddresses(johnDoe):
    default = 'INSERT INTO Customer_Address(StreetAddress, City, CState, ZipCode, CustId) VALUES'
    for address in johnDoe.addresses.addresses:
        unique = '('+ address.StreetAddress+','+address.City+','+address.state+','+address.zipCode+','+johnDoe.CustID +')'
        query = default + unique
        DB.WriteData(query)