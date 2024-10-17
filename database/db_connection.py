import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Lonewolf@31',
        database='weather_website'
    )
