import os
import cx_Oracle
import csv
import time

#SQL command to extract the report WHATEVER.csv
SQL=''' select * from help where topic = 'ACCEPT' '''

#timestamp
timestr = time.strftime("%d-%m-%Y_%H:%M:%S")

filename='/interfaces/custom_sql/Extracao/utl_file_dir/WHATEVER'+timestr+'.csv'
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')

#setting system variables
#os.putenv('ORACLE_HOME', '/u01/app/oracle/product/12.1.0/dbhome_1')
#os.putenv('LD_LIBRARY_PATH', '/u01/app/oracle/product/12.1.0/dbhome_1/lib')

#connection with Oracle DB
print "Realizando conexao com o Banco de Dados..."
connection = cx_Oracle.connect('system/oracle@127.0.0.1/orcl')

cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
	output.writerow(row)
cursor.close()
connection.close()
FILE.close()

print "END of extraction"