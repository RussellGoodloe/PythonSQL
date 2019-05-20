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
    AddToCustomerListID(johnDoe)
    print ('pass that, on to emails')
    AddToEmail(johnDoe)
    print ('passed that, on to numbers')
    AddToPhoneNumbers(johnDoe)
    print ('passed that, on to addresses')
    AddToAddresses(johnDoe)

def AddtoCustomer(johnDoe):
    #default = 'INSERT INTO Customer(CustID, Created, LastSeen, TotalNoOfOrders, BasketSum, BasketAvg, PriceSum, PriceAvg, CustStatus, CustName) VALUES'
    #print ('add check 1')
    #unique = '('+str(johnDoe.CustID) +','+str(johnDoe.Created)+','+str(johnDoe.LastSeen)+','+str(johnDoe.TotalNoOfOrders)+','+str(johnDoe.BasketSum)+','+str(johnDoe.BasketAvg)+','+str(johnDoe.PriceSum)+','+str(johnDoe.PriceAvg)+','+str(johnDoe.CustStatus)+','+str(johnDoe.CustName)+')'
    #unique = '''(1116969,date(2018,5,5),date(2019,4,8),25,100,4,600,24,'Active','John Doe')'''
    #print ('add check 2')
    query = '''INSERT INTO Customer(CustID, Created, LastSeen, TotalNoOfOrders, BasketSum, BasketAvg, PriceSum, PriceAvg, CustStatus, CustName) VALUES 
                ('''+str(johnDoe.custID)+''','2018-04-08','2019-05-07',25,100,4,600,24,'Active','John Doe')'''
    #query = default + unique
    #print (query)
    query2 = 'SELECT * FROM Customer'
    DB.SelectData(query2)
    print ('check')
    DB.WriteData(query)

def AddToCustomerListID(johnDoe):
    d1 = date(2015,1,1)
    d2 = date(2016,1,1)
    d3 = date(2017,1,1)
    d4 = date(2018,1,1)
    d5 = date(2019,1,1)
    custListID = '2015' if d1 <= johnDoe.created < d2 else '2016' if d2 <= johnDoe.created < d3 else '2017' if d3 <= johnDoe.created < d4 else '2018' if d4 <= johnDoe.created < d5 else '2019'
    query = 'INSERT INTO Customer_ListID(ListID, CustID) VALUES (' + custListID + ',' + str(johnDoe.custID)+')'
    DB.WriteData(query)

def AddToEmail(johnDoe):
    default = 'INSERT INTO Customer_Email(Email, CustID) VALUES'
    for email in johnDoe.emails.emails:
        unique = '('+email+ ',' +str(johnDoe.custID)+')'
        query = default + unique
        DB.WriteData(query)

def AddToPhoneNumbers(johnDoe):
    default = 'INSERT INTO Customer_PhoneNo(PhoneNo, CustId) VALUES'
    for number in johnDoe.numbers.numbers:
        unique = '('+str(number)+','+str(johnDoe.custID)+')'
        query = default + unique
        DB.WriteData(query)

def AddToAddresses(johnDoe):
    default = 'INSERT INTO Customer_Address(StreetAddress, City, CState, ZipCode, CustId) VALUES'
    for address in johnDoe.addresses.addresses:
        unique = '('+ address.streetAddress+','+address.city+','+address.state+','+str(address.zipCode)+','+str(johnDoe.custID) +')'
        query = default + unique
        DB.WriteData(query)

def WriteToCustomerList():
    query = '''INSERT INTO CustomerList(ListID, Title) VALUES
            ('2015', 'title'),
            ('2016', 'another?'),
            ('2017', 'title2?'),
            ('2018', 'another2?'),
            ('2019', 'again')'''
    DB.WriteData(query)