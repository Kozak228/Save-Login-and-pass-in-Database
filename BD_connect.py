from config import host, user, password, db_name, port
import pymysql

class Database:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port

        self.spisok_vsi = []

    def create_database(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
                cursor = connection.cursor()

                # create table
                with connection.cursor() as cursor:
                    create_table_query = "CREATE TABLE `users` (id int AUTO_INCREMENT,\
                                          site varchar(255) NOT NULL, \
                                          login varchar(255) NOT NULL, \
                                          password varchar(255) NOT NULL,\
                                          PRIMARY KEY (id));"
                    cursor.execute(create_table_query)
                    return "Information", "Table created successfully"

            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."

    def drop_database(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
                cursor = connection.cursor()

                # create table
                with connection.cursor() as cursor:
                    create_table_query = "DROP TABLE `users`"
                    cursor.execute(create_table_query)
                    return "Information", "Table droped successfully"

            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."

    def Select_db(self):  
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
                # select all data from table
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM `users`")
                    rows = cursor.fetchall()
                    for row in rows:
                        self.spisok_vsi.append([row.get("id"), row.get("site"), row.get("login"), row.get("password")])
                    
                return "Information", "Success"
            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."
            
    def Select_db_in_param(self, param, site_bool):  
        spisok_vsi_param = []
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
                if site_bool:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM `users` where site = '{param}'")
                        rows = cursor.fetchall()
                        for row in rows:
                            spisok_vsi_param.append([row.get("id"), row.get("site"), row.get("login"), row.get("password")])
                else:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM `users` where login = '{param}'")
                        rows = cursor.fetchall()
                        for row in rows:
                            spisok_vsi_param.append([row.get("id"), row.get("site"), row.get("login"), row.get("password")])

                return "Er", spisok_vsi_param
            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."

    def ret_data(self):
        kol_rows_vsi = len(self.spisok_vsi)
        return self.spisok_vsi, kol_rows_vsi

    def Insert_in_BD(self, site, login, password):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
                # insert data
                with connection.cursor() as cursor:
                    insert_query = f"INSERT INTO `users` (site, login, password) VALUES ('{site}', '{login}', '{password}')"
                    cursor.execute(insert_query)
                    connection.commit()

                return "Information", "Данные добавлены в БД!"


            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."

    def Update_bd(self, id, site, login, password):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
            # update data
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE `users` SET site = '{site}', login = '{login}', password = '{password}' WHERE id = {id}")
                    connection.commit()
                
                return "Information", "Данные oбновлены в БД!"
            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."
            
    def Update_bd_in_param(self, id, login, password):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
            # update data
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE `users` SET login = '{login}', password = '{password}' WHERE id = {id}")
                    connection.commit()
                
                return "Information", "Данные oбновлены в БД!"
            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."
                
    def Remove_row(self, id):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor)

            try:
            #  delete data
                with connection.cursor() as cursor:
                    delete_query = f"DELETE FROM `users` WHERE id = {id}"
                    cursor.execute(delete_query)
                    connection.commit()
                
                return "Information", "Данные удалены в БД!"
            finally:
                connection.close()

        except:
            return "Error", "Connection refused..."