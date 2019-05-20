import pyodbc
import CustomerFile

def Connect():
    return pyodbc.connect('Driver={SQL Server};'
                      'Server=10.1.10.114,1434;'
                      'Database=TestDB;'
                      'Trusted_Connection=no;'
                      'UID=ugoadmin;'
                      'PWD=ugo-2019')

def ReadData(query):
    conn = Connect()
    reader = conn.cursor()
    reader.execute(query)
    rowResults = []
    for row in reader:
        columnsResults = []
        for column in row:
            columnsResults.append(column)
        rowResults.append(columnsResults)
    reader.close()
    conn.close()
    return rowResults

def WriteData(query):
    conn = Connect()
    writer = conn.cursor()
    writer.execute(query)
    writer.close()
    conn.commit()
    conn.close()
def SelectData(query):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.commit()
    conn.close()


