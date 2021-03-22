import mysql.connector as mysql
class mysql():    

    mydb=None
    mycursor=None

    def __init__(self):
        self.mydb = mysql.connect(
                host="localhost",
                user="root",
                password="1234",
                database="product_price_tracker"
                )
        self.mycursor = mydb.cursor()

    def add_to_sql(self, url, website, price):
            sql = 'Insert into price(url, price, website) values(%s,%s,%s);'
            self.mycursor.exceute(sql,(url,price,website))
            self.mydb.commit()
    
    def fetch_all(self):
        sql = 'select * from price;'
        self.mycursor.exceute(sql)
        result = self.mycursor.fetch_all()
        return result

    def delete(self, id):
        sql = 'delete from price where id=%s;'
        self.mycursor.exceute(sql, id)
        self.mydb.commit()

    def delete_all(self):
        sql = 'delete from price;'
        self.mycursor.exceute(sql)
        self.mydb.commit()