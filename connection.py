import mysql.connector

tables = {
    'notes': ['Note']
}
 
class MySQLConnection():
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect( #Quité los datos de inicio de sesión
                host="localhost",
                user="Username",
                password="password",
                database = "database"
                )
        
    def select(self, table):
        query = f"SELECT * FROM {table}"

        cursor = self.mydb.cursor()
        cursor.execute(query)

        return cursor.fetchall()
        
    def insert(self, table, values):
        columns = ''
        insert_values = []
        insert_values_type = ''


        for i in tables[table]:
            columns += f'{i}, '

        columns = columns[:-2]

        for data in values:
            insert_values_type += f"{data[1]}, "
            insert_values.append(data[0])

        insert_values_type = insert_values_type[:-2]

        query = f"INSERT INTO {table} ({columns}) VALUES ({insert_values_type})"

        cursor = self.mydb.cursor()
        cursor.execute(query, insert_values)

        self.mydb.commit()

