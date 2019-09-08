import sqlite3
from sqlite3 import Error


class sqliteHelper:
    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def get_all_data(self, conn):
        """
        Query all rows in the products table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def get_data(self, conn):
        """
        Query all rows in the products table
        :param conn: the Connection object
        :return: id of result
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM products where used = 0 limit 1")

        rows = cur.fetchall()
        return rows[0]

    def create_product(self, conn, product):
        """
         Create a new product into the products table
         :param conn:
         :param product:
         :return: product id
         """
        sql = ''' INSERT INTO products(product_name,manufacturer,model,meta,img_url,used)
                   VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, product)
        return cur.lastrowid

    def build_db_table(self):
        database = "../Data/test.db"

        sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                                id integer PRIMARY KEY,
                                                product_name text,
                                                manufacturer text,
                                                model text,
                                                meta text,
                                                img_url text,
                                                used integer
                                            ); """

        # create a database connection
        conn = self.create_connection(database)

        # create tables
        if conn is not None:
            # create products table
            self.create_table(conn, sql_create_products_table)

        else:
            print("Error! cannot create the database connection.")

    def add_product(self, product_name, manufacturer, model, meta, img_url, used):
        database = "../Data/test.db"
        conn = self.create_connection(database)
        with conn:
            product = (product_name, manufacturer, model, meta, img_url, used)
            product_id = self.create_product(conn, product)

    def update_product(self, conn, product):
        """
        update priority, begin_date, and end date of a product
        :param conn:
        :param product:
        :return: project id
        """
        sql = ''' UPDATE products
                  SET used = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, product)
        conn.commit()

    def upd_product(self, id):
        database = "../Data/test.db"
        conn = self.create_connection(database)
        with conn:
            self.update_product(conn, (1, id))
