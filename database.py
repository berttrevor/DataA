from psycopg2 import connect
import csv
# connect to the database
# connect = connect(database= 'crime', user ='postgres', password ='admin')
# cursor = connect.cursor()
# cursor.execute('')
# connect.commit()

con = connect(database='crime', user= 'postgres', password='admin')
cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS offencecode (offenceCode VARCHAR(50) PRIMARY KEY);""")

# with open ('data/offencecode.csv', 'r') as d:
#     sql_f = """
#             COPY offencecode FROM stdin WITH CSV HEADER DELIMITER as ',' 
#             """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()
# con.close()


# con = connect(database='crime', user= 'postgres', password='admin')
# cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS  referencOffence (OffenceCode VARCHAR (25),
# offenceDescription VARCHAR(100),
# oldPRCOffenceGroup VARCHAR(100),
# oldOffenceSubGroup VARCHAR(100),
# newONSOffenceGroup VARCHAR(100),
# newONSSubOffenceGroup VARCHAR(100),
# Foreign key (OffenceCode)
# references
# offencecode(offenceCode));""")

# with open ('data/ReferenceTableOffences.csv', 'r') as d:
#     sql_f = """
#             COPY referencOffence FROM stdin WITH CSV HEADER DELIMITER as ',' 
#             """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()
# con.close()

con = connect(database='crime', user= 'postgres', password='admin')
cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS offenceDetails (
# FinancialYear VARCHAR (50),
# FinancialQuarter INT ,
# ForceName VARCHAR (100),
# OffenceDescription VARCHAR (200),
# OffenceGroup VARCHAR (100),
# OffenceSubgroup VARCHAR (100),
# OffenceCode VARCHAR(200),
# NumberOfOffences INT,
# Foreign key (OffenceCode)
# references
# offenceCode(offenceCode));""")

# with open ('data/2012-13.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()
# con.close()


# with open ('data/2013-14.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()


# with open ('data/2014-15.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()

# cur.execute('INSERT INTO offencecode(offenceCode) VALUES(\'4.10\')')
# con.commit()    
# with open ('data/2015-16.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()


# with open ('data/2016-17.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()
    
# with open ('data/2017-18.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()
    
# with open ('data/2018-19.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()    
   
# with open ('data/2019-20.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit() 

# with open ('data/2020-21.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit() 

# with open ('data/2021-22.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit()    
  

# with open ('data/2022-23.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit() 
# cur.execute('INSERT INTO offencecode(offenceCode) VALUES(\'280\')')
# con.commit()  
# cur.execute('INSERT INTO offencecode(offenceCode) VALUES(\'29B\')')
# cur.execute('INSERT INTO offencecode(offenceCode) VALUES(\'28O\')')
# con.commit()
# with open ('data/2023-24.csv', 'r') as d:
#     sql_f = """
#             COPY offenceDetails FROM stdin WITH CSV HEADER DELIMITER as ',' 
#              """
#     cur.copy_expert(sql=sql_f, file=d)
# con.commit() 

# cur.execute('SELECT COUNT(*) FROM offenceDetails')
# rt = cur.fetchall()[0]
# print(rt)