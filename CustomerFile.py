
class Customer:
    def __init__(self, custID, created, lastSeen, totalNoOfOrders, basketSum, basketAvg, priceSum, priceAvg, custStatus, custName, emails, addresses, numbers):
        self.custID = custID
        self.created = created
        self.lastSeen = lastSeen
        self.totalNoOfOrders = totalNoOfOrders
        self.basketSum = basketSum
        self.basketAvg = basketAvg
        self.priceSum = priceSum
        self.priceAvg = priceAvg
        self.custStatus = custStatus
        self.custName = custName
        self.emails = emails
        self.addresses = addresses
        self.numbers = numbers

    @staticmethod
    def ToStringSmall(customer):
        return str(customer.custID) + " | " + str(customer.custName) + " | " + str(customer.custStatus) + " | " + str(customer.totalNoOfOrders)


    class CustomerEmails:
        def __init__(self, custID, emails):
            self.custID = custID
            self.emails = emails

    class CustomerAddresses:
        def __init__(self, custID, addresses):
            self.custID = custID
            self.addresses = addresses

    class CustomerPhoneNumbers:
        def __init__(self, custID, numbers):
            self.custID = custID
            self.numbers = numbers

class Address:
    def __init__(self, streetAddress, city, state, zipCode):
        self.streetAddress = addresses
        self.city = city
        self.state = state
        self.zipCode = zipCode