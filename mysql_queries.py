#tutorial link: https://www.youtube.com/watch?v=3vsC05rxZ8c&t=552s&ab_channel=TechWithTim

import mysql.connector
import pandas as pd 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hulCK9ky",
    database="testdatabase"

)

mycursor = db.cursor()

#sql = "CREATE TABLE Search_Rank_CA (time_tcraped VARCHAR(50), category VARCHAR(50), title VARCHAR(100), price VARCHAR(10), review_Count VARCHAR(10), unique_ID int PRIMARY KEY AUTO_INCREMENT"
#mycursor.execute("CREATE TABLE Search_Rank_CA (time_scraped VARCHAR(50), category VARCHAR(50), title VARCHAR(100), price VARCHAR(10), review_Count VARCHAR(10))")
#mycursor.execute("CREATE TABLE test(time_captured VARCHAR(5))")
#how to change the properties of the table
#mycursor.execute("ALTER TABLE search_rank_ca CHANGE title title VARCHAR(1000)")
#how to delete a table 
#mycursor.execute("DROP TABLE search_rank_ca")

mycursor.execute("SELECT * FROM search_rank_ca")
table_rows = mycursor.fetchall()
df = pd.DataFrame(table_rows)
df.columns=["time_scraped","category","title","price","review_Count"]
#how to search for all results by catgory based on mulltiple conditions
#print(df.loc[(df['category'] == 'cookies') & (df['time_scraped'] == '22/11/2020')])     


'''
names of tables:
search_rank_ca
sponsored_products_ca
'''
