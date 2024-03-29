import pyodbc
testdb_columns = 'First, Middle, Last, Street, City, State, Zip, SSN, Bureau'
connection_string = 'Driver={SQL Server};Server=.\\SQLEXPRESS;Database=test;Trusted_Connection=true'  # escape char

cnct = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=test;Trusted_Connection=true')
# r to read without escaping
cursor = cnct.cursor()  # cursor is the connection to the database drivers
cursor.execute("insert into TestUsers(First, Middle, Last, Street, City, State, Zip, SSN) "
               "values ('Mary', 'Z', 'Bernard', 'PO Box 190648', 'Anchorage', 'AK', '99519', '666016220')")
cnct.commit()  # without a commit the sql commands are only staged in memory
